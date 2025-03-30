import io
import json
from importlib import resources
from enum import Enum
from typing import Any, Dict, List, Optional, Union


def load_json_resource(filename: str) -> Any:
    """
    Loads a JSON file from the package's 'base' directory using importlib.resources.

    Args:
        filename (str): The JSON file name.

    Returns:
        The parsed JSON object.
    """
    with resources.open_text("ABConnect.base", filename) as f:
        return json.load(f)


def to_file_dict(response, job: int, form_name: str, filetype: str = "pdf") -> dict:
    file_name = f"{job}_{form_name}.{filetype}"
    bytes = io.BytesIO(response.content)
    return {file_name: bytes.getvalue()}


class BolType(Enum):
    """LTL is special case - if last mile exists, LTL the carrier bol -- else, delivery is"""

    HOUSE = 0
    PICKUP = 2
    LTL = 5
    DELIVERY = 6
    CARRIER = 56


class FormId(Enum):
    QuickSaleReceipt = 0
    CustomerQuotes = 1
    CreditCardAuthorization = 2
    USARv7 = 3
    USARv7_TextOnly = 4
    Invoice = 5
    BillOfLading = 6
    OperationsForm_New_v2 = 7
    AddressLabel = 8
    PackagingSpecifications = 9
    PackingLabels1 = 10
    PackingSlip = 11
    PackingLabels2 = 12


class FormType(str, Enum):
    """all support usar, first two support invoice"""

    NO_BREAKDOWN = "no-breakdown"
    BLANK = "blank"
    NO_PRICES = "no-prices"
    TEXTONLY = "textonly"


class TaskCodes(str, Enum):
    """used by abconnect calendar / timeline"""

    PICKUP = "PU"
    PACKAGING = "PK"
    STORAGE = "ST"
    CARRIER = "CP"
    DELIVERY = "DE"


class DocType(str, Enum):
    Label = 1
    USAR = 2
    Credit_Card_Auth = 3
    BOL = 4
    Electronic_Invoice = 5
    Item_Photo = 6
    Other = 7
    Manifest = 8
    Commercial_Invoice = 9
    Pro_Forma_Invoice = 10
    Packing_List = 11
    International_Forms = 12
    Air_Waybill = 13
    Terms_and_Conditions = 14
    Customer_Quote = 15
    Pickup_Receipt = 16
    UPS_Control_Log = 18

    @property
    def fmt(self):
        return self.name.replace("_", " ").title()
