import logging
from typing import Optional, Dict, Any
from ABConnect.api.endpoints.jobs.form import JobFormEndpoint

logger = logging.getLogger(__name__)

class JobFormHelper(JobFormEndpoint):
    def get_bol(self, job: str, transport_mode: Optional[str] = "LTL"):
        shipments = self.get_form_shipments(job)
        shipment = next((s for s in shipments if s['transportType'] == transport_mode), None)
        shipmentPlanId = shipment['jobShipmentID']
        optionIndex = shipment['optionIndex']
        name = f"{job}_{transport_mode}_BOL.pdf"
        data = self.get_form_bill_of_lading(job, shipmentPlanId, optionIndex)
        return {name: data}

        
    def get_hbl(self, job: str):
        return self.get_bol(job, "House")

    def get_ops(self, job: str):
        name = f"{job}_ops.pdf"
        data = self.get_form_operations(job)
        return {name: data}