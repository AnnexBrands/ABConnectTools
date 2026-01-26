# Routes Refactor Progress

Tracking implementation of route-based endpoints with examples, fixtures, and tests.

> **⚠️ CRITICAL: Swagger `response_model` is frequently WRONG!**
> Do NOT trust swagger's response types. Always create an example, verify the actual response, then update type hints accordingly. See "Response Model Validation Workflow" section below.

## Legend
- ❗ Hooman intervention required (params/DELETE/PATCH/PUT/500 errors)
- ✅ Complete
- ⏳ In progress
- ❌ Not started
- ⚠️ Swagger response_model needs verification

## Directive
All endpoints MUST use routes from SCHEMA, not hardcoded paths:
```python
route = self.routes['ROUTE_KEY']
route.params = {"paramName": value}
return self._make_request(route.method, route, **kwargs)
```

---

## COMPANIES (31 routes) - ✅ TYPE HINTS COMPLETE

All endpoints have proper return type hints and response casting.

| Route | Hooman | Endpoint | TypeHints | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_AVAILABLE_BY_CURRENT_USER | | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_BRANDS | | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_BRANDSTREE | | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_CAPABILITIES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_CARRIER_ACOUNTS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_COMPANY_GEOSETTINGS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_DETAILS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_FRANCHISEE_ADDRESSES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_FULLDETAILS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_GEOSETTINGS | | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_GEO_AREA_COMPANIES | | ✅ | ✅ | ❌ | ✅ | ✅ |
| GET_INFO_FROM_KEY | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_INHERITEDPACKAGINGLABOR | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_INHERITED_PACKAGING_TARIFFS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PACKAGINGLABOR | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PACKAGINGSETTINGS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SEARCH | | ✅ | ✅ | ✅ | ❌ | ✅ |
| GET_SEARCH_CARRIER_ACCOUNTS | | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SUGGEST_CARRIERS | | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_CAPABILITIES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_CARRIER_ACOUNTS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_FILTERED_CUSTOMERS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_FULLDETAILS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_GEOSETTINGS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_LIST | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PACKAGINGLABOR | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PACKAGINGSETTINGS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SEARCH_V2 | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SIMPLELIST | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_FULLDETAILS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

**Notes:**
- `GET_GEO_AREA_COMPANIES`: ✅ Now working (was HTTP 500, test now XPASS)
- `GET_COMPANY_GEOSETTINGS`: New route added for company-specific geo settings

---

## COMPANY (17 routes) - separate from COMPANIES

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_ACCOUNTS_STRIPE | ❗ | ❌ | ❌ | ❌ | ❌ |
| DELETE_CONTAINERTHICKNESSINCHES | ❗ | ❌ | ❌ | ❌ | ❌ |
| DELETE_MATERIAL | ❗ | ❌ | ❌ | ❌ | ❌ |
| DELETE_TRUCK | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_ACCOUNTS_STRIPE_CONNECTURL | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CALENDAR | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CALENDAR_BASEINFO | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CALENDAR_ENDOFDAY | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CALENDAR_STARTOFDAY | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CONTAINERTHICKNESSINCHES | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_GRIDSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_MATERIAL | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PLANNER | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SETUPDATA | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_TRUCK | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_ACCOUNTS_STRIPE_COMPLETECONNECTION | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_CONTAINERTHICKNESSINCHES | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_GRIDSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_MATERIAL | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TRUCK | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_MATERIAL | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_TRUCK | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## CONTACTS (14 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_EDITDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| HISTORY_AGGREGATED | ❗ | ❌ | ❌ | ❌ | ❌ |
| HISTORY_GRAPHDATA | ❗ | ❌ | ❌ | ❌ | ❌ |
| PRIMARYDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| USER | | ✅ | ✅ | ✅ | ✅ |
| CUSTOMERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_EDITDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| HISTORY | ❗ | ❌ | ❌ | ❌ | ❌ |
| MERGE_PREVIEW | ❗ | ❌ | ❌ | ❌ | ❌ |
| SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ |
| V2_SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_EDITDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| MERGE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Forms (15 routes)

Using `JOB_DISPLAY_ID = "2000000"` from `tests/constants.py`.

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_FORM_ADDRESS_LABEL | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_BILL_OF_LADING | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_CREDIT_CARD_AUTHORIZATION | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_CUSTOMER_QUOTE | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_INVOICE | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_INVOICE_EDITABLE | ✅ | ✅ | ✅ | ❌ | xfail |
| GET_FORM_ITEM_LABELS | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_OPERATIONS | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_PACKAGING_LABELS | ✅ | ✅ | ✅ | ❌ | xfail |
| GET_FORM_PACKAGING_SPECIFICATION | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_PACKING_SLIP | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_QUICK_SALE | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_SHIPMENTS | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_USAR | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_FORM_USAR_EDITABLE | ✅ | ✅ | ✅ | ❌ | xfail |

**Form Helpers** (in `form_helpers.py`):
| Helper | Example | Test |
|--------|---------|------|
| `get_bol(job, transport_mode)` | ✅ | ✅ |
| `get_hbl(job)` | ✅ | ✅ |
| `get_ops(job)` | ✅ | ✅ |

---

## JOB - Core (10 routes)

All core job endpoints now use SCHEMA routes with proper docstrings (jobs/job.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_CALENDARITEMS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_DOCUMENT_CONFIG | | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_FEEDBACK | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_JOB_ACCESS_LEVEL | | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SEARCH | | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_UPDATE_PAGE_CONFIG | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_BOOK | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SEARCH_BY_DETAILS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_TRANSFER | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_SAVE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - OnHold (9 routes)

All OnHold endpoints now use SCHEMA routes with proper docstrings (jobs/onhold.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| DELETE_ONHOLD | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_ONHOLD | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_ONHOLD_LIST | | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_ONHOLD_FOLLOWUPUSER | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_ONHOLD_FOLLOWUPUSERS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_ONHOLD | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_ONHOLD_COMMENT | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_ONHOLD | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_ONHOLD_DATES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_ONHOLD_RESOLVE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - Payment (12 routes)

All Payment endpoints now use SCHEMA routes with proper docstrings (jobs/payment.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET_PAYMENT | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PAYMENT_CREATE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PAYMENT_SOURCES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PRICE | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_ACHCREDIT_TRANSFER | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PAYMENT_ACHPAYMENT_SESSION | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PAYMENT_ATTACH_CUSTOMER_BANK | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PAYMENT_BANKSOURCE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PAYMENT_BYSOURCE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PAYMENT_CANCEL_JOB_ACHVERIFICATION | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PAYMENT_VERIFY_JOB_ACHSOURCE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - Shipment (12 routes)

All Shipment endpoints now use SCHEMA routes with proper docstrings (jobs/shipment.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| DELETE_SHIPMENT | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| DELETE_SHIPMENT_ACCESSORIAL | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_ACCESSORIALS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_EXPORTDATA | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_ORIGINDESTINATION | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_RATEQUOTES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_RATESSTATE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_ACCESSORIAL | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_BOOK | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_EXPORTDATA | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_RATEQUOTES | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - Timeline (8 routes) - ⚠️ NEEDS INTEGRATION TESTS

All Timeline endpoints now use SCHEMA routes with proper docstrings (jobs/timeline.py refactored).

**Status:** Type hints complete. Model validation tests exist. Missing: integration tests, examples, fixtures.

**NOTE:** Swagger response_model accuracy is UNVERIFIED. Create examples to test actual API responses.

| Route | Hooman | Endpoint | Docstring | TypeHints | Example | Fixture | IntegTest | ModelTest |
|-------|--------|----------|-----------|-----------|---------|---------|-----------|-----------|
| DELETE_TIMELINE | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| GET_TIMELINE | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| GET_TIMELINE_LIST | | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| GET_TIMELINE_AGENT | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| PATCH_TIMELINE | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| POST_TIMELINE | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| POST_TIMELINE_INCREMENTJOBSTATUS | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| POST_TIMELINE_UNDOINCREMENTJOBSTATUS | ❗ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |

**IntegTest** = Integration test calling actual API | **ModelTest** = Model validation test (exists in test_timeline.py)

**Also exists:** `TimelineHelpers` class in `timeline_helpers.py` with convenience methods (schedule, received, pack_start, etc.)

---

## JOB - FreightProviders (4 routes)

All FreightProviders endpoints now use SCHEMA routes with proper docstrings (jobs/freightproviders.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET_FREIGHTPROVIDERS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_FREIGHTITEMS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_FREIGHTPROVIDERS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_FREIGHTPROVIDERS_RATEQUOTE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - ParcelItems (5 routes)

All ParcelItems endpoints now use SCHEMA routes with proper docstrings (jobs/parcelitems.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| DELETE_PARCELITEMS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PACKAGINGCONTAINERS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_PARCELITEMS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_PARCEL_ITEMS_WITH_MATERIALS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_PARCELITEMS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - Email (4 routes)

All Email endpoints now use SCHEMA routes with proper docstrings (jobs/email.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| POST_EMAIL | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_EMAIL_CREATETRANSACTIONALEMAIL | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_EMAIL_SEND | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_EMAIL_SENDDOCUMENT | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - SMS (4 routes)

All SMS endpoints now use SCHEMA routes with proper docstrings (jobs/sms.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET_SMS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SMS_TEMPLATEBASED | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SMS | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_SMS_READ | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - RFQ (2 routes)

All RFQ endpoints now use SCHEMA routes with proper docstrings (jobs/rfq.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET_RFQ | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_RFQ_STATUSOF_FORCOMPANY | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - Notes (5 routes)

All Note endpoints now use SCHEMA routes with proper docstrings (jobs/note.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET_NOTE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_NOTE_LIST | | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST_ITEM_NOTES | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_NOTE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_NOTE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## JOB - Tracking (3 routes)

All Tracking endpoints now use SCHEMA routes with proper docstrings (jobs/tracking.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| GET_TRACKING | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_TRACKING_SHIPMENT | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET_SUBMANAGEMENTSTATUS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Other (3 routes)

Status endpoint now uses SCHEMA routes with proper docstrings (jobs/status.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| POST_CHANGE_AGENT | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_STATUS_QUOTE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PUT_ITEM | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## SMSTEMPLATE (6 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE | ❗ | ✅ | ❌ | ❌ | ❌ |
| GET | ❗ | ✅ | ❌ | ❌ | ❌ |
| JOB_STATUSES | | ✅ | ✅ | ✅ | ✅ |
| LIST | | ✅ | ✅ | ✅ | ✅ |
| NOTIFICATION_TOKENS | | ✅ | ✅ | ✅ | ✅ |
| SAVE | ❗ | ✅ | ❌ | ❌ | ❌ |

---

## ACCOUNT (10 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_PAYMENTSOURCE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PROFILE | | ✅ | ✅ | ✅ | ✅ |
| GET_VERIFYRESETTOKEN | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_CONFIRM | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_FORGOT | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_REGISTER | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_RESETPASSWORD | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SEND_CONFIRMATION | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SETPASSWORD | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_PAYMENTSOURCE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## ADDRESS (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_ISVALID | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PROPERTYTYPE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_AVOID_VALIDATION | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_VALIDATED | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## ADMIN (13 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_ADVANCEDSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_ADVANCEDSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_ADVANCEDSETTINGS_ALL | | ❌ | ❌ | ❌ | ❌ |
| GET_CARRIERERRORMESSAGE_ALL | | ❌ | ❌ | ❌ | ❌ |
| GET_GLOBALSETTINGS_COMPANYHIERARCHY | | ❌ | ❌ | ❌ | ❌ |
| GET_GLOBALSETTINGS_COMPANYHIERARCHY_COMPANY | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_ADVANCEDSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_CARRIERERRORMESSAGE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_GLOBALSETTINGS_APPROVEINSURANCEEXCEPTION | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_GLOBALSETTINGS_GETINSURANCEEXCEPTIONS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_GLOBALSETTINGS_INTACCT | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_LOGBUFFER_FLUSH | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_LOGBUFFER_FLUSH_ALL | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## COMMODITY (5 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SUGGESTIONS | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## COMMODITY_MAP (5 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## DASHBOARD (9 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | | ✅ | ✅ | ✅ | ✅ |
| GRIDVIEWS | | ✅ | ✅ | ✅ | ✅ |
| GRIDVIEWSTATE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_GRIDVIEWSTATE | ❗ | ❌ | ❌ | ❌ | ❌ |
| INBOUND | ❗ | ❌ | ❌ | ❌ | ❌ |
| INHOUSE | ❗ | ❌ | ❌ | ❌ | ❌ |
| LOCAL_DELIVERIES | ❗ | ❌ | ❌ | ❌ | ❌ |
| OUTBOUND | ❗ | ❌ | ❌ | ❌ | ❌ |
| RECENTESTIMATES | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## DOCUMENTS (6 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ✅ | ❌ | ❌ | ❌ |
| THUMBNAIL | ❗ | ✅ | ❌ | ❌ | ❌ |
| LIST | | ✅ | ❌ | ❌ | ❌ |
| POST | ❗ | ✅ | ❌ | ❌ | ❌ |
| HIDE | ❗ | ✅ | ❌ | ❌ | ❌ |
| UPDATE | ❗ | ✅ | ❌ | ❌ | ❌ |

---

## E_SIGN (2 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_RESULT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## EMAIL (1 route)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| LABELREQUEST | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOBINTACCT (5 routes)

All JobIntacct endpoints now use SCHEMA routes with proper docstrings (jobs/intacct.py refactored).

| Route | Hooman | Endpoint | Docstring | Example | Fixture | Test |
|-------|--------|----------|-----------|---------|---------|------|
| DELETE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| GET | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| POST | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| APPLY_REBATE | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |
| DRAFT | ❗ | ✅ | ✅ | ❌ | ❌ | ❌ |

---

## LOOKUP (14 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ✅ | ❌ | ❌ | ❌ |
| ACCESS_KEY | ❗ | ✅ | ❌ | ❌ | ❌ |
| ACCESS_KEYS | | ✅ | ✅ | ✅ | ✅ |
| COMON_INSURANCE | | ✅ | ❌ | ❌ | ❌ |
| CONTACT_TYPES | | ✅ | ✅ | ✅ | ✅ |
| COUNTRIES | | ✅ | ✅ | ✅ | ✅ |
| DENSITY_CLASS_MAP | | ✅ | ✅ | ✅ | ✅ |
| DOCUMENT_TYPES | | ✅ | ✅ | ✅ | ✅ |
| ITEMS | ❗ | ✅ | ❌ | ❌ | ❌ |
| PARCEL_PACKAGE_TYPES | | ✅ | ✅ | ✅ | ✅ |
| PPCCAMPAIGNS | | ✅ | ❌ | ❌ | ❌ |
| REFER_CATEGORY | | ✅ | ❌ | ❌ | ❌ |
| REFER_CATEGORY_HEIRACHY | | ✅ | ❌ | ❌ | ❌ |
| RESET_MASTER_CONSTANT_CACHE | | ✅ | ❌ | ❌ | ❌ |

---

## NOTE (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | | ❌ | ❌ | ❌ | ❌ |
| GET_SUGGEST_USERS | | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## NOTIFICATIONS (1 route)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | | ✅ | ✅ | ✅ | ✅ |

---

## PARTNER (2 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | | ✅ | ✅ | ✅ | ✅ |
| POST_SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## REPORTS (8 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| INSURANCE | ❗ | ❌ | ❌ | ❌ | ❌ |
| REFERRED_BY | ❗ | ❌ | ❌ | ❌ | ❌ |
| SALES | ❗ | ❌ | ❌ | ❌ | ❌ |
| SALES_DRILLDOWN | ❗ | ❌ | ❌ | ❌ | ❌ |
| SALES_SUMMARY | ❗ | ❌ | ❌ | ❌ | ❌ |
| TOP_REVENUE_CUSTOMERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| TOP_REVENUE_SALES_REPS | ❗ | ❌ | ❌ | ❌ | ❌ |
| WEB2LEAD | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## RFQ (7 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| FORJOB | ❗ | ❌ | ❌ | ❌ | ❌ |
| ACCEPT | ❗ | ❌ | ❌ | ❌ | ❌ |
| ACCEPTWINNER | ❗ | ❌ | ❌ | ❌ | ❌ |
| CANCEL | ❗ | ❌ | ❌ | ❌ | ❌ |
| COMMENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| DECLINE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## SHIPMENT (3 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| ACCESSORIALS | | ✅ | ✅ | ✅ | ✅ |
| DOCUMENT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## USERS (5 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| POCUSERS | | ✅ | ✅ | ✅ | ✅ |
| ROLES | | ✅ | ✅ | ✅ | ✅ |
| LIST | ❗ | ❌ | ❌ | ❌ | ❌ |
| USER | ❗ | ❌ | ❌ | ❌ | ❌ |
| USER_UPDATE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## V2 (1 route)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| JOB_TRACKING | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## V3 (1 route)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| JOB_TRACKING | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## VALUES (1 route)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | | ✅ | ✅ | ✅ | ✅ |

---

## VIEWS (8 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE | ❗ | ✅ | ❌ | ❌ | ❌ |
| GET | ❗ | ✅ | ❌ | ❌ | ❌ |
| ACCESSINFO | ❗ | ✅ | ❌ | ❌ | ❌ |
| ALL | | ✅ | ✅ | ✅ | ✅ |
| DATASETSP | ❗ | ✅ | ❌ | ❌ | ❌ |
| DATASETSPS | | ✅ | ✅ | ✅ | ✅ |
| POST | ❗ | ✅ | ❌ | ❌ | ❌ |
| PUT_ACCESS | ❗ | ✅ | ❌ | ❌ | ❌ |

---

## WEBHOOKS (6 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| POST_STRIPE_CHECKOUT_SESSION_COMPLETED | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_STRIPE_CONNECT_HANDLE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_STRIPE_HANDLE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TWILIO_BODY_SMS_INBOUND | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TWILIO_FORM_SMS_INBOUND | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TWILIO_SMS_STATUS_CALLBACK | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## Summary

**Total Routes:** ~220

**Completed (with endpoint, example, fixture, and test):**
- COMPANIES: GET, GET_AVAILABLE_BY_CURRENT_USER, GET_BRANDS, GET_BRANDSTREE (4)
- CONTACTS: GET, USER (2)
- JOB Forms: 15 routes (12 with fixtures, 3 xfail for API errors)
- SMSTEMPLATE: JOB_STATUSES, LIST, NOTIFICATION_TOKENS (3)
- ACCOUNT: GET_PROFILE (1)
- DASHBOARD: GET, GRIDVIEWS (2)
- LOOKUP: COUNTRIES, CONTACT_TYPES, DOCUMENT_TYPES, ACCESS_KEYS, DENSITY_CLASS_MAP, PARCEL_PACKAGE_TYPES (6)
- NOTIFICATIONS: GET (1)
- PARTNER: GET (1)
- SHIPMENT: ACCESSORIALS (1)
- USERS: POCUSERS, ROLES (2)
- VALUES: GET (1)
- VIEWS: ALL, DATASETSPS (2)

**Endpoints Exist (need examples/fixtures/tests):**
- SMSTEMPLATE: GET, DELETE, SAVE
- DOCUMENTS: GET, THUMBNAIL, LIST, POST, HIDE, UPDATE
- VIEWS: DELETE, GET, ACCESSINFO, DATASETSP, POST, PUT_ACCESS

**Needs Hooman Input:**
- All POST/PUT/DELETE/PATCH routes (except those noted above with endpoints)
- All routes with path parameters (need test IDs)
- COMPANIES.GET_SEARCH: HTTP 500 without searchValue (requires searchValue param)

**xfail Notes:**
- JOB Forms: GET_FORM_INVOICE_EDITABLE, GET_FORM_PACKAGING_LABELS, GET_FORM_USAR_EDITABLE (API returns 500)
- Fixtures generated using `instaquote` user which has elevated permissions

---

## Human Follow-Up Required

### High Priority

1. **Complete routes refactoring for remaining files**
   - COMPLETED: lookup.py, views.py, dashboard.py, users.py, account.py, contacts.py, companies.py, SmsTemplate.py, shipment.py, partner.py, notifications.py, Values.py, documents.py
   - COMPLETED: All `ABConnect/api/endpoints/jobs/` sub-endpoints (job.py, timeline.py, shipment.py, payment.py, onhold.py, sms.py, note.py, email.py, tracking.py, parcelitems.py, rfq.py, freightproviders.py, intacct.py, status.py, form.py)
   - REMAINING (still using hardcoded paths):
     - `ABConnect/api/endpoints/webhooks.py`
     - `ABConnect/api/endpoints/rfq.py` (standalone RFQ endpoint, not job-related)
     - `ABConnect/api/endpoints/reports.py`
     - `ABConnect/api/endpoints/note.py` (standalone NOTE endpoint, not job-related)
     - `ABConnect/api/endpoints/email.py` (standalone EMAIL endpoint, not job-related)
     - `ABConnect/api/endpoints/e_sign.py`
     - `ABConnect/api/endpoints/address.py`
     - `ABConnect/api/endpoints/admin.py`
     - `ABConnect/api/endpoints/commodity.py`
     - `ABConnect/api/endpoints/commoditymap.py`
     - `ABConnect/api/endpoints/company.py`
     - `ABConnect/api/endpoints/v2.py`
     - `ABConnect/api/endpoints/v3.py`

2. **Add examples/fixtures/tests for endpoints that exist**
   - SMSTEMPLATE: GET (needs templateId), DELETE (needs templateId), SAVE
   - DOCUMENTS: GET (needs docPath), THUMBNAIL (needs docPath), LIST, POST, HIDE (needs docId), UPDATE (needs docId)
   - VIEWS: DELETE (needs viewId), GET (needs viewId), ACCESSINFO (needs viewId), DATASETSP (needs spName), POST, PUT_ACCESS (needs viewId)
   - LOOKUP: COMON_INSURANCE, PPCCAMPAIGNS, REFER_CATEGORY, REFER_CATEGORY_HEIRACHY, RESET_MASTER_CONSTANT_CACHE

### Medium Priority

3. **Investigate HTTP 500 errors**
   - ~~`COMPANIES.GET_GEO_AREA_COMPANIES`: Returns 500~~ ✅ RESOLVED - Now working
   - `COMPANIES.GET_SEARCH`: Returns 500 without `searchValue` parameter (param required)

4. **Test data IDs needed**
   - Need valid test IDs for endpoints with path parameters (viewId, templateId, docId, contactId, etc.)
   - Consider creating test data in staging environment

### Low Priority

5. **Documentation alignment**
   - Ensure sphinx docs match implemented endpoints
   - Add CLI examples to examples/ for new endpoints

6. **Model validation**
   - Add Pydantic model validation tests for all fixtures

---

## Response Model Validation Workflow

**IMPORTANT: Swagger `response_model` is frequently incorrect.**

The swagger.json often indicates generic response types like `SaveResponseModel` when the actual API returns a domain-specific type (e.g., `Timeline`, `TimelineResponse`). Always verify actual responses before trusting swagger.

### Validation Workflow

For each endpoint, follow this sequence:

1. **Create Example** (`examples/`)
   - Write a minimal example that calls the endpoint
   - Print the raw response to see actual structure
   - Run: `python examples/timeline_1.py`

2. **Verify Response Type**
   - Compare actual response against swagger's claimed `response_model`
   - Check if response casts correctly to the expected Pydantic model
   - If mismatch: document the TRUE response type

3. **Update Endpoint Type Hints**
   - Fix return type annotation to match actual response
   - Ensure `_make_request()` casts to correct model
   - Example: `def post_timeline(...) -> Timeline:` not `-> SaveResponseModel:`

4. **Update Tests**
   - Add `isinstance()` check for actual response type
   - Validate schema's `response_model` matches reality (or document discrepancy)
   - Test model validation with sample data

### Known Swagger Inaccuracies

| Route | Swagger Says | Actually Returns | Verified? |
|-------|--------------|------------------|-----------|
| `POST_TIMELINE` | `SaveResponseModel` | Possibly `Timeline` | ❌ Unverified |
| `PATCH_TIMELINE` | `ServiceBaseResponse` | Unknown | ❌ Unverified |
| (add more as discovered) | | | |

**To verify:** Create example, call API, print raw response, compare to swagger claim.

---

## Type Hints & Casting Progress

Tracking proper return type hints and Pydantic model casting for all endpoint modules.

| Module | TypeHints | Casting | Tests | Status |
|--------|-----------|---------|-------|--------|
| `companies.py` | ✅ 30/31 | ✅ | ✅ 9/10 | Complete |
| `contacts.py` | ❌ | ❌ | ❌ | Not started |
| `jobs/timeline.py` | ✅ 8/8 | ✅ | ⏳ Model tests only | TypeHints complete; needs integration tests |
| `jobs/*.py` (other) | ❌ | ❌ | ❌ | Not started |
| `lookup.py` | ❌ | ❌ | ❌ | Not started |
| `users.py` | ❌ | ❌ | ❌ | Not started |
| `account.py` | ❌ | ❌ | ❌ | Not started |
| `dashboard.py` | ❌ | ❌ | ❌ | Not started |
| `documents.py` | ❌ | ❌ | ❌ | Not started |
| `views.py` | ❌ | ❌ | ❌ | Not started |
| `smstemplate.py` | ❌ | ❌ | ❌ | Not started |
| `shipment.py` | ❌ | ❌ | ❌ | Not started |
| `partner.py` | ❌ | ❌ | ❌ | Not started |
| `notifications.py` | ❌ | ❌ | ❌ | Not started |
| `values.py` | ❌ | ❌ | ❌ | Not started |

---

## Progress Update: 2026-01-25 - Companies Endpoints

### Completed Work

1. **Return Type Hints Added** (`ABConnect/api/endpoints/companies.py`)
   - All 30 endpoint methods now have correct return type hints matching route schema
   - Imports updated for all Pydantic model types used
   - Removed unused `cast` parameter from `get()` method

2. **Bug Fixes**
   - Fixed `get_geosettings()` which was incorrectly passing `"GET"` string to `_make_request()`
   - Added missing route `GET_COMPANY_GEOSETTINGS` to `ABConnect/api/routes.py`
   - Added missing fields to `SearchCompanyResponse` model: `id`, `code`, `name`, `type_id`

3. **Tests Updated** (`tests/api/test_companies.py`)
   - All List response tests now validate each element is correct Pydantic type
   - Added schema response_model assertions
   - Added tests for GET_SEARCH and GET_GEO_AREA_COMPANIES

### Test Results (All Passing)

```
tests/api/test_companies.py::test_get_company_by_id PASSED
tests/api/test_companies.py::test_company_simple_model PASSED
tests/api/test_companies.py::test_get_brands PASSED
tests/api/test_companies.py::test_brands_fixture PASSED
tests/api/test_companies.py::test_get_brandstree PASSED
tests/api/test_companies.py::test_brandstree_fixture PASSED
tests/api/test_companies.py::test_get_availablebycurrentuser PASSED
tests/api/test_companies.py::test_availablebycurrentuser_fixture PASSED
tests/api/test_companies.py::test_get_search PASSED
tests/api/test_companies.py::test_get_geoareacompanies XPASS
```

**9 passed, 1 xpassed**

### Issues Resolved

1. ~~**SearchCompanyResponse Model Validation Failure**~~ ✅ FIXED
   - Added missing fields: `id`, `code`, `name`, `type_id` (alias: typeId)

2. **GET_GEO_AREA_COMPANIES No Longer Returns 500** ✅
   - Test marked xfail now passes (XPASS)
   - Consider removing xfail marker
