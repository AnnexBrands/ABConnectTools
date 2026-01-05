"""Companies models for ABConnect API."""

from typing import Any, Dict, List, Optional, TYPE_CHECKING
from pydantic import Field
from .base import ABConnectBaseModel, ActiveModel, CompanyRelatedModel, IdentifiedModel, TimestampedModel
from .shared import (
    LatLng, FranchiseeCarrierAccounts, InsuranceOption, TransportationCharges,
    ServicePricingsMarkup, LaborCharges, AccesorialCharges, RoyaltiesCharges,
    OnlinePaymentSettings, Base64File, SimplePriceTariff, PickupLaborHoursRule,
    TaxOption, PackagingLaborHours, SortingInfo, GroupingInfo, SummaryInfo
)
from .enums import CommercialCapabilities, InheritSettingFrom, GeometryType, CopyMaterialsFrom
from .address import AddressDetails, AddressData, OverridableAddressData, PlannerAddress

if TYPE_CHECKING:
    from .contacts import Contact
    from .address import Address

class CompanySimple(IdentifiedModel):
    """Simple company model for GET /companies/{id} response.

    This is the minimal response from the companies/{id} endpoint.
    """

    code: Optional[str] = Field(None, description="Company code")
    name: Optional[str] = Field(None, description="Company name")
    company_name: Optional[str] = Field(None, alias="companyName", description="Company name (alternate field)")
    type_id: Optional[str] = Field(None, alias="typeId", description="Company type ID")
    parent_company_id: Optional[str] = Field(None, alias="parentCompanyId", description="Parent company ID")


class CompanyBrandTreeNode(ABConnectBaseModel):
    """Company brand tree node for GET /companies/brandstree response.

    Represents a hierarchical tree of company brands where each node
    can have children nodes of the same type.
    """

    id: Optional[str] = Field(None, description="Company brand UUID")
    name: Optional[str] = Field(None, description="Brand name")
    code: Optional[str] = Field(None, description="Brand code")
    maps_marker_image: Optional[str] = Field(None, alias="mapsMarkerImage", description="Maps marker image path")
    children: Optional[List["CompanyBrandTreeNode"]] = Field(None, description="Child brand nodes")

    def __repr__(self) -> str:
        """
        Return a nicely indented, recursive string representation of the tree node.
        
        Example output:
            CompanyBrandTreeNode(code='ROOT', name='Acme Corp', children=[
                CompanyBrandTreeNode(code='BR1', name='Brand One', children=[]),
                CompanyBrandTreeNode(code='BR2', name='Brand Two', children=[
                    CompanyBrandTreeNode(code='SUB1', name='Sub Brand', children=[]),
                ]),
            ])
        """
        lines = []
        lines.append(f"CompanyBrandTreeNode(")
        lines.append(f"    code={self.code!r},")
        lines.append(f"    name={self.name!r},")
        
        if not self.children:
            lines.append(f"    children=[]")
        else:
            lines.append(f"    children=[")
            for child in self.children:
                # Recursive repr, indent each child line by 8 spaces
                child_repr = repr(child).split("\n")
                for line in child_repr:
                    lines.append(f"        {line}")
            lines.append(f"    ],")
        
        lines.append(f")")
        
        return "\n".join(lines)


class Company(TimestampedModel):
    """Company model"""

    company_id: Optional[str] = Field(None, alias="companyID")  # API uses uppercase ID
    address_id: Optional[str] = Field(None, alias="addressID")  # API uses uppercase ID
    address1: Optional[str] = Field(None)
    address2: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    state_code: Optional[str] = Field(None, alias="stateCode")
    country_name: Optional[str] = Field(None, alias="countryName")
    country_code: Optional[str] = Field(None, alias="countryCode")
    country_id: Optional[str] = Field(None, alias="countryID")  # API uses uppercase ID
    zip_code: Optional[str] = Field(None, alias="zipCode")
    is_active: Optional[bool] = Field(None, alias="isActive")
    latitude: Optional[str] = Field(None)
    longitude: Optional[str] = Field(None)
    result: Optional[str] = Field(None)
    address_mapping_id: Optional[str] = Field(None, alias="addressMappingID")  # API uses uppercase ID
    contact_id: Optional[str] = Field(None, alias="contactID")  # API uses uppercase ID
    user_id: Optional[str] = Field(None, alias="userId")  # API sends lowercase
    user_id_upper: Optional[str] = Field(None, alias="userID")  # API also sends uppercase in same response
    primary_customer_name: Optional[str] = Field(None, alias="primaryCustomerName")
    contact_info: Optional["Contact"] = Field(None, alias="contactInfo")
    address: Optional["Address"] = Field(None)
    company_name: Optional[str] = Field(None, alias="companyName")
    contact_name: Optional[str] = Field(None, alias="contactName")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    company_type: Optional[str] = Field(None, alias="companyType")
    parcel_only: Optional[bool] = Field(None, alias="parcelOnly")
    is_third_party: Optional[bool] = Field(None, alias="isThirdParty")
    company_code: Optional[str] = Field(None, alias="companyCode")
    parent_company_name: Optional[str] = Field(None, alias="parentCompanyName")
    company_type_id: Optional[str] = Field(None, alias="companyTypeID")  # API uses uppercase ID
    parent_company_id: Optional[str] = Field(None, alias="parentCompanyID")  # API uses uppercase ID
    company_phone: Optional[str] = Field(None, alias="companyPhone")
    company_email: Optional[str] = Field(None, alias="companyEmail")
    company_fax: Optional[str] = Field(None, alias="companyFax")
    company_web_site: Optional[str] = Field(None, alias="companyWebSite")
    industry_type: Optional[str] = Field(None, alias="industryType")
    industry_type_name: Optional[str] = Field(None, alias="industryTypeName")
    tax_id: Optional[str] = Field(None, alias="taxId")
    customer_cell: Optional[str] = Field(None, alias="customerCell")
    company_cell: Optional[str] = Field(None, alias="companyCell")
    pz_code: Optional[str] = Field(None, alias="pzCode")
    referral_code: Optional[str] = Field(None, alias="referralCode")
    company_logo: Optional[str] = Field(None, alias="companyLogo")
    letter_head_logo: Optional[str] = Field(None, alias="letterHeadLogo")
    thumbnail_logo: Optional[str] = Field(None, alias="thumbnailLogo")
    maps_marker_image: Optional[str] = Field(None, alias="mapsMarkerImage")
    color_theme: Optional[str] = Field(None, alias="colorTheme")
    franchisee_maturity_type: Optional[str] = Field(None, alias="franchiseeMaturityType")
    pricing_to_use: Optional[str] = Field(None, alias="pricingToUse")
    total_rows: Optional[int] = Field(None, alias="totalRows")
    company_insurance_pricing: Optional["CompanyInsurancePricing"] = Field(None, alias="companyInsurancePricing")
    company_service_pricing: Optional["CompanyServicePricing"] = Field(None, alias="companyServicePricing")
    company_tax_pricing: Optional["CompanyTaxPricing"] = Field(None, alias="companyTaxPricing")
    whole_sale_markup: Optional[float] = Field(None, alias="wholeSaleMarkup")
    base_markup: Optional[float] = Field(None, alias="baseMarkup")
    medium_markup: Optional[float] = Field(None, alias="mediumMarkup")
    high_markup: Optional[float] = Field(None, alias="highMarkup")
    miles: Optional[float] = Field(None)
    insurance_type: Optional[str] = Field(None, alias="insuranceType")
    is_global: Optional[bool] = Field(None, alias="isGlobal")
    is_qb_user: Optional[bool] = Field(None, alias="isQbUser")
    skip_intacct: Optional[bool] = Field(None, alias="skipIntacct")
    is_access: Optional[str] = Field(None, alias="isAccess")
    is_readonly: Optional[bool] = Field(None, alias="isReadonly")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayID")  # API uses uppercase ID
    depth: Optional[int] = Field(None)
    franchisee_name: Optional[str] = Field(None, alias="franchiseeName")
    is_prefered: Optional[bool] = Field(None, alias="isPrefered")
    created_user: Optional[str] = Field(None, alias="createdUser")
    mapping_locations: Optional[str] = Field(None, alias="mappingLocations")
    location_count: Optional[str] = Field(None, alias="locationCount")
    base_parent: Optional[str] = Field(None, alias="baseParent")
    copy_material_from: Optional[str] = Field(None, alias="copyMaterialFrom")
    is_hide: Optional[bool] = Field(None, alias="isHide")
    is_dont_use: Optional[bool] = Field(None, alias="isDontUse")
    main_address: Optional[AddressDetails] = Field(None, alias="mainAddress")
    account_manager_franchisee_id: Optional[str] = Field(None, alias="accountManagerFranchiseeId")
    account_manager_franchisee_name: Optional[str] = Field(None, alias="accountManagerFranchiseeName")
    carrier_accounts_source_company_id: Optional[str] = Field(None, alias="carrierAccountsSourceCompanyId")
    carrier_accounts_source_company_name: Optional[str] = Field(None, alias="carrierAccountsSourceCompanyName")
    auto_price_api_enable_emails: Optional[bool] = Field(None, alias="autoPriceAPIEnableEmails")  # API uses uppercase API
    auto_price_api_enable_sms: Optional[bool] = Field(None, alias="autoPriceAPIEnableSMSs")  # API uses uppercase API/SMSs
    commercial_capabilities: Optional[CommercialCapabilities] = Field(None, alias="commercialCapabilities")
    primary_contact_id: Optional[int] = Field(None, alias="primaryContactId")
    payer_contact_id: Optional[int] = Field(None, alias="payerContactId")
    payer_contact_name: Optional[str] = Field(None, alias="payerContactName")
    total_jobs: Optional[int] = Field(None, alias="totalJobs")
    total_jobs_revenue: Optional[float] = Field(None, alias="totalJobsRevenue")
    total_sales: Optional[int] = Field(None, alias="totalSales")
    total_sales_revenue: Optional[float] = Field(None, alias="totalSalesRevenue")
    address_data: Optional[AddressData] = Field(None, alias="addressData")
    overridable_address_data: Optional[OverridableAddressData] = Field(None, alias="overridableAddressData")
    company_info: Optional["CompanyInfo"] = Field(None, alias="companyInfo")


class CompanyAddressInfo(CompanyRelatedModel):
    """CompanyAddressInfo model"""

    company_code: Optional[str] = Field(None, alias="companyCode")
    address: Optional[PlannerAddress] = Field(None)


class CompanyDetails(IdentifiedModel):
    """CompanyDetails model"""

    details: Optional["CompanyDetailsBaseInfo"] = Field(None)
    preferences: Optional["CompanyDetailsPreferences"] = Field(None)
    capabilities: Optional[CommercialCapabilities] = Field(None)
    address: Optional[AddressDetails] = Field(None)
    account_information: Optional[FranchiseeCarrierAccounts] = Field(None, alias="accountInformation")
    pricing: Optional["CompanyDetailsServicePricings"] = Field(None)
    insurance: Optional["CompanyDetailsInsurancePricing"] = Field(None)
    final_mile_tariff: Optional[List["CompanyDetailsFinalMileTariffItem"]] = Field(None, alias="finalMileTariff")
    taxes: Optional["CompanyDetailsTaxPricing"] = Field(None)
    read_only_access: Optional[bool] = Field(None, alias="readOnlyAccess")


class CompanyDetailsBaseInfo(ActiveModel):
    """CompanyDetailsBaseInfo model"""

    display_id: Optional[str] = Field(None, alias="displayId")
    name: Optional[str] = Field(None)
    tax_id: Optional[str] = Field(None, alias="taxId")
    code: Optional[str] = Field(None)
    parent_id: Optional[str] = Field(None, alias="parentId")
    franchisee_id: Optional[str] = Field(None, alias="franchiseeId")
    company_type_id: Optional[str] = Field(None, alias="companyTypeId")
    industry_type_id: Optional[str] = Field(None, alias="industryTypeId")
    cell_phone: Optional[str] = Field(None, alias="cellPhone")
    phone: Optional[str] = Field(None)
    fax: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    website: Optional[str] = Field(None)
    is_hidden: Optional[bool] = Field(None, alias="isHidden")
    is_global: Optional[bool] = Field(None, alias="isGlobal")
    is_not_used: Optional[bool] = Field(None, alias="isNotUsed")
    is_preferred: Optional[bool] = Field(None, alias="isPreferred")
    payer_contact_id: Optional[int] = Field(None, alias="payerContactId")
    payer_contact_name: Optional[str] = Field(None, alias="payerContactName")


class CompanyDetailsFinalMileTariffItem(ABConnectBaseModel):
    """CompanyDetailsFinalMileTariffItem model"""

    group_id: Optional[str] = Field(None, alias="groupId")
    from_amount: Optional[float] = Field(None, alias="from")
    to_amount: Optional[float] = Field(None, alias="to")
    to_curb: Optional[float] = Field(None, alias="toCurb")
    into_garage: Optional[float] = Field(None, alias="intoGarage")
    room_of_choice: Optional[float] = Field(None, alias="roomOfChoice")
    white_glove: Optional[float] = Field(None, alias="whiteGlove")
    delete_group: Optional[bool] = Field(None, alias="deleteGroup")


class CompanyDetailsInsurancePricing(ABConnectBaseModel):
    """CompanyDetailsInsurancePricing model"""

    isp: Optional[InsuranceOption] = Field(None)
    nsp: Optional[InsuranceOption] = Field(None)
    ltl: Optional[InsuranceOption] = Field(None)


class CompanyDetailsPreferences(ABConnectBaseModel):
    """CompanyDetailsPreferences model"""

    company_header_logo: Optional["CompanyImageData"] = Field(None, alias="companyHeaderLogo")
    thumbnail_logo: Optional["CompanyImageData"] = Field(None, alias="thumbnailLogo")
    letter_head_logo: Optional["CompanyImageData"] = Field(None, alias="letterHeadLogo")
    maps_marker: Optional["CompanyImageData"] = Field(None, alias="mapsMarker")
    is_qb_user: Optional[bool] = Field(None, alias="isQbUser")
    skip_intacct: Optional[bool] = Field(None, alias="skipIntacct")
    pricing_to_use: Optional[str] = Field(None, alias="pricingToUse")
    pz_code: Optional[str] = Field(None, alias="pzCode")
    insurance_type_id: Optional[str] = Field(None, alias="insuranceTypeId")
    franchisee_maturity_type_id: Optional[str] = Field(None, alias="franchiseeMaturityTypeId")
    is_company_used_as_carrier_source: Optional[bool] = Field(None, alias="isCompanyUsedAsCarrierSource")
    carrier_accounts_source_company_id: Optional[str] = Field(None, alias="carrierAccountsSourceCompanyId")
    carrier_accounts_source_company_name: Optional[str] = Field(None, alias="carrierAccountsSourceCompanyName")
    account_manager_franchisee_id: Optional[str] = Field(None, alias="accountManagerFranchiseeId")
    account_manager_franchisee_name: Optional[str] = Field(None, alias="accountManagerFranchiseeName")
    auto_price_api_enable_emails: Optional[bool] = Field(None, alias="autoPriceAPIEnableEmails")  # API uses uppercase API
    auto_price_api_enable_sms: Optional[bool] = Field(None, alias="autoPriceAPIEnableSMSs")  # API uses uppercase API/SMSs
    copy_materials: Optional[CopyMaterialsFrom] = Field(None, alias="copyMaterials")


class CompanyDetailsServicePricings(ABConnectBaseModel):
    """CompanyDetailsServicePricings model"""

    transportation_charge: Optional[TransportationCharges] = Field(None, alias="transportationCharge")
    transportation_markups: Optional[ServicePricingsMarkup] = Field(None, alias="transportationMarkups")
    carrier_freight_markups: Optional[ServicePricingsMarkup] = Field(None, alias="carrierFreightMarkups")
    carrier_other_markups: Optional[ServicePricingsMarkup] = Field(None, alias="carrierOtherMarkups")
    material_markups: Optional[ServicePricingsMarkup] = Field(None, alias="materialMarkups")
    labor_charge: Optional[LaborCharges] = Field(None, alias="laborCharge")
    accesorial_charge: Optional[AccesorialCharges] = Field(None, alias="accesorialCharge")
    royalties: Optional[RoyaltiesCharges] = Field(None)
    payment_settings: Optional[OnlinePaymentSettings] = Field(None, alias="paymentSettings")


class CompanyDetailsTaxPricing(ABConnectBaseModel):
    """CompanyDetailsTaxPricing model"""

    delivery_service: Optional[TaxOption] = Field(None, alias="deliveryService")
    insurance: Optional[TaxOption] = Field(None)
    pickup_service: Optional[TaxOption] = Field(None, alias="pickupService")
    services: Optional[TaxOption] = Field(None)
    transportation_service: Optional[TaxOption] = Field(None, alias="transportationService")
    packaging_material: Optional[TaxOption] = Field(None, alias="packagingMaterial")
    packaging_labor: Optional[TaxOption] = Field(None, alias="packagingLabor")


class CompanyImageData(ABConnectBaseModel):
    """CompanyImageData model"""

    file_path: Optional[str] = Field(None, alias="filePath")
    new_file: Optional[Base64File] = Field(None, alias="newFile")


class CompanyInfo(ActiveModel):
    """CompanyInfo model"""

    company_id: Optional[str] = Field(None, alias="companyId")
    company_type_id: Optional[str] = Field(None, alias="companyTypeId")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    company_name: Optional[str] = Field(None, alias="companyName")
    company_code: Optional[str] = Field(None, alias="companyCode")
    company_email: Optional[str] = Field(None, alias="companyEmail")
    company_phone: Optional[str] = Field(None, alias="companyPhone")
    thumbnail_logo: Optional[str] = Field(None, alias="thumbnailLogo")
    company_logo: Optional[str] = Field(None, alias="companyLogo")
    maps_marker_image: Optional[str] = Field(None, alias="mapsMarkerImage")
    main_address: Optional[AddressDetails] = Field(None, alias="mainAddress")
    is_third_party: Optional[bool] = Field(None, alias="isThirdParty")
    is_hidden: Optional[bool] = Field(None, alias="isHidden")


class CompanyInsurancePricing(ActiveModel):
    """CompanyInsurancePricing model"""

    insurance_slab_id: Optional[str] = Field(None, alias="insuranceSlabId")
    deductible_amount: Optional[float] = Field(None, alias="deductibleAmount")
    rate: Optional[float] = Field(None)
    company_id: Optional[str] = Field(None, alias="companyId")
    transp_type_id: Optional[str] = Field(None, alias="transpTypeId")
    company_name: Optional[str] = Field(None, alias="companyName")
    createdby: Optional[str] = Field(None)
    modifiedby: Optional[str] = Field(None)
    revision: Optional[int] = Field(None)
    insurance_type: Optional[str] = Field(None, alias="insuranceType")
    whole_sale_markup: Optional[float] = Field(None, alias="wholeSaleMarkup")
    base_markup: Optional[float] = Field(None, alias="baseMarkup")
    medium_markup: Optional[float] = Field(None, alias="mediumMarkup")
    high_markup: Optional[float] = Field(None, alias="highMarkup")


class CompanyServicePricing(TimestampedModel):
    """CompanyServicePricing model"""

    service_pricing_id: Optional[str] = Field(None, alias="servicePricingId")
    user_id: Optional[str] = Field(None, alias="userId")
    company_id: Optional[str] = Field(None, alias="companyId")
    service_category_id: Optional[str] = Field(None, alias="serviceCategoryId")
    category_value: Optional[float] = Field(None, alias="categoryValue")
    whole_sale_markup: Optional[float] = Field(None, alias="wholeSaleMarkup")
    base_markup: Optional[float] = Field(None, alias="baseMarkup")
    medium_markup: Optional[float] = Field(None, alias="mediumMarkup")
    high_markup: Optional[float] = Field(None, alias="highMarkup")
    is_active: Optional[bool] = Field(None, alias="isActive")
    is_taxable: Optional[bool] = Field(None, alias="isTaxable")
    tax_percent: Optional[float] = Field(None, alias="taxPercent")
    company_code: Optional[str] = Field(None, alias="companyCode")
    service_category_name: Optional[str] = Field(None, alias="serviceCategoryName")
    company_name: Optional[str] = Field(None, alias="companyName")
    company_type_id: Optional[str] = Field(None, alias="companyTypeId")
    parent_category_id: Optional[str] = Field(None, alias="parentCategoryId")
    zip_code: Optional[str] = Field(None, alias="zipCode")


class CompanyTaxPricing(CompanyRelatedModel):
    """CompanyTaxPricing model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    service_category_id: Optional[str] = Field(None, alias="serviceCategoryId")
    tax_slab_id: Optional[str] = Field(None, alias="taxSlabId")
    is_taxable: Optional[bool] = Field(None, alias="isTaxable")
    tax_percent: Optional[float] = Field(None, alias="taxPercent")
    service_categoty_name: Optional[str] = Field(None, alias="serviceCategotyName")


class ContactDetailsCompanyInfo(ActiveModel):
    """ContactDetailsCompanyInfo model"""

    company_id: Optional[str] = Field(None, alias="companyId")
    company_type_id: Optional[str] = Field(None, alias="companyTypeId")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    company_name: Optional[str] = Field(None, alias="companyName")
    company_code: Optional[str] = Field(None, alias="companyCode")
    company_email: Optional[str] = Field(None, alias="companyEmail")
    company_phone: Optional[str] = Field(None, alias="companyPhone")
    thumbnail_logo: Optional[str] = Field(None, alias="thumbnailLogo")
    company_logo: Optional[str] = Field(None, alias="companyLogo")
    maps_marker_image: Optional[str] = Field(None, alias="mapsMarkerImage")
    main_address: Optional[AddressDetails] = Field(None, alias="mainAddress")
    is_third_party: Optional[bool] = Field(None, alias="isThirdParty")
    is_hidden: Optional[bool] = Field(None, alias="isHidden")
    is_global: Optional[bool] = Field(None, alias="isGlobal")
    industry_type_id: Optional[str] = Field(None, alias="industryTypeId")
    payer_id: Optional[str] = Field(None, alias="payerId")
    payer_name: Optional[str] = Field(None, alias="payerName", max_length=100)
    tax_id: Optional[str] = Field(None, alias="taxId", max_length=100)


class PackagingLaborSettings(ABConnectBaseModel):
    """PackagingLaborSettings model"""

    inherit_tariffs_from: Optional[InheritSettingFrom] = Field(None, alias="inheritTariffsFrom")
    own_tariffs: Optional[List[PackagingLaborHours]] = Field(None, alias="ownTariffs")


class PackagingTariffSettings(ABConnectBaseModel):
    """PackagingTariffSettings model"""

    inherit_tariffs_from: Optional[InheritSettingFrom] = Field(None, alias="inheritTariffsFrom")
    own_tariffs: Optional[List[SimplePriceTariff]] = Field(None, alias="ownTariffs")


class SaveGeoSettingModel(IdentifiedModel):
    """SaveGeoSettingModel model"""

    name: Optional[str] = Field(None)
    geometry_type: Optional[GeometryType] = Field(None, alias="geometryType")
    coordinates: Optional[List[LatLng]] = Field(None)
    center: Optional[LatLng] = Field(None)
    radius: Optional[float] = Field(None)
    is_exclusive: Optional[bool] = Field(None, alias="isExclusive")
    is_active: Optional[bool] = Field(None, alias="isActive")
    use_only_for_condition_json: Optional[str] = Field(None, alias="useOnlyForConditionJson")
    use_only_for_filter_expression_json: Optional[str] = Field(None, alias="useOnlyForFilterExpressionJson")
    pickup_rules: Optional[List[SimplePriceTariff]] = Field(None, alias="pickupRules")
    pickup_labor_hours_rules: Optional[List[PickupLaborHoursRule]] = Field(None, alias="pickupLaborHoursRules")
    delivery_rules: Optional[List[SimplePriceTariff]] = Field(None, alias="deliveryRules")


class SearchCompanyDataSourceLoadOptions(ABConnectBaseModel):
    """SearchCompanyDataSourceLoadOptions model"""

    require_total_count: Optional[bool] = Field(None, alias="requireTotalCount")
    require_group_count: Optional[bool] = Field(None, alias="requireGroupCount")
    is_count_query: Optional[bool] = Field(None, alias="isCountQuery")
    is_summary_query: Optional[bool] = Field(None, alias="isSummaryQuery")
    skip: Optional[int] = Field(None)
    take: Optional[int] = Field(None)
    sort: Optional[List[SortingInfo]] = Field(None)
    group: Optional[List[GroupingInfo]] = Field(None)
    filter: Optional[List[Dict[str, Any]]] = Field(None)
    total_summary: Optional[List[SummaryInfo]] = Field(None, alias="totalSummary")
    group_summary: Optional[List[SummaryInfo]] = Field(None, alias="groupSummary")
    select: Optional[List[str]] = Field(None)
    pre_select: Optional[List[str]] = Field(None, alias="preSelect")
    remote_select: Optional[bool] = Field(None, alias="remoteSelect")
    remote_grouping: Optional[bool] = Field(None, alias="remoteGrouping")
    expand_linq_sum_type: Optional[bool] = Field(None, alias="expandLinqSumType")
    primary_key: Optional[List[str]] = Field(None, alias="primaryKey")
    default_sort: Optional[str] = Field(None, alias="defaultSort")
    string_to_lower: Optional[bool] = Field(None, alias="stringToLower")
    paginate_via_primary_key: Optional[bool] = Field(None, alias="paginateViaPrimaryKey")
    sort_by_primary_key: Optional[bool] = Field(None, alias="sortByPrimaryKey")
    allow_async_over_sync: Optional[bool] = Field(None, alias="allowAsyncOverSync")
    search_model: Optional["SearchCompanyModel"] = Field(None, alias="searchModel")


class SearchCompanyModel(CompanyRelatedModel):
    """SearchCompanyModel model"""

    company_code: Optional[str] = Field(None, alias="companyCode")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    company_type_id: Optional[str] = Field(None, alias="companyTypeId")
    phone: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")


class SearchCompanyResponse(CompanyRelatedModel):
    """SearchCompanyResponse model"""

    company_code: Optional[str] = Field(None, alias="companyCode")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    parent_company_id: Optional[str] = Field(None, alias="parentCompanyId")
    parent_company_name: Optional[str] = Field(None, alias="parentCompanyName")
    company_type_id: Optional[str] = Field(None, alias="companyTypeId")
    company_type: Optional[str] = Field(None, alias="companyType")
    phone: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    address1: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip: Optional[str] = Field(None)


class TagBoxDataSourceLoadOptions(ABConnectBaseModel):
    """TagBoxDataSourceLoadOptions model"""

    require_total_count: Optional[bool] = Field(None, alias="requireTotalCount")
    require_group_count: Optional[bool] = Field(None, alias="requireGroupCount")
    is_count_query: Optional[bool] = Field(None, alias="isCountQuery")
    is_summary_query: Optional[bool] = Field(None, alias="isSummaryQuery")
    skip: Optional[int] = Field(None)
    take: Optional[int] = Field(None)
    sort: Optional[List[SortingInfo]] = Field(None)
    group: Optional[List[GroupingInfo]] = Field(None)
    filter: Optional[List[Dict[str, Any]]] = Field(None)
    total_summary: Optional[List[SummaryInfo]] = Field(None, alias="totalSummary")
    group_summary: Optional[List[SummaryInfo]] = Field(None, alias="groupSummary")
    select: Optional[List[str]] = Field(None)
    pre_select: Optional[List[str]] = Field(None, alias="preSelect")
    remote_select: Optional[bool] = Field(None, alias="remoteSelect")
    remote_grouping: Optional[bool] = Field(None, alias="remoteGrouping")
    expand_linq_sum_type: Optional[bool] = Field(None, alias="expandLinqSumType")
    primary_key: Optional[List[str]] = Field(None, alias="primaryKey")
    default_sort: Optional[str] = Field(None, alias="defaultSort")
    string_to_lower: Optional[bool] = Field(None, alias="stringToLower")
    paginate_via_primary_key: Optional[bool] = Field(None, alias="paginateViaPrimaryKey")
    sort_by_primary_key: Optional[bool] = Field(None, alias="sortByPrimaryKey")
    allow_async_over_sync: Optional[bool] = Field(None, alias="allowAsyncOverSync")
    search_value: Optional[str] = Field(None, alias="searchValue")


class UpdateCarrierAccountsModel(ABConnectBaseModel):
    """UpdateCarrierAccountsModel model"""

    use_source_company: Optional[bool] = Field(None, alias="useSourceCompany")
    carrier_accounts_source_company_id: Optional[str] = Field(None, alias="carrierAccountsSourceCompanyId")
    carrier_accounts: Optional[FranchiseeCarrierAccounts] = Field(None, alias="carrierAccounts")


class WebApiDataSourceLoadOptions(ABConnectBaseModel):
    """WebApiDataSourceLoadOptions model"""

    require_total_count: Optional[bool] = Field(None, alias="requireTotalCount")
    require_group_count: Optional[bool] = Field(None, alias="requireGroupCount")
    is_count_query: Optional[bool] = Field(None, alias="isCountQuery")
    is_summary_query: Optional[bool] = Field(None, alias="isSummaryQuery")
    skip: Optional[int] = Field(None)
    take: Optional[int] = Field(None)
    sort: Optional[List[SortingInfo]] = Field(None)
    group: Optional[List[GroupingInfo]] = Field(None)
    filter: Optional[List[Dict[str, Any]]] = Field(None)
    total_summary: Optional[List[SummaryInfo]] = Field(None, alias="totalSummary")
    group_summary: Optional[List[SummaryInfo]] = Field(None, alias="groupSummary")
    select: Optional[List[str]] = Field(None)
    pre_select: Optional[List[str]] = Field(None, alias="preSelect")
    remote_select: Optional[bool] = Field(None, alias="remoteSelect")
    remote_grouping: Optional[bool] = Field(None, alias="remoteGrouping")
    expand_linq_sum_type: Optional[bool] = Field(None, alias="expandLinqSumType")
    primary_key: Optional[List[str]] = Field(None, alias="primaryKey")
    default_sort: Optional[str] = Field(None, alias="defaultSort")
    string_to_lower: Optional[bool] = Field(None, alias="stringToLower")
    paginate_via_primary_key: Optional[bool] = Field(None, alias="paginateViaPrimaryKey")
    sort_by_primary_key: Optional[bool] = Field(None, alias="sortByPrimaryKey")
    allow_async_over_sync: Optional[bool] = Field(None, alias="allowAsyncOverSync")


class CompanyMaterial(ABConnectBaseModel):
    """Company material model for packaging materials.

    .. versionadded:: 709
    """

    id: Optional[str] = Field(None, description="Material UUID")
    company_id: Optional[str] = Field(None, alias="companyId", description="Company UUID")
    is_active: bool = Field(True, alias="isActive", description="Whether material is active")
    name: Optional[str] = Field(None, description="Material name")
    description: Optional[str] = Field(None, description="Material description")
    code: Optional[str] = Field(None, description="Material code")
    type: Optional[str] = Field(None, description="Material type")
    unit: Optional[str] = Field(None, description="Unit of measurement")
    length: Optional[float] = Field(None, description="Length dimension")
    width: Optional[float] = Field(None, description="Width dimension")
    height: Optional[float] = Field(None, description="Height dimension")
    weight: Optional[float] = Field(None, description="Weight")
    cost: Optional[float] = Field(None, description="Cost")
    price: Optional[float] = Field(None, description="Price")
    waste_factor: Optional[float] = Field(None, alias="wasteFactor", description="Waste factor percentage")


class SaveCompanyMaterialModel(ABConnectBaseModel):
    """Model for saving company materials.

    .. versionadded:: 709
    """

    name: Optional[str] = Field(None, description="Material name")
    description: Optional[str] = Field(None, description="Material description")
    code: Optional[str] = Field(None, description="Material code")
    type: Optional[str] = Field(None, description="Material type")
    unit: Optional[str] = Field(None, description="Unit of measurement")
    is_active: bool = Field(True, alias="isActive", description="Whether material is active")
    length: Optional[float] = Field(None, description="Length dimension")
    width: Optional[float] = Field(None, description="Width dimension")
    height: Optional[float] = Field(None, description="Height dimension")
    weight: Optional[float] = Field(None, description="Weight")
    cost: Optional[float] = Field(None, description="Cost")
    price: Optional[float] = Field(None, description="Price")
    waste_factor: Optional[float] = Field(None, alias="wasteFactor", description="Waste factor percentage")


class CompanyGeoAreaCompanies(ABConnectBaseModel):
    """Company geo area item for GET /companies/geoAreaCompanies response."""

    code: Optional[str] = Field(None, description="Company code")
    brand: Optional[str] = Field(None, description="Company brand")
    location: Optional[LatLng] = Field(None, description="Geographic coordinates")
    marker_image: Optional[str] = Field(None, alias="markerImage", description="Map marker image path")


__all__ = ['Company', 'CompanyAddressInfo', 'CompanyBrandTreeNode', 'CompanyDetails', 'CompanyDetailsBaseInfo', 'CompanyDetailsFinalMileTariffItem', 'CompanyDetailsInsurancePricing', 'CompanyDetailsPreferences', 'CompanyDetailsServicePricings', 'CompanyDetailsTaxPricing', 'CompanyGeoAreaCompanies', 'CompanyImageData', 'CompanyInfo', 'CompanyInsurancePricing', 'CompanyMaterial', 'CompanyServicePricing', 'CompanySimple', 'CompanyTaxPricing', 'ContactDetailsCompanyInfo', 'PackagingLaborSettings', 'PackagingTariffSettings', 'SaveCompanyMaterialModel', 'SaveGeoSettingModel', 'SearchCompanyDataSourceLoadOptions', 'SearchCompanyModel', 'SearchCompanyResponse', 'TagBoxDataSourceLoadOptions', 'UpdateCarrierAccountsModel', 'WebApiDataSourceLoadOptions']
