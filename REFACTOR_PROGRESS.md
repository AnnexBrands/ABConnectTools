# Routes Refactor Progress

Tracking implementation of route-based endpoints with examples, fixtures, and tests.

## Legend
- ❗ Hooman intervention required (params/DELETE/PATCH/PUT/500 errors)
- ✅ Complete
- ⏳ In progress
- ❌ Not started

---

## COMPANIES (21 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_AVAILABLE_BY_CURRENT_USER | | ✅ | ✅ | ✅ | ❌ |
| GET_BRANDS | | ✅ | ✅ | ✅ | ❌ |
| GET_BRANDSTREE | | ✅ | ✅ | ✅ | ❌ |
| GET_CAPABILITIES | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CARRIER_ACOUNTS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_DETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_FRANCHISEE_ADDRESSES | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_FULLDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_GEOSETTINGS | | ✅ | ❌ | ❌ | ❌ |
| GET_GEO_AREA_COMPANIES | ❗ | ✅ | ❌ | ✅ | ❌ |
| GET_INFO_FROM_KEY | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_INHERITEDPACKAGINGLABOR | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_INHERITED_PACKAGING_TARIFFS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PACKAGINGLABOR | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PACKAGINGSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SEARCH | ❗ | ✅ | ❌ | ❌ | ❌ |
| GET_SEARCH_CARRIER_ACCOUNTS | | ✅ | ❌ | ❌ | ❌ |
| GET_SUGGEST_CARRIERS | | ❌ | ❌ | ❌ | ❌ |
| POST_CAPABILITIES | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_CARRIER_ACOUNTS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_FILTERED_CUSTOMERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_FULLDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_GEOSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_LIST | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PACKAGINGLABOR | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PACKAGINGSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SEARCH_V2 | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SIMPLELIST | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_FULLDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |

**Errors requiring hooman input:**
- `GET_GEO_AREA_COMPANIES`: HTTP 500 (fixture exists from prior run)
- `GET_SEARCH`: HTTP 500 when called without searchValue

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
| USER | | ✅ | ✅ | ✅ | ❌ |
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

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_CALENDARITEMS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_DOCUMENT_CONFIG | | ✅ | ❌ | ❌ | ❌ |
| GET_FEEDBACK | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_JOB_ACCESS_LEVEL | | ❌ | ❌ | ❌ | ❌ |
| GET_SEARCH | | ❌ | ❌ | ❌ | ❌ |
| GET_UPDATE_PAGE_CONFIG | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_BOOK | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SEARCH_BY_DETAILS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TRANSFER | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_SAVE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - OnHold (9 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_ONHOLD | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_ONHOLD | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_ONHOLD_FOLLOWUPUSER | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_ONHOLD_FOLLOWUPUSERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_ONHOLD | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_ONHOLD_COMMENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_ONHOLD | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_ONHOLD_DATES | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_ONHOLD_RESOLVE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Payment (12 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_PAYMENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PAYMENT_CREATE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PAYMENT_SOURCES | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PRICE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_ACHCREDIT_TRANSFER | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_ACHPAYMENT_SESSION | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_ATTACH_CUSTOMER_BANK | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_BANKSOURCE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_BYSOURCE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_CANCEL_JOB_ACHVERIFICATION | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PAYMENT_VERIFY_JOB_ACHSOURCE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Shipment (12 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_SHIPMENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| DELETE_SHIPMENT_ACCESSORIAL | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_ACCESSORIALS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_EXPORTDATA | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_ORIGINDESTINATION | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_RATEQUOTES | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SHIPMENT_RATESSTATE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_ACCESSORIAL | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_BOOK | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_EXPORTDATA | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SHIPMENT_RATEQUOTES | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Timeline (7 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_TIMELINE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_TIMELINE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_TIMELINE_AGENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| PATCH_TIMELINE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TIMELINE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TIMELINE_INCREMENTJOBSTATUS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_TIMELINE_UNDOINCREMENTJOBSTATUS | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - FreightProviders (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_FREIGHTPROVIDERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_FREIGHTITEMS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_FREIGHTPROVIDERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_FREIGHTPROVIDERS_RATEQUOTE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - ParcelItems (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_PARCELITEMS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PACKAGINGCONTAINERS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PARCELITEMS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PARCEL_ITEMS_WITH_MATERIALS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_PARCELITEMS | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Email (5 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| POST_EMAIL | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_EMAIL_CREATETRANSACTIONALEMAIL | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_EMAIL_SEND | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_EMAIL_SENDDOCUMENT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - SMS (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_SMS | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SMS_TEMPLATEBASED | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SMS | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_SMS_READ | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - RFQ (3 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_RFQ | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_RFQ_STATUSOF_FORCOMPANY | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Notes (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_NOTE | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_ITEM_NOTES | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_NOTE | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_NOTE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Tracking (4 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET_TRACKING | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_TRACKING_SHIPMENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_SUBMANAGEMENTSTATUS | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## JOB - Other (3 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| POST_CHANGE_AGENT | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST_STATUS_QUOTE | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_ITEM | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## SMSTEMPLATE (6 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| JOB_STATUSES | | ✅ | ✅ | ✅ | ❌ |
| LIST | | ✅ | ✅ | ✅ | ❌ |
| NOTIFICATION_TOKENS | | ✅ | ✅ | ✅ | ❌ |
| SAVE | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## ACCOUNT (10 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE_PAYMENTSOURCE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET_PROFILE | | ❌ | ❌ | ❌ | ❌ |
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
| GET | | ❌ | ❌ | ❌ | ❌ |
| GRIDVIEWS | | ❌ | ❌ | ❌ | ❌ |
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
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| THUMBNAIL | ❗ | ❌ | ❌ | ❌ | ❌ |
| LIST | | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| HIDE | ❗ | ❌ | ❌ | ❌ | ❌ |
| UPDATE | ❗ | ❌ | ❌ | ❌ | ❌ |

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

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| APPLY_REBATE | ❗ | ❌ | ❌ | ❌ | ❌ |
| DRAFT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## LOOKUP (14 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| ACCESS_KEY | ❗ | ❌ | ❌ | ❌ | ❌ |
| ACCESS_KEYS | | ❌ | ❌ | ❌ | ❌ |
| COMON_INSURANCE | | ❌ | ❌ | ❌ | ❌ |
| CONTACT_TYPES | | ❌ | ❌ | ❌ | ❌ |
| COUNTRIES | | ❌ | ❌ | ❌ | ❌ |
| DENSITY_CLASS_MAP | | ❌ | ❌ | ❌ | ❌ |
| DOCUMENT_TYPES | | ❌ | ❌ | ❌ | ❌ |
| ITEMS | | ❌ | ❌ | ❌ | ❌ |
| PARCEL_PACKAGE_TYPES | | ❌ | ❌ | ❌ | ❌ |
| PPCCAMPAIGNS | | ❌ | ❌ | ❌ | ❌ |
| REFER_CATEGORY | | ❌ | ❌ | ❌ | ❌ |
| REFER_CATEGORY_HEIRACHY | | ❌ | ❌ | ❌ | ❌ |
| RESET_MASTER_CONSTANT_CACHE | | ❌ | ❌ | ❌ | ❌ |

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
| GET | | ❌ | ❌ | ❌ | ❌ |

---

## PARTNER (2 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| GET | | ❌ | ❌ | ❌ | ❌ |
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
| ACCESSORIALS | | ❌ | ❌ | ❌ | ❌ |
| DOCUMENT | ❗ | ❌ | ❌ | ❌ | ❌ |

---

## USERS (5 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| POCUSERS | | ❌ | ❌ | ❌ | ❌ |
| ROLES | | ❌ | ❌ | ❌ | ❌ |
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
| GET | | ❌ | ❌ | ❌ | ❌ |

---

## VIEWS (8 routes)

| Route | Hooman | Endpoint | Example | Fixture | Test |
|-------|--------|----------|---------|---------|------|
| DELETE | ❗ | ❌ | ❌ | ❌ | ❌ |
| GET | ❗ | ❌ | ❌ | ❌ | ❌ |
| ACCESSINFO | ❗ | ❌ | ❌ | ❌ | ❌ |
| ALL | | ❌ | ❌ | ❌ | ❌ |
| DATASETSP | ❗ | ❌ | ❌ | ❌ | ❌ |
| DATASETSPS | | ❌ | ❌ | ❌ | ❌ |
| POST | ❗ | ❌ | ❌ | ❌ | ❌ |
| PUT_ACCESS | ❗ | ❌ | ❌ | ❌ | ❌ |

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

**Completed (with endpoint, example, and fixture):**
- COMPANIES: GET, GET_AVAILABLE_BY_CURRENT_USER, GET_BRANDS, GET_BRANDSTREE (4)
- CONTACTS: GET, USER (2)
- JOB Forms: 15 routes (12 with fixtures, 3 xfail)
- SMSTEMPLATE: JOB_STATUSES, LIST, NOTIFICATION_TOKENS (3)

**Needs Hooman Input:**
- All POST/PUT/DELETE/PATCH routes
- All routes with path parameters (need test IDs)
- COMPANIES.GET_GEO_AREA_COMPANIES: HTTP 500
- COMPANIES.GET_SEARCH: HTTP 500 without searchValue
