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
import re
from typing import Any, Dict


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
    _path_param_names: set[str] = field(default_factory=dict)

    def __post_init__(self):
            # Extract {param} names from template
            self._path_param_names = set(re.findall(r"\{([^}]+)\}", self.path))

    @property
    def url(self) -> str:
        return self.path.format(**{k: v for k, v in self.params.items() if k in self._path_param_names})

    @property
    def params(self) -> Dict[str, Any]:
        used_in_path = {k for k in self.params if k in self._path_param_names}
        query_kwargs = {k: v for k, v in self.params.items() if k not in used_in_path and v is not None}
        return query_kwargs

SCHEMA = {
    "ACCOUNT": {
        "DELETE_PAYMENTSOURCE": Route("DELETE", "/account/paymentsource/{sourceId}", None, "ServiceBaseResponse", {}),
        "GET_PROFILE": Route("GET", "/account/profile", None, "AccountProfile", {}),
        "GET_VERIFYRESETTOKEN": Route("GET", "/account/verifyresettoken", None, "ServiceBaseResponse", {}),
        "POST_CONFIRM": Route("POST", "/account/confirm", "ConfirmEmailModel", "ServiceBaseResponse", {}),
        "POST_FORGOT": Route("POST", "/account/forgot", "ForgotLoginModel", "ServiceBaseResponse", {}),
        "POST_REGISTER": Route("POST", "/account/register", "RegistrationModel", "ServiceBaseResponse", {}),
        "POST_RESETPASSWORD": Route("POST", "/account/resetpassword", "ResetPasswordModel", "ServiceBaseResponse", {}),
        "POST_SEND_CONFIRMATION": Route("POST", "/account/sendConfirmation", None, "ServiceBaseResponse", {}),
        "POST_SETPASSWORD": Route("POST", "/account/setpassword", "ChangePasswordModel", "ServiceBaseResponse", {}),
        "PUT_PAYMENTSOURCE": Route("PUT", "/account/paymentsource/{sourceId}", None, "ServiceBaseResponse", {}),
    },
    "ADDRESS": {
        "GET_ISVALID": Route("GET", "/address/isvalid", None, "AddressIsValidResult", {}),
        "GET_PROPERTYTYPE": Route("GET", "/address/propertytype", None, "PropertyType", {}),
        "POST_AVOID_VALIDATION": Route("POST", "/address/{addressId}/avoidValidation", None, "ServiceBaseResponse", {}),
        "POST_VALIDATED": Route("POST", "/address/{addressId}/validated", "SaveValidatedRequest", "ServiceBaseResponse", {}),
    },
    "ADMIN": {
        "DELETE_ADVANCEDSETTINGS": Route("DELETE", "/admin/advancedsettings/{id}", None, "ServiceBaseResponse", {}),
        "GET_ADVANCEDSETTINGS": Route("GET", "/admin/advancedsettings/{id}", None, "AdvancedSettingsEntitySaveModel", {}),
        "GET_ADVANCEDSETTINGS_ALL": Route("GET", "/admin/advancedsettings/all", None, "List[AdvancedSettingsEntitySaveModel]", {}),
        "GET_CARRIERERRORMESSAGE_ALL": Route("GET", "/admin/carriererrormessage/all", None, "List[CarrierErrorMessage]", {}),
        "GET_GLOBALSETTINGS_COMPANYHIERARCHY": Route("GET", "/admin/globalsettings/companyhierarchy", None, "CompanyHierarchyInfo", {}),
        "GET_GLOBALSETTINGS_COMPANYHIERARCHY_COMPANY": Route("GET", "/admin/globalsettings/companyhierarchy/company/{companyId}", None, "CompanyHierarchyInfo", {}),
        "POST_ADVANCEDSETTINGS": Route("POST", "/admin/advancedsettings", "AdvancedSettingsEntitySaveModel", "ServiceBaseResponse", {}),
        "POST_CARRIERERRORMESSAGE": Route("POST", "/admin/carriererrormessage", "CarrierErrorMessage", "ServiceBaseResponse", {}),
        "POST_GLOBALSETTINGS_APPROVEINSURANCEEXCEPTION": Route("POST", "/admin/globalsettings/approveinsuranceexception", None, "ServiceBaseResponse", {}),
        "POST_GLOBALSETTINGS_GETINSURANCEEXCEPTIONS": Route("POST", "/admin/globalsettings/getinsuranceexceptions", "WebApiDataSourceLoadOptions", "List[SelectApproveInsuranceResult]", {}),
        "POST_GLOBALSETTINGS_INTACCT": Route("POST", "/admin/globalsettings/intacct", "WebApiDataSourceLoadOptions", "ServiceBaseResponse", {}),
        "POST_LOGBUFFER_FLUSH": Route("POST", "/admin/logbuffer/flush", None, "ServiceBaseResponse", {}),
        "POST_LOGBUFFER_FLUSH_ALL": Route("POST", "/admin/logbuffer/flushAll", None, "ServiceBaseResponse", {}),
    },
    "COMMODITY": {
        "GET": Route("GET", "/commodity/{id}", None, "CommodityWithParentsServiceResponse", {}),
        "POST": Route("POST", "/commodity", "AddCommodityModel", "CommodityServiceResponse", {}),
        "POST_SEARCH": Route("POST", "/commodity/search", "WebApiDataSourceLoadOptions", "List[CommodityDetails]", {}),
        "POST_SUGGESTIONS": Route("POST", "/commodity/suggestions", "GetCommoditySuggestionsDataSourceLoadOptions", "List[CommodityWithParents]", {}),
        "PUT": Route("PUT", "/commodity/{id}", "UpdateCommodityModel", "CommodityServiceResponse", {}),
    },
    "COMMODITY_MAP": {
        "DELETE": Route("DELETE", "/commodity-map/{id}", None, "ServiceBaseResponse", {}),
        "GET": Route("GET", "/commodity-map/{id}", None, "CommodityMapDetailsServiceResponse", {}),
        "POST": Route("POST", "/commodity-map", "AddCommodityMapModel", "CommodityMapServiceResponse", {}),
        "POST_SEARCH": Route("POST", "/commodity-map/search", "WebApiDataSourceLoadOptions", "List[CommodityMapDetails]", {}),
        "PUT": Route("PUT", "/commodity-map/{id}", "UpdateCommodityMapModel", "CommodityMapServiceResponse", {}),
    },
    "COMPANIES": {
        "GET": Route("GET", "/companies/{id}", None, "CompanySimple", {}),
        "GET_AVAILABLE_BY_CURRENT_USER": Route("GET", "/companies/availableByCurrentUser", None, "List[CompanySimple]", {}),
        "GET_BRANDS": Route("GET", "/companies/brands", None, "List[CompanyBrandTreeNode]", {}),
        "GET_BRANDSTREE": Route("GET", "/companies/brandstree", None, "List[CompanyBrandTreeNode]", {}),
        "GET_CAPABILITIES": Route("GET", "/companies/{companyId}/capabilities", None, "CommercialCapabilities", {}),
        "GET_CARRIER_ACOUNTS": Route("GET", "/companies/{companyId}/carrierAcounts", None, "FranchiseeCarrierAccounts", {}),
        "GET_DETAILS": Route("GET", "/companies/{companyId}/details", None, "CompanyDetails", {}),
        "GET_FRANCHISEE_ADDRESSES": Route("GET", "/companies/{companyId}/franchiseeAddresses", None, "List[CompanyAddressInfo]", {}),
        "GET_FULLDETAILS": Route("GET", "/companies/{companyId}/fulldetails", None, "CompanyDetails", {}),
        "GET_GEOSETTINGS": Route("GET", "/companies/geosettings", None, "List[SaveGeoSettingModel]", {}),
        "GET_GEO_AREA_COMPANIES": Route("GET", "/companies/geoAreaCompanies", None, "List[CompanyGeoAreaCompanies]", {}),
        "GET_INFO_FROM_KEY": Route("GET", "/companies/infoFromKey", None, "CompanyInfo", {}),
        "GET_INHERITEDPACKAGINGLABOR": Route("GET", "/companies/{companyId}/inheritedpackaginglabor", None, "PackagingLaborSettings", {}),
        "GET_INHERITED_PACKAGING_TARIFFS": Route("GET", "/companies/{companyId}/inheritedPackagingTariffs", None, "PackagingTariffSettings", {}),
        "GET_PACKAGINGLABOR": Route("GET", "/companies/{companyId}/packaginglabor", None, "PackagingLaborSettings", {}),
        "GET_PACKAGINGSETTINGS": Route("GET", "/companies/{companyId}/packagingsettings", None, "PackagingTariffSettings", {}),
        "GET_SEARCH": Route("GET", "/companies/search", None, "List[SearchCompanyResponse]", {}),
        "GET_SEARCH_CARRIER_ACCOUNTS": Route("GET", "/companies/search/carrier-accounts", None, "List[CarrierAccountInfo]", {}),
        "GET_SUGGEST_CARRIERS": Route("GET", "/companies/suggest-carriers", None, "List[CarrierCompanyInfo]", {}),
        "POST_CAPABILITIES": Route("POST", "/companies/{companyId}/capabilities", "CommercialCapabilities", "ServiceBaseResponse", {}),
        "POST_CARRIER_ACOUNTS": Route("POST", "/companies/{companyId}/carrierAcounts", "UpdateCarrierAccountsModel", "ServiceBaseResponse", {}),
        "POST_FILTERED_CUSTOMERS": Route("POST", "/companies/filteredCustomers", "WebApiDataSourceLoadOptions", "ServiceBaseResponse", {}),
        "POST_FULLDETAILS": Route("POST", "/companies/fulldetails", "CompanyDetails", "ServiceBaseResponse", {}),
        "POST_GEOSETTINGS": Route("POST", "/companies/{companyId}/geosettings", "SaveGeoSettingModel", "ServiceBaseResponse", {}),
        "POST_LIST": Route("POST", "/companies/list", "TagBoxDataSourceLoadOptions", "ServiceBaseResponse", {}),
        "POST_PACKAGINGLABOR": Route("POST", "/companies/{companyId}/packaginglabor", "PackagingLaborSettings", "ServiceBaseResponse", {}),
        "POST_PACKAGINGSETTINGS": Route("POST", "/companies/{companyId}/packagingsettings", "PackagingTariffSettings", "ServiceBaseResponse", {}),
        "POST_SEARCH_V2": Route("POST", "/companies/search/v2", "SearchCompanyDataSourceLoadOptions", "List[SearchCompanyResponse]", {}),
        "POST_SIMPLELIST": Route("POST", "/companies/simplelist", "TagBoxDataSourceLoadOptions", "ServiceBaseResponse", {}),
        "PUT_FULLDETAILS": Route("PUT", "/companies/{companyId}/fulldetails", "CompanyDetails", "CompanyDetails", {}),
    },
    "COMPANY": {
        "DELETE_ACCOUNTS_STRIPE": Route("DELETE", "/company/{companyId}/accounts/stripe", None, "ServiceBaseResponse", {}),
        "DELETE_CONTAINERTHICKNESSINCHES": Route("DELETE", "/company/{companyId}/containerthicknessinches", None, "ServiceBaseResponse", {}),
        "DELETE_MATERIAL": Route("DELETE", "/company/{companyId}/material/{materialId}", None, "ServiceBaseResponse", {}),
        "DELETE_TRUCK": Route("DELETE", "/company/{companyId}/truck/{truckId}", None, "ServiceWarningResponse", {}),
        "GET_ACCOUNTS_STRIPE_CONNECTURL": Route("GET", "/company/{companyId}/accounts/stripe/connecturl", None, None, {}),
        "GET_CALENDAR": Route("GET", "/company/{companyId}/calendar/{date}", None, "Calendar", {}),
        "GET_CALENDAR_BASEINFO": Route("GET", "/company/{companyId}/calendar/{date}/baseinfo", None, "BaseInfoCalendar", {}),
        "GET_CALENDAR_ENDOFDAY": Route("GET", "/company/{companyId}/calendar/{date}/endofday", None, None, {}),
        "GET_CALENDAR_STARTOFDAY": Route("GET", "/company/{companyId}/calendar/{date}/startofday", None, None, {}),
        "GET_CONTAINERTHICKNESSINCHES": Route("GET", "/company/{companyId}/containerthicknessinches", None, "List[ContainerThickness]", {}),
        "GET_GRIDSETTINGS": Route("GET", "/company/{companyId}/gridsettings", None, "GridSettingsEntity", {}),
        "GET_MATERIAL": Route("GET", "/company/{companyId}/material", None, "List[CompanyMaterial]", {}),
        "GET_PLANNER": Route("GET", "/company/{companyId}/planner", None, "List[PlannerTask]", {}),
        "GET_SETUPDATA": Route("GET", "/company/{companyId}/setupdata", None, "CompanySetupData", {}),
        "GET_TRUCK": Route("GET", "/company/{companyId}/truck", None, "List[Truck]", {}),
        "POST_ACCOUNTS_STRIPE_COMPLETECONNECTION": Route("POST", "/company/{companyId}/accounts/stripe/completeconnection", None, "ServiceBaseResponse", {}),
        "POST_CONTAINERTHICKNESSINCHES": Route("POST", "/company/{companyId}/containerthicknessinches", "ContainerThickness", "ServiceBaseResponse", {}),
        "POST_GRIDSETTINGS": Route("POST", "/company/{companyId}/gridsettings", "SaveGridSettingsModel", "ServiceBaseResponse", {}),
        "POST_MATERIAL": Route("POST", "/company/{companyId}/material", "SaveCompanyMaterialModel", "CompanyMaterial", {}),
        "POST_TRUCK": Route("POST", "/company/{companyId}/truck", "SaveTruckRequest", "SaveEntityResponse", {}),
        "PUT_MATERIAL": Route("PUT", "/company/{companyId}/material/{materialId}", "SaveCompanyMaterialModel", "CompanyMaterial", {}),
        "PUT_TRUCK": Route("PUT", "/company/{companyId}/truck/{truckId}", "SaveTruckRequest", "SaveEntityResponse", {}),
    },
    "CONTACTS": {
        "GET": Route("GET", "/contacts/{id}", None, "ContactDetails", {}),
        "GET_EDITDETAILS": Route("GET", "/contacts/{contactId}/editdetails", None, "ContactDetailedInfo", {}),
        "HISTORY_AGGREGATED": Route("GET", "/contacts/{contactId}/history/aggregated", None, "ContactHistoryAggregatedCost", {}),
        "HISTORY_GRAPHDATA": Route("GET", "/contacts/{contactId}/history/graphdata", None, "ContactHistoryGraphData", {}),
        "PRIMARYDETAILS": Route("GET", "/contacts/{contactId}/primarydetails", None, "ContactPrimaryDetails", {}),
        "USER": Route("GET", "/contacts/user", None, "ContactUser", {}),
        "CUSTOMERS": Route("POST", "/contacts/customers", "SearchContactRequest", "ServiceBaseResponse", {}),
        "POST_EDITDETAILS": Route("POST", "/contacts/editdetails", "ContactDetailedInfo", "ServiceBaseResponse", {}),
        "HISTORY": Route("POST", "/contacts/{contactId}/history", "ContactHistoryDataSourceLoadOptions", "ContactHistoryInfo", {}),
        "MERGE_PREVIEW": Route("POST", "/contacts/{mergeToId}/merge/preview", "MergeContactsPreviewRequestModel", "MergeContactsPreviewInfo", {}),
        "SEARCH": Route("POST", "/contacts/search", "WebApiDataSourceLoadOptions", "ServiceBaseResponse", {}),
        "V2_SEARCH": Route("POST", "/contacts/v2/search", "MergeContactsSearchRequestModel", "List[SearchContactEntityResult]", {}),
        "PUT_EDITDETAILS": Route("PUT", "/contacts/{contactId}/editdetails", "ContactDetailedInfo", "ServiceBaseResponse", {}),
        "MERGE": Route("PUT", "/contacts/{mergeToId}/merge", "MergeContactsRequestModel", "ServiceBaseResponse", {}),
    },
    "DASHBOARD": {
        "GET": Route("GET", "/dashboard", None, "DashboardResponse", {}),
        "GRIDVIEWS": Route("GET", "/dashboard/gridviews", None, "List[GridViewDetails]", {}),
        "GRIDVIEWSTATE": Route("GET", "/dashboard/gridviewstate/{id}", None, "GridViewDetails", {}),
        "POST_GRIDVIEWSTATE": Route("POST", "/dashboard/gridviewstate/{id}", None, "ServiceBaseResponse", {}),
        "INBOUND": Route("POST", "/dashboard/inbound", "WebApiDataSourceLoadOptions", "List[AgentInboundViewRecord]", {}),
        "INHOUSE": Route("POST", "/dashboard/inhouse", "WebApiDataSourceLoadOptions", "List[AgentInhouseViewRecord]", {}),
        "LOCAL_DELIVERIES": Route("POST", "/dashboard/local-deliveries", "WebApiDataSourceLoadOptions", "List[AgentLocalDeliveriesViewRecord]", {}),
        "OUTBOUND": Route("POST", "/dashboard/outbound", "WebApiDataSourceLoadOptions", "List[AgentOutboundViewRecord]", {}),
        "RECENTESTIMATES": Route("POST", "/dashboard/recentestimates", "WebApiDataSourceLoadOptions", "List[AgentRecentEstimatesViewRecord]", {}),
    },
    "DOCUMENTS": {
        "GET": Route("GET", "/documents/get/{docPath}", None, "DocumentDetails", {}),
        "THUMBNAIL": Route("GET", "/documents/get/thumbnail/{docPath}", None, None, {}),
        "LIST": Route("GET", "/documents/list", None, "List[DocumentDetails]", {}),
        "POST": Route("POST", "/documents", "DocumentUpdateModel", "ServiceBaseResponse", {}),
        "HIDE": Route("PUT", "/documents/hide/{docId}", None, "ServiceBaseResponse", {}),
        "UPDATE": Route("PUT", "/documents/update/{docId}", "DocumentUpdateModel", "ServiceBaseResponse", {}),
    },
    "E_SIGN": {
        "GET": Route("GET", "/e-sign/{jobDisplayId}/{bookingKey}", None, None, {}),
        "GET_RESULT": Route("GET", "/e-sign/result", None, None, {}),
    },
    "EMAIL": {
        "LABELREQUEST": Route("POST", "/email/{jobDisplayId}/labelrequest", None, "ServiceBaseResponse", {}),
    },
    "JOB": {
        "DELETE_ONHOLD": Route("DELETE", "/job/{jobDisplayId}/onhold", None, "ServiceBaseResponse", {}),
        "DELETE_PARCELITEMS": Route("DELETE", "/job/{jobDisplayId}/parcelitems/{parcelItemId}", None, "ServiceBaseResponse", {}),
        "DELETE_SHIPMENT": Route("DELETE", "/job/{jobDisplayId}/shipment", "DeleteShipRequestModel", "ServiceBaseResponse", {}),
        "DELETE_SHIPMENT_ACCESSORIAL": Route("DELETE", "/job/{jobDisplayId}/shipment/accessorial/{addOnId}", None, "ServiceBaseResponse", {}),
        "DELETE_TIMELINE": Route("DELETE", "/job/{jobDisplayId}/timeline/{timelineTaskId}", None, "DeleteTaskResponse", {}),
        "GET": Route("GET", "/job/{jobDisplayId}", None, "CalendarJob", {}),
        "GET_CALENDARITEMS": Route("GET", "/job/{jobDisplayId}/calendaritems", None, "List[CalendarItem]", {}),
        "GET_DOCUMENT_CONFIG": Route("GET", "/job/documentConfig", None, None, {}),
        "GET_FEEDBACK": Route("GET", "/job/feedback/{jobDisplayId}", None, "FeedbackSaveModel", {}),
        "GET_FORM_ADDRESS_LABEL": Route("GET", "/job/{jobDisplayId}/form/address-label", None, "bytes", {}),
        "GET_FORM_BILL_OF_LADING": Route("GET", "/job/{jobDisplayId}/form/bill-of-lading", None, "bytes", {}),
        "GET_FORM_CREDIT_CARD_AUTHORIZATION": Route("GET", "/job/{jobDisplayId}/form/credit-card-authorization", None, "bytes", {}),
        "GET_FORM_CUSTOMER_QUOTE": Route("GET", "/job/{jobDisplayId}/form/customer-quote", None, "bytes", {}),
        "GET_FORM_INVOICE": Route("GET", "/job/{jobDisplayId}/form/invoice", None, "bytes", {}),
        "GET_FORM_INVOICE_EDITABLE": Route("GET", "/job/{jobDisplayId}/form/invoice/editable", None, "USAREditableFormResponseModel", {}),
        "GET_FORM_ITEM_LABELS": Route("GET", "/job/{jobDisplayId}/form/item-labels", None, "bytes", {}),
        "GET_FORM_OPERATIONS": Route("GET", "/job/{jobDisplayId}/form/operations", None, "bytes", {}),
        "GET_FORM_PACKAGING_LABELS": Route("GET", "/job/{jobDisplayId}/form/packaging-labels", None, "bytes", {}),
        "GET_FORM_PACKAGING_SPECIFICATION": Route("GET", "/job/{jobDisplayId}/form/packaging-specification", None, "bytes", {}),
        "GET_FORM_PACKING_SLIP": Route("GET", "/job/{jobDisplayId}/form/packing-slip", None, "bytes", {}),
        "GET_FORM_QUICK_SALE": Route("GET", "/job/{jobDisplayId}/form/quick-sale", None, "bytes", {}),
        "GET_FORM_SHIPMENTS": Route("GET", "/job/{jobDisplayId}/form/shipments", None, "List[FormsShipmentPlan]", {}),
        "GET_FORM_USAR": Route("GET", "/job/{jobDisplayId}/form/usar", None, "bytes", {}),
        "GET_FORM_USAR_EDITABLE": Route("GET", "/job/{jobDisplayId}/form/usar/editable", None, "USAREditableFormResponseModel", {}),
        "GET_FREIGHTPROVIDERS": Route("GET", "/job/{jobDisplayId}/freightproviders", None, "List[PricedFreightProvider]", {}),
        "GET_JOB_ACCESS_LEVEL": Route("GET", "/job/jobAccessLevel", None, "JobAccessLevel", {}),
        "GET_NOTE": Route("GET", "/job/{jobDisplayId}/note/{id}", None, "JobTaskNote", {}),
        "GET_NOTE_LIST": Route("GET", "/job/{jobDisplayId}/note", None, "List[JobTaskNote]", {}),
        "GET_ONHOLD": Route("GET", "/job/{jobDisplayId}/onhold/{id}", None, "OnHoldDetails", {}),
        "GET_ONHOLD_LIST": Route("GET", "/job/{jobDisplayId}/onhold", None, "List[OnHoldDetails]", {}),
        "GET_ONHOLD_FOLLOWUPUSER": Route("GET", "/job/{jobDisplayId}/onhold/followupuser/{contactId}", None, "OnHoldUser", {}),
        "GET_ONHOLD_FOLLOWUPUSERS": Route("GET", "/job/{jobDisplayId}/onhold/followupusers", None, "List[OnHoldUser]", {}),
        "GET_PACKAGINGCONTAINERS": Route("GET", "/job/{jobDisplayId}/packagingcontainers", None, "List[Packaging]", {}),
        "GET_PARCELITEMS": Route("GET", "/job/{jobDisplayId}/parcelitems", None, "List[ParcelItemWithPackage]", {}),
        "GET_PARCEL_ITEMS_WITH_MATERIALS": Route("GET", "/job/{jobDisplayId}/parcel-items-with-materials", None, "List[ParcelItemWithMaterials]", {}),
        "GET_PAYMENT": Route("GET", "/job/{jobDisplayId}/payment", None, None, {}),
        "GET_PAYMENT_CREATE": Route("GET", "/job/{jobDisplayId}/payment/create", None, None, {}),
        "GET_PAYMENT_SOURCES": Route("GET", "/job/{jobDisplayId}/payment/sources", None, "List[PaymentSourceDetails]", {}),
        "GET_PRICE": Route("GET", "/job/{jobDisplayId}/price", None, None, {}),
        "GET_RFQ": Route("GET", "/job/{jobDisplayId}/rfq", None, "List[QuoteRequestDisplayInfo]", {}),
        "GET_RFQ_STATUSOF_FORCOMPANY": Route("GET", "/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}", None, "QuoteRequestStatus", {}),
        "GET_SEARCH": Route("GET", "/job/search", None, "List[SearchJobInfo]", {}),
        "GET_SHIPMENT_ACCESSORIALS": Route("GET", "/job/{jobDisplayId}/shipment/accessorials", None, "List[JobParcelAddOn]", {}),
        "GET_SHIPMENT_EXPORTDATA": Route("GET", "/job/{jobDisplayId}/shipment/exportdata", None, "JobExportData", {}),
        "GET_SHIPMENT_ORIGINDESTINATION": Route("GET", "/job/{jobDisplayId}/shipment/origindestination", None, "ShipmentOriginDestination", {}),
        "GET_SHIPMENT_RATEQUOTES": Route("GET", "/job/{jobDisplayId}/shipment/ratequotes", None, "JobCarrierRatesModel", {}),
        "GET_SHIPMENT_RATESSTATE": Route("GET", "/job/{jobDisplayId}/shipment/ratesstate", None, None, {}),
        "GET_SMS": Route("GET", "/job/{jobDisplayId}/sms", None, None, {}),
        "GET_SMS_TEMPLATEBASED": Route("GET", "/job/{jobDisplayId}/sms/templatebased/{templateId}", None, "SmsTemplateModel", {}),
        "GET_SUBMANAGEMENTSTATUS": Route("GET", "/job/{jobDisplayId}/submanagementstatus", None, None, {}),
        "GET_TIMELINE": Route("GET", "/job/{jobDisplayId}/timeline/{timelineTaskIdentifier}", None, "CarrierTask", {}),
        "GET_TIMELINE_AGENT": Route("GET", "/job/{jobDisplayId}/timeline/{taskCode}/agent", None, "CompanyListItem", {}),
        "GET_TIMELINE_LIST": Route("GET", "/job/{jobDisplayId}/timeline", None, "List[CarrierTask]", {}),
        "GET_TRACKING": Route("GET", "/job/{jobDisplayId}/tracking", None, "ShipmentTrackingDetails", {}),
        "GET_TRACKING_SHIPMENT": Route("GET", "/job/{jobDisplayId}/tracking/shipment/{proNumber}", None, "ShipmentTrackingDetails", {}),
        "GET_UPDATE_PAGE_CONFIG": Route("GET", "/job/{jobDisplayId}/updatePageConfig", None, "JobUpdatePageConfig", {}),
        "PATCH_TIMELINE": Route("PATCH", "/job/{jobDisplayId}/timeline/{timelineTaskId}", "UpdateTaskModel", "ServiceBaseResponse", {}),
        "POST": Route("POST", "/job", "JobSaveRequestModel", "ServiceBaseResponse", {}),
        "POST_BOOK": Route("POST", "/job/{jobDisplayId}/book", None, "ServiceBaseResponse", {}),
        "POST_CHANGE_AGENT": Route("POST", "/job/{jobDisplayId}/changeAgent", "ChangeJobAgentRequest", "ServiceBaseResponse", {}),
        "POST_EMAIL": Route("POST", "/job/{jobDisplayId}/email", "SendDocumentEmailModel", "ServiceBaseResponse", {}),
        "POST_EMAIL_CREATETRANSACTIONALEMAIL": Route("POST", "/job/{jobDisplayId}/email/createtransactionalemail", None, "ServiceBaseResponse", {}),
        "POST_EMAIL_SEND": Route("POST", "/job/{jobDisplayId}/email/{emailTemplateGuid}/send", None, "ServiceBaseResponse", {}),
        "POST_EMAIL_SENDDOCUMENT": Route("POST", "/job/{jobDisplayId}/email/senddocument", "SendDocumentEmailModel", "ServiceBaseResponse", {}),
        "POST_FEEDBACK": Route("POST", "/job/feedback/{jobDisplayId}", "FeedbackSaveModel", "ServiceBaseResponse", {}),
        "POST_FREIGHTITEMS": Route("POST", "/job/{jobDisplayId}/freightitems", "SaveAllFreightItemsRequest", "ServiceBaseResponse", {}),
        "POST_FREIGHTPROVIDERS": Route("POST", "/job/{jobDisplayId}/freightproviders", None, "ServiceBaseResponse", {}),
        "POST_FREIGHTPROVIDERS_RATEQUOTE": Route("POST", "/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote", "SetRateModel", "ServiceBaseResponse", {}),
        "POST_ITEM_NOTES": Route("POST", "/job/{jobDisplayId}/item/notes", "JobItemNotesData", "ServiceBaseResponse", {}),
        "POST_NOTE": Route("POST", "/job/{jobDisplayId}/note", "TaskNoteModel", "JobTaskNote", {}),
        "POST_ONHOLD": Route("POST", "/job/{jobDisplayId}/onhold", "SaveOnHoldRequest", "SaveOnHoldResponse", {}),
        "POST_ONHOLD_COMMENT": Route("POST", "/job/{jobDisplayId}/onhold/{onHoldId}/comment", None, "OnHoldNoteDetails", {}),
        "POST_PARCELITEMS": Route("POST", "/job/{jobDisplayId}/parcelitems", "SaveAllParcelItemsRequest", "List[ParcelItemWithPackage]", {}),
        "POST_PAYMENT_ACHCREDIT_TRANSFER": Route("POST", "/job/{jobDisplayId}/payment/ACHCreditTransfer", None, "ServiceBaseResponse", {}),
        "POST_PAYMENT_ACHPAYMENT_SESSION": Route("POST", "/job/{jobDisplayId}/payment/ACHPaymentSession", None, "ServiceBaseResponse", {}),
        "POST_PAYMENT_ATTACH_CUSTOMER_BANK": Route("POST", "/job/{jobDisplayId}/payment/attachCustomerBank", "AttachCustomerBankModel", "ServiceBaseResponse", {}),
        "POST_PAYMENT_BANKSOURCE": Route("POST", "/job/{jobDisplayId}/payment/banksource", "PaymentSourceDetails", "ServiceBaseResponse", {}),
        "POST_PAYMENT_BYSOURCE": Route("POST", "/job/{jobDisplayId}/payment/bysource", None, "ServiceBaseResponse", {}),
        "POST_PAYMENT_CANCEL_JOB_ACHVERIFICATION": Route("POST", "/job/{jobDisplayId}/payment/cancelJobACHVerification", None, "ServiceBaseResponse", {}),
        "POST_PAYMENT_VERIFY_JOB_ACHSOURCE": Route("POST", "/job/{jobDisplayId}/payment/verifyJobACHSource", "VerifyBankAccountRequest", "ServiceBaseResponse", {}),
        "POST_SEARCH_BY_DETAILS": Route("POST", "/job/searchByDetails", "SearchJobFilter", "ServiceBaseResponse", {}),
        "POST_SHIPMENT_ACCESSORIAL": Route("POST", "/job/{jobDisplayId}/shipment/accessorial", "JobParcelAddOn", "ServiceBaseResponse", {}),
        "POST_SHIPMENT_BOOK": Route("POST", "/job/{jobDisplayId}/shipment/book", "BookShipmentRequest", "ServiceBaseResponse", {}),
        "POST_SHIPMENT_EXPORTDATA": Route("POST", "/job/{jobDisplayId}/shipment/exportdata", "InternationalParams", "ServiceBaseResponse", {}),
        "POST_SHIPMENT_RATEQUOTES": Route("POST", "/job/{jobDisplayId}/shipment/ratequotes", "TransportationRatesRequestModel", "JobCarrierRatesModel", {}),
        "POST_SMS": Route("POST", "/job/{jobDisplayId}/sms", "SendSMSModel", "ServiceBaseResponse", {}),
        "POST_SMS_READ": Route("POST", "/job/{jobDisplayId}/sms/read", "MarkSmsAsReadModel", "ServiceBaseResponse", {}),
        "POST_STATUS_QUOTE": Route("POST", "/job/{jobDisplayId}/status/quote", None, "ServiceBaseResponse", {}),
        "POST_TIMELINE": Route("POST", "/job/{jobDisplayId}/timeline", "TimelineTaskInput", "SaveResponseModel", {}),
        "POST_TIMELINE_INCREMENTJOBSTATUS": Route("POST", "/job/{jobDisplayId}/timeline/incrementjobstatus", "IncrementJobStatusInputModel", "IncrementJobStatusResponseModel", {}),
        "POST_TIMELINE_UNDOINCREMENTJOBSTATUS": Route("POST", "/job/{jobDisplayId}/timeline/undoincrementjobstatus", None, "ServiceBaseResponse", {}),
        "POST_TRANSFER": Route("POST", "/job/transfer/{jobDisplayId}", "TransferModel", "ServiceBaseResponse", {}),
        "PUT_ITEM": Route("PUT", "/job/{jobDisplayId}/item/{itemId}", "JobItemInfoData", "ServiceBaseResponse", {}),
        "PUT_NOTE": Route("PUT", "/job/{jobDisplayId}/note/{id}", "TaskNoteModel", "ServiceBaseResponse", {}),
        "PUT_ONHOLD": Route("PUT", "/job/{jobDisplayId}/onhold/{onHoldId}", "SaveOnHoldRequest", "SaveOnHoldResponse", {}),
        "PUT_ONHOLD_DATES": Route("PUT", "/job/{jobDisplayId}/onhold/{onHoldId}/dates", "SaveOnHoldDatesModel", "ResolveJobOnHoldResponse", {}),
        "PUT_ONHOLD_RESOLVE": Route("PUT", "/job/{jobDisplayId}/onhold/{onHoldId}/resolve", "SaveOnHoldRequest", "ResolveJobOnHoldResponse", {}),
        "PUT_SAVE": Route("PUT", "/job/save", "JobSaveRequest", "ServiceBaseResponse", {}),
    },
    "JOBINTACCT": {
        "DELETE": Route("DELETE", "/jobintacct/{jobDisplayId}/{franchiseeId}", None, "ServiceBaseResponse", {}),
        "GET": Route("GET", "/jobintacct/{jobDisplayId}", None, "CreateJobIntacctModel", {}),
        "POST": Route("POST", "/jobintacct/{jobDisplayId}", "CreateJobIntacctModel", "ServiceBaseResponse", {}),
        "APPLY_REBATE": Route("POST", "/jobintacct/{jobDisplayId}/applyRebate", None, "ServiceBaseResponse", {}),
        "DRAFT": Route("POST", "/jobintacct/{jobDisplayId}/draft", "CreateJobIntacctModel", "ServiceBaseResponse", {}),
    },
    "LOOKUP": {
        "GET": Route("GET", "/lookup/{masterConstantKey}/{valueId}", None, "LookupValue", {}),
        "ACCESS_KEY": Route("GET", "/lookup/accessKey/{accessKey}", None, "LookupAccessKey", {}),
        "ACCESS_KEYS": Route("GET", "/lookup/accessKeys", None, "List[LookupAccessKey]", {}),
        "COMON_INSURANCE": Route("GET", "/lookup/comonInsurance", None, None, {}),
        "CONTACT_TYPES": Route("GET", "/lookup/contactTypes", None, "List[ContactTypeEntity]", {}),
        "COUNTRIES": Route("GET", "/lookup/countries", None, "List[CountryCodeDto]", {}),
        "DENSITY_CLASS_MAP": Route("GET", "/lookup/densityClassMap", None, "List[GuidSequentialRangeValue]", {}),
        "DOCUMENT_TYPES": Route("GET", "/lookup/documentTypes", None, "List[LookupDocumentType]", {}),
        "ITEMS": Route("GET", "/lookup/items", None, None, {}),
        "PARCEL_PACKAGE_TYPES": Route("GET", "/lookup/parcelPackageTypes", None, "List[LookupValue]", {}),
        "PPCCAMPAIGNS": Route("GET", "/lookup/PPCCampaigns", None, None, {}),
        "REFER_CATEGORY": Route("GET", "/lookup/referCategory", None, None, {}),
        "REFER_CATEGORY_HEIRACHY": Route("GET", "/lookup/referCategoryHeirachy", None, None, {}),
        "RESET_MASTER_CONSTANT_CACHE": Route("GET", "/lookup/resetMasterConstantCache", None, None, {}),
    },
    "NOTE": {
        "GET": Route("GET", "/note", None, "List[Notes]", {}),
        "GET_SUGGEST_USERS": Route("GET", "/note/suggestUsers", None, "List[SuggestedContactEntity]", {}),
        "POST": Route("POST", "/note", "NoteModel", "Notes", {}),
        "PUT": Route("PUT", "/note/{id}", "NoteModel", "ServiceBaseResponse", {}),
    },
    "NOTIFICATIONS": {
        "GET": Route("GET", "/notifications", None, "NotificationsResponse", {}),
    },
    "PARTNER": {
        "GET": Route("GET", "/partner", None, "List[Partner]", {}),
        "POST_SEARCH": Route("POST", "/partner/search", "SearchPartnersDataSourceLoadOptions", "List[Partner]", {}),
    },
    "REPORTS": {
        "INSURANCE": Route("POST", "/reports/insurance", "InsuranceReportRequest", "InsuranceReport", {}),
        "REFERRED_BY": Route("POST", "/reports/referredBy", "ReferredByReportRequest", "ReferredByReport", {}),
        "SALES": Route("POST", "/reports/sales", "SalesForecastReportRequest", "SalesForecastReport", {}),
        "SALES_DRILLDOWN": Route("POST", "/reports/salesDrilldown", "Web2LeadRevenueFilter", "ServiceBaseResponse", {}),
        "SALES_SUMMARY": Route("POST", "/reports/sales/summary", "SalesForecastSummaryRequest", "SalesForecastSummary", {}),
        "TOP_REVENUE_CUSTOMERS": Route("POST", "/reports/topRevenueCustomers", "Web2LeadRevenueFilter", "RevenueCustomer", {}),
        "TOP_REVENUE_SALES_REPS": Route("POST", "/reports/topRevenueSalesReps", "Web2LeadRevenueFilter", "RevenueCustomer", {}),
        "WEB2LEAD": Route("POST", "/reports/web2Lead", "Web2LeadV2RequestModel", "Web2LeadReport", {}),
    },
    "RFQ": {
        "GET": Route("GET", "/rfq/{rfqId}", None, "QuoteRequestDisplayInfo", {}),
        "FORJOB": Route("GET", "/rfq/forjob/{jobId}", None, "List[QuoteRequestDisplayInfo]", {}),
        "ACCEPT": Route("POST", "/rfq/{rfqId}/accept", "AcceptModel", "ServiceBaseResponse", {}),
        "ACCEPTWINNER": Route("POST", "/rfq/{rfqId}/acceptwinner", None, "ServiceBaseResponse", {}),
        "CANCEL": Route("POST", "/rfq/{rfqId}/cancel", None, "ServiceBaseResponse", {}),
        "COMMENT": Route("POST", "/rfq/{rfqId}/comment", None, "ServiceBaseResponse", {}),
        "DECLINE": Route("POST", "/rfq/{rfqId}/decline", None, "ServiceBaseResponse", {}),
    },
    "SHIPMENT": {
        "GET": Route("GET", "/shipment", None, "ShipmentDetails", {}),
        "ACCESSORIALS": Route("GET", "/shipment/accessorials", None, "List[ParcelAddOn]", {}),
        "DOCUMENT": Route("GET", "/shipment/document/{docId}", None, "ShippingDocument", {}),
    },
    "SMSTEMPLATE": {
        "DELETE": Route("DELETE", "/SmsTemplate/{templateId}", None, "ServiceBaseResponse", {}),
        "GET": Route("GET", "/SmsTemplate/{templateId}", None, "SmsTemplateModel", {}),
        "JOB_STATUSES": Route("GET", "/SmsTemplate/jobStatuses", None, "List[SmsJobStatus]", {}),
        "LIST": Route("GET", "/SmsTemplate/list", None, "List[SmsTemplateModel]", {}),
        "NOTIFICATION_TOKENS": Route("GET", "/SmsTemplate/notificationTokens", None, "List[NotificationTokenGroup]", {}),
        "SAVE": Route("POST", "/SmsTemplate/save", "SmsTemplateModel", "ServiceBaseResponse", {}),
    },
    "USERS": {
        "POCUSERS": Route("GET", "/users/pocusers", None, "List[PocUser]", {}),
        "ROLES": Route("GET", "/users/roles", None, "List[str]", {}),
        "LIST": Route("POST", "/users/list", "WebApiDataSourceLoadOptions", "ServiceBaseResponse", {}),
        "USER": Route("POST", "/users/user", "CreateUserModel", "ServiceBaseResponse", {}),
        "USER_UPDATE": Route("PUT", "/users/user", "UserInfo", "ServiceBaseResponse", {}),
    },
    "V2": {
        "JOB_TRACKING": Route("GET", "/v2/job/{jobDisplayId}/tracking/{historyAmount}", None, "ShipmentTrackingDetails", {}),
    },
    "V3": {
        "JOB_TRACKING": Route("GET", "/v3/job/{jobDisplayId}/tracking/{historyAmount}", None, "JobTrackingResponseV3", {}),
    },
    "VALUES": {
        "GET": Route("GET", "/Values", None, "ValuesResponse", {}),
    },
    "VIEWS": {
        "DELETE": Route("DELETE", "/views/{viewId}", None, "ServiceBaseResponse", {}),
        "GET": Route("GET", "/views/{viewId}", None, "GridViewDetails", {}),
        "ACCESSINFO": Route("GET", "/views/{viewId}/accessinfo", None, "GridViewAccess", {}),
        "ALL": Route("GET", "/views/all", None, "List[GridViewDetails]", {}),
        "DATASETSP": Route("GET", "/views/datasetsp/{spName}", None, "List[StoredProcedureColumn]", {}),
        "DATASETSPS": Route("GET", "/views/datasetsps", None, "List[str]", {}),
        "POST": Route("POST", "/views", "GridViewDetails", "ServiceBaseResponse", {}),
        "PUT_ACCESS": Route("PUT", "/views/{viewId}/access", None, "ServiceBaseResponse", {}),
    },
    "WEBHOOKS": {
        "POST_STRIPE_CHECKOUT_SESSION_COMPLETED": Route("POST", "/webhooks/stripe/checkout.session.completed", None, "ServiceBaseResponse", {}),
        "POST_STRIPE_CONNECT_HANDLE": Route("POST", "/webhooks/stripe/connect/handle", None, "ServiceBaseResponse", {}),
        "POST_STRIPE_HANDLE": Route("POST", "/webhooks/stripe/handle", None, "ServiceBaseResponse", {}),
        "POST_TWILIO_BODY_SMS_INBOUND": Route("POST", "/webhooks/twilio/body-sms-inbound", "TwilioInboundMessageWebhookModel", "ServiceBaseResponse", {}),
        "POST_TWILIO_FORM_SMS_INBOUND": Route("POST", "/webhooks/twilio/form-sms-inbound", None, "ServiceBaseResponse", {}),
        "POST_TWILIO_SMS_STATUS_CALLBACK": Route("POST", "/webhooks/twilio/smsStatusCallback", None, "ServiceBaseResponse", {}),
    },
}


__all__ = ["SCHEMA", "Route"]
