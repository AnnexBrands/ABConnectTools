# Swagger 708 vs 709 Breaking Changes Report

## Executive Summary

| Metric | 708 | 709 | Change |
|--------|-----|-----|--------|
| Total Paths | 227 | 257 | +30 |
| Removed Paths | - | - | 4 |
| Added Paths | - | - | 34 |
| Total Schemas | 299 | 330 | +31 |
| Removed Schemas | - | - | 9 |
| Added Schemas | - | - | 40 |

---

## Breaking Changes (Requiring Code Updates)

### 1. Removed Endpoints

These endpoints have been removed and must be migrated:

| Old Endpoint | Methods | Replacement |
|--------------|---------|-------------|
| `/api/dashboard/gridsettings` | GET, POST | `/api/company/{companyId}/gridsettings` |
| `/api/dashboard/incrementjobstatus` | POST | `/api/job/{jobDisplayId}/timeline/incrementjobstatus` |
| `/api/dashboard/undoincrementjobstatus` | POST | `/api/job/{jobDisplayId}/timeline/undoincrementjobstatus` |
| `/api/job/{jobDisplayId}/form/{formid}` | GET | Multiple specific form endpoints (see below) |

### 2. Form Endpoint Migration

The generic form endpoint has been replaced with type-specific endpoints:

**Old (708):**
```
GET /api/job/{jobDisplayId}/form/{formid}
```

**New (709) - Specific form endpoints:**
- `GET /api/job/{jobDisplayId}/form/address-label`
- `GET /api/job/{jobDisplayId}/form/bill-of-lading`
- `GET /api/job/{jobDisplayId}/form/credit-card-authorization`
- `GET /api/job/{jobDisplayId}/form/customer-quote`
- `GET /api/job/{jobDisplayId}/form/invoice`
- `GET /api/job/{jobDisplayId}/form/invoice/editable`
- `GET /api/job/{jobDisplayId}/form/item-labels`
- `GET /api/job/{jobDisplayId}/form/operations`
- `GET /api/job/{jobDisplayId}/form/packaging-labels`
- `GET /api/job/{jobDisplayId}/form/packaging-specification`
- `GET /api/job/{jobDisplayId}/form/packing-slip`
- `GET /api/job/{jobDisplayId}/form/quick-sale`
- `GET /api/job/{jobDisplayId}/form/shipments` (already exists)
- `GET /api/job/{jobDisplayId}/form/usar`
- `GET /api/job/{jobDisplayId}/form/usar/editable`

### 3. Schema Changes (Breaking)

#### `Commodity` - Complete Restructure
**Removed properties:**
- `scheduleBNumber`
- `countryId`
- `unitPrice`
- `specialMarks`
- `weight`
- `exportLicenseCode`
- `countryIATACode`
- `unitOfMeasure`
- `eccn`
- `fullDescription`
- `quantity`
- `itemValue`

**Added properties:**
- `id`
- `code`
- `name`
- `parentId`
- `isActive`

#### `IncrementJobStatusInputModel`
- **REMOVED:** `jobId` property (now passed via URL path parameter)

#### `SaveGridSettingsModel`
- **REMOVED:** `companyId` property (now passed via URL path parameter)

#### `FranchiseeCarrierAccounts`
- **REMOVED:** `pilot`
- **Added:** `maersk`

---

## Non-Breaking Additions

### New Endpoints (34 total)

#### Commodity Management (New Feature)
- `POST /api/commodity` - Create commodity
- `GET /api/commodity/{id}` - Get commodity
- `PUT /api/commodity/{id}` - Update commodity
- `POST /api/commodity/search` - Search commodities
- `POST /api/commodity/suggestions` - Get commodity suggestions

#### Commodity Mapping (New Feature)
- `POST /api/commodity-map` - Create mapping
- `GET /api/commodity-map/{id}` - Get mapping
- `PUT /api/commodity-map/{id}` - Update mapping
- `DELETE /api/commodity-map/{id}` - Delete mapping
- `POST /api/commodity-map/search` - Search mappings

#### Company Materials (New Feature)
- `GET /api/company/{companyId}/material` - List materials
- `POST /api/company/{companyId}/material` - Create material
- `PUT /api/company/{companyId}/material/{materialId}` - Update material
- `DELETE /api/company/{companyId}/material/{materialId}` - Delete material

#### Partner Management (New Feature)
- `GET /api/partner` - List partners
- `GET /api/partner/{id}` - Get partner
- `POST /api/partner/search` - Search partners

#### Job Item Updates
- `PUT /api/job/{jobDisplayId}/item/{itemId}` - Update job item

#### SMS Features
- `POST /api/job/{jobDisplayId}/sms/read` - Mark SMS as read

#### Carrier Suggestions
- `GET /api/companies/suggest-carriers` - Get carrier suggestions

#### Webhook Endpoints
- `POST /api/webhooks/twilio/body-sms-inbound` - Twilio body SMS webhook
- `POST /api/webhooks/twilio/form-sms-inbound` - Twilio form SMS webhook

### New Schemas (40 total)

Key additions:
- `CommodityDetails`, `CommodityWithParents`, `CommodityMap`, `CommodityMapDetails`
- `CompanyMaterial`, `SaveCompanyMaterialModel`
- `Partner`, `PartnerServiceResponse`
- `FormType`, `OperationsFormType`
- `MaerskAccountData` (replaces `PilotAccountData`)
- `MarkSmsAsReadModel`
- Various Agent view records for dashboard

### Schema Property Additions (Non-Breaking)

| Schema | New Property |
|--------|--------------|
| `CalendarJob` | `unreadSMSCount` |
| `CompanyHierarchyInfo` | `mapsMarkerImage` |
| `Items` | `commodityId`, `doNotTip` |
| `JobContactDetails` | `propertyType` |
| `SearchCustomerInfo` | `phoneNumber` |
| `SearchJobFilter` | `quickSearchText` |

---

## Removed Schemas

These schemas are no longer in the spec:
- `InboundNewDashboardItem`
- `InhouseNewDashboardItem`
- `LocalDeliveriesNewDashboardItem`
- `OutboundNewDashboardItem`
- `RecentEstimatesNewDashboardItem`
- `KnownFormId` (replaced by `FormType`)
- `PilotAccountData` (replaced by `MaerskAccountData`)
- `TwilioSmsStatusCallback`
- `UndoIncrementJobStatusInputModel`

---

## Implementation Impact Analysis

### Currently Implemented (Requires Update)

| File | Affected Method | Action Required |
|------|-----------------|-----------------|
| `ABConnect/api/endpoints/dashboard.py:172` | `post_incrementjobstatus()` | Migrate to job timeline endpoint |
| `ABConnect/api/endpoints/dashboard.py:185` | `post_undoincrementjobstatus()` | Migrate to job timeline endpoint |
| `ABConnect/api/endpoints/dashboard.py:198` | `get_gridsettings()` | Migrate to company endpoint |
| `ABConnect/api/endpoints/dashboard.py:216` | `post_gridsettings()` | Migrate to company endpoint |
| `ABConnect/api/endpoints/jobs/form.py:31` | `get_form()` | Replace with specific form methods |

### Migration Strategy

1. **Deprecate** old methods with warnings
2. **Add** new methods for 709 endpoints
3. **Create** compatibility layer that:
   - Maps old `get_form(formId)` calls to specific form methods
   - Maps old `post_incrementjobstatus(data)` to new path-based endpoint
4. **Update** tests and examples
5. **Document** migration path for users

---

## Recommended Action Items

- [ ] Add new endpoint class for `/api/company/{companyId}/gridsettings`
- [ ] Add new endpoint class for `/api/job/{jobDisplayId}/timeline/`
- [ ] Expand `JobFormEndpoint` with 14 new specific form methods
- [ ] Add `CommodityEndpoint` for new commodity management
- [ ] Add `CommodityMapEndpoint` for commodity mapping
- [ ] Add `PartnerEndpoint` for partner management
- [ ] Add `CompanyMaterialEndpoint` for company materials
- [ ] Update `Items` model with `commodityId` and `doNotTip`
- [ ] Deprecate old dashboard methods with version warnings
- [ ] Create Pydantic models for new schemas
