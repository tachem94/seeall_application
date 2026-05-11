# CLAUDE.md

Guidance for Claude Code working in this repo.

## Run

```bash
pip install -r requirements.txt
python lancer_application.py          # or main_application.py, or lancer_application.bat
python -m pytest test_quote_number.py # only test file
```

No build step. The app is a Tkinter desktop application; most logic lives in `main_application.py` (~3700 lines), with config split into `config.py`.

## Architecture

`main_application.py` contains:

- **`DatabaseManager`** — SQLite wrapper (`seeall_database.db`). Schema migrations run inline at the bottom of `init_database()` via `ALTER TABLE … ADD COLUMN` guarded by try/except — add new migrations the same way.
- **`BackupManager`** — copies the DB to `backups/` on startup and rotates old files. Runs **before** the DB connection is opened, so it operates on a closed file.
- **`Client`**, **`Quote`**, **`SiteItem`**, **`QuoteItem`** — dataclasses. `QuoteItem` / `quote_items` table is legacy (kept for backward compat); `SiteItem` / `quote_sites` is the current model (one site per row: address, coords, description, price HT).
- **`Quote`** — represents either a devis or a facture, distinguished by `is_invoice`. Conversion creates a new row linked via `linked_invoice_id`. Invoices also carry `is_paid` (drives the green-row highlight and the paid/unpaid totals on the Factures tab).
- **`PDFGenerator`** (ReportLab), **`WordGenerator`** (python-docx), **`export_quotes_to_excel()`** (openpyxl, top-level). All three deps are optional — the app degrades gracefully when missing.
- **`MainApplication`** — the Tk root with three tabs: Clients, Devis, Factures.
- **`QuoteDialog`**, **`ConvertToInvoiceDialog`** — modal editors.

## Numbering

- Quotes:   `SA.<CLIENT>.<MMYYYY><seq>` (e.g. `SA.STAUBINSURMER.112025001`)
- Invoices: `FA.<CLIENT>.<MMYYYY><seq>`
- Sequence counters live in the `counters` table, scoped per client + month.

## Database tables

| Table | Purpose |
|---|---|
| `clients` | Customer records |
| `quotes` | Devis and factures (shared, distinguished by `is_invoice`) |
| `quote_sites` | Sites per quote — **current** item model |
| `quote_items` | Legacy items — backward compat only, don't add features here |
| `counters` | Per-client/month sequence counters |

## Config

All company info, VAT rate, numbering prefixes, UI and export settings are plain dicts in `config.py` (`COMPANY_CONFIG`, `BUSINESS_CONFIG`, `UI_CONFIG`, `EXPORT_CONFIG`, …). `main_application.py` imports them with hardcoded fallbacks, so a missing `config.py` won't crash the app. See README for the full key reference.
