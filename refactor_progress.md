# Example Runner Refactor Progress

Refactoring all `examples/api/*.py` files to use the `ExampleRunner` base class from `_base.py`.

| File | Status | Examples |
|------|--------|----------|
| `_base.py` | DONE | Base class with `add()`, `run()`, `list()`, lazy `self.api` |
| `companies.py` | DONE | get, brands, brandstree, available, search, geoarea |
| `accounts.py` | DONE | forgot |
| `agent.py` | DONE | assign |
| `contacts.py` | DONE | get, user |
| `dashboard.py` | DONE | get |
| `documents.py` | DONE | upload, list, thumbnail |
| `forms.py` | DONE | simple_pdfs, operations, shipments, helpers |
| `items.py` | DONE | parcel, freight, cli |
| `items_helper.py` | DONE | parcel, freight, calendar, delete, replace, comparison |
| `lookup.py` | DONE | countries, contacttypes, documenttypes, accesskeys, densityclassmap, parcelpackagetypes |
| `misc_endpoints.py` | DONE | profile, dashboard, gridviews, partners, accessorials, pocusers, roles, views_all, datasetsps, notifications, values |
| `note.py` | DONE | get |
| `notes.py` | DONE | get, create, filter, taskcodes, cli |
| `ship.py` | DONE | timestamp (WIP placeholder) |
| `smstemplate.py` | DONE | tokens, statuses, list |
| `SmsTemplate.py` | DONE | python_api, cli, models |
| `tasks.py` | DONE | schedule |
| `views.py` | DONE | datasetsp |

## Usage Pattern

Every example file now supports:
```bash
python <file>.py              # Run all examples
python <file>.py <name>       # Run a single example by name
python <file>.py help         # List available examples
```
