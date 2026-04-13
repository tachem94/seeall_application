# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the application
python lancer_application.py
# or directly
python main_application.py

# On Windows you can also double-click lancer_application.bat
```

## Architecture

This is a single-file Python desktop application (`main_application.py`) with a separate configuration file (`config.py`). There are no tests and no build step.

### Key classes in `main_application.py`

- **`DatabaseManager`** — wraps SQLite (`seeall_database.db`), creates tables on init, handles all CRUD for clients, quotes, and sites. Schema migrations are applied inline in `init_database()`.
- **`Client`**, **`Quote`**, **`SiteItem`**, **`QuoteItem`** — dataclasses representing the domain model. `QuoteItem` is deprecated; `SiteItem` is the current item type (one site = one row with address, coordinates, description, price HT).
- **`Quote`** — can represent either a devis (quote) or facture (invoice) via `is_invoice` flag. Quotes and invoices share the same table; conversion creates a new row linked via `linked_invoice_id`.
- The main Tkinter application class drives the UI with three tabs: Clients, Devis, Factures.

### Configuration (`config.py`)

All company info, VAT rate, numbering prefixes, UI settings, and export settings live here as plain dicts (`COMPANY_CONFIG`, `BUSINESS_CONFIG`, `UI_CONFIG`, `EXPORT_CONFIG`, etc.). `main_application.py` imports these with a fallback to hardcoded defaults if the file is missing.

### Numbering scheme

- Quotes: `SA.<CLIENT>.<MMYYYY><seq>` (e.g. `SA.STAUBINSURMER.112025001`)
- Invoices: `FA.<CLIENT>.<MMYYYY><seq>`
- Sequence counters are stored in the `counters` SQLite table, scoped per client + month.

### Export

PDF is generated with ReportLab; Word with python-docx. Both are optional — the app degrades gracefully if the libraries are absent. Export functions are methods on the main app class.

### Database tables

| Table | Purpose |
|---|---|
| `clients` | Customer records |
| `quotes` | Devis and factures (shared, distinguished by `is_invoice`) |
| `quote_sites` | One-to-many sites per quote (current model) |
| `quote_items` | Legacy items per quote (backward compat only) |
| `counters` | Auto-increment counters for quote/invoice numbering |

## Customisation

To change company details, VAT rate, bank info, or document prefixes — edit `config.py`. The README contains a full description of every config key.
