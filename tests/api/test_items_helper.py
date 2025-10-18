"""Tests for ABConnect.api.endpoints.jobs.items_helpers module."""

from unittest.mock import patch, MagicMock
from base_test import ABConnectTestCase
from ABConnect import ABConnectAPI
from ABConnect.api.endpoints.jobs.items_helpers import ItemsHelper
from ABConnect.api.models.jobparcelitems import ParcelItem
from ABConnect.config import Config


class TestItemsHelper(ABConnectTestCase):
    """Test suite for ItemsHelper class."""

    @patch('ABConnect.api.endpoints.base.BaseEndpoint._r', new=MagicMock())
    def setUp(self):
        """Set up test fixtures."""
        super().setUp()
        # Create ItemsHelper directly without needing full API initialization
        self.items_helper = ItemsHelper()

    def test_items_helper_initialization(self):
        """Test ItemsHelper initialization."""
        self.assertIsNotNone(self.items_helper)
        self.assertIsInstance(self.items_helper, ItemsHelper)
        self.assertTrue(hasattr(self.items_helper, 'parcelitems'))
        self.assertTrue(hasattr(self.items_helper, 'freightitems'))
        self.assertTrue(hasattr(self.items_helper, 'jobitems'))
        self.assertTrue(hasattr(self.items_helper, 'logged_delete_parcel_items'))

    @patch('ABConnect.api.endpoints.jobs.items_helpers.get_config')
    @patch('ABConnect.api.endpoints.jobs.items_helpers.ItemsHelper.parcelitems')
    @patch('ABConnect.api.endpoints.jobs.note.JobNoteEndpoint.post_note')
    @patch('ABConnect.api.endpoints.jobs.parcelitems.JobParcelItemsEndpoint.delete_parcelitems')
    def test_logged_delete_parcel_items_success(
        self, mock_delete, mock_post_note, mock_parcelitems, mock_get_config
    ):
        """Test successful logged deletion of parcel items."""
        # Mock username from config
        mock_get_config.return_value = 'testuser'

        # Mock parcel items
        mock_item1 = ParcelItem(
            id=2443776,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe65',
            description='Box',
            quantity=2,
            job_item_pkd_length=10.0,
            job_item_pkd_width=5.0,
            job_item_pkd_height=3.0,
            job_item_pkd_weight=25.0
        )
        mock_item2 = ParcelItem(
            id=2443777,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe66',
            description='Crate',
            quantity=1,
            job_item_pkd_length=20.0,
            job_item_pkd_width=10.0,
            job_item_pkd_height=8.0,
            job_item_pkd_weight=50.0
        )
        mock_parcelitems.return_value = [mock_item1, mock_item2]

        # Mock note creation response
        mock_post_note.return_value = {'id': 'note-123'}

        # Mock successful deletions
        mock_delete.return_value = {'status': 'success'}

        # Execute
        result = self.items_helper.logged_delete_parcel_items(4675060)

        # Verify
        self.assertTrue(result)
        mock_get_config.assert_called_once_with('ABCONNECT_USERNAME', '')
        mock_parcelitems.assert_called_once_with(4675060)
        mock_post_note.assert_called_once()

        # Verify note content
        call_args = mock_post_note.call_args
        self.assertEqual(call_args[1]['jobDisplayId'], '4675060')
        note_data = call_args[1]['data']
        self.assertIn('testuser deleted parcel items', note_data['comments'])
        self.assertIn('2 Box 10.0x3.0x5.0 25.0lbs', note_data['comments'])
        self.assertIn('1 Crate 20.0x8.0x10.0 50.0lbs', note_data['comments'])
        self.assertEqual(note_data['taskCode'], 'PK')

        # Verify deletions
        self.assertEqual(mock_delete.call_count, 2)

    @patch('ABConnect.api.endpoints.jobs.items_helpers.get_config')
    @patch('ABConnect.api.endpoints.jobs.items_helpers.ItemsHelper.parcelitems')
    def test_logged_delete_parcel_items_no_items(
        self, mock_parcelitems, mock_get_config
    ):
        """Test logged deletion when no parcel items exist."""
        # Mock username from config
        mock_get_config.return_value = 'testuser'

        # Mock empty parcel items list
        mock_parcelitems.return_value = []

        # Execute
        result = self.items_helper.logged_delete_parcel_items(4675060)

        # Verify - should return True since there's nothing to delete
        self.assertTrue(result)
        mock_get_config.assert_called_once_with('ABCONNECT_USERNAME', '')
        mock_parcelitems.assert_called_once_with(4675060)

    @patch('ABConnect.api.endpoints.jobs.items_helpers.get_config')
    @patch('ABConnect.api.endpoints.jobs.items_helpers.ItemsHelper.parcelitems')
    @patch('ABConnect.api.endpoints.jobs.note.JobNoteEndpoint.post_note')
    @patch('ABConnect.api.endpoints.jobs.parcelitems.JobParcelItemsEndpoint.delete_parcelitems')
    def test_logged_delete_parcel_items_delete_failure(
        self, mock_delete, mock_post_note, mock_parcelitems, mock_get_config
    ):
        """Test logged deletion when item deletion fails - should try all items."""
        # Mock username from config
        mock_get_config.return_value = 'testuser'

        # Mock multiple parcel items
        mock_item1 = ParcelItem(
            id=2443776,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe65',
            description='Box',
            quantity=1,
            job_item_pkd_length=10.0,
            job_item_pkd_width=5.0,
            job_item_pkd_height=3.0,
            job_item_pkd_weight=25.0
        )
        mock_item2 = ParcelItem(
            id=2443777,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe66',
            description='Crate',
            quantity=1,
            job_item_pkd_length=20.0,
            job_item_pkd_width=10.0,
            job_item_pkd_height=8.0,
            job_item_pkd_weight=50.0
        )
        mock_parcelitems.return_value = [mock_item1, mock_item2]

        # Mock note creation response
        mock_post_note.return_value = {'id': 'note-123'}

        # Mock deletion failure for first item only
        mock_delete.side_effect = [Exception("Deletion failed"), {'status': 'success'}]

        # Execute
        result = self.items_helper.logged_delete_parcel_items(4675060)

        # Verify - should return False due to deletion failure, but both items attempted
        self.assertFalse(result)
        mock_post_note.assert_called_once()
        self.assertEqual(mock_delete.call_count, 2)  # Both items should be attempted

    @patch('ABConnect.api.endpoints.jobs.items_helpers.get_config')
    @patch('ABConnect.api.endpoints.jobs.items_helpers.ItemsHelper.parcelitems')
    @patch('ABConnect.api.endpoints.jobs.note.JobNoteEndpoint.post_note')
    @patch('ABConnect.api.endpoints.jobs.parcelitems.JobParcelItemsEndpoint.delete_parcelitems')
    def test_logged_delete_parcel_items_user_fetch_failure(
        self, mock_delete, mock_post_note, mock_parcelitems, mock_get_config
    ):
        """Test logged deletion when username not available - should still work without user name."""
        # Mock config returning empty username
        mock_get_config.return_value = ""

        # Mock parcel items
        mock_item = ParcelItem(
            id=2443776,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe65',
            description='Box',
            quantity=1,
            job_item_pkd_length=10.0,
            job_item_pkd_width=5.0,
            job_item_pkd_height=3.0,
            job_item_pkd_weight=25.0
        )
        mock_parcelitems.return_value = [mock_item]

        # Mock note and delete responses
        mock_post_note.return_value = {'id': 'note-123'}
        mock_delete.return_value = {'status': 'success'}

        # Execute
        result = self.items_helper.logged_delete_parcel_items(4675060)

        # Verify - should succeed even without user name
        self.assertTrue(result)
        mock_get_config.assert_called_once_with('ABCONNECT_USERNAME', '')
        mock_parcelitems.assert_called_once()

        # Verify note was created without user name (starts with "Deleted" not username)
        call_args = mock_post_note.call_args
        note_data = call_args[1]['data']
        self.assertIn('Deleted parcel items', note_data['comments'])
        self.assertTrue(note_data['comments'].startswith('Deleted parcel items'))

    @patch('ABConnect.api.endpoints.jobs.items_helpers.get_config')
    @patch('ABConnect.api.endpoints.jobs.items_helpers.ItemsHelper.parcelitems')
    def test_logged_delete_parcel_items_with_missing_fields(
        self, mock_parcelitems, mock_get_config
    ):
        """Test logged deletion with items missing optional fields."""
        # Mock username from config
        mock_get_config.return_value = 'testuser'

        # Mock parcel item with missing optional fields
        mock_item = ParcelItem(
            id=2443776,
            # No description, quantity, dimensions, or weight
        )
        mock_parcelitems.return_value = [mock_item]

        # Mock note creation response
        with patch('ABConnect.api.endpoints.jobs.note.JobNoteEndpoint.post_note') as mock_post_note, \
             patch('ABConnect.api.endpoints.jobs.parcelitems.JobParcelItemsEndpoint.delete_parcelitems') as mock_delete:

            mock_post_note.return_value = {'id': 'note-123'}
            mock_delete.return_value = {'status': 'success'}

            # Execute
            result = self.items_helper.logged_delete_parcel_items(4675060)

            # Verify
            self.assertTrue(result)

            # Verify note uses default values
            call_args = mock_post_note.call_args
            note_data = call_args[1]['data']
            self.assertIn('1 Item 0x0x0 0lbs', note_data['comments'])


    @patch('ABConnect.api.endpoints.jobs.items_helpers.get_config')
    @patch('ABConnect.api.endpoints.jobs.items_helpers.ItemsHelper.parcelitems')
    @patch('ABConnect.api.endpoints.jobs.note.JobNoteEndpoint.post_note')
    @patch('ABConnect.api.endpoints.jobs.parcelitems.JobParcelItemsEndpoint.delete_parcelitems')
    def test_logged_delete_parcel_items_non_json_response(
        self, mock_delete, mock_post_note, mock_parcelitems, mock_get_config
    ):
        """Test deletion when delete endpoint returns 200 with non-JSON response for multiple items."""
        # Mock username from config
        mock_get_config.return_value = 'testuser'

        # Mock multiple parcel items
        mock_item1 = ParcelItem(
            id=2559204,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe65',
            description='Box',
            quantity=1,
            job_item_pkd_length=10.0,
            job_item_pkd_width=5.0,
            job_item_pkd_height=3.0,
            job_item_pkd_weight=25.0
        )
        mock_item2 = ParcelItem(
            id=2559205,
            job_item_id='623f2748-b538-4b8d-18c8-08de0e96fe66',
            description='Crate',
            quantity=1,
            job_item_pkd_length=20.0,
            job_item_pkd_width=10.0,
            job_item_pkd_height=8.0,
            job_item_pkd_weight=50.0
        )
        mock_parcelitems.return_value = [mock_item1, mock_item2]

        # Mock note creation response
        mock_post_note.return_value = {'id': 'note-123'}

        # Mock deletion with 200 non-JSON error for all items (actual behavior from API)
        from ABConnect.exceptions import RequestError
        mock_delete.side_effect = [
            RequestError(200, "Response content was not valid JSON."),
            RequestError(200, "Response content was not valid JSON.")
        ]

        # Execute
        result = self.items_helper.logged_delete_parcel_items(4675060)

        # Verify - should return True since HTTP 200 means success for all items
        self.assertTrue(result)
        mock_post_note.assert_called_once()
        self.assertEqual(mock_delete.call_count, 2)  # Both items should be deleted


if __name__ == '__main__':
    import unittest
    unittest.main()
