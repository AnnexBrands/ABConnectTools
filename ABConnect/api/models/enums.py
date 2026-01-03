"""Enumeration types for ABConnect API models."""

from enum import Enum, IntFlag


class CarrierAPI(int, Enum):
    """CarrierAPI enumeration"""

    UNK = 0
    LMI = 1
    FEDEX = 2
    UPS = 3
    ROADRUNNER = 4
    REMOVED = 5
    DHL = 6
    MAERSK = 7
    TEAMWW = 8
    ESTES = 9
    FORWARDAIR = 10
    GLOBALTRANZ = 11
    FEDEXFREIGHT = 12
    USPS = 20


class CommercialCapabilities(IntFlag):
    """CommercialCapabilities flags enumeration - supports combinations like 7 (PARCEL|SOME_COMMERCIAL|FULL_COMMERCIAL)"""

    PARCEL = 1
    SOME_COMMERCIAL = 2
    FULL_COMMERCIAL = 4
    CAN_GET_API_LEADS = 8
    CARD_PAYMENTS = 16
    ACH_PAYMENTS = 32
    PREFER_STOCK_BOXES = 64
    DONT_SUPPORT_CUSTOM_BOXES = 128
    ELABEL_ONLY = 256


class CopyMaterialsFrom(int, Enum):
    """CopyMaterialsFrom enumeration"""

    NONE = 0
    PARENT = 1
    CORPORATE = 2


class DashboardType(int, Enum):
    """DashboardType enumeration"""

    INBOUND = 1
    RECENTESTIMATES = 11
    INHOUSE = 12
    OUTBOUND = 13
    LOCALDELIVERIES = 14

class DocumentSource(int, Enum):
    """DocumentSource enumeration"""

    JOB = 1
    SHIPMENT = 4
    COMPANY = 8


class DocumentType(int, Enum):
    """DocumentType enumeration for document uploads and management."""

    LABEL = 1
    USAR = 2
    CREDIT_CARD_AUTH = 3
    BOL = 4
    ELECTRONIC_INVOICE = 5
    ITEM_PHOTO = 6
    OTHER = 7
    MANIFEST = 8
    COMMERCIAL_INVOICE = 9
    PRO_FORMA_INVOICE = 10
    PACKING_LIST = 11
    INTERNATIONAL_FORMS = 12
    AIR_WAYBILL = 13
    TERMS_AND_CONDITIONS = 14
    CUSTOMER_QUOTE = 15
    PICKUP_RECEIPT = 16
    EMAIL_CONTENT = 17
    UPS_CONTROL_LOG = 18
    DELETED_LABEL = 19


class ForgotType(int, Enum):
    """ForgotType enumeration"""

    PASSWORD = 0
    USERNAME = 1


class GeometryType(int, Enum):
    """GeometryType enumeration"""

    UNKNOWN = 0
    POLYGON = 1
    CIRCLE = 2


class HistoryCodeABCState(int, Enum):
    """HistoryCodeABCState enumeration"""

    ITR = 1
    DLY = 2
    EXC = 3
    DEC = 4


class InheritSettingFrom(int, Enum):
    """InheritSettingFrom enumeration"""

    NONE = 0
    PARENT = 1
    CORPORATE = 2


class JobAccessLevel(int, Enum):
    """JobAccessLevel enumeration"""
    NONE = 0,
    OWNER = 1,
    CUSTOMER = 2,
    PICKUP_AGENT = 4,
    PACKAGING_AGENT = 8,
    DELIVERY_AGENT = 16,
    ALL_AGENTS = 28,
    AGENTS = 29


class JobContactType(int, Enum):
    """JobContactType enumeration"""

    CUSTOMER = 0
    PICKUPS = 1
    DELIVERY = 2


class JobType(int, Enum):
    """JobType enumeration"""

    NONE = 0
    PICKPACK = 1
    REGULAR = 2
    DELIVERY = 3
    _3PL = 4


class KnownFormId(int, Enum):
    """KnownFormId enumeration"""

    QUICKSALERECEIPT = 0
    CUSTOMERQUOTE = 1
    CREDITCARDAUTHORIZATION = 2
    UNIVERSALSHIPPINGAGREEMENT = 3
    INVOICE = 4
    BILLOFLADING = 5
    OPERATIONS = 6
    ADDRESSLABEL = 7
    PACKAGINGSPECIFICATIONS = 8
    PACKAGINGLABELS = 9
    PACKINGSLIP = 10
    ITEMLABELS = 11
    VALUE_12 = 12


class LabelImageType(int, Enum):
    """LabelImageType enumeration"""

    PDF = 0
    ZPL = 1
    IMAGE = 2


class LabelType(int, Enum):
    """LabelType enumeration"""

    LABEL2X4 = 0
    LABEL4X6 = 1
    LABEL4X6DOCTAB = 2
    LABEL8X11 = 3
    LABEL8X11MIRAMAR = 4
    LABEL8X11TTC = 5


class ListSortDirection(int, Enum):
    """ListSortDirection enumeration"""

    ASC = 0
    DESC = 1


class PaymentType(int, Enum):
    """PaymentType enumeration"""

    PREPAID = 0
    THIRDPARTY = 1
    COLLECT = 2


class PropertyType(int, Enum):
    """PropertyType enumeration"""

    RESIDENCE = 1
    LIMITED_ACCESS = 2
    COMMERCIAL = 3


class QuoteRequestStatus(int, Enum):
    """QuoteRequestStatus enumeration"""

    DRAFT = 0
    REQUESTED = 1
    RESPONSERECEIVED = 2
    BIDRECEIVED = 3
    DECLINED = 4
    SELECTED = 5
    CANCELLED = 6
    INSTAQUOTED = 7



class RangeDateEnum(int, Enum):
    """RangeDateEnum enumeration"""

    DAY = 0
    WEEK = 1
    MONTH = 2
    QUARTER = 3
    YEAR = 4


class RetransTimeZoneEnum(int, Enum):
    """RetransTimeZoneEnum enumeration"""

    ET = 0
    CT = 1
    MT = 2
    PT = 3


class SelectedOption(int, Enum):
    """SelectedOption enumeration"""

    NONE = 0
    OPTION100 = 1
    OPTION500 = 2
    OPTION750 = 3
    OPTION1500 = 4


class SendEmailStatus(int, Enum):
    """SendEmailStatus enumeration"""

    UNKNOWN = 0
    SENT = 1
    QUEUED = 2
    REJECTED = 4
    INVALID = 8
    SCHEDULED = 16
    BOUNCED = 32
    DEFFERED = 64
    SOFTBOUNCED = 128
    SPAM = 256
    UNSUB = 512


class ServiceType(int, Enum):
    """ServiceType enumeration"""

    UNDEFINED = 0
    PICK = 1
    PACK = 2
    PICKANDPACK = 3
    DELIVERY = 4


class SortByField(int, Enum):
    """SortByField enumeration"""

    JobDisplayID = 0
    JobMgmtId = 1
    CompletedDate = 2
    ContactFirstName = 3
    ContactFullName = 4
    EstimateDate = 5
    QuoteDate = 6
    PUAddress1 = 7
    DelAddress1 = 8
    ContactLastName = 9
    Name = 10
    CreateDate = 11
    NoteImportant = 12
    NoteCategory = 13
    NoteDate = 14
    NoteDueDate = 15
    NoteComment = 16
    NoteAuthor = 17
    NoteCompleted = 18
    NoteGlobal = 19
    NoteShared = 20
    CompanyName = 21
    City = 22
    IndustryType = 23
    ContactPhone = 24
    ContactEmail = 25
    JobNumber = 26
    Franchisee = 27
    InsuranceType = 28
    NoOfPiece = 29
    TotalValue = 30
    JobDate = 31
    INSURANCECOST = 32
    CARRIER = 33
    INACCTDATE = 34
    JobID = 35
    Company = 36
    BookedDate = 37
    Revenue = 38
    Profit = 39
    GrossMargin = 40
    Status = 41
    Industry = 42
    CustomerZipCode = 43
    ReferredBy = 44
    ReferredName = 45
    ReferedByCategory = 46
    Type = 47
    IntactStatus = 48
    LeadDate = 49
    ReferrerPage = 50
    EntryURL = 51
    SubmissionPage = 52
    HowHeard = 53
    Email = 54
    Phone = 55
    ShipFrom = 56
    ShipTo = 57
    CustomerComments = 58
    CurrentBookPrice = 59
    CurrentBookProfit = 60
    FranchiseeID = 61
    IntacctDate = 62
    Jobtype = 63
    CreatedByUserName = 64


class StatusEnum(int, Enum):
    """StatusEnum enumeration"""

    Estimate = 0
    Booked = 1
    Quoted = 2
    Completed = 3
    TemplateJob = 4
    Cancelled = 5
    NotViewed = 6


class FormType(int, Enum):
    """FormType enumeration for job forms"""

    NOBREAKDOWN = 0
    BREAKDOWN = 1
    BLANK = 2
    CUSTOMIZED = 3


class OperationsFormType(int, Enum):
    """OperationsFormType enumeration for operations forms"""

    DEFAULT = 0
    WITHNOTES = 1


__all__ = [
    "CarrierAPI",
    "CommercialCapabilities",
    "CopyMaterialsFrom",
    "DashboardType",
    "DocumentSource",
    "DocumentType",
    "ForgotType",
    "FormType",
    "GeometryType",
    "HistoryCodeABCState",
    "InheritSettingFrom",
    "JobAccessLevel",
    "JobContactType",
    "JobType",
    "KnownFormId",
    "LabelImageType",
    "LabelType",
    "ListSortDirection",
    "OperationsFormType",
    "PaymentType",
    "PropertyType",
    "QuoteRequestStatus",
    "RangeDateEnum",
    "RetransTimeZoneEnum",
    "SelectedOption",
    "SendEmailStatus",
    "ServiceType",
    "SortByField",
    "StatusEnum",
]
