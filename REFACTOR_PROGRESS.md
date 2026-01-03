# Routes Refactor Progress

Tracking implementation of route-based endpoints with examples, fixtures, and tests.

## Legend
- ❗ Hooman intervention required (params/DELETE/PATCH/PUT)
- ✅ Complete
- ⏳ In progress
- ❌ Not started

## COMPANIES

| Route | Hooman | Endpoint | Example | Fixture | Test (API) | Test (Model) |
|-------|--------|----------|---------|---------|------------|--------------|
| GET | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_AVAILABLE_BY_CURRENT_USER | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_BRANDS | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_BRANDSTREE | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_CAPABILITIES | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_CARRIER_ACOUNTS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_DETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_FRANCHISEE_ADDRESSES | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_FULLDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_GEOSETTINGS | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_GEO_AREA_COMPANIES | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_INFO_FROM_KEY | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_INHERITEDPACKAGINGLABOR | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_INHERITED_PACKAGING_TARIFFS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_PACKAGINGLABOR | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_PACKAGINGSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_SEARCH | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_SEARCH_CARRIER_ACCOUNTS | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_SUGGEST_CARRIERS | | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_CAPABILITIES | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_CARRIER_ACOUNTS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_FILTERED_CUSTOMERS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_FULLDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_GEOSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_LIST | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_PACKAGINGLABOR | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_PACKAGINGSETTINGS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_SEARCH_V2 | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_SIMPLELIST | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| PUT_FULLDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |

## CONTACTS

| Route | Hooman | Endpoint | Example | Fixture | Test (API) | Test (Model) |
|-------|--------|----------|---------|---------|------------|--------------|
| GET | ❗ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GET_EDITDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| HISTORY_AGGREGATED | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| HISTORY_GRAPHDATA | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| PRIMARYDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| USER | | ❌ | ❌ | ❌ | ❌ | ❌ |
| CUSTOMERS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| POST_EDITDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| HISTORY | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| MERGE_PREVIEW | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| V2_SEARCH | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| PUT_EDITDETAILS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| MERGE | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |

## JOB

| Route | Hooman | Endpoint | Example | Fixture | Test (API) | Test (Model) |
|-------|--------|----------|---------|---------|------------|--------------|
| DELETE_ONHOLD | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| DELETE_PARCELITEMS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| DELETE_SHIPMENT | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| DELETE_SHIPMENT_ACCESSORIAL | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| DELETE_TIMELINE | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_CALENDARITEMS | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_DOCUMENT_CONFIG | | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_FEEDBACK | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_FORM_ADDRESS_LABEL | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET_FORM_BILL_OF_LADING | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| ... | ... | ... | ... | ... | ... | ... |

## SMSTEMPLATE

| Route | Hooman | Endpoint | Example | Fixture | Test (API) | Test (Model) |
|-------|--------|----------|---------|---------|------------|--------------|
| DELETE | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GET | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |
| JOB_STATUSES | | ❌ | ❌ | ❌ | ❌ | ❌ |
| LIST | | ❌ | ❌ | ❌ | ❌ | ❌ |
| NOTIFICATION_TOKENS | | ❌ | ❌ | ❌ | ❌ | ❌ |
| SAVE | ❗ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

*Note: Tables for other tags (ACCOUNT, ADDRESS, ADMIN, COMMODITY, etc.) to be added as needed.*
