"""Forms endpoint for retrieving various shipping and logistics forms.

This module provides methods for downloading different types of forms associated
with jobs, including Bills of Lading (BOL), shipping documents, and other
logistics paperwork.
"""

import logging
import urllib.parse
from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import FormId, FormType, BolType, to_file_dict

logging.basicConfig(level=logging.INFO)


class FormsEndpoint(BaseEndpoint):
    """Endpoint for form-related API operations.
    
    This endpoint provides methods to retrieve various forms and documents
    related to shipping and logistics operations. It specializes in Bills
    of Lading (BOL) but also supports other form types.
    
    Available Methods:
        - get_bol: Get carrier Bill of Lading
        - get_hbl: Get house Bill of Lading
        - get_pbl: Get pickup Bill of Lading  
        - get_dbl: Get delivery Bill of Lading
        - get_form: Generic form retrieval method
    """
    def _get_bol_params(self, jobid: int, seq: BolType) -> Dict[str, Any]:
        """Get parameters for Bill of Lading retrieval.
        
        Internal method that determines the correct shipment plan ID for
        retrieving a specific type of Bill of Lading.
        
        Sequence number mapping:
            - 0: House BOL
            - 2: Pickup BOL
            - 5: LTL/Last Mile Carrier BOL
            - 6: Delivery BOL
            - CARRIER (56): Prefers sequence 5 if exists, otherwise 6
        
        Args:
            jobid (int): The job identifier.
            seq (BolType): The type of BOL to retrieve.
            
        Returns:
            dict: Parameters needed for BOL retrieval::

                {
                    'jobid': 12345,
                    'shipmentPlanID': 'SP-123-456'
                }

        Raises:
            ABConnectError: If no matching shipment plan is found.
        """
        shipmentplans = self._r.call("GET", "api/job/%s/form/shipments" % jobid)
        candidates = (
            [5, 6] if seq == BolType.CARRIER else [seq.value]
        )  # results ordered so 5 precedes 6

        for plan in shipmentplans:
            if plan.get("sequenceNo") in candidates:
                return {"jobid": jobid, "shipmentPlanID": plan.get("jobShipmentID")}

    def get_bill_of_lading(self, jobid: int, boltype: BolType) -> Dict[str, Any]:
        """Retrieve a Bill of Lading document for a job.
        
        Downloads a specific type of Bill of Lading (BOL) as a PDF document.
        This is the generic method used by the specific BOL retrieval methods.
        
        Args:
            jobid (int): The job identifier.
            boltype (BolType): The type of BOL to retrieve (HOUSE, PICKUP,
                CARRIER, or DELIVERY).
                
        Returns:
            dict: A dictionary containing the PDF file data::

                {
                    'filename': 'JOB12345_CARRIER_BOL.pdf',
                    'content': b'<pdf binary data>',
                    'content_type': 'application/pdf',
                    'size': 98765
                }

        Raises:
            ABConnectError: If the BOL cannot be generated or retrieved.
            
        Example:
            >>> endpoint = FormsEndpoint()
            >>> bol = endpoint.get_bill_of_lading(12345, BolType.CARRIER)
            >>> with open(bol['filename'], 'wb') as f:
            ...     f.write(bol['content'])
        """
        url_params = self._get_bol_params(jobid, boltype)
        bol_url = (
            "job/%(jobid)s/form/BillOfLading?ProviderOptionIndex=&shipmentPlanID=%(shipmentPlanID)s"
            % url_params
        )
        response = self._r.call("GET", bol_url, raw=True)

        return to_file_dict(
            response,
            jobid,
            boltype.name,
        )

    def get_bol(self, jobid: int) -> Dict[str, Any]:
        """Get the carrier Bill of Lading for a job.
        
        Retrieves the primary carrier BOL, which is typically used for
        the main transportation leg of the shipment.
        
        Args:
            jobid (int): The job identifier.
            
        Returns:
            dict: PDF file data for the carrier BOL.
            
        Example:
            >>> endpoint = FormsEndpoint()
            >>> carrier_bol = endpoint.get_bol(12345)
            >>> print(f"Retrieved: {carrier_bol['filename']}")
        """
        return self.get_bill_of_lading(jobid, BolType.CARRIER)

    def get_hbl(self, jobid: int) -> Dict[str, Any]:
        """Get the house Bill of Lading for a job.
        
        Retrieves the house BOL, which is typically issued by a freight
        forwarder or NVOCC for their customers.
        
        Args:
            jobid (int): The job identifier.
            
        Returns:
            dict: PDF file data for the house BOL.
            
        Example:
            >>> endpoint = FormsEndpoint()
            >>> house_bol = endpoint.get_hbl(12345)
        """
        return self.get_bill_of_lading(jobid, BolType.HOUSE)

    def get_pbl(self, jobid: int) -> Dict[str, Any]:
        """Get the pickup Bill of Lading for a job.
        
        Retrieves the pickup BOL, which is used at the origin location
        when goods are collected.
        
        Args:
            jobid (int): The job identifier.
            
        Returns:
            dict: PDF file data for the pickup BOL.
            
        Example:
            >>> endpoint = FormsEndpoint()
            >>> pickup_bol = endpoint.get_pbl(12345)
        """
        return self.get_bill_of_lading(jobid, BolType.PICKUP)

    def get_dbl(self, jobid: int) -> Dict[str, Any]:
        """Get the delivery Bill of Lading for a job.
        
        Retrieves the delivery BOL, which is used at the destination
        location when goods are delivered.
        
        Args:
            jobid (int): The job identifier.
            
        Returns:
            dict: PDF file data for the delivery BOL.
            
        Example:
            >>> endpoint = FormsEndpoint()
            >>> delivery_bol = endpoint.get_dbl(12345)
        """
        return self.get_bill_of_lading(jobid, BolType.DELIVERY)

    def get_form(
        self,
        jobid: int,
        formid: FormId,
        formtype: Optional[FormType] = None,
        spid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generic method to retrieve any type of form.
        
        This is the base method for retrieving various forms associated with
        a job. It can be used to get forms that aren't covered by the specific
        BOL methods.
        
        Args:
            jobid (int): The job identifier.
            formid (FormId): The form identifier enum specifying which form
                to retrieve.
            formtype (FormType, optional): Additional form type specification
                if needed for certain forms.
            spid (str, optional): Shipment Plan ID if required for the
                specific form.
                
        Returns:
            dict: A dictionary containing the form file data::

                {
                    'filename': 'JOB12345_FormName.pdf',
                    'content': b'<file binary data>',
                    'content_type': 'application/pdf',
                    'size': 45678
                }

        Raises:
            ABConnectError: If the form cannot be generated or retrieved.
            
        Example:
            >>> endpoint = FormsEndpoint()
            >>> # Get a customs form
            >>> customs_form = endpoint.get_form(
            ...     jobid=12345,
            ...     formid=FormId.CUSTOMS_INVOICE,
            ...     formtype=FormType.EXPORT
            ... )
            >>> 
            >>> # Get a packing list
            >>> packing_list = endpoint.get_form(
            ...     jobid=12345,
            ...     formid=FormId.PACKING_LIST
            ... )
            
        Note:
            Available form IDs and types depend on the job type and
            configuration. Not all combinations are valid for all jobs.
        """
        base_url = "job/%s/form/%s" % (jobid, formid.value)
        get_params = {
            "type": formtype.value if formtype else None,
            "shipmentPlanID": spid,
        }
        query_string = urllib.parse.urlencode(
            {k: v for k, v in get_params.items() if v is not None}
        )
        url = f"{base_url}?{query_string}" if query_string else base_url

        response = self._r.call("GET", url, raw=True)
        return to_file_dict(
            response,
            jobid,
            formid.name,
        )
