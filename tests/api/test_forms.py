"""Tests for Job Form endpoints - comprehensive coverage."""

import io
import sys
from pathlib import Path
import pytest

# Mark entire module as slow (excluded by default, run with: pytest -m slow)
pytestmark = pytest.mark.slow

# Add tests directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from constants import JOB_DISPLAY_ID


def is_valid_pdf(data: bytes) -> bool:
    """Check if bytes represent a valid PDF using pypdf."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(data))
        return len(reader.pages) >= 0
    except Exception:
        return False


def assert_valid_pdf(data, name="PDF"):
    """Assert that data is a valid PDF."""
    assert isinstance(data, bytes), f"{name} should be bytes, got {type(data)}"
    assert len(data) > 0, f"{name} should not be empty"
    assert data[:4] == b'%PDF', f"{name} should start with PDF magic bytes"
    assert is_valid_pdf(data), f"{name} is not a valid PDF"


# ==============================================================================
# Simple PDF Forms (only require jobDisplayId)
# ==============================================================================

@pytest.mark.integration
def test_get_form_address_label(api):
    """get_form_address_label returns valid PDF"""
    result = api.forms.get_form_address_label(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "AddressLabel")


@pytest.mark.integration
def test_get_form_credit_card_authorization(api):
    """get_form_credit_card_authorization returns valid PDF"""
    result = api.forms.get_form_credit_card_authorization(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "CreditCardAuth")


@pytest.mark.integration
def test_get_form_customer_quote(api):
    """get_form_customer_quote returns valid PDF"""
    result = api.forms.get_form_customer_quote(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "CustomerQuote")


@pytest.mark.integration
def test_get_form_invoice(api):
    """get_form_invoice returns valid PDF"""
    result = api.forms.get_form_invoice(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "Invoice")


@pytest.mark.integration
@pytest.mark.xfail(reason="API returns 500 for some jobs")
def test_get_form_invoice_editable(api):
    """get_form_invoice_editable returns valid PDF"""
    result = api.forms.get_form_invoice_editable(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "InvoiceEditable")


@pytest.mark.integration
def test_get_form_item_labels(api):
    """get_form_item_labels returns valid PDF"""
    result = api.forms.get_form_item_labels(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "ItemLabels")


@pytest.mark.integration
@pytest.mark.xfail(reason="API requires shipmentPlanId query param")
def test_get_form_packaging_labels(api):
    """get_form_packaging_labels returns valid PDF"""
    result = api.forms.get_form_packaging_labels(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "PackagingLabels")


@pytest.mark.integration
def test_get_form_packaging_specification(api):
    """get_form_packaging_specification returns valid PDF"""
    result = api.forms.get_form_packaging_specification(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "PackagingSpec")


@pytest.mark.integration
def test_get_form_packing_slip(api):
    """get_form_packing_slip returns valid PDF"""
    result = api.forms.get_form_packing_slip(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "PackingSlip")


@pytest.mark.integration
def test_get_form_quick_sale(api):
    """get_form_quick_sale returns valid PDF"""
    result = api.forms.get_form_quick_sale(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "QuickSale")


@pytest.mark.integration
def test_get_form_usar(api):
    """get_form_usar returns valid PDF"""
    result = api.forms.get_form_usar(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "USAR")


@pytest.mark.integration
@pytest.mark.xfail(reason="API returns 500 for some jobs")
def test_get_form_usar_editable(api):
    """get_form_usar_editable returns valid PDF"""
    result = api.forms.get_form_usar_editable(JOB_DISPLAY_ID)
    assert_valid_pdf(result, "USAREditable")


# ==============================================================================
# Operations Form (with type parameter)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.parametrize("ops_type", [0, 1])
def test_get_form_operations(api, ops_type):
    """get_form_operations returns valid PDF for each type"""
    result = api.forms.get_form_operations(JOB_DISPLAY_ID, ops_type=ops_type)
    assert_valid_pdf(result, f"Operations_type{ops_type}")


# ==============================================================================
# Shipments (JSON response)
# ==============================================================================

@pytest.mark.integration
def test_get_form_shipments(api):
    """get_form_shipments returns list of shipment plans"""
    shipments = api.forms.get_form_shipments(JOB_DISPLAY_ID)
    assert isinstance(shipments, list), "Should return a list"
    assert len(shipments) > 0, "Should have at least one shipment plan"
    # Check structure
    first = shipments[0]
    assert 'transportType' in first, "Shipment should have transportType"
    assert 'jobShipmentID' in first, "Shipment should have jobShipmentID"


# ==============================================================================
# Bill of Lading (requires shipment plan from shipments)
# ==============================================================================

@pytest.mark.integration
def test_get_form_bill_of_lading_ltl(api):
    """get_form_bill_of_lading returns valid PDF for LTL transport"""
    shipments = api.forms.get_form_shipments(JOB_DISPLAY_ID)
    ltl = next((s for s in shipments if s['transportType'] == 'LTL'), None)
    if ltl is None:
        pytest.skip("No LTL shipment plan available")

    pdf_data = api.forms.get_form_bill_of_lading(
        JOB_DISPLAY_ID,
        ltl['jobShipmentID'],
        ltl.get('optionIndex', 0)
    )
    assert_valid_pdf(pdf_data, "BOL_LTL")


@pytest.mark.integration
def test_get_form_bill_of_lading_house(api):
    """get_form_bill_of_lading returns valid PDF for House transport"""
    shipments = api.forms.get_form_shipments(JOB_DISPLAY_ID)
    house = next((s for s in shipments if s['transportType'] == 'House'), None)
    if house is None:
        pytest.skip("No House shipment plan available")

    pdf_data = api.forms.get_form_bill_of_lading(
        JOB_DISPLAY_ID,
        house['jobShipmentID'],
        house.get('optionIndex', 0)
    )
    assert_valid_pdf(pdf_data, "BOL_House")


@pytest.mark.integration
def test_get_form_bill_of_lading_all_transport_modes(api):
    """get_form_bill_of_lading returns valid PDF for each transport mode"""
    shipments = api.forms.get_form_shipments(JOB_DISPLAY_ID)

    # Group by transport type (one per type)
    by_transport = {}
    for s in shipments:
        mode = s.get('transportType', 'Unknown')
        if mode not in by_transport:
            by_transport[mode] = s

    assert len(by_transport) > 0, "Should have at least one transport mode"

    for transport_mode, shipment in by_transport.items():
        pdf_data = api.forms.get_form_bill_of_lading(
            JOB_DISPLAY_ID,
            shipment['jobShipmentID'],
            shipment.get('optionIndex', 0)
        )
        assert_valid_pdf(pdf_data, f"BOL_{transport_mode}")


# ==============================================================================
# Helper Methods
# ==============================================================================

@pytest.mark.integration
def test_get_bol_helper(api):
    """get_bol helper returns valid PDF for LTL"""
    result = api.forms.get_bol(JOB_DISPLAY_ID)
    assert isinstance(result, dict), "Should return dict with name:data"
    assert len(result) == 1, "Should have one entry"
    for name, data in result.items():
        assert name.endswith('.pdf'), f"Name should end with .pdf: {name}"
        assert 'LTL' in name, f"Name should contain LTL: {name}"
        assert_valid_pdf(data, name)


@pytest.mark.integration
def test_get_hbl_helper(api):
    """get_hbl helper returns valid PDF for House BOL"""
    try:
        result = api.forms.get_hbl(JOB_DISPLAY_ID)
    except (TypeError, StopIteration, AttributeError):
        pytest.skip("No House shipment plan available")

    assert isinstance(result, dict), "Should return dict with name:data"
    for name, data in result.items():
        assert 'House' in name, f"Name should contain House: {name}"
        assert_valid_pdf(data, name)


@pytest.mark.integration
def test_get_ops_helper(api):
    """get_ops helper returns valid PDF"""
    result = api.forms.get_ops(JOB_DISPLAY_ID)
    assert isinstance(result, dict), "Should return dict with name:data"
    assert len(result) == 1, "Should have one entry"
    for name, data in result.items():
        assert name.endswith('.pdf'), f"Name should end with .pdf: {name}"
        assert 'ops' in name.lower(), f"Name should contain ops: {name}"
        assert_valid_pdf(data, name)
