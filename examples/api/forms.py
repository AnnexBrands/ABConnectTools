"""
Job Forms API Examples - Comprehensive form endpoint coverage

Demonstrates all form endpoints:
- Simple PDF forms (just jobDisplayId)
- Operations form (with type parameter)
- Shipments (JSON response)
- Bill of Lading (requires shipment plan from shipments)
- Helper methods (get_bol, get_hbl, get_ops)
"""

from ABConnect.api import ABConnectAPI
from _helpers import save_pdf_fixture, validate_pdf
from _constants import JOB_DISPLAY_ID

api = ABConnectAPI(env='staging', username='instaquote')

print(f"=== Job Forms for {JOB_DISPLAY_ID} ===\n")

# ------------------------------------------------------------------------------
# 1. Simple PDF forms (only require jobDisplayId)
# ------------------------------------------------------------------------------
SIMPLE_FORMS = [
    ("get_form_address_label", "AddressLabel"),
    ("get_form_credit_card_authorization", "CreditCardAuth"),
    ("get_form_customer_quote", "CustomerQuote"),
    ("get_form_invoice", "Invoice"),
    ("get_form_invoice_editable", "InvoiceEditable"),
    ("get_form_item_labels", "ItemLabels"),
    ("get_form_packaging_labels", "PackagingLabels"),
    ("get_form_packaging_specification", "PackagingSpec"),
    ("get_form_packing_slip", "PackingSlip"),
    ("get_form_quick_sale", "QuickSale"),
    ("get_form_usar", "USAR"),
    ("get_form_usar_editable", "USAREditable"),
]

print("--- Simple PDF Forms ---")
for method_name, fixture_name in SIMPLE_FORMS:
    try:
        method = getattr(api.forms, method_name)
        result = method(JOB_DISPLAY_ID)
        if isinstance(result, bytes):
            validate_pdf(result, fixture_name)
            save_pdf_fixture(result, fixture_name)
            print(f"  {method_name}: Valid PDF ({len(result)} bytes)")
        else:
            print(f"  {method_name}: {type(result).__name__} response")
    except Exception as e:
        print(f"  {method_name}: {e}")

# ------------------------------------------------------------------------------
# 2. Operations form (with type parameter)
# ------------------------------------------------------------------------------
print("\n--- Operations Form (with type param) ---")
for ops_type in [0, 1]:
    try:
        result = api.forms.get_form_operations(JOB_DISPLAY_ID, ops_type=ops_type)
        if isinstance(result, bytes):
            validate_pdf(result, f"Operations_type{ops_type}")
            save_pdf_fixture(result, f"Operations_type{ops_type}")
            print(f"  operations type={ops_type}: Valid PDF ({len(result)} bytes)")
        else:
            print(f"  operations type={ops_type}: {type(result).__name__} response")
    except Exception as e:
        print(f"  operations type={ops_type}: {e}")

# ------------------------------------------------------------------------------
# 3. Shipments (JSON response with transport modes)
# ------------------------------------------------------------------------------
print("\n--- Shipments (JSON) ---")
try:
    shipments = api.forms.get_form_shipments(JOB_DISPLAY_ID)
    print(f"  Found {len(shipments)} shipment plans")

    # Group by transport type
    by_transport = {}
    for s in shipments:
        mode = s.get('transportType', 'Unknown')
        if mode not in by_transport:
            by_transport[mode] = s

    print(f"  Transport modes: {list(by_transport.keys())}")

    # ------------------------------------------------------------------------------
    # 4. Bill of Lading PDFs (one per transport mode)
    # ------------------------------------------------------------------------------
    print("\n--- Bill of Lading PDFs (per transport mode) ---")
    for transport_mode, shipment in by_transport.items():
        shipment_plan_id = shipment['jobShipmentID']
        option_index = shipment.get('optionIndex', 0)

        try:
            pdf_data = api.forms.get_form_bill_of_lading(
                JOB_DISPLAY_ID,
                shipment_plan_id,
                option_index
            )
            fixture_name = f"BOL_{transport_mode}"
            validate_pdf(pdf_data, fixture_name)
            save_pdf_fixture(pdf_data, fixture_name)
            print(f"  {transport_mode}: Valid PDF ({len(pdf_data)} bytes)")
            print(f"    shipmentPlanId: {shipment_plan_id}")
            print(f"    optionIndex: {option_index}")
        except Exception as e:
            print(f"  {transport_mode}: {e}")

except Exception as e:
    print(f"  Error: {e}")

# ------------------------------------------------------------------------------
# 5. Helper methods
# ------------------------------------------------------------------------------
print("\n--- Helper Methods ---")

# get_bol (LTL by default)
try:
    result = api.forms.get_bol(JOB_DISPLAY_ID)
    for name, data in result.items():
        validate_pdf(data, name)
        print(f"  get_bol: {name} ({len(data)} bytes)")
except Exception as e:
    print(f"  get_bol: {e}")

# get_hbl (House BOL)
try:
    result = api.forms.get_hbl(JOB_DISPLAY_ID)
    for name, data in result.items():
        validate_pdf(data, name)
        print(f"  get_hbl: {name} ({len(data)} bytes)")
except Exception as e:
    print(f"  get_hbl: {e}")

# get_ops
try:
    result = api.forms.get_ops(JOB_DISPLAY_ID)
    for name, data in result.items():
        validate_pdf(data, name)
        print(f"  get_ops: {name} ({len(data)} bytes)")
except Exception as e:
    print(f"  get_ops: {e}")

print("\n=== Done ===")
