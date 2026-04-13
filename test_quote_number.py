"""
Unit tests for DatabaseManager.generate_quote_number()

Run with:
    python -m pytest test_quote_number.py -v
    # or without pytest:
    python3 test_quote_number.py
"""

import os
import re
import sys
import tempfile
import unittest
import datetime
from unittest.mock import patch, MagicMock

# Stub out GUI-only modules so main_application can be imported in a
# headless environment (no display / tkinter) without crashing.
for _mod in (
    "tkinter",
    "tkinter.ttk",
    "tkinter.messagebox",
    "tkinter.filedialog",
    "tkinter.simpledialog",
):
    sys.modules.setdefault(_mod, MagicMock())

from main_application import DatabaseManager


# Fixed date used across all tests so MMYYYY is deterministic
FIXED_NOW = datetime.datetime(2026, 4, 13)
FIXED_MMYYYY = "042026"


def make_db() -> DatabaseManager:
    """Return a DatabaseManager backed by a temporary SQLite file.

    SQLite :memory: databases are connection-scoped, so every sqlite3.connect()
    call would create a separate empty database.  A real temp file is shared
    across all connections opened by DatabaseManager, which is what we need.
    """
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    return DatabaseManager(db_path=path)


class TestGenerateQuoteNumber(unittest.TestCase):

    def setUp(self):
        # Patch datetime.datetime.now() so month/year is always FIXED_NOW
        patcher = patch("main_application.datetime.datetime")
        self.mock_dt = patcher.start()
        self.mock_dt.now.return_value = FIXED_NOW
        self.addCleanup(patcher.stop)

        self.db = make_db()
        self.addCleanup(os.unlink, self.db.db_path)

    # ------------------------------------------------------------------
    # Case 1 — CLIENT, SITE and VILLE all provided
    # ------------------------------------------------------------------
    def test_all_segments_present(self):
        number = self.db.generate_quote_number("Dupont", site="SITE42", ville="Paris")
        # Expected: SA.DUPONT.SITE42.Paris.042026001
        self.assertRegex(number, r"^SA\.DUPONT\.SITE42\.Paris\." + FIXED_MMYYYY + r"\d{3}$")
        self.assertTrue(number.endswith(f"{FIXED_MMYYYY}001"))

    def test_all_segments_invoice_prefix(self):
        number = self.db.generate_quote_number(
            "Dupont", is_invoice=True, site="SITE42", ville="Paris"
        )
        self.assertTrue(number.startswith("FA.DUPONT.SITE42.Paris."))

    # ------------------------------------------------------------------
    # Case 2 — SITE is empty, CLIENT and VILLE provided
    # ------------------------------------------------------------------
    def test_site_empty_string(self):
        number = self.db.generate_quote_number("Dupont", site="", ville="Lyon")
        # SITE segment must be absent; VILLE must be present
        self.assertRegex(number, r"^SA\.DUPONT\.Lyon\." + FIXED_MMYYYY + r"\d{3}$")

    def test_site_none(self):
        number = self.db.generate_quote_number("Dupont", site=None, ville="Lyon")
        self.assertRegex(number, r"^SA\.DUPONT\.Lyon\." + FIXED_MMYYYY + r"\d{3}$")

    def test_site_whitespace_only(self):
        # A value that is only spaces should be treated as absent
        number = self.db.generate_quote_number("Dupont", site="   ", ville="Lyon")
        self.assertRegex(number, r"^SA\.DUPONT\.Lyon\." + FIXED_MMYYYY + r"\d{3}$")

    # ------------------------------------------------------------------
    # Case 3 — VILLE is empty, CLIENT and SITE provided
    # ------------------------------------------------------------------
    def test_ville_empty_string(self):
        number = self.db.generate_quote_number("Dupont", site="SITE99", ville="")
        # VILLE segment must be absent; SITE must be present
        self.assertRegex(number, r"^SA\.DUPONT\.SITE99\." + FIXED_MMYYYY + r"\d{3}$")

    def test_ville_none(self):
        number = self.db.generate_quote_number("Dupont", site="SITE99", ville=None)
        self.assertRegex(number, r"^SA\.DUPONT\.SITE99\." + FIXED_MMYYYY + r"\d{3}$")

    def test_ville_whitespace_only(self):
        number = self.db.generate_quote_number("Dupont", site="SITE99", ville="   ")
        self.assertRegex(number, r"^SA\.DUPONT\.SITE99\." + FIXED_MMYYYY + r"\d{3}$")

    # ------------------------------------------------------------------
    # Case 4 — Both SITE and VILLE empty (fallback to old format)
    # ------------------------------------------------------------------
    def test_both_absent_none(self):
        number = self.db.generate_quote_number("Dupont")
        # Old format: SA.DUPONT.MMYYYY<SEQ>
        self.assertRegex(number, r"^SA\.DUPONT\." + FIXED_MMYYYY + r"\d{3}$")

    def test_both_absent_empty_strings(self):
        number = self.db.generate_quote_number("Dupont", site="", ville="")
        self.assertRegex(number, r"^SA\.DUPONT\." + FIXED_MMYYYY + r"\d{3}$")

    def test_both_absent_whitespace(self):
        number = self.db.generate_quote_number("Dupont", site="  ", ville="  ")
        self.assertRegex(number, r"^SA\.DUPONT\." + FIXED_MMYYYY + r"\d{3}$")

    # ------------------------------------------------------------------
    # Counter increments correctly across calls
    # ------------------------------------------------------------------
    def test_counter_increments(self):
        n1 = self.db.generate_quote_number("Dupont", site="S1", ville="Paris")
        n2 = self.db.generate_quote_number("Dupont", site="S1", ville="Paris")
        n3 = self.db.generate_quote_number("Dupont", site="S1", ville="Paris")
        self.assertTrue(n1.endswith("001"))
        self.assertTrue(n2.endswith("002"))
        self.assertTrue(n3.endswith("003"))

    def test_counter_is_per_client(self):
        # Different clients have independent counters
        a = self.db.generate_quote_number("Dupont", site="S1", ville="Paris")
        b = self.db.generate_quote_number("Martin", site="S1", ville="Paris")
        self.assertTrue(a.endswith("001"))
        self.assertTrue(b.endswith("001"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
