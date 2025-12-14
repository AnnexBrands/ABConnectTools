"""Jobs API endpoints package.

This package contains all job-related endpoints organized by their swagger tags.
"""

from .job import JobEndpoint
from .agent_helpers import AgentEndpoint
from .email import JobEmailEndpoint
from .form_helpers import JobFormHelper
from .freightproviders import JobFreightProvidersEndpoint
from .intacct import JobIntacctEndpoint
from .items_helpers import ItemsHelper
from .note import JobNoteEndpoint
from .onhold import JobOnHoldEndpoint
from .parcelitems import JobParcelItemsEndpoint
from .payment import JobPaymentEndpoint
from .rfq import JobRfqEndpoint
from .ship_helpers import ShipHelper
from .shipment import JobShipmentEndpoint
from .sms import JobSmsEndpoint
from .status import JobStatusEndpoint
from .timeline import JobTimelineEndpoint
from .timeline_helpers import TimelineHelpers
from .tracking import JobTrackingEndpoint


class JobsPackage:
    """Container for all job-related endpoints."""

    def __init__(self, request_handler=None):
        """Initialize all job endpoints.

        Args:
            request_handler: Optional request handler (for backward compatibility)
        """
        # All endpoint classes use the shared request handler via BaseEndpoint
        self.agent = AgentEndpoint()  # Use enhanced job endpoint with helpers
        self.job = JobEndpoint()
        self.email = JobEmailEndpoint()
        self.form = JobFormHelper()
        self.freightproviders = JobFreightProvidersEndpoint()
        self.intacct = JobIntacctEndpoint()
        self.items = ItemsHelper()  # Items helper with Pydantic model casting
        self.note = JobNoteEndpoint()
        self.onhold = JobOnHoldEndpoint()
        self.parcelitems = JobParcelItemsEndpoint()
        self.payment = JobPaymentEndpoint()
        self.rfq = JobRfqEndpoint()
        self.ship = ShipHelper()
        self.shipment = JobShipmentEndpoint()
        self.sms = JobSmsEndpoint()
        self.status = JobStatusEndpoint()
        self.timeline = TimelineHelpers()
        self.tracking = JobTrackingEndpoint()


__all__ = [
    "JobsPackage",
    "JobEndpoint",
    "AgentEndpoint",
    "JobEmailEndpoint",
    "JobFormEndpoint",
    "JobFreightProvidersEndpoint",
    "JobIntacctEndpoint",
    "ItemsHelper",
    "JobNoteEndpoint",
    "JobOnHoldEndpoint",
    "JobParcelItemsEndpoint",
    "JobPaymentEndpoint",
    "JobRfqEndpoint",
    "ShipHelper",
    "JobShipmentEndpoint",
    "JobSmsEndpoint",
    "JobStatusEndpoint",
    "JobTimelineEndpoint",
    "TimelineHelpers",
    "JobTrackingEndpoint",
]
