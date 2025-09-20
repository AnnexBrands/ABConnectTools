"""Enumeration types for ABConnect API models."""

from enum import Enum

class CarrierAPI(int, Enum):
    """CarrierAPI enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_20 = 20


class CommercialCapabilities(int, Enum):
    """CommercialCapabilities enumeration"""
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_128 = 128


class CopyMaterialsFrom(int, Enum):
    """CopyMaterialsFrom enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class DashboardType(int, Enum):
    """DashboardType enumeration"""
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class DocumentSource(int, Enum):
    """DocumentSource enumeration"""
    VALUE_1 = 1
    VALUE_4 = 4
    VALUE_8 = 8


class ForgotType(int, Enum):
    """ForgotType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1


class GeometryType(int, Enum):
    """GeometryType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class HistoryCodeABCState(int, Enum):
    """HistoryCodeABCState enumeration"""
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class InheritSettingFrom(int, Enum):
    """InheritSettingFrom enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class JobAccessLevel(int, Enum):
    """JobAccessLevel enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_29 = 29


class JobContactType(int, Enum):
    """JobContactType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class JobType(int, Enum):
    """JobType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class KnownFormId(int, Enum):
    """KnownFormId enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12


class LabelImageType(int, Enum):
    """LabelImageType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class LabelType(int, Enum):
    """LabelType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class ListSortDirection(int, Enum):
    """ListSortDirection enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1


class PaymentType(int, Enum):
    """PaymentType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class PropertyType(int, Enum):
    """PropertyType enumeration"""
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class QuoteRequestStatus(int, Enum):
    """QuoteRequestStatus enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class RangeDateEnum(int, Enum):
    """RangeDateEnum enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class RetransTimeZoneEnum(int, Enum):
    """RetransTimeZoneEnum enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class SelectedOption(int, Enum):
    """SelectedOption enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class SendEmailStatus(int, Enum):
    """SendEmailStatus enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_128 = 128
    VALUE_256 = 256
    VALUE_512 = 512


class ServiceType(int, Enum):
    """ServiceType enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class SortByField(int, Enum):
    """SortByField enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_39 = 39
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_60 = 60
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_63 = 63
    VALUE_64 = 64


class StatusEnum(int, Enum):
    """StatusEnum enumeration"""
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


__all__ = ['CarrierAPI', 'CommercialCapabilities', 'CopyMaterialsFrom', 'DashboardType', 'DocumentSource', 'ForgotType', 'GeometryType', 'HistoryCodeABCState', 'InheritSettingFrom', 'JobAccessLevel', 'JobContactType', 'JobType', 'KnownFormId', 'LabelImageType', 'LabelType', 'ListSortDirection', 'PaymentType', 'PropertyType', 'QuoteRequestStatus', 'RangeDateEnum', 'RetransTimeZoneEnum', 'SelectedOption', 'SendEmailStatus', 'ServiceType', 'SortByField', 'StatusEnum']
