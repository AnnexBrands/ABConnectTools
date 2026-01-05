"""ABConnect API models package.

Auto-generated from swagger.json specification.
Contains Pydantic models for all API schemas.
"""

from typing import TYPE_CHECKING

# Import base and enums first as they don't have dependencies
from .base import *
from .enums import *

# TYPE_CHECKING imports for IDE support (not imported at runtime)
if TYPE_CHECKING:
    from .account import AccountProfile, ChangePasswordModel, ConfirmEmailModel, ForgotLoginModel, RegistrationModel, ResetPasswordModel
    from .address import Address, AddressData, AddressDetails, AddressDetailsMergePreviewDataItem, AddressIsValidResult, CalendarAddress, FreightRateRequestAddressDetails, OverridableAddressData, PlannerAddress, SaveValidatedRequest, SearchAddress, SoldToAddress
    from .advancedsettings import AdvancedSettingsEntitySaveModel
    from .calendar import BaseInfoCalendar, Calendar
    from .carriererrormessage import CarrierErrorMessage
    from .catalog import AddCatalogRequest, AddLotRequest, AddSellerRequest, BulkInsertCatalogRequest, BulkInsertLotRequest, BulkInsertRequest, BulkInsertSellerRequest, CatalogDto, CatalogExpandedDto, CatalogExpandedDtoPaginatedList, CatalogWithSellersDto, GetLotsOverridesQuery, ImageLinkDto, LotCatalogDto, LotCatalogInformationDto, LotDataDto, LotDto, LotDtoPaginatedList, LotOverrideDto, PaginatedList, SellerDto, SellerExpandedDto, SellerExpandedDtoPaginatedList, UpdateCatalogRequest, UpdateLotRequest, UpdateSellerRequest
    from .commodity import CommodityDetails, CommodityForMapInfo, CommodityMap, CommodityMapDetails, CommodityWithParents
    from .companies import Company, CompanyAddressInfo, CompanyBrandTreeNode, CompanyDetails, CompanyDetailsBaseInfo, CompanyDetailsFinalMileTariffItem, CompanyDetailsInsurancePricing, CompanyDetailsPreferences, CompanyDetailsServicePricings, CompanyDetailsTaxPricing, CompanyImageData, CompanyInfo, CompanyInsurancePricing, CompanyMaterial, CompanyServicePricing, CompanySimple, CompanyTaxPricing, ContactDetailsCompanyInfo, PackagingLaborSettings, PackagingTariffSettings, SaveCompanyMaterialModel, SaveGeoSettingModel, SearchCompanyDataSourceLoadOptions, SearchCompanyModel, SearchCompanyResponse, TagBoxDataSourceLoadOptions, UpdateCarrierAccountsModel, WebApiDataSourceLoadOptions
    from .companysettings import CompanySetupData
    from .contacthistory import ContactHistoryAggregatedCost, ContactHistoryDataSourceLoadOptions, ContactHistoryGraphData, ContactHistoryInfo
    from .contactmerge import MergeContactsPreviewInfo, MergeContactsPreviewRequestModel, MergeContactsRequestModel
    from .contacts import BaseContactDetails, CalendarContact, Contact, ContactAddressDetails, ContactAddressEditDetails, ContactDetailedInfo, ContactDetails, ContactEmailDetails, ContactEmailEditDetails, ContactHistoryPricePerPound, ContactHistoryRevenueSum, ContactPhoneDetails, ContactPhoneEditDetails, ContactPrimaryDetails, MergeContactsSearchRequestModel, MergeContactsSearchRequestParameters, PlannerContact, SearchContactEntityResult, SearchContactRequest, ShipmentContactAddressDetails, ShipmentContactDetails
    from .containerthicknessinches import ContainerThickness
    from .dashboard import GridSettingsEntity, InboundNewDashboardItem, IncrementJobStatusInputModel, IncrementJobStatusResponseModel, InhouseNewDashboardItem, LocalDeliveriesNewDashboardItem, OutboundNewDashboardItem, RecentEstimatesNewDashboardItem, SaveGridSettingsModel, UndoIncrementJobStatusInputModel
    from .document_upload import ItemPhotoUploadRequest, ItemPhotoUploadResponse, UploadedFile
    from .documents import DocumentUpdateModel
    from .globalsettings import CompanyHierarchyInfo, SelectApproveInsuranceResult
    from .gridviews import GridViewAccess, GridViewDetails
    from .job import BaseInfoCalendarJob, CalendarJob, ChangeJobAgentRequest, CreateScheduledJobEmailResponse, FeedbackSaveModel, FreightShimpment, JobContactDetails, JobExportData, JobItemNotesData, JobSaveRequest, JobSaveRequestModel, SearchJobFilter, SearchJobInfo, TransferModel
    from .jobemail import SendDocumentEmailModel
    from .jobform import FormsShipmentPlan
    from .jobfreightproviders import PricedFreightProvider, SetRateModel, ShipmentPlanProvider
    from .jobintacct import CreateJobIntacctModel
    from .jobnote import JobTaskNote, TaskNoteModel
    from .jobonhold import ExtendedOnHoldInfo, OnHoldDetails, OnHoldNoteDetails, OnHoldUser, ResolveJobOnHoldResponse, SaveOnHoldDatesModel, SaveOnHoldRequest, SaveOnHoldResponse
    from .jobparcelitems import ParcelItem, ParcelItemWithPackage
    from .jobpayment import AttachCustomerBankModel, PaymentSourceDetails, VerifyBankAccountRequest
    from .jobrfq import QuoteRequestDisplayInfo
    from .jobshipment import BookShipmentRequest, DeleteShipRequestModel, InternationalParams, JobCarrierRatesModel, JobParcelAddOn, ShipmentOriginDestination, TransportationRatesRequestModel
    from .jobsms import MarkSmsAsReadModel, SendSMSModel
    from .jobsmstemplate import NotificationToken, NotificationTokenGroup, SmsJobStatus, SmsTemplateModel
    from .jobtimeline import BaseTaskModel, CarrierTask, CompanyListItem, DeleteTaskResponse, SaveResponseModel, TimelineResponse, TimelineTaskInput, UpdateTaskModel
    from .jobtracking import ShipmentTrackingDetails
    from .jobtrackingv3 import JobTrackingResponseV3
    from .lookup import ContactTypeEntity, CountryCodeDto, LookupKeys, LookupValue
    from .note import NoteModel, Notes, SuggestedContactEntity
    from .partner import Partner, PartnerServiceResponse
    from .planner import PlannerTask
    from .reports import InsuranceReport, InsuranceReportRequest, ReferredByReport, ReferredByReportRequest, RevenueCustomer, SalesForecastReport, SalesForecastReportRequest, SalesForecastSummary, SalesForecastSummaryRequest, Web2LeadReport, Web2LeadRevenueFilter, Web2LeadV2RequestModel
    from .rfq import AcceptModel
    from .shared import AccesorialCharges, AutoCompleteValue, Base64File, BaseTask, BookShipmentSpecificParams, CalendarItem, CalendarNotes, CalendarTask, CarrierAccountInfo, CarrierInfo, CarrierProviderMessage, CarrierRateModel, CarrierTaskModel, Commodity, CreatedTask, CustomerInfo, Details, DocumentDetails, EmailDetails, EstesAccountData, ExportPackingInfo, ExportTotalCosts, ExpressFreightDetail, FedExAccountData, FedExRestApiAccount, FedExSpecific, ForwardAirAccountData, FranchiseeCarrierAccounts, GlobalTranzAccountData, GroupingInfo, HandlingUnitModel, InTheFieldTaskModel, InitialNoteModel, InsuranceOption, ItemTotals, Items, JToken, LaborCharges, LastObtainNFM, LatLng, LookupItem, MaerskAccountData, MasterMaterials, NameValueEntity, ObtainNFMParcelItem, ObtainNFMParcelService, OnlinePaymentSettings, PackagingLaborHours, PageOrderedRequestModel, PhoneDetails, PickupLaborHoursRule, PilotAccountData, PlannerLabor, QuoteRequestComment, RequestedParcelPackaging, RoadRunnerAccountData, RoyaltiesCharges, SearchCustomerInfo, ServiceBaseResponse, ServiceInfo, ServicePricingsMarkup, ServiceWarningResponse, ShipmentTrackingDocument, ShippingHistoryStatus, ShippingPackageInfo, SimplePriceTariff, SimpleTaskModel, SoldToDetails, SortBy, SortByModel, SortingInfo, StoredProcedureColumn, StringMergePreviewDataItem, StringOverridable, SummaryInfo, TaskTruckInfo, TaxOption, TeamWWAccountData, TimeLog, TimeLogModel, TimeLogPause, TimeLogPauseModel, TimeSpan, TrackingCarrierProps, TrackingStatusV2, TransportationCharges, TransportationRatesRequest, UPSAccountData, UPSSpecific, USPSAccountData, USPSSpecific, UpdateDateModel, UpdateTruckModel, WeightInfo, WorkTimeLog
    from .shipment import ParcelAddOn, ParcelAddOnOptionsGroup, ParcelAddOnRadioOption, ShipmentDetails, ShippingDocument
    from .truck import SaveEntityResponse, SaveTruckRequest, Truck
    from .twiliowebhook import TwilioSmsStatusCallback
    from .users import CreateUserModel, PocUser, UserInfo, Users
    from .notifications import NotificationsResponse
    from .values import ValuesResponse

# Lazy loading function to avoid circular imports
_MODELS = {}
_REBUILT = False

def __getattr__(name):
    """Lazy load models to avoid circular imports.

    Automatically rebuilds all models on first access to resolve forward references.
    """
    global _REBUILT

    # Rebuild all models once on first access to resolve forward references
    if not _REBUILT:
        rebuild_models()
        _REBUILT = True

    # Check cache (models may have been loaded during rebuild)
    if name in _MODELS:
        return _MODELS[name]

    # Map of model names to their modules (auto-generated from swagger.json)
    module_map = {
        'AcceptModel': 'rfq',
        'AccountProfile': 'account',
        'AddCatalogRequest': 'catalog',
        'AddLotRequest': 'catalog',
        'AddSellerRequest': 'catalog',
        'AccesorialCharges': 'shared',
        'Address': 'address',
        'AddressData': 'address',
        'AddressDetails': 'address',
        'AddressDetailsMergePreviewDataItem': 'address',
        'AddressIsValidResult': 'address',
        'AdvancedSettingsEntitySaveModel': 'advancedsettings',
        'AttachCustomerBankModel': 'jobpayment',
        'AutoCompleteValue': 'shared',
        'Base64File': 'shared',
        'BaseContactDetails': 'contacts',
        'BaseInfoCalendar': 'calendar',
        'BaseInfoCalendarJob': 'job',
        'BaseTask': 'shared',
        'BaseTaskModel': 'jobtimeline',
        'BookShipmentRequest': 'jobshipment',
        'BulkInsertCatalogRequest': 'catalog',
        'BulkInsertLotRequest': 'catalog',
        'BulkInsertRequest': 'catalog',
        'BulkInsertSellerRequest': 'catalog',
        'BookShipmentSpecificParams': 'shared',
        'Calendar': 'calendar',
        'CalendarAddress': 'address',
        'CalendarContact': 'contacts',
        'CalendarItem': 'shared',
        'CalendarJob': 'job',
        'CalendarNotes': 'shared',
        'CalendarTask': 'shared',
        'CatalogDto': 'catalog',
        'CatalogExpandedDto': 'catalog',
        'CatalogExpandedDtoPaginatedList': 'catalog',
        'CatalogWithSellersDto': 'catalog',
        'CarrierAccountInfo': 'shared',
        'CarrierErrorMessage': 'carriererrormessage',
        'CarrierInfo': 'shared',
        'CarrierProviderMessage': 'shared',
        'CarrierRateModel': 'shared',
        'CarrierTask': 'jobtimeline',
        'CarrierTaskModel': 'shared',
        'ChangeJobAgentRequest': 'job',
        'ChangePasswordModel': 'account',
        'Commodity': 'shared',
        'Company': 'companies',
        'CompanyAddressInfo': 'companies',
        'CompanyBrandTreeNode': 'companies',
        'CompanyDetails': 'companies',
        'CompanyDetailsBaseInfo': 'companies',
        'CompanyDetailsFinalMileTariffItem': 'companies',
        'CompanyDetailsInsurancePricing': 'companies',
        'CompanyDetailsPreferences': 'companies',
        'CompanyDetailsServicePricings': 'companies',
        'CompanyDetailsTaxPricing': 'companies',
        'CompanyGeoAreaCompanies': 'companies',
        'CompanyHierarchyInfo': 'globalsettings',
        'CompanyImageData': 'companies',
        'CompanyInfo': 'companies',
        'CompanyInsurancePricing': 'companies',
        'CompanyListItem': 'jobtimeline',
        'CompanyMaterial': 'companies',
        'CompanyServicePricing': 'companies',
        'CompanySimple': 'companies',
        'CompanySetupData': 'companysettings',
        'CompanyTaxPricing': 'companies',
        'CommodityDetails': 'commodity',
        'CommodityForMapInfo': 'commodity',
        'CommodityMap': 'commodity',
        'CommodityMapDetails': 'commodity',
        'CommodityWithParents': 'commodity',
        'ConfirmEmailModel': 'account',
        'Contact': 'contacts',
        'ContactAddressDetails': 'contacts',
        'ContactAddressEditDetails': 'contacts',
        'ContactDetailedInfo': 'contacts',
        'ContactDetails': 'contacts',
        'ContactDetailsCompanyInfo': 'companies',
        'ContactEmailDetails': 'contacts',
        'ContactEmailEditDetails': 'contacts',
        'ContactHistoryAggregatedCost': 'contacthistory',
        'ContactHistoryDataSourceLoadOptions': 'contacthistory',
        'ContactHistoryGraphData': 'contacthistory',
        'ContactHistoryInfo': 'contacthistory',
        'ContactHistoryPricePerPound': 'contacts',
        'ContactHistoryRevenueSum': 'contacts',
        'ContactPhoneDetails': 'contacts',
        'ContactPhoneEditDetails': 'contacts',
        'ContactPrimaryDetails': 'contacts',
        'ContactUser': 'contacts',
        'ContactTypeEntity': 'lookup',
        'ContainerThickness': 'containerthicknessinches',
        'CountryCodeDto': 'lookup',
        'CreateJobIntacctModel': 'jobintacct',
        'CreateScheduledJobEmailResponse': 'job',
        'CreateUserModel': 'users',
        'CreatedTask': 'shared',
        'CustomerInfo': 'shared',
        'DashboardResponse': 'dashboard',
        'DeleteShipRequestModel': 'jobshipment',
        'DeleteTaskResponse': 'jobtimeline',
        'Details': 'shared',
        'DocumentDetails': 'shared',
        'DocumentUploadRequest': 'document_upload',
        'DocumentUploadResponse': 'document_upload',
        'DocumentUpdateModel': 'documents',
        'EmailDetails': 'shared',
        'EstesAccountData': 'shared',
        'ExportPackingInfo': 'shared',
        'ExportTotalCosts': 'shared',
        'ExpressFreightDetail': 'shared',
        'ExtendedOnHoldInfo': 'jobonhold',
        'FedExAccountData': 'shared',
        'FedExRestApiAccount': 'shared',
        'FedExSpecific': 'shared',
        'FeedbackSaveModel': 'job',
        'ForgotLoginModel': 'account',
        'FormsShipmentPlan': 'jobform',
        'ForwardAirAccountData': 'shared',
        'FranchiseeCarrierAccounts': 'shared',
        'FreightRateRequestAddressDetails': 'address',
        'FreightShimpment': 'job',
        'GetLotsOverridesQuery': 'catalog',
        'GuidSequentialRangeValue': 'lookup',
        'GlobalTranzAccountData': 'shared',
        'GridSettingsEntity': 'dashboard',
        'GridViewAccess': 'gridviews',
        'GridViewDetails': 'gridviews',
        'GroupingInfo': 'shared',
        'HandlingUnitModel': 'shared',
        'ImageLinkDto': 'catalog',
        'InTheFieldTaskModel': 'shared',
        'InboundNewDashboardItem': 'dashboard',
        'IncrementJobStatusInputModel': 'dashboard',
        'IncrementJobStatusResponseModel': 'dashboard',
        'InhouseNewDashboardItem': 'dashboard',
        'InitialNoteModel': 'shared',
        'InsuranceOption': 'shared',
        'InsuranceReport': 'reports',
        'InsuranceReportRequest': 'reports',
        'InternationalParams': 'jobshipment',
        'ItemPhotoUploadRequest': 'document_upload',
        'ItemPhotoUploadResponse': 'document_upload',
        'ItemTotals': 'shared',
        'Items': 'shared',
        'JToken': 'shared',
        'JobCarrierRatesModel': 'jobshipment',
        'JobContactDetails': 'job',
        'JobExportData': 'job',
        'JobItemNotesData': 'job',
        'JobParcelAddOn': 'jobshipment',
        'JobSaveRequest': 'job',
        'JobSaveRequestModel': 'job',
        'JobTaskNote': 'jobnote',
        'JobTrackingResponseV3': 'jobtrackingv3',
        'LaborCharges': 'shared',
        'LastObtainNFM': 'shared',
        'LatLng': 'shared',
        'LocalDeliveriesNewDashboardItem': 'dashboard',
        'LotCatalogDto': 'catalog',
        'LotCatalogInformationDto': 'catalog',
        'LotDataDto': 'catalog',
        'LotDto': 'catalog',
        'LotDtoPaginatedList': 'catalog',
        'LotOverrideDto': 'catalog',
        'LookupItem': 'shared',
        'LookupKeys': 'lookup',
        'LookupAccessKey': 'lookup',
        'LookupDocumentType': 'lookup',
        'LookupValue': 'lookup',
        'MaerskAccountData': 'shared',
        'MarkSmsAsReadModel': 'jobsms',
        'MasterMaterials': 'shared',
        'MergeContactsPreviewInfo': 'contactmerge',
        'MergeContactsPreviewRequestModel': 'contactmerge',
        'MergeContactsRequestModel': 'contactmerge',
        'MergeContactsSearchRequestModel': 'contacts',
        'MergeContactsSearchRequestParameters': 'contacts',
        'NameValueEntity': 'shared',
        'NoteModel': 'note',
        'Notes': 'note',
        'NotificationToken': 'jobsmstemplate',
        'NotificationTokenGroup': 'jobsmstemplate',
        'NotificationsResponse': 'notifications',
        'ObtainNFMParcelItem': 'shared',
        'ObtainNFMParcelService': 'shared',
        'OnHoldDetails': 'jobonhold',
        'OnHoldNoteDetails': 'jobonhold',
        'OnHoldUser': 'jobonhold',
        'OnlinePaymentSettings': 'shared',
        'OutboundNewDashboardItem': 'dashboard',
        'OverridableAddressData': 'address',
        'PackagingLaborHours': 'shared',
        'PackagingLaborSettings': 'companies',
        'PackagingTariffSettings': 'companies',
        'PageOrderedRequestModel': 'shared',
        'PaginatedList': 'catalog',
        'ParcelAddOn': 'shipment',
        'ParcelAddOnOptionsGroup': 'shipment',
        'ParcelAddOnRadioOption': 'shipment',
        'ParcelItem': 'jobparcelitems',
        'ParcelItemWithPackage': 'jobparcelitems',
        'Partner': 'partner',
        'PartnerServiceResponse': 'partner',
        'PaymentSourceDetails': 'jobpayment',
        'PhoneDetails': 'shared',
        'PickupLaborHoursRule': 'shared',
        'PilotAccountData': 'shared',
        'PlannerAddress': 'address',
        'PlannerContact': 'contacts',
        'PlannerLabor': 'shared',
        'PlannerTask': 'planner',
        'PricedFreightProvider': 'jobfreightproviders',
        'QuoteRequestComment': 'shared',
        'QuoteRequestDisplayInfo': 'jobrfq',
        'RecentEstimatesNewDashboardItem': 'dashboard',
        'ReferredByReport': 'reports',
        'ReferredByReportRequest': 'reports',
        'RegistrationModel': 'account',
        'RequestedParcelPackaging': 'shared',
        'ResetPasswordModel': 'account',
        'ResolveJobOnHoldResponse': 'jobonhold',
        'RevenueCustomer': 'reports',
        'RoadRunnerAccountData': 'shared',
        'RoyaltiesCharges': 'shared',
        'SalesForecastReport': 'reports',
        'SalesForecastReportRequest': 'reports',
        'SalesForecastSummary': 'reports',
        'SalesForecastSummaryRequest': 'reports',
        'SaveCompanyMaterialModel': 'companies',
        'SaveEntityResponse': 'truck',
        'SaveGeoSettingModel': 'companies',
        'SaveGridSettingsModel': 'dashboard',
        'SaveOnHoldDatesModel': 'jobonhold',
        'SaveOnHoldRequest': 'jobonhold',
        'SaveOnHoldResponse': 'jobonhold',
        'SaveResponseModel': 'jobtimeline',
        'SaveTruckRequest': 'truck',
        'SaveValidatedRequest': 'address',
        'SearchAddress': 'address',
        'SearchCompanyDataSourceLoadOptions': 'companies',
        'SearchCompanyModel': 'companies',
        'SearchCompanyResponse': 'companies',
        'SearchContactEntityResult': 'contacts',
        'SearchContactRequest': 'contacts',
        'SellerDto': 'catalog',
        'SellerExpandedDto': 'catalog',
        'SellerExpandedDtoPaginatedList': 'catalog',
        'SearchCustomerInfo': 'shared',
        'SearchJobFilter': 'job',
        'SearchJobInfo': 'job',
        'SelectApproveInsuranceResult': 'globalsettings',
        'SendDocumentEmailModel': 'jobemail',
        'SendSMSModel': 'jobsms',
        'ServiceBaseResponse': 'shared',
        'ServiceInfo': 'shared',
        'ServicePricingsMarkup': 'shared',
        'ServiceWarningResponse': 'shared',
        'SetRateModel': 'jobfreightproviders',
        'ShipmentContactAddressDetails': 'contacts',
        'ShipmentContactDetails': 'contacts',
        'ShipmentDetails': 'shipment',
        'ShipmentOriginDestination': 'jobshipment',
        'ShipmentPlanProvider': 'jobfreightproviders',
        'ShipmentTrackingDetails': 'jobtracking',
        'ShipmentTrackingDocument': 'shared',
        'ShippingDocument': 'shipment',
        'ShippingHistoryStatus': 'shared',
        'ShippingPackageInfo': 'shared',
        'SimplePriceTariff': 'shared',
        'SimpleTaskModel': 'shared',
        'SmsJobStatus': 'jobsmstemplate',
        'SmsTemplateModel': 'jobsmstemplate',
        'SoldToAddress': 'address',
        'SoldToDetails': 'shared',
        'SortBy': 'shared',
        'SortByModel': 'shared',
        'SortingInfo': 'shared',
        'StoredProcedureColumn': 'shared',
        'StringMergePreviewDataItem': 'shared',
        'StringOverridable': 'shared',
        'SuggestedContactEntity': 'note',
        'SummaryInfo': 'shared',
        'TagBoxDataSourceLoadOptions': 'companies',
        'TaskNoteModel': 'jobnote',
        'TaskTruckInfo': 'shared',
        'TaxOption': 'shared',
        'TeamWWAccountData': 'shared',
        'TimeLog': 'shared',
        'TimeLogModel': 'shared',
        'TimeLogPause': 'shared',
        'TimeLogPauseModel': 'shared',
        'TimeSpan': 'shared',
        'TimelineResponse': 'jobtimeline',
        'TimelineTaskInput': 'jobtimeline',
        'TrackingCarrierProps': 'shared',
        'TrackingStatusV2': 'shared',
        'TransferModel': 'job',
        'TransportationCharges': 'shared',
        'TransportationRatesRequest': 'shared',
        'TransportationRatesRequestModel': 'jobshipment',
        'Truck': 'truck',
        'TwilioSmsStatusCallback': 'twiliowebhook',
        'UPSAccountData': 'shared',
        'UPSSpecific': 'shared',
        'USPSAccountData': 'shared',
        'USPSSpecific': 'shared',
        'UndoIncrementJobStatusInputModel': 'dashboard',
        'UpdateCarrierAccountsModel': 'companies',
        'UpdateCatalogRequest': 'catalog',
        'UpdateDateModel': 'shared',
        'UpdateLotRequest': 'catalog',
        'UpdateSellerRequest': 'catalog',
        'UpdateTaskModel': 'jobtimeline',
        'UpdateTruckModel': 'shared',
        'UploadedFile': 'document_upload',
        'UserInfo': 'users',
        'PocUser': 'users',
        'Users': 'users',
        'ValuesResponse': 'values',
        'VerifyBankAccountRequest': 'jobpayment',
        'Web2LeadReport': 'reports',
        'Web2LeadRevenueFilter': 'reports',
        'Web2LeadV2RequestModel': 'reports',
        'WebApiDataSourceLoadOptions': 'companies',
        'WeightInfo': 'shared',
        'WorkTimeLog': 'shared',
    }

    if name in module_map:
        module_name = module_map[name]
        # Import the module
        import importlib
        module = importlib.import_module(f'.{module_name}', package='ABConnect.api.models')
        # Get the model from the module
        model = getattr(module, name)
        # Cache it
        _MODELS[name] = model
        return model

    raise AttributeError(f"module 'ABConnect.api.models' has no attribute '{name}'")

# Rebuild models after all are defined (called when needed)
def rebuild_models():
    """Rebuild all Pydantic models to resolve forward references."""
    # Import all model modules
    import importlib
    modules_to_rebuild = [
        'shared', 'jobtimeline', 'jobpayment',  # These first to resolve forward refs
        'account', 'address', 'companies', 'contacts', 'job',
        'jobform', 'jobshipment', 'documents',
        'users', 'dashboard', 'reports', 'lookup', 'jobnote'
    ]

    # Build a namespace with all model classes for forward reference resolution
    namespace = {}
    for module_name in modules_to_rebuild:
        try:
            module = importlib.import_module(f'.{module_name}', package='ABConnect.api.models')
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if hasattr(attr, 'model_rebuild'):
                    namespace[attr_name] = attr
        except ImportError:
            pass

    # Now rebuild all models with the complete namespace
    for module_name in modules_to_rebuild:
        try:
            module = importlib.import_module(f'.{module_name}', package='ABConnect.api.models')
            # Call model_rebuild on all Pydantic models in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if hasattr(attr, 'model_rebuild'):
                    try:
                        attr.model_rebuild(_types_namespace=namespace)
                    except:
                        pass  # Some models might not need rebuilding
        except ImportError:
            pass  # Module might not exist


# Explicit __all__ for IDE autocompletion and star imports
__all__ = [
    # Base classes
    'ABConnectBaseModel', 'IdentifiedModel', 'TimestampedModel', 'ActiveModel',
    'CompanyRelatedModel', 'JobRelatedModel', 'FullAuditModel', 'CompanyAuditModel', 'JobAuditModel',
    # Enums
    'CarrierAPI', 'CommercialCapabilities', 'CopyMaterialsFrom', 'DashboardType', 'DocumentSource',
    'DocumentType', 'ForgotType', 'FormType', 'GeometryType', 'HistoryCodeABCState', 'InheritSettingFrom',
    'JobAccessLevel', 'JobContactType', 'JobType', 'KnownFormId', 'LabelImageType', 'LabelType',
    'ListSortDirection', 'OperationsFormType', 'PaymentType', 'PropertyType', 'QuoteRequestStatus',
    'RangeDateEnum', 'RetransTimeZoneEnum', 'SelectedOption', 'SendEmailStatus', 'ServiceType',
    'SortByField', 'StatusEnum',
    # Models (lazily loaded)
    'AcceptModel', 'AccesorialCharges', 'AddCatalogRequest', 'AddLotRequest', 'AddSellerRequest',
    'Address', 'AddressData', 'AddressDetails', 'AddressDetailsMergePreviewDataItem', 'AddressIsValidResult',
    'AdvancedSettingsEntitySaveModel', 'AttachCustomerBankModel', 'AutoCompleteValue', 'Base64File',
    'BaseContactDetails', 'BaseInfoCalendar', 'BaseInfoCalendarJob', 'BaseTask', 'BaseTaskModel',
    'BookShipmentRequest', 'BookShipmentSpecificParams', 'BulkInsertCatalogRequest', 'BulkInsertLotRequest',
    'BulkInsertRequest', 'BulkInsertSellerRequest', 'Calendar', 'CalendarAddress', 'CalendarContact',
    'CalendarItem', 'CalendarJob', 'CalendarNotes', 'CalendarTask', 'CarrierAccountInfo', 'CarrierErrorMessage',
    'CarrierInfo', 'CarrierProviderMessage', 'CarrierRateModel', 'CarrierTask', 'CarrierTaskModel',
    'CatalogDto', 'CatalogExpandedDto', 'CatalogExpandedDtoPaginatedList', 'CatalogWithSellersDto',
    'ChangeJobAgentRequest', 'ChangePasswordModel', 'Commodity', 'CommodityDetails', 'CommodityForMapInfo',
    'CommodityMap', 'CommodityMapDetails', 'CommodityWithParents', 'Company', 'CompanyAddressInfo',
    'CompanyBrandTreeNode', 'CompanyDetails', 'CompanyDetailsBaseInfo', 'CompanyDetailsFinalMileTariffItem',
    'CompanyDetailsInsurancePricing', 'CompanyDetailsPreferences', 'CompanyDetailsServicePricings',
    'CompanyDetailsTaxPricing', 'CompanyHierarchyInfo', 'CompanyImageData', 'CompanyInfo',
    'CompanyInsurancePricing', 'CompanyListItem', 'CompanyMaterial', 'CompanyServicePricing',
    'CompanySimple', 'CompanySetupData', 'CompanyTaxPricing', 'ConfirmEmailModel', 'Contact', 'ContactAddressDetails',
    'ContactAddressEditDetails', 'ContactDetailedInfo', 'ContactDetails', 'ContactDetailsCompanyInfo',
    'ContactEmailDetails', 'ContactEmailEditDetails', 'ContactHistoryAggregatedCost',
    'ContactHistoryDataSourceLoadOptions', 'ContactHistoryGraphData', 'ContactHistoryInfo',
    'ContactHistoryPricePerPound', 'ContactHistoryRevenueSum', 'ContactPhoneDetails',
    'ContactPhoneEditDetails', 'ContactPrimaryDetails', 'ContactTypeEntity', 'ContainerThickness',
    'CountryCodeDto', 'CreateJobIntacctModel', 'CreateScheduledJobEmailResponse', 'CreateUserModel',
    'CreatedTask', 'CustomerInfo', 'DeleteShipRequestModel', 'DeleteTaskResponse', 'Details',
    'DocumentDetails', 'DocumentUpdateModel', 'EmailDetails', 'EstesAccountData', 'ExportPackingInfo',
    'ExportTotalCosts', 'ExpressFreightDetail', 'ExtendedOnHoldInfo', 'FedExAccountData',
    'FedExRestApiAccount', 'FedExSpecific', 'FeedbackSaveModel', 'ForgotLoginModel', 'FormsShipmentPlan',
    'ForwardAirAccountData', 'FranchiseeCarrierAccounts', 'FreightRateRequestAddressDetails',
    'FreightShimpment', 'GetLotsOverridesQuery', 'GlobalTranzAccountData', 'GridSettingsEntity',
    'GridViewAccess', 'GridViewDetails', 'GroupingInfo', 'HandlingUnitModel', 'ImageLinkDto',
    'InTheFieldTaskModel', 'InboundNewDashboardItem', 'IncrementJobStatusInputModel',
    'IncrementJobStatusResponseModel', 'InhouseNewDashboardItem', 'InitialNoteModel', 'InsuranceOption',
    'InsuranceReport', 'InsuranceReportRequest', 'InternationalParams', 'ItemPhotoUploadRequest',
    'ItemPhotoUploadResponse', 'ItemTotals', 'Items', 'JToken', 'JobCarrierRatesModel', 'JobContactDetails',
    'JobExportData', 'JobItemNotesData', 'JobParcelAddOn', 'JobSaveRequest', 'JobSaveRequestModel',
    'JobTaskNote', 'JobTrackingResponseV3', 'LaborCharges', 'LastObtainNFM', 'LatLng',
    'LocalDeliveriesNewDashboardItem', 'LookupItem', 'LookupKeys', 'LookupValue', 'LotCatalogDto',
    'LotCatalogInformationDto', 'LotDataDto', 'LotDto', 'LotDtoPaginatedList', 'LotOverrideDto',
    'MaerskAccountData', 'MarkSmsAsReadModel', 'MasterMaterials', 'MergeContactsPreviewInfo',
    'MergeContactsPreviewRequestModel', 'MergeContactsRequestModel', 'MergeContactsSearchRequestModel',
    'MergeContactsSearchRequestParameters', 'NameValueEntity', 'NoteModel', 'Notes', 'ObtainNFMParcelItem',
    'ObtainNFMParcelService', 'OnHoldDetails', 'OnHoldNoteDetails', 'OnHoldUser', 'OnlinePaymentSettings',
    'OutboundNewDashboardItem', 'OverridableAddressData', 'PackagingLaborHours', 'PackagingLaborSettings',
    'PackagingTariffSettings', 'PageOrderedRequestModel', 'PaginatedList', 'ParcelItem',
    'ParcelItemWithPackage', 'Partner', 'PartnerServiceResponse', 'PaymentSourceDetails', 'PhoneDetails',
    'PickupLaborHoursRule', 'PilotAccountData', 'PlannerAddress', 'PlannerContact', 'PlannerLabor',
    'PlannerTask', 'PricedFreightProvider', 'QuoteRequestComment', 'QuoteRequestDisplayInfo',
    'RecentEstimatesNewDashboardItem', 'ReferredByReport', 'ReferredByReportRequest', 'RegistrationModel',
    'RequestedParcelPackaging', 'ResetPasswordModel', 'ResolveJobOnHoldResponse', 'RevenueCustomer',
    'RoadRunnerAccountData', 'RoyaltiesCharges', 'SalesForecastReport', 'SalesForecastReportRequest',
    'SalesForecastSummary', 'SalesForecastSummaryRequest', 'SaveCompanyMaterialModel', 'SaveEntityResponse',
    'SaveGeoSettingModel', 'SaveGridSettingsModel', 'SaveOnHoldDatesModel', 'SaveOnHoldRequest',
    'SaveOnHoldResponse', 'SaveResponseModel', 'SaveTruckRequest', 'SaveValidatedRequest', 'SearchAddress',
    'SearchCompanyDataSourceLoadOptions', 'SearchCompanyModel', 'SearchCompanyResponse',
    'SearchContactEntityResult', 'SearchContactRequest', 'SearchCustomerInfo', 'SearchJobFilter',
    'SearchJobInfo', 'SelectApproveInsuranceResult', 'SellerDto', 'SellerExpandedDto',
    'SellerExpandedDtoPaginatedList', 'SendDocumentEmailModel', 'SendSMSModel', 'ServiceBaseResponse',
    'ServiceInfo', 'ServicePricingsMarkup', 'ServiceWarningResponse', 'SetRateModel',
    'ShipmentContactAddressDetails', 'ShipmentContactDetails', 'ShipmentDetails', 'ShipmentOriginDestination',
    'ShipmentPlanProvider', 'ShipmentTrackingDetails', 'ShipmentTrackingDocument', 'ShippingDocument',
    'ShippingHistoryStatus', 'ShippingPackageInfo', 'SimplePriceTariff', 'SimpleTaskModel', 'SmsTemplateModel',
    'SoldToAddress', 'SoldToDetails', 'SortBy', 'SortByModel', 'SortingInfo', 'StoredProcedureColumn',
    'StringMergePreviewDataItem', 'StringOverridable', 'SuggestedContactEntity', 'SummaryInfo',
    'TagBoxDataSourceLoadOptions', 'TaskNoteModel', 'TaskTruckInfo', 'TaxOption', 'TeamWWAccountData',
    'TimeLog', 'TimeLogModel', 'TimeLogPause', 'TimeLogPauseModel', 'TimeSpan', 'TimelineResponse',
    'TimelineTaskInput', 'TrackingCarrierProps', 'TrackingStatusV2', 'TransferModel', 'TransportationCharges',
    'TransportationRatesRequest', 'TransportationRatesRequestModel', 'Truck', 'TwilioSmsStatusCallback',
    'UPSAccountData', 'UPSSpecific', 'USPSAccountData', 'USPSSpecific', 'UndoIncrementJobStatusInputModel',
    'UpdateCarrierAccountsModel', 'UpdateCatalogRequest', 'UpdateDateModel', 'UpdateLotRequest',
    'UpdateSellerRequest', 'UpdateTaskModel', 'UpdateTruckModel', 'UploadedFile', 'UserInfo', 'Users',
    'VerifyBankAccountRequest', 'Web2LeadReport', 'Web2LeadRevenueFilter', 'Web2LeadV2RequestModel',
    'WebApiDataSourceLoadOptions', 'WeightInfo', 'WorkTimeLog',
    # Utilities
    'rebuild_models',
]