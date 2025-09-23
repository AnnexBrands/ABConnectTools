"""Job Job API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobEndpoint(BaseEndpoint):
    """Job API endpoint operations.

    Total endpoints: 19
    """

    api_path = "job"

    def post_book(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/book

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/book"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_search(self, job_display_id: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/search

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/search"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_searchByDetails(self, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/searchByDetails

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/searchByDetails"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_calendaritems(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/calendaritems

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/calendaritems"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def put_save(self, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PUT /api/job/save

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/save"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)

    def post(self, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = ""
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_feedback(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/feedback/{jobDisplayId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/feedback/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_feedback(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/feedback/{jobDisplayId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/feedback/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_transfer(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/transfer/{jobDisplayId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/transfer/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_freightitems(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/freightitems

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/freightitems"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_submanagementstatus(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/submanagementstatus

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/submanagementstatus"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_item_notes(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/item/notes

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/item/notes"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_changeAgent(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/changeAgent

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/changeAgent"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_updatePageConfig(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/updatePageConfig

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/updatePageConfig"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_price(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/price

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/price"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_jobAccessLevel(self, job_display_id: Optional[str] = None, job_item_id: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/jobAccessLevel

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/jobAccessLevel"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if job_item_id is not None:
            params["jobItemId"] = job_item_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def get_documentConfig(self) -> Dict[str, Any]:
        """GET /api/job/documentConfig

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/documentConfig"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_packagingcontainers(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/packagingcontainers

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/packagingcontainers"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
