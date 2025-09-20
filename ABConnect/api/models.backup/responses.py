"""Response wrapper models for ABConnect API."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, ConfigDict


class PaginatedResponse(BaseModel):
    """Paginated response wrapper."""
    
    model_config = ConfigDict(extra="allow")
    
    data: List[Any] = Field(default_factory=list)
    page: int = 1
    per_page: int = 50
    total: int = 0
    total_pages: int = 0
    has_next: bool = False
    has_prev: bool = False
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], item_class: Optional[type] = None) -> "PaginatedResponse":
        """Create paginated response from dictionary."""
        page = data.get("page", 1)
        per_page = data.get("per_page", data.get("perPage", 50))
        total = data.get("total", 0)
        total_pages = data.get("total_pages", data.get("totalPages", 0))
        has_next = data.get("has_next", data.get("hasNext", False))
        has_prev = data.get("has_prev", data.get("hasPrev", False))
        
        items = data.get("data", data.get("items", data.get("results", [])))
        
        if item_class and hasattr(item_class, "model_validate"):
            parsed_items = [item_class.model_validate(item) for item in items]
        else:
            parsed_items = items
        
        return cls(
            data=parsed_items,
            page=page,
            per_page=per_page,
            total=total,
            total_pages=total_pages,
            has_next=has_next,
            has_prev=has_prev,
        )


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    message: str
    code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)