"""Tests for contacts endpoint."""

from .base_endpoint_test import BaseEndpointTest


class TestContactsEndpoint(BaseEndpointTest):
    """Test suite for contacts endpoint."""

    endpoint_name = "contacts"
    required_models = ["Contact", "ContactDetails", "ContactModel"]

    def test_contact_creation(self):
        """Test creating a new contact."""
        self.skipTest("Not yet implemented")

    def test_contact_merge(self):
        """Test merging contacts."""
        self.skipTest("Not yet implemented")

    def test_contact_sync(self):
        """Test contact synchronization."""
        self.skipTest("Not yet implemented")