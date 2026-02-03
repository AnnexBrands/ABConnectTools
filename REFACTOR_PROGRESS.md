# Endpoint Refactoring Plan

Systematic plan to bring all API endpoints to full "Four-Way Harmony":
endpoint implementation, example, fixture, and test.

**Approach established by timeline/agent work:**
- Examples import from `_constants` and `_helpers`, use `save_fixture()`, assert `isinstance`
- Tests use conftest data fixtures, `@pytest.mark.integration` for live calls, fixture validation
- `@pytest.mark.xfail(reason="Human: <instructions>")` for routes needing human intervention
- Each path root = one git commit

---

## Legend

- [x] Done
- [ ] To do
- xfail = test exists but marked xfail pending human input

---

## Tier 1 — Extend existing complete path roots

### Commit 1: LOOKUP (extend)

**Status:** 6/14 routes complete. 8 routes have endpoints but no example/fixture/test.

| Route | Endpoint | Example | Fixture | Test | Action |
|-------|----------|---------|---------|------|--------|
| GET | yes | no | no | no | xfail — needs `lookupType` param |
| ACCESS_KEY | yes | no | no | no | xfail — needs `accessKeyId` param |
| ACCESS_KEYS | yes | yes | yes | yes | done |
| COMON_INSURANCE | yes | no | no | no | add to example, fixture, test |
| CONTACT_TYPES | yes | yes | yes | yes | done |
| COUNTRIES | yes | yes | yes | yes | done |
| DENSITY_CLASS_MAP | yes | yes | yes | yes | done |
| DOCUMENT_TYPES | yes | yes | yes | yes | done |
| ITEMS | yes | no | no | no | xfail — needs `lookupItemType` param |
| PARCEL_PACKAGE_TYPES | yes | yes | yes | yes | done |
| PPCCAMPAIGNS | yes | no | no | no | add to example, fixture, test |
| REFER_CATEGORY | yes | no | no | no | add to example, fixture, test |
| REFER_CATEGORY_HEIRACHY | yes | no | no | no | add to example, fixture, test |
| RESET_MASTER_CONSTANT_CACHE | yes | no | no | no | xfail — POST, side-effecting |

**Work:**
- [ ] Extend `examples/api/lookup.py` — add COMON_INSURANCE, PPCCAMPAIGNS, REFER_CATEGORY, REFER_CATEGORY_HEIRACHY
- [ ] Run example to generate fixtures
- [ ] Extend `tests/api/test_lookup.py` — add fixture+integration tests for new routes
- [ ] Add xfail tests for parameterized GETs (GET, ACCESS_KEY, ITEMS)
- [ ] Add xfail test for RESET_MASTER_CONSTANT_CACHE (POST, side-effecting)
- [ ] Add conftest fixtures for new JSON files

---

### Commit 2: VIEWS (extend)

**Status:** 2/8 routes complete (ALL, DATASETSPS). 6 have endpoints but no example/fixture/test.

| Route | Endpoint | Example | Fixture | Test | Action |
|-------|----------|---------|---------|------|--------|
| DELETE | yes | no | no | no | xfail — destructive |
| GET | yes | no | no | no | xfail — needs `viewId` |
| ACCESSINFO | yes | no | no | no | xfail — needs `viewId` |
| ALL | yes | yes | yes | yes | done |
| DATASETSP | yes | no | no | no | add — use known SP name from fixture |
| DATASETSPS | yes | yes | yes | yes | done |
| POST | yes | no | no | no | xfail — creates data |
| PUT_ACCESS | yes | no | no | no | xfail — needs `viewId` |

**Work:**
- [ ] Extend `examples/api/views.py` — add DATASETSP (pick SP name from ViewsDatasetSps fixture)
- [ ] Run example to generate fixture
- [ ] Add tests for DATASETSP (fixture + integration)
- [ ] Add xfail tests for GET, ACCESSINFO (use VIEW_ID from constants), DELETE, POST, PUT_ACCESS
- [ ] Add conftest fixture for new JSON files

---

### Commit 3: SMSTEMPLATE (extend)

**Status:** 3/6 routes complete. 3 have endpoints but no example/fixture/test.

| Route | Endpoint | Example | Fixture | Test | Action |
|-------|----------|---------|---------|------|--------|
| DELETE | yes | no | no | no | xfail — destructive |
| GET | yes | no | no | no | xfail — needs `templateId` |
| JOB_STATUSES | yes | yes | yes | yes | done |
| LIST | yes | yes | yes | yes | done |
| NOTIFICATION_TOKENS | yes | yes | yes | yes | done |
| SAVE | yes | no | no | no | xfail — creates/modifies data |

**Work:**
- [ ] Add xfail tests for GET (needs templateId from LIST fixture), DELETE, SAVE
- [ ] Note: GET could potentially work with a templateId from the LIST fixture — try integration test

---

### Commit 4: COMPANIES (extend)

**Status:** 4/21+ routes complete. Many need params.

| Route | Endpoint | Action |
|-------|----------|--------|
| GET | yes/done | done |
| GET_AVAILABLE_BY_CURRENT_USER | yes/done | done |
| GET_BRANDS | yes/done | done |
| GET_BRANDSTREE | yes/done | done |
| GET_CAPABILITIES | no | xfail — needs companyId |
| GET_CARRIER_ACOUNTS | no | xfail — needs companyId |
| GET_DETAILS | no | xfail — needs companyId |
| GET_FRANCHISEE_ADDRESSES | no | xfail — needs companyId |
| GET_FULLDETAILS | no | xfail — needs companyId |
| GET_GEOSETTINGS | yes | add — parameterless |
| GET_GEO_AREA_COMPANIES | yes | xfail — HTTP 500 |
| GET_INFO_FROM_KEY | no | xfail — needs accessKey |
| GET_SEARCH | yes | xfail — needs searchValue param |
| GET_SEARCH_CARRIER_ACCOUNTS | yes | xfail — needs searchValue param |
| GET_SUGGEST_CARRIERS | no | xfail — needs params |
| POST_* | no | xfail — all write operations |
| PUT_* | no | xfail — all write operations |

**Work:**
- [ ] Extend `examples/api/companies.py` — add GET_GEOSETTINGS
- [ ] Run example to generate fixture
- [ ] Extend `tests/api/test_companies.py` — add GET_GEOSETTINGS fixture+integration test
- [ ] Add xfail tests for parameterized GET routes using COMPANY_ID from constants
- [ ] Add conftest fixture for new JSON file

---

### Commit 5: CONTACTS (extend)

**Status:** 2/14 routes complete (GET, USER).

| Route | Endpoint | Action |
|-------|----------|--------|
| GET | yes/done | done |
| USER | yes/done | done |
| GET_EDITDETAILS | no | xfail — needs contactId |
| PRIMARYDETAILS | no | xfail — needs contactId |
| HISTORY* | no | xfail — needs contactId |
| CUSTOMERS | no | xfail — needs params |
| SEARCH, V2_SEARCH | no | xfail — needs searchValue |
| POST/PUT/MERGE | no | xfail — write ops |

**Work:**
- [ ] Add xfail tests for parameterized GETs using CONTACT_ID from constants
- [ ] No new example work possible without human providing working call params

---

### Commit 6: DASHBOARD (extend)

**Status:** 2/9 routes complete (GET, GRIDVIEWS).

| Route | Endpoint | Action |
|-------|----------|--------|
| GET | yes/done | done |
| GRIDVIEWS | yes/done | done |
| GRIDVIEWSTATE | no | xfail — needs viewId |
| POST_GRIDVIEWSTATE | no | xfail — write op |
| INBOUND | no | xfail — needs DashboardType |
| INHOUSE | no | xfail — needs DashboardType |
| LOCAL_DELIVERIES | no | xfail — needs DashboardType |
| OUTBOUND | no | xfail — needs DashboardType |
| RECENTESTIMATES | no | xfail — needs DashboardType |

**Work:**
- [ ] Add xfail tests for dashboard type endpoints (INBOUND, INHOUSE, etc.)
- [ ] Human: These may work with DashboardType enum values — try adding to example

---

### Commit 7: ACCOUNT (extend)

**Status:** 1/10 routes complete (GET_PROFILE).

All other routes (POST_CONFIRM, POST_FORGOT, POST_REGISTER, etc.) are write operations that modify authentication state.

**Work:**
- [ ] Add xfail tests for remaining routes — all are destructive/auth-modifying
- [ ] Human: Do NOT test POST_RESETPASSWORD, POST_SETPASSWORD, etc. against staging

---

### Commit 8: USERS (extend)

**Status:** 2/5 routes complete (POCUSERS, ROLES).

| Route | Endpoint | Action |
|-------|----------|--------|
| POCUSERS | yes/done | done |
| ROLES | yes/done | done |
| LIST | no | xfail — needs params |
| USER | no | xfail — needs userId |
| USER_UPDATE | no | xfail — write op, needs userId |

**Work:**
- [ ] Add xfail tests for LIST, USER, USER_UPDATE

---

## Tier 2 — Job sub-endpoints (endpoints exist, need examples/fixtures/tests)

All use `JOB_DISPLAY_ID = "2000000"` from `tests/constants.py`.

### Commit 9: JOB Timeline

**Status:** Endpoints complete. Helpers done (schedule, received, pack_start, etc.). Example exists (`tasks.py`). No test file.

**Work:**
- [ ] Create `tests/api/test_timeline.py`
- [ ] Add integration test: `api.jobs.timeline.get_timeline(JOB_DISPLAY_ID)` → assert TimelineResponse
- [ ] Add fixture validation test for TimelineResponse if fixture exists
- [ ] Add xfail tests for write operations (POST, PATCH, DELETE, increment/undo)
- [ ] Add conftest fixture if `TimelineResponse.json` exists

---

### Commit 10: JOB Core

**Status:** All endpoints have docstrings. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET | add — use JOB_DISPLAY_ID |
| GET_CALENDARITEMS | xfail — needs jobId UUID |
| GET_DOCUMENT_CONFIG | add — parameterless |
| GET_FEEDBACK | xfail — needs jobId |
| GET_JOB_ACCESS_LEVEL | add — use JOB_DISPLAY_ID |
| GET_SEARCH | add — try parameterless |
| GET_UPDATE_PAGE_CONFIG | xfail — needs jobId |
| POST/POST_BOOK/POST_SEARCH_BY_DETAILS/POST_TRANSFER/PUT_SAVE | xfail — write ops |

**Work:**
- [ ] Create `examples/api/job_core.py` — GET, GET_DOCUMENT_CONFIG, GET_JOB_ACCESS_LEVEL
- [ ] Run example to generate fixtures
- [ ] Create `tests/api/test_job_core.py` — fixture+integration tests
- [ ] Add xfail tests for write operations
- [ ] Add conftest fixtures

---

### Commit 11: JOB OnHold

**Status:** All endpoints have docstrings. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_ONHOLD | xfail — needs onHoldId |
| GET_ONHOLD_LIST | add — use JOB_DISPLAY_ID |
| GET_ONHOLD_FOLLOWUPUSER | xfail — needs onHoldId |
| GET_ONHOLD_FOLLOWUPUSERS | xfail — needs params |
| DELETE/POST/PUT_ONHOLD* | xfail — write ops |

**Work:**
- [ ] Create `examples/api/job_onhold.py` — GET_ONHOLD_LIST
- [ ] Run example to generate fixture
- [ ] Create `tests/api/test_job_onhold.py`
- [ ] Add xfail tests for parameterized/write routes

---

### Commit 12: JOB Notes

**Status:** Endpoints exist. No proper example/fixture/test.

| Route | Action |
|-------|--------|
| GET_NOTE | xfail — needs noteId or jobDisplayId (explore) |
| GET_NOTE_LIST | add — use JOB_DISPLAY_ID |
| POST_ITEM_NOTES | xfail — write op, no endpoint |
| POST_NOTE | xfail — write op |
| PUT_NOTE | xfail — write op |

**Work:**
- [ ] Rewrite `examples/api/note.py` — use `_constants`, `_helpers`, proper pattern
- [ ] Try GET_NOTE_LIST with JOB_DISPLAY_ID
- [ ] Create `tests/api/test_job_notes.py`
- [ ] Add conftest fixture if generated

---

### Commit 13: JOB Tracking

**Status:** Endpoints exist. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_TRACKING | xfail — needs jobDisplayId + trackingId |
| GET_TRACKING_SHIPMENT | xfail — needs jobDisplayId + shipmentId |
| GET_SUBMANAGEMENTSTATUS | xfail — no endpoint yet |

**Work:**
- [ ] Create `tests/api/test_job_tracking.py` with xfail tests
- [ ] Human: Need valid trackingId/shipmentId for JOB_DISPLAY_ID 2000000

---

### Commit 14: JOB SMS

**Status:** Endpoints exist. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_SMS | xfail — needs jobDisplayId |
| GET_SMS_TEMPLATEBASED | xfail — needs jobDisplayId + templateId |
| POST_SMS | xfail — write op (sends SMS!) |
| POST_SMS_READ | xfail — write op |

**Work:**
- [ ] Create `tests/api/test_job_sms.py` with xfail tests
- [ ] Human: GET_SMS may work with JOB_DISPLAY_ID — try it

---

### Commit 15: JOB Email

**Status:** Endpoints exist. No examples/fixtures/tests. All POST routes.

All routes are write operations that send emails. All xfail.

**Work:**
- [ ] Create `tests/api/test_job_email.py` with xfail tests
- [ ] Human: Do NOT test email-sending routes against staging without confirmation

---

### Commit 16: JOB RFQ

**Status:** Endpoints exist. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_RFQ | xfail — needs rfqId |
| GET_RFQ_STATUSOF_FORCOMPANY | xfail — needs rfqId + companyId |

**Work:**
- [ ] Create `tests/api/test_job_rfq.py` with xfail tests
- [ ] Human: Need valid rfqId for testing

---

### Commit 17: JOB Payment

**Status:** Endpoints exist. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_PAYMENT | xfail — needs jobDisplayId |
| GET_PAYMENT_CREATE | xfail — needs jobDisplayId |
| GET_PAYMENT_SOURCES | xfail — needs jobDisplayId |
| GET_PRICE | no endpoint | skip |
| POST_PAYMENT_* | xfail — all write/financial ops |

**Work:**
- [ ] Create `tests/api/test_job_payment.py` with xfail tests
- [ ] Human: GET_PAYMENT may work with JOB_DISPLAY_ID — try it

---

### Commit 18: JOB Shipment

**Status:** Endpoints exist. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_SHIPMENT_ACCESSORIALS | xfail — needs jobDisplayId + shipmentId |
| GET_SHIPMENT_EXPORTDATA | xfail — needs jobDisplayId |
| GET_SHIPMENT_ORIGINDESTINATION | xfail — needs jobDisplayId |
| GET_SHIPMENT_RATEQUOTES | xfail — needs jobDisplayId + shipmentId |
| GET_SHIPMENT_RATESSTATE | xfail — needs jobDisplayId + shipmentId |
| DELETE/POST_SHIPMENT_* | xfail — write ops |

**Work:**
- [ ] Create `tests/api/test_job_shipment.py` with xfail tests
- [ ] Human: Need valid shipmentId for JOB_DISPLAY_ID 2000000

---

### Commit 19: JOB FreightProviders

**Status:** Endpoints exist. No examples/fixtures/tests. All need params.

**Work:**
- [ ] Create `tests/api/test_job_freight.py` with xfail tests

---

### Commit 20: JOB ParcelItems

**Status:** Endpoints exist. No examples/fixtures/tests.

| Route | Action |
|-------|--------|
| GET_PARCELITEMS | xfail — needs jobDisplayId |
| GET_PARCEL_ITEMS_WITH_MATERIALS | xfail — needs jobDisplayId |
| GET_PACKAGINGCONTAINERS | no endpoint — skip |
| DELETE/POST_PARCELITEMS | xfail — write ops |

**Work:**
- [ ] Create `tests/api/test_job_parcelitems.py` with xfail tests
- [ ] Human: GET_PARCELITEMS may work with JOB_DISPLAY_ID — try it

---

### Commit 21: JOB Intacct

**Status:** Endpoints exist. No examples/fixtures/tests.

All routes need jobDisplayId and most are write ops (POST, DELETE).

**Work:**
- [ ] Create `tests/api/test_job_intacct.py` with xfail tests

---

### Commit 22: JOB Other (Agent/Status)

**Status:** Agent helpers done. Status endpoint exists. Agent example exists.

| Route | Action |
|-------|--------|
| POST_CHANGE_AGENT | done (agent_helpers.py + example) |
| POST_STATUS_QUOTE | xfail — needs jobDisplayId + quote data |
| PUT_ITEM | xfail — no endpoint, write op |

**Work:**
- [ ] Create `tests/api/test_job_agent.py` — test ChangeAgent_OA fixture against model
- [ ] Add xfail tests for POST_STATUS_QUOTE, PUT_ITEM
- [ ] Add conftest fixture for ChangeAgent_OA.json

---

### Commit 23: DOCUMENTS

**Status:** Endpoints exist. Example exists but is commented out. No fixtures/tests.

| Route | Endpoint | Action |
|-------|----------|--------|
| GET | yes | xfail — needs docPath |
| THUMBNAIL | yes | xfail — needs docPath |
| LIST | yes | add — use JOB_DISPLAY_ID |
| POST | yes | xfail — write op (upload) |
| HIDE | yes | xfail — needs docId, destructive |
| UPDATE | yes | xfail — needs docId, write op |

**Work:**
- [ ] Rewrite `examples/api/documents.py` — use `_constants`, `_helpers`, call LIST
- [ ] Run example to generate fixture
- [ ] Create `tests/api/test_documents.py`
- [ ] Add xfail tests for parameterized/write routes
- [ ] Human: LIST with JOB_DISPLAY_ID should work — try it

---

## Tier 3 — Path roots needing route refactoring + everything

These endpoint files still use hardcoded paths instead of SCHEMA routes.
Each needs: route refactoring, example, fixture, test.

### Commit 24: COMPANY (separate from COMPANIES)

**Status:** 17 routes. No endpoints, examples, fixtures, or tests. All need companyId.

All routes are ❗ human-intervention. All need companyId param.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/company.py` to use SCHEMA routes
- [ ] Create `tests/api/test_company.py` with xfail tests for all routes
- [ ] Human: Need a valid companyId for testing calendar, truck, material, etc.

---

### Commit 25: ADDRESS

**Status:** 4 routes. No endpoints, examples, fixtures, or tests.

| Route | Action |
|-------|--------|
| GET_ISVALID | xfail — needs address params |
| GET_PROPERTYTYPE | xfail — needs address params |
| POST_AVOID_VALIDATION | xfail — write op |
| POST_VALIDATED | xfail — write op |

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/address.py` to use SCHEMA routes
- [ ] Create `tests/api/test_address.py` with xfail tests
- [ ] Human: Provide sample address for validation testing

---

### Commit 26: ADMIN

**Status:** 13 routes. No endpoints, examples, fixtures, or tests.

| Route | Action |
|-------|--------|
| GET_ADVANCEDSETTINGS_ALL | add — parameterless |
| GET_CARRIERERRORMESSAGE_ALL | add — parameterless |
| GET_GLOBALSETTINGS_COMPANYHIERARCHY | add — parameterless |
| All others | xfail — need params or are write ops |

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/admin.py` to use SCHEMA routes
- [ ] Create `examples/api/admin.py` for parameterless GETs
- [ ] Run example to generate fixtures
- [ ] Create `tests/api/test_admin.py`
- [ ] Human: Verify instaquote user has admin permissions for these endpoints

---

### Commit 27: COMMODITY + COMMODITY_MAP

**Status:** 5+5 routes. No endpoints, examples, fixtures, or tests. All need params.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/commodity.py` to use SCHEMA routes
- [ ] Refactor `ABConnect/api/endpoints/commoditymap.py` to use SCHEMA routes
- [ ] Create `tests/api/test_commodity.py` with xfail tests
- [ ] Human: Need sample commodity data for testing

---

### Commit 28: NOTE (standalone, not job-note)

**Status:** 4 routes. No endpoints, examples, fixtures, or tests.

| Route | Action |
|-------|--------|
| GET | add — may work parameterless |
| GET_SUGGEST_USERS | add — may work parameterless |
| POST | xfail — write op |
| PUT | xfail — write op |

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/note.py` to use SCHEMA routes
- [ ] Create `examples/api/notes_standalone.py` — try parameterless GETs
- [ ] Create `tests/api/test_note_standalone.py`
- [ ] Human: Verify GET behavior without params

---

### Commit 29: RFQ (standalone)

**Status:** 7 routes. No endpoints, examples, fixtures, or tests. All need rfqId.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/rfq.py` to use SCHEMA routes
- [ ] Create `tests/api/test_rfq.py` with xfail tests
- [ ] Human: Need valid rfqId for testing

---

### Commit 30: REPORTS

**Status:** 8 routes. No endpoints, examples, fixtures, or tests. All need params (date ranges, etc.).

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/reports.py` to use SCHEMA routes
- [ ] Create `tests/api/test_reports.py` with xfail tests
- [ ] Human: Provide date range and report parameters for testing

---

### Commit 31: E_SIGN

**Status:** 2 routes. No endpoints, examples, fixtures, or tests.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/e_sign.py` to use SCHEMA routes
- [ ] Create `tests/api/test_esign.py` with xfail tests
- [ ] Human: Need valid eSign document ID for testing

---

### Commit 32: EMAIL (standalone)

**Status:** 1 route (LABELREQUEST). No endpoint, example, fixture, or test.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/email.py` to use SCHEMA routes
- [ ] Create `tests/api/test_email_standalone.py` with xfail test
- [ ] Human: This sends email — do NOT test without confirmation

---

### Commit 33: WEBHOOKS

**Status:** 6 routes. No endpoints. All POST routes for external service callbacks.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/webhooks.py` to use SCHEMA routes
- [ ] Create `tests/api/test_webhooks.py` with xfail tests
- [ ] Human: Webhook endpoints receive external callbacks — not testable via API client

---

### Commit 34: V2 + V3

**Status:** 1+1 routes (JOB_TRACKING). No endpoints.

**Work:**
- [ ] Refactor `ABConnect/api/endpoints/v2.py` to use SCHEMA routes
- [ ] Refactor `ABConnect/api/endpoints/v3.py` to use SCHEMA routes
- [ ] Create `tests/api/test_versioned.py` with xfail tests
- [ ] Human: Need jobDisplayId for tracking — may work with JOB_DISPLAY_ID

---

### Commit 35: SHIPMENT (standalone) + PARTNER (extend)

**Status:** SHIPMENT 1/3 complete (ACCESSORIALS). PARTNER 1/2 complete (GET).

| Route | Action |
|-------|--------|
| SHIPMENT.GET | xfail — needs shipmentId |
| SHIPMENT.DOCUMENT | xfail — needs shipmentId + documentId |
| PARTNER.POST_SEARCH | xfail — needs search params |

**Work:**
- [ ] Add xfail tests for remaining SHIPMENT and PARTNER routes
- [ ] No new example work possible without params

---

### Commit 36: NOTIFICATIONS + VALUES (verify complete)

**Status:** Both 1/1 complete. Just verify.

**Work:**
- [ ] Verify tests pass
- [ ] No changes needed

---

## xfail Test Pattern

When a route cannot be tested automatically, create an xfail test with instructions:

```python
@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.jobs.tracking.get_tracking(jobDisplayId, trackingId) "
    "with valid IDs. Save fixture via save_fixture(result, 'JobTracking'). "
    "Then remove xfail and add fixture validation test."
))
def test_get_tracking(api):
    """get_tracking returns tracking details"""
    from tests.constants import JOB_DISPLAY_ID
    result = api.jobs.tracking.get_tracking(
        jobDisplayId=JOB_DISPLAY_ID, trackingId="NEED_VALID_ID"
    )
    assert result is not None
```

---

## Summary

| Tier | Commits | Automatable | xfail-only |
|------|---------|-------------|------------|
| Tier 1 (extend existing) | 1-8 | ~12 new routes | ~25 routes |
| Tier 2 (job sub-endpoints) | 9-23 | ~8 new routes | ~60 routes |
| Tier 3 (route refactor + everything) | 24-36 | ~5 new routes | ~50 routes |
| **Total** | **36 commits** | **~25 routes** | **~135 routes** |

**Already complete:** ~36 routes across all path roots.
**Total tracked:** ~220 routes.

---

## Execution Order

Start with Tier 1 (highest value, most can be automated), then Tier 2, then Tier 3.
Within each tier, do automatable work first, xfail-only work last.
Each commit message: `feat(<path-root>): add examples, fixtures, and tests`
