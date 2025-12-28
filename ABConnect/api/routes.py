"""Route definitions with Python 3.14 template string support.

Example:
    GET_CONTACT = Route[None, ContactDetails](
        template=t"/{id}",
        response_model=ContactDetails,
    )

    bound = GET_CONTACT.bind(id="123")
    print(bound.url)  # "/{id}" interpolated to "/123"
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Route:
    """
    Attributes:
        method: HTTP method
        template: Path
        request_model: Pydantic model for request body, or None
        response_model: Pydantic model for response
        params: Bound path parameters
    """

    method: str
    path: str
    request_model: type | None = None
    response_model: type | None = None
    params: dict[str, str] = field(default_factory=dict)

    @property
    def url(self) -> str:
        """Return interpolated path."""
        return self.path.format(**self.params)


SCHEMA = {
    # commodity
    # commoditymap
    # companies
    # company
    # dashboard
    # documents
    # e_sign
    # email
    # jobintacct
    # jobs
    # lookup
    # note
    # notifications
    # partner
    # reports
    # rfq
    "ACCOUNT": {
        "DELETE_ACCOUNT_PAYMENTSOURCE": Route(
            "DELETE", "/account/paymentsource/{sourceId}", None, {}
        ),
        "GET_ACCOUNT_PROFILE": Route("GET", "/account/profile", None, {}),
        "GET_ACCOUNT_VERIFYRESETTOKEN": Route(
            "GET", "/account/verifyresettoken", None, {}
        ),
    },
    "ADMIN": {
        "DELETE_ADMIN_ADVANCEDSETTINGS": Route(
            "DELETE", "/admin/advancedsettings/{id}", None, {}
        )
    },
    "DELETE_COMMODITY_MAP": Route(
        "DELETE", "/commodity-map/{id}", None, "ServiceBaseResponse", {}
    ),
    "DELETE_COMPANY_ACCOUNTS_STRIPE": Route(
        "DELETE", "/company/{companyId}/accounts/stripe", None, {}
    ),
    "DELETE_COMPANY_CONTAINERTHICKNESSINCHES": Route(
        "DELETE", "/company/{companyId}/containerthicknessinches", None, {}
    ),
    "DELETE_COMPANY_MATERIAL": Route(
        "DELETE", "/company/{companyId}/material/{materialId}", None, {}
    ),
    "DELETE_COMPANY_TRUCK": Route(
        "DELETE",
        "/company/{companyId}/truck/{truckId}",
        None,
        "ServiceWarningResponse",
        {},
    ),
    "DELETE_JOBINTACCT": Route(
        "DELETE", "/jobintacct/{jobDisplayId}/{franchiseeId}", None, {}
    ),
    "DELETE_JOB_ONHOLD": Route("DELETE", "/job/{jobDisplayId}/onhold", None, {}),
    "DELETE_JOB_PARCELITEMS": Route(
        "DELETE", "/job/{jobDisplayId}/parcelitems/{parcelItemId}", None, {}
    ),
    "DELETE_JOB_SHIPMENT": Route(
        "DELETE", "/job/{jobDisplayId}/shipment", "DeleteShipRequestModel", {}
    ),
    "DELETE_JOB_SHIPMENT_ACCESSORIAL": Route(
        "DELETE", "/job/{jobDisplayId}/shipment/accessorial/{addOnId}", None, {}
    ),
    "DELETE_JOB_TIMELINE": Route(
        "DELETE",
        "/job/{jobDisplayId}/timeline/{timelineTaskId}",
        None,
        "DeleteTaskResponse",
        {},
    ),
    "DELETE_SMS_TEMPLATE": Route("DELETE", "/SmsTemplate/{templateId}", None, {}),
    "DELETE_VIEWS": Route("DELETE", "/views/{viewId}", None, {}),
    "GET_ADDRESS_ISVALID": Route(
        "GET", "/address/isvalid", None, "AddressIsValidResult", {}
    ),
    "GET_ADDRESS_PROPERTYTYPE": Route(
        "GET", "/address/propertytype", None, "PropertyType", {}
    ),
    "GET_ADMIN_ADVANCEDSETTINGS": Route(
        "GET", "/admin/advancedsettings/{id}", None, {}
    ),
    "GET_ADMIN_ADVANCEDSETTINGS_ALL": Route(
        "GET", "/admin/advancedsettings/all", None, {}
    ),
    "GET_ADMIN_CARRIERERRORMESSAGE_ALL": Route(
        "GET", "/admin/carriererrormessage/all", None, {}
    ),
    "GET_ADMIN_GLOBALSETTINGS_COMPANYHIERARCHY": Route(
        "GET",
        "/admin/globalsettings/companyhierarchy",
        None,
        "CompanyHierarchyInfo",
        {},
    ),
    "GET_ADMIN_GLOBALSETTINGS_COMPANYHIERARCHY_COMPANY": Route(
        "GET",
        "/admin/globalsettings/companyhierarchy/company/{companyId}",
        None,
        "CompanyHierarchyInfo",
        {},
    ),
    "GET_COMMODITY": Route(
        "GET", "/commodity/{id}", None, "CommodityWithParentsServiceResponse", {}
    ),
    "GET_COMMODITY_MAP": Route(
        "GET", "/commodity-map/{id}", None, "CommodityMapDetailsServiceResponse", {}
    ),
    "GET_COMPANIES": Route("GET", "/companies/{id}", None, {}),
    "GET_COMPANIES_AVAILABLE_BY_CURRENT_USER": Route(
        "GET", "/companies/availableByCurrentUser", None, {}
    ),
    "GET_COMPANIES_BRANDS": Route("GET", "/companies/brands", None, {}),
    "GET_COMPANIES_BRANDSTREE": Route("GET", "/companies/brandstree", None, {}),
    "GET_COMPANIES_CAPABILITIES": Route(
        "GET", "/companies/{companyId}/capabilities", None, {}
    ),
    "GET_COMPANIES_CARRIER_ACOUNTS": Route(
        "GET", "/companies/{companyId}/carrierAcounts", None, {}
    ),
    "GET_COMPANIES_DETAILS": Route("GET", "/companies/{companyId}/details", None, {}),
    "GET_COMPANIES_FRANCHISEE_ADDRESSES": Route(
        "GET",
        "/companies/{companyId}/franchiseeAddresses",
        None,
        "List[CompanyAddressInfo",
        {},
    ),
    "GET_COMPANIES_FULLDETAILS": Route(
        "GET", "/companies/{companyId}/fulldetails", None, "CompanyDetails", {}
    ),
    "GET_COMPANIES_GEOSETTINGS": Route("GET", "/companies/geosettings", None, {}),
    "GET_COMPANIES_GEO_AREA_COMPANIES": Route(
        "GET", "/companies/geoAreaCompanies", None, {}
    ),
    "GET_COMPANIES_INFO_FROM_KEY": Route("GET", "/companies/infoFromKey", None, {}),
    "GET_COMPANIES_INHERITEDPACKAGINGLABOR": Route(
        "GET", "/companies/{companyId}/inheritedpackaginglabor", None, {}
    ),
    "GET_COMPANIES_INHERITED_PACKAGING_TARIFFS": Route(
        "GET", "/companies/{companyId}/inheritedPackagingTariffs", None, {}
    ),
    "GET_COMPANIES_PACKAGINGLABOR": Route(
        "GET", "/companies/{companyId}/packaginglabor", None, {}
    ),
    "GET_COMPANIES_PACKAGINGSETTINGS": Route(
        "GET", "/companies/{companyId}/packagingsettings", None, {}
    ),
    "GET_COMPANIES_SEARCH": Route("GET", "/companies/search", None, {}),
    "GET_COMPANIES_SEARCH_CARRIER_ACCOUNTS": Route(
        "GET", "/companies/search/carrier-accounts", None, {}
    ),
    "GET_COMPANIES_SUGGEST_CARRIERS": Route(
        "GET", "/companies/suggest-carriers", None, "List[CarrierCompanyInfo", {}
    ),
    "GET_COMPANY_ACCOUNTS_STRIPE_CONNECTURL": Route(
        "GET", "/company/{companyId}/accounts/stripe/connecturl", None, {}
    ),
    "GET_COMPANY_CALENDAR": Route(
        "GET", "/company/{companyId}/calendar/{date}", None, "Calendar", {}
    ),
    "GET_COMPANY_CALENDAR_BASEINFO": Route(
        "GET",
        "/company/{companyId}/calendar/{date}/baseinfo",
        None,
        "BaseInfoCalendar",
        {},
    ),
    "GET_COMPANY_CALENDAR_ENDOFDAY": Route(
        "GET", "/company/{companyId}/calendar/{date}/endofday", None, {}
    ),
    "GET_COMPANY_CALENDAR_STARTOFDAY": Route(
        "GET", "/company/{companyId}/calendar/{date}/startofday", None, {}
    ),
    "GET_COMPANY_CONTAINERTHICKNESSINCHES": Route(
        "GET",
        "/company/{companyId}/containerthicknessinches",
        None,
        "List[ContainerThickness",
        {},
    ),
    "GET_COMPANY_GRIDSETTINGS": Route(
        "GET", "/company/{companyId}/gridsettings", None, "GridSettingsEntity", {}
    ),
    "GET_COMPANY_MATERIAL": Route(
        "GET", "/company/{companyId}/material", None, "List[CompanyMaterial", {}
    ),
    "GET_COMPANY_PLANNER": Route(
        "GET", "/company/{companyId}/planner", None, "List[PlannerTask", {}
    ),
    "GET_COMPANY_SETUPDATA": Route(
        "GET", "/company/{companyId}/setupdata", None, "CompanySetupData", {}
    ),
    "GET_COMPANY_TRUCK": Route(
        "GET", "/company/{companyId}/truck", None, "List[Truck", {}
    ),
    # contacts
    "GET_CONTACTS": Route("GET", "/contacts/{id}", None, {}),
    "GET_CONTACTS_EDITDETAILS": Route(
        "GET", "/contacts/{contactId}/editdetails", None, "ContactDetailedInfo", {}
    ),
    "GET_CONTACTS_HISTORY_AGGREGATED": Route(
        "GET",
        "/contacts/{contactId}/history/aggregated",
        None,
        "ContactHistoryAggregatedCost",
        {},
    ),
    "GET_CONTACTS_HISTORY_GRAPHDATA": Route(
        "GET",
        "/contacts/{contactId}/history/graphdata",
        None,
        "ContactHistoryGraphData",
        {},
    ),
    "GET_CONTACTS_PRIMARYDETAILS": Route(
        "GET", "/contacts/{contactId}/primarydetails", None, "ContactPrimaryDetails", {}
    ),
    "GET_CONTACTS_USER": Route("GET", "/contacts/user", None, {}),
    "GET_DASHBOARD": Route("GET", "/dashboard", None, {}),
    "GET_DASHBOARD_GRIDVIEWS": Route("GET", "/dashboard/gridviews", None, {}),
    "GET_DASHBOARD_GRIDVIEWSTATE": Route(
        "GET", "/dashboard/gridviewstate/{id}", None, {}
    ),
    "GET_DOCUMENTS_GET": Route("GET", "/documents/get/{docPath}", None, {}),
    "GET_DOCUMENTS_GET_THUMBNAIL": Route(
        "GET", "/documents/get/thumbnail/{docPath}", None, {}
    ),
    "GET_DOCUMENTS_LIST": Route("GET", "/documents/list", None, {}),
    "GET_E_SIGN": Route("GET", "/e-sign/{jobDisplayId}/{bookingKey}", None, {}),
    "GET_E_SIGN_RESULT": Route("GET", "/e-sign/result", None, {}),
    "GET_JOB": Route("GET", "/job/{jobDisplayId}", None, {}),
    "GET_JOBINTACCT": Route("GET", "/jobintacct/{jobDisplayId}", None, {}),
    "GET_JOB_CALENDARITEMS": Route(
        "GET", "/job/{jobDisplayId}/calendaritems", None, {}
    ),
    "GET_JOB_DOCUMENT_CONFIG": Route("GET", "/job/documentConfig", None, {}),
    "GET_JOB_FEEDBACK": Route("GET", "/job/feedback/{jobDisplayId}", None, {}),
    "GET_JOB_FORM_ADDRESS_LABEL": Route(
        "GET", "/job/{jobDisplayId}/form/address-label", None, {}
    ),
    "GET_JOB_FORM_BILL_OF_LADING": Route(
        "GET", "/job/{jobDisplayId}/form/bill-of-lading", None, {}
    ),
    "GET_JOB_FORM_CREDIT_CARD_AUTHORIZATION": Route(
        "GET", "/job/{jobDisplayId}/form/credit-card-authorization", None, {}
    ),
    "GET_JOB_FORM_CUSTOMER_QUOTE": Route(
        "GET", "/job/{jobDisplayId}/form/customer-quote", None, {}
    ),
    "GET_JOB_FORM_INVOICE": Route("GET", "/job/{jobDisplayId}/form/invoice", None, {}),
    "GET_JOB_FORM_INVOICE_EDITABLE": Route(
        "GET",
        "/job/{jobDisplayId}/form/invoice/editable",
        None,
        "USAREditableFormResponseModel",
        {},
    ),
    "GET_JOB_FORM_ITEM_LABELS": Route(
        "GET", "/job/{jobDisplayId}/form/item-labels", None, {}
    ),
    "GET_JOB_FORM_OPERATIONS": Route(
        "GET", "/job/{jobDisplayId}/form/operations", None, {}
    ),
    "GET_JOB_FORM_PACKAGING_LABELS": Route(
        "GET", "/job/{jobDisplayId}/form/packaging-labels", None, {}
    ),
    "GET_JOB_FORM_PACKAGING_SPECIFICATION": Route(
        "GET", "/job/{jobDisplayId}/form/packaging-specification", None, {}
    ),
    "GET_JOB_FORM_PACKING_SLIP": Route(
        "GET", "/job/{jobDisplayId}/form/packing-slip", None, {}
    ),
    "GET_JOB_FORM_QUICK_SALE": Route(
        "GET", "/job/{jobDisplayId}/form/quick-sale", None, {}
    ),
    "GET_JOB_FORM_SHIPMENTS": Route(
        "GET", "/job/{jobDisplayId}/form/shipments", None, "List[FormsShipmentPlan", {}
    ),
    "GET_JOB_FORM_USAR": Route("GET", "/job/{jobDisplayId}/form/usar", None, {}),
    "GET_JOB_FORM_USAR_EDITABLE": Route(
        "GET",
        "/job/{jobDisplayId}/form/usar/editable",
        None,
        "USAREditableFormResponseModel",
        {},
    ),
    "GET_JOB_FREIGHTPROVIDERS": Route(
        "GET",
        "/job/{jobDisplayId}/freightproviders",
        None,
        "List[PricedFreightProvider",
        {},
    ),
    "GET_JOB_JOB_ACCESS_LEVEL": Route("GET", "/job/jobAccessLevel", None, {}),
    "GET_JOB_NOTE": Route(
        "GET", "/job/{jobDisplayId}/note/{id}", None, "JobTaskNote", {}
    ),
    "GET_JOB_ONHOLD": Route(
        "GET", "/job/{jobDisplayId}/onhold/{id}", None, "OnHoldDetails", {}
    ),
    "GET_JOB_ONHOLD_FOLLOWUPUSER": Route(
        "GET",
        "/job/{jobDisplayId}/onhold/followupuser/{contactId}",
        None,
        "OnHoldUser",
        {},
    ),
    "GET_JOB_ONHOLD_FOLLOWUPUSERS": Route(
        "GET", "/job/{jobDisplayId}/onhold/followupusers", None, "List[OnHoldUser", {}
    ),
    "GET_JOB_PACKAGINGCONTAINERS": Route(
        "GET", "/job/{jobDisplayId}/packagingcontainers", None, "List[Packaging", {}
    ),
    "GET_JOB_PARCELITEMS": Route(
        "GET", "/job/{jobDisplayId}/parcelitems", None, "List[ParcelItemWithPackage", {}
    ),
    "GET_JOB_PARCEL_ITEMS_WITH_MATERIALS": Route(
        "GET",
        "/job/{jobDisplayId}/parcel-items-with-materials",
        None,
        "List[ParcelItemWithMaterials",
        {},
    ),
    "GET_JOB_PAYMENT": Route("GET", "/job/{jobDisplayId}/payment", None, {}),
    "GET_JOB_PAYMENT_CREATE": Route(
        "GET", "/job/{jobDisplayId}/payment/create", None, {}
    ),
    "GET_JOB_PAYMENT_SOURCES": Route(
        "GET", "/job/{jobDisplayId}/payment/sources", None, {}
    ),
    "GET_JOB_PRICE": Route("GET", "/job/{jobDisplayId}/price", None, {}),
    "GET_JOB_RFQ": Route(
        "GET", "/job/{jobDisplayId}/rfq", None, "List[QuoteRequestDisplayInfo", {}
    ),
    "GET_JOB_RFQ_STATUSOF_FORCOMPANY": Route(
        "GET",
        "/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}",
        None,
        "QuoteRequestStatus",
        {},
    ),
    "GET_JOB_SEARCH": Route("GET", "/job/search", None, {}),
    "GET_JOB_SHIPMENT_ACCESSORIALS": Route(
        "GET",
        "/job/{jobDisplayId}/shipment/accessorials",
        None,
        "List[JobParcelAddOn",
        {},
    ),
    "GET_JOB_SHIPMENT_EXPORTDATA": Route(
        "GET", "/job/{jobDisplayId}/shipment/exportdata", None, {}
    ),
    "GET_JOB_SHIPMENT_ORIGINDESTINATION": Route(
        "GET",
        "/job/{jobDisplayId}/shipment/origindestination",
        None,
        "ShipmentOriginDestination",
        {},
    ),
    "GET_JOB_SHIPMENT_RATEQUOTES": Route(
        "GET",
        "/job/{jobDisplayId}/shipment/ratequotes",
        None,
        "JobCarrierRatesModel",
        {},
    ),
    "GET_JOB_SHIPMENT_RATESSTATE": Route(
        "GET", "/job/{jobDisplayId}/shipment/ratesstate", None, {}
    ),
    "GET_JOB_SMS": Route("GET", "/job/{jobDisplayId}/sms", None, {}),
    "GET_JOB_SMS_TEMPLATEBASED": Route(
        "GET", "/job/{jobDisplayId}/sms/templatebased/{templateId}", None, {}
    ),
    "GET_JOB_SUBMANAGEMENTSTATUS": Route(
        "GET", "/job/{jobDisplayId}/submanagementstatus", None, {}
    ),
    "GET_JOB_TIMELINE": Route(
        "GET",
        "/job/{jobDisplayId}/timeline/{timelineTaskIdentifier}",
        None,
        "CarrierTask",
        {},
    ),
    "GET_JOB_TIMELINE_AGENT": Route(
        "GET",
        "/job/{jobDisplayId}/timeline/{taskCode}/agent",
        None,
        "CompanyListItem",
        {},
    ),
    "GET_JOB_TRACKING": Route("GET", "/job/{jobDisplayId}/tracking", None, {}),
    "GET_JOB_TRACKING_SHIPMENT": Route(
        "GET",
        "/job/{jobDisplayId}/tracking/shipment/{proNumber}",
        None,
        "ShipmentTrackingDetails",
        {},
    ),
    "GET_JOB_UPDATE_PAGE_CONFIG": Route(
        "GET", "/job/{jobDisplayId}/updatePageConfig", None, "JobUpdatePageConfig", {}
    ),
    "GET_LOOKUP": Route("GET", "/lookup/{masterConstantKey}/{valueId}", None, {}),
    "GET_LOOKUP_ACCESS_KEY": Route("GET", "/lookup/accessKey/{accessKey}", None, {}),
    "GET_LOOKUP_ACCESS_KEYS": Route("GET", "/lookup/accessKeys", None, {}),
    "GET_LOOKUP_COMON_INSURANCE": Route("GET", "/lookup/comonInsurance", None, {}),
    "GET_LOOKUP_CONTACT_TYPES": Route(
        "GET", "/lookup/contactTypes", None, "List[ContactTypeEntity", {}
    ),
    "GET_LOOKUP_COUNTRIES": Route(
        "GET", "/lookup/countries", None, "List[CountryCodeDto", {}
    ),
    "GET_LOOKUP_DENSITY_CLASS_MAP": Route(
        "GET", "/lookup/densityClassMap", None, "List[GuidSequentialRangeValue", {}
    ),
    "GET_LOOKUP_DOCUMENT_TYPES": Route("GET", "/lookup/documentTypes", None, {}),
    "GET_LOOKUP_ITEMS": Route("GET", "/lookup/items", None, {}),
    "GET_LOOKUP_PARCEL_PACKAGE_TYPES": Route(
        "GET", "/lookup/parcelPackageTypes", None, {}
    ),
    "GET_LOOKUP_PPCCAMPAIGNS": Route("GET", "/lookup/PPCCampaigns", None, {}),
    "GET_LOOKUP_REFER_CATEGORY": Route("GET", "/lookup/referCategory", None, {}),
    "GET_LOOKUP_REFER_CATEGORY_HEIRACHY": Route(
        "GET", "/lookup/referCategoryHeirachy", None, {}
    ),
    "GET_LOOKUP_RESET_MASTER_CONSTANT_CACHE": Route(
        "GET", "/lookup/resetMasterConstantCache", None, {}
    ),
    "GET_NOTE": Route("GET", "/note", None, "List[Notes", {}),
    "GET_NOTE_SUGGEST_USERS": Route(
        "GET", "/note/suggestUsers", None, "List[SuggestedContactEntity", {}
    ),
    "GET_NOTIFICATIONS": Route("GET", "/notifications", None, {}),
    "GET_PARTNER": Route("GET", "/partner", None, "List[Partner", {}),
    "GET_RFQ": Route("GET", "/rfq/{rfqId}", None, {}),
    "GET_RFQ_FORJOB": Route("GET", "/rfq/forjob/{jobId}", None, {}),
    "GET_SHIPMENT": Route("GET", "/shipment", None, "ShipmentDetails", {}),
    "GET_SHIPMENT_ACCESSORIALS": Route("GET", "/shipment/accessorials", None, {}),
    "GET_SHIPMENT_DOCUMENT": Route(
        "GET", "/shipment/document/{docId}", None, "ShippingDocument", {}
    ),
    "GET_SMS_TEMPLATE": Route("GET", "/SmsTemplate/{templateId}", None, {}),
    "GET_SMS_TEMPLATE_JOB_STATUSES": Route("GET", "/SmsTemplate/jobStatuses", None, {}),
    "GET_SMS_TEMPLATE_LIST": Route("GET", "/SmsTemplate/list", None, {}),
    "GET_SMS_TEMPLATE_NOTIFICATION_TOKENS": Route(
        "GET", "/SmsTemplate/notificationTokens", None, {}
    ),
    "GET_USERS_POCUSERS": Route("GET", "/users/pocusers", None, {}),
    "GET_USERS_ROLES": Route("GET", "/users/roles", None, {}),
    "GET_V2_JOB_TRACKING": Route(
        "GET", "/v2/job/{jobDisplayId}/tracking/{historyAmount}", None, {}
    ),
    "GET_V3_JOB_TRACKING": Route(
        "GET",
        "/v3/job/{jobDisplayId}/tracking/{historyAmount}",
        None,
        "JobTrackingResponseV3",
        {},
    ),
    "GET_VALUES": Route("GET", "/Values", None, {}),
    "GET_VIEWS": Route("GET", "/views/{viewId}", None, {}),
    "GET_VIEWS_ACCESSINFO": Route("GET", "/views/{viewId}/accessinfo", None, {}),
    "GET_VIEWS_ALL": Route("GET", "/views/all", None, {}),
    "GET_VIEWS_DATASETSP": Route("GET", "/views/datasetsp/{spName}", None, {}),
    "GET_VIEWS_DATASETSPS": Route("GET", "/views/datasetsps", None, {}),
    "PATCH_JOB_TIMELINE": Route(
        "PATCH", "/job/{jobDisplayId}/timeline/{timelineTaskId}", "UpdateTaskModel", {}
    ),
    "POST_ACCOUNT_CONFIRM": Route("POST", "/account/confirm", "ConfirmEmailModel", {}),
    "POST_ACCOUNT_FORGOT": Route("POST", "/account/forgot", "ForgotLoginModel", {}),
    "POST_ACCOUNT_REGISTER": Route(
        "POST", "/account/register", "RegistrationModel", {}
    ),
    "POST_ACCOUNT_RESETPASSWORD": Route(
        "POST", "/account/resetpassword", "ResetPasswordModel", {}
    ),
    "POST_ACCOUNT_SEND_CONFIRMATION": Route(
        "POST", "/account/sendConfirmation", None, {}
    ),
    "POST_ACCOUNT_SETPASSWORD": Route(
        "POST", "/account/setpassword", "ChangePasswordModel", {}
    ),
    "POST_ADDRESS_AVOID_VALIDATION": Route(
        "POST", "/address/{addressId}/avoidValidation", None, {}
    ),
    "POST_ADDRESS_VALIDATED": Route(
        "POST", "/address/{addressId}/validated", "SaveValidatedRequest", {}
    ),
    "POST_ADMIN_ADVANCEDSETTINGS": Route(
        "POST", "/admin/advancedsettings", "AdvancedSettingsEntitySaveModel", {}
    ),
    "POST_ADMIN_CARRIERERRORMESSAGE": Route(
        "POST", "/admin/carriererrormessage", "CarrierErrorMessage", {}
    ),
    "POST_ADMIN_GLOBALSETTINGS_APPROVEINSURANCEEXCEPTION": Route(
        "POST", "/admin/globalsettings/approveinsuranceexception", None, {}
    ),
    "POST_ADMIN_GLOBALSETTINGS_GETINSURANCEEXCEPTIONS": Route(
        "POST",
        "/admin/globalsettings/getinsuranceexceptions",
        "WebApiDataSourceLoadOptions",
        "List[SelectApproveInsuranceResult]",
        {},
    ),
    "POST_ADMIN_GLOBALSETTINGS_INTACCT": Route(
        "POST", "/admin/globalsettings/intacct", "WebApiDataSourceLoadOptions", {}
    ),
    "POST_ADMIN_LOGBUFFER_FLUSH": Route("POST", "/admin/logbuffer/flush", None, {}),
    "POST_ADMIN_LOGBUFFER_FLUSH_ALL": Route(
        "POST", "/admin/logbuffer/flushAll", None, {}
    ),
    "POST_COMMODITY": Route(
        "POST", "/commodity", "AddCommodityModel", "CommodityServiceResponse", {}
    ),
    "POST_COMMODITY_MAP": Route(
        "POST",
        "/commodity-map",
        "AddCommodityMapModel",
        "CommodityMapServiceResponse",
        {},
    ),
    "POST_COMMODITY_MAP_SEARCH": Route(
        "POST",
        "/commodity-map/search",
        "WebApiDataSourceLoadOptions",
        "List[CommodityMapDetails]",
        {},
    ),
    "POST_COMMODITY_SEARCH": Route(
        "POST",
        "/commodity/search",
        "WebApiDataSourceLoadOptions",
        "List[CommodityDetails]",
        {},
    ),
    "POST_COMMODITY_SUGGESTIONS": Route(
        "POST",
        "/commodity/suggestions",
        "GetCommoditySuggestionsDataSourceLoadOptions",
        "List[CommodityWithParents]",
        {},
    ),
    "POST_COMPANIES_CAPABILITIES": Route(
        "POST", "/companies/{companyId}/capabilities", "CommercialCapabilities", {}
    ),
    "POST_COMPANIES_CARRIER_ACOUNTS": Route(
        "POST",
        "/companies/{companyId}/carrierAcounts",
        "UpdateCarrierAccountsModel",
        {},
    ),
    "POST_COMPANIES_FILTERED_CUSTOMERS": Route(
        "POST", "/companies/filteredCustomers", "WebApiDataSourceLoadOptions", {}
    ),
    "POST_COMPANIES_FULLDETAILS": Route(
        "POST", "/companies/fulldetails", "CompanyDetails", {}
    ),
    "POST_COMPANIES_GEOSETTINGS": Route(
        "POST", "/companies/{companyId}/geosettings", "SaveGeoSettingModel", {}
    ),
    "POST_COMPANIES_LIST": Route(
        "POST", "/companies/list", "TagBoxDataSourceLoadOptions", {}
    ),
    "POST_COMPANIES_PACKAGINGLABOR": Route(
        "POST", "/companies/{companyId}/packaginglabor", "PackagingLaborSettings", {}
    ),
    "POST_COMPANIES_PACKAGINGSETTINGS": Route(
        "POST",
        "/companies/{companyId}/packagingsettings",
        "PackagingTariffSettings",
        {},
    ),
    "POST_COMPANIES_SEARCH_V2": Route(
        "POST",
        "/companies/search/v2",
        "SearchCompanyDataSourceLoadOptions",
        "List[SearchCompanyResponse]",
        {},
    ),
    "POST_COMPANIES_SIMPLELIST": Route(
        "POST", "/companies/simplelist", "TagBoxDataSourceLoadOptions", {}
    ),
    "POST_COMPANY_ACCOUNTS_STRIPE_COMPLETECONNECTION": Route(
        "POST", "/company/{companyId}/accounts/stripe/completeconnection", None, {}
    ),
    "POST_COMPANY_CONTAINERTHICKNESSINCHES": Route(
        "POST",
        "/company/{companyId}/containerthicknessinches",
        "ContainerThickness",
        {},
    ),
    "POST_COMPANY_GRIDSETTINGS": Route(
        "POST", "/company/{companyId}/gridsettings", "SaveGridSettingsModel", {}
    ),
    "POST_COMPANY_MATERIAL": Route(
        "POST",
        "/company/{companyId}/material",
        "SaveCompanyMaterialModel",
        "CompanyMaterial",
        {},
    ),
    "POST_COMPANY_TRUCK": Route(
        "POST",
        "/company/{companyId}/truck",
        "SaveTruckRequest",
        "SaveEntityResponse",
        {},
    ),
    "POST_CONTACTS_CUSTOMERS": Route(
        "POST", "/contacts/customers", "SearchContactRequest", {}
    ),
    "POST_CONTACTS_EDITDETAILS": Route(
        "POST", "/contacts/editdetails", "ContactDetailedInfo", {}
    ),
    "POST_CONTACTS_HISTORY": Route(
        "POST",
        "/contacts/{contactId}/history",
        "ContactHistoryDataSourceLoadOptions",
        "ContactHistoryInfo",
        {},
    ),
    "POST_CONTACTS_MERGE_PREVIEW": Route(
        "POST",
        "/contacts/{mergeToId}/merge/preview",
        "MergeContactsPreviewRequestModel",
        "MergeContactsPreviewInfo",
        {},
    ),
    "POST_CONTACTS_SEARCH": Route(
        "POST", "/contacts/search", "WebApiDataSourceLoadOptions", {}
    ),
    "POST_CONTACTS_V2_SEARCH": Route(
        "POST",
        "/contacts/v2/search",
        "MergeContactsSearchRequestModel",
        "List[SearchContactEntityResult]",
        {},
    ),
    "POST_DASHBOARD_GRIDVIEWSTATE": Route(
        "POST", "/dashboard/gridviewstate/{id}", None, {}
    ),
    "POST_DASHBOARD_INBOUND": Route(
        "POST",
        "/dashboard/inbound",
        "WebApiDataSourceLoadOptions",
        "List[AgentInboundViewRecord]",
        {},
    ),
    "POST_DASHBOARD_INHOUSE": Route(
        "POST",
        "/dashboard/inhouse",
        "WebApiDataSourceLoadOptions",
        "List[AgentInhouseViewRecord]",
        {},
    ),
    "POST_DASHBOARD_LOCAL_DELIVERIES": Route(
        "POST",
        "/dashboard/local-deliveries",
        "WebApiDataSourceLoadOptions",
        "List[AgentLocalDeliveriesViewRecord]",
        {},
    ),
    "POST_DASHBOARD_OUTBOUND": Route(
        "POST",
        "/dashboard/outbound",
        "WebApiDataSourceLoadOptions",
        "List[AgentOutboundViewRecord]",
        {},
    ),
    "POST_DASHBOARD_RECENTESTIMATES": Route(
        "POST",
        "/dashboard/recentestimates",
        "WebApiDataSourceLoadOptions",
        "List[AgentRecentEstimatesViewRecord]",
        {},
    ),
    "POST_DOCUMENTS": Route("POST", "/documents", None, {}),
    "POST_EMAIL_LABELREQUEST": Route(
        "POST", "/email/{jobDisplayId}/labelrequest", None, {}
    ),
    "JOBS": {
        "GET_PARCELITEMS": Route(
            "GET", "/job/{jobDisplayId}/parcelitems", None, "List[ParcelItem]", {}
        ),
        "POST_JOB": Route("POST", "/job", "JobSaveRequestModel", {}),
    },
    "POST_JOBINTACCT": Route(
        "POST", "/jobintacct/{jobDisplayId}", "CreateJobIntacctModel", {}
    ),
    "POST_JOBINTACCT_APPLY_REBATE": Route(
        "POST", "/jobintacct/{jobDisplayId}/applyRebate", None, {}
    ),
    "POST_JOBINTACCT_DRAFT": Route(
        "POST", "/jobintacct/{jobDisplayId}/draft", "CreateJobIntacctModel", {}
    ),
    "POST_JOB_BOOK": Route("POST", "/job/{jobDisplayId}/book", None, {}),
    "POST_JOB_CHANGE_AGENT": Route(
        "POST", "/job/{jobDisplayId}/changeAgent", "ChangeJobAgentRequest", {}
    ),
    "POST_JOB_EMAIL": Route(
        "POST", "/job/{jobDisplayId}/email", "SendDocumentEmailModel", {}
    ),
    "POST_JOB_EMAIL_CREATETRANSACTIONALEMAIL": Route(
        "POST", "/job/{jobDisplayId}/email/createtransactionalemail", None, {}
    ),
    "POST_JOB_EMAIL_SEND": Route(
        "POST", "/job/{jobDisplayId}/email/{emailTemplateGuid}/send", None, {}
    ),
    "POST_JOB_EMAIL_SENDDOCUMENT": Route(
        "POST", "/job/{jobDisplayId}/email/senddocument", "SendDocumentEmailModel", {}
    ),
    "POST_JOB_FEEDBACK": Route(
        "POST", "/job/feedback/{jobDisplayId}", "FeedbackSaveModel", {}
    ),
    "POST_JOB_FREIGHTITEMS": Route(
        "POST", "/job/{jobDisplayId}/freightitems", "SaveAllFreightItemsRequest", {}
    ),
    "POST_JOB_FREIGHTPROVIDERS": Route(
        "POST", "/job/{jobDisplayId}/freightproviders", None, "ServiceBaseResponse"
    ),
    "POST_JOB_FREIGHTPROVIDERS_RATEQUOTE": Route(
        "POST",
        "/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote",
        "SetRateModel",
        "ServiceBaseResponse",
        {},
    ),
    "POST_JOB_ITEM_NOTES": Route(
        "POST", "/job/{jobDisplayId}/item/notes", "JobItemNotesData", {}
    ),
    "POST_JOB_NOTE": Route(
        "POST", "/job/{jobDisplayId}/note", "TaskNoteModel", "JobTaskNote", {}
    ),
    "POST_JOB_ONHOLD": Route(
        "POST",
        "/job/{jobDisplayId}/onhold",
        "SaveOnHoldRequest",
        "SaveOnHoldResponse",
        {},
    ),
    "POST_JOB_ONHOLD_COMMENT": Route(
        "POST",
        "/job/{jobDisplayId}/onhold/{onHoldId}/comment",
        None,
        "OnHoldNoteDetails",
        {},
    ),
    "POST_JOB_PARCELITEMS": Route(
        "POST",
        "/job/{jobDisplayId}/parcelitems",
        "SaveAllParcelItemsRequest",
        "List[ParcelItemWithPackage]",
        {},
    ),
    "POST_JOB_PAYMENT_ACHCREDIT_TRANSFER": Route(
        "POST", "/job/{jobDisplayId}/payment/ACHCreditTransfer", None, {}
    ),
    "POST_JOB_PAYMENT_ACHPAYMENT_SESSION": Route(
        "POST", "/job/{jobDisplayId}/payment/ACHPaymentSession", None, {}
    ),
    "POST_JOB_PAYMENT_ATTACH_CUSTOMER_BANK": Route(
        "POST",
        "/job/{jobDisplayId}/payment/attachCustomerBank",
        "AttachCustomerBankModel",
        {},
    ),
    "POST_JOB_PAYMENT_BANKSOURCE": Route(
        "POST", "/job/{jobDisplayId}/payment/banksource", "PaymentSourceDetails", {}
    ),
    "POST_JOB_PAYMENT_BYSOURCE": Route(
        "POST", "/job/{jobDisplayId}/payment/bysource", None, {}
    ),
    "POST_JOB_PAYMENT_CANCEL_JOB_ACHVERIFICATION": Route(
        "POST", "/job/{jobDisplayId}/payment/cancelJobACHVerification", None, {}
    ),
    "POST_JOB_PAYMENT_VERIFY_JOB_ACHSOURCE": Route(
        "POST",
        "/job/{jobDisplayId}/payment/verifyJobACHSource",
        "VerifyBankAccountRequest",
        {},
    ),
    "POST_JOB_SEARCH_BY_DETAILS": Route(
        "POST", "/job/searchByDetails", "SearchJobFilter", {}
    ),
    "POST_JOB_SHIPMENT_ACCESSORIAL": Route(
        "POST", "/job/{jobDisplayId}/shipment/accessorial", "JobParcelAddOn", {}
    ),
    "POST_JOB_SHIPMENT_BOOK": Route(
        "POST", "/job/{jobDisplayId}/shipment/book", "BookShipmentRequest", {}
    ),
    "POST_JOB_SHIPMENT_EXPORTDATA": Route(
        "POST", "/job/{jobDisplayId}/shipment/exportdata", "InternationalParams", {}
    ),
    "POST_JOB_SHIPMENT_RATEQUOTES": Route(
        "POST",
        "/job/{jobDisplayId}/shipment/ratequotes",
        "TransportationRatesRequestModel",
        "JobCarrierRatesModel",
        {},
    ),
    "POST_JOB_SMS": Route("POST", "/job/{jobDisplayId}/sms", "SendSMSModel", {}),
    "POST_JOB_SMS_READ": Route(
        "POST", "/job/{jobDisplayId}/sms/read", "MarkSmsAsReadModel", {}
    ),
    "POST_JOB_STATUS_QUOTE": Route(
        "POST", "/job/{jobDisplayId}/status/quote", None, {}
    ),
    "POST_JOB_TIMELINE": Route(
        "POST",
        "/job/{jobDisplayId}/timeline",
        "TimelineTaskInput",
        "SaveResponseModel",
        {},
    ),
    "POST_JOB_TIMELINE_INCREMENTJOBSTATUS": Route(
        "POST",
        "/job/{jobDisplayId}/timeline/incrementjobstatus",
        "IncrementJobStatusInputModel",
        "IncrementJobStatusResponseModel",
        {},
    ),
    "POST_JOB_TIMELINE_UNDOINCREMENTJOBSTATUS": Route(
        "POST", "/job/{jobDisplayId}/timeline/undoincrementjobstatus", None, {}
    ),
    "POST_JOB_TRANSFER": Route(
        "POST", "/job/transfer/{jobDisplayId}", "TransferModel", {}
    ),
    "POST_NOTE": Route("POST", "/note", "NoteModel", "Notes", {}),
    "POST_PARTNER_SEARCH": Route(
        "POST",
        "/partner/search",
        "SearchPartnersDataSourceLoadOptions",
        "List[Partner]",
        {},
    ),
    "POST_REPORTS_INSURANCE": Route(
        "POST", "/reports/insurance", "InsuranceReportRequest", "InsuranceReport"
    ),
    "POST_REPORTS_REFERRED_BY": Route(
        "POST", "/reports/referredBy", "ReferredByReportRequest", "ReferredByReport"
    ),
    "POST_REPORTS_SALES": Route(
        "POST", "/reports/sales", "SalesForecastReportRequest", "SalesForecastReport"
    ),
    "POST_REPORTS_SALES_DRILLDOWN": Route(
        "POST", "/reports/salesDrilldown", "Web2LeadRevenueFilter", {}
    ),
    "POST_REPORTS_SALES_SUMMARY": Route(
        "POST",
        "/reports/sales/summary",
        "SalesForecastSummaryRequest",
        "SalesForecastSummary",
        {},
    ),
    "POST_REPORTS_TOP_REVENUE_CUSTOMERS": Route(
        "POST",
        "/reports/topRevenueCustomers",
        "Web2LeadRevenueFilter",
        "RevenueCustomer",
        {},
    ),
    "POST_REPORTS_TOP_REVENUE_SALES_REPS": Route(
        "POST",
        "/reports/topRevenueSalesReps",
        "Web2LeadRevenueFilter",
        "RevenueCustomer",
        {},
    ),
    "POST_REPORTS_WEB2_LEAD": Route(
        "POST", "/reports/web2Lead", "Web2LeadV2RequestModel", "Web2LeadReport", {}
    ),
    "POST_RFQ_ACCEPT": Route("POST", "/rfq/{rfqId}/accept", "AcceptModel", {}),
    "POST_RFQ_ACCEPTWINNER": Route("POST", "/rfq/{rfqId}/acceptwinner", None, {}),
    "POST_RFQ_CANCEL": Route("POST", "/rfq/{rfqId}/cancel", None, {}),
    "POST_RFQ_COMMENT": Route("POST", "/rfq/{rfqId}/comment", None, {}),
    "POST_RFQ_DECLINE": Route("POST", "/rfq/{rfqId}/decline", None, {}),
    "POST_SMS_TEMPLATE_SAVE": Route(
        "POST", "/SmsTemplate/save", "SmsTemplateModel", {}
    ),
    "POST_USERS_LIST": Route("POST", "/users/list", "WebApiDataSourceLoadOptions", {}),
    "POST_USERS_USER": Route("POST", "/users/user", "CreateUserModel", {}),
    "POST_VIEWS": Route("POST", "/views", "GridViewDetails", {}),
    "POST_WEBHOOKS_STRIPE_CHECKOUT.SESSION.COMPLETED": Route(
        "POST", "/webhooks/stripe/checkout.session.completed", None, {}
    ),
    "POST_WEBHOOKS_STRIPE_CONNECT_HANDLE": Route(
        "POST", "/webhooks/stripe/connect/handle", None, {}
    ),
    "POST_WEBHOOKS_STRIPE_HANDLE": Route("POST", "/webhooks/stripe/handle", None, {}),
    "POST_WEBHOOKS_TWILIO_BODY_SMS_INBOUND": Route(
        "POST",
        "/webhooks/twilio/body-sms-inbound",
        "TwilioInboundMessageWebhookModel",
        {},
    ),
    "POST_WEBHOOKS_TWILIO_FORM_SMS_INBOUND": Route(
        "POST", "/webhooks/twilio/form-sms-inbound", None, {}
    ),
    "POST_WEBHOOKS_TWILIO_SMS_STATUS_CALLBACK": Route(
        "POST", "/webhooks/twilio/smsStatusCallback", None, {}
    ),
    "PUT_ACCOUNT_PAYMENTSOURCE": Route(
        "PUT", "/account/paymentsource/{sourceId}", None, {}
    ),
    "PUT_COMMODITY": Route(
        "PUT", "/commodity/{id}", "UpdateCommodityModel", "CommodityServiceResponse", {}
    ),
    "PUT_COMMODITY_MAP": Route(
        "PUT",
        "/commodity-map/{id}",
        "UpdateCommodityMapModel",
        "CommodityMapServiceResponse",
        {},
    ),
    "PUT_COMPANIES_FULLDETAILS": Route(
        "PUT",
        "/companies/{companyId}/fulldetails",
        "CompanyDetails",
        "CompanyDetails",
        {},
    ),
    "PUT_COMPANY_MATERIAL": Route(
        "PUT",
        "/company/{companyId}/material/{materialId}",
        "SaveCompanyMaterialModel",
        "CompanyMaterial",
        {},
    ),
    "PUT_COMPANY_TRUCK": Route(
        "PUT",
        "/company/{companyId}/truck/{truckId}",
        "SaveTruckRequest",
        "SaveEntityResponse",
        {},
    ),
    "PUT_CONTACTS_EDITDETAILS": Route(
        "PUT", "/contacts/{contactId}/editdetails", "ContactDetailedInfo", {}
    ),
    "PUT_CONTACTS_MERGE": Route(
        "PUT", "/contacts/{mergeToId}/merge", "MergeContactsRequestModel", {}
    ),
    "PUT_DOCUMENTS_HIDE": Route("PUT", "/documents/hide/{docId}", None, {}),
    "PUT_DOCUMENTS_UPDATE": Route(
        "PUT", "/documents/update/{docId}", "DocumentUpdateModel", {}
    ),
    "PUT_JOB_ITEM": Route(
        "PUT", "/job/{jobDisplayId}/item/{itemId}", "JobItemInfoData", {}
    ),
    "PUT_JOB_NOTE": Route("PUT", "/job/{jobDisplayId}/note/{id}", "TaskNoteModel", {}),
    "PUT_JOB_ONHOLD": Route(
        "PUT",
        "/job/{jobDisplayId}/onhold/{onHoldId}",
        "SaveOnHoldRequest",
        "SaveOnHoldResponse",
        {},
    ),
    "PUT_JOB_ONHOLD_DATES": Route(
        "PUT",
        "/job/{jobDisplayId}/onhold/{onHoldId}/dates",
        "SaveOnHoldDatesModel",
        "ResolveJobOnHoldResponse",
        {},
    ),
    "PUT_JOB_ONHOLD_RESOLVE": Route(
        "PUT",
        "/job/{jobDisplayId}/onhold/{onHoldId}/resolve",
        "SaveOnHoldRequest",
        "ResolveJobOnHoldResponse",
        {},
    ),
    "PUT_JOB_SAVE": Route("PUT", "/job/save", "JobSaveRequest", {}),
    "PUT_NOTE": Route("PUT", "/note/{id}", "NoteModel", {}),
    "PUT_USERS_USER": Route("PUT", "/users/user", "UserInfo", {}),
    "PUT_VIEWS_ACCESS": Route("PUT", "/views/{viewId}/access", None, None),
}


__all__ = ["SCHEMA", "Route"]
