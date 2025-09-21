"""Tests for APIRequestBuilder."""

from . import BuilderTestCase
from ABConnect import APIRequestBuilder


class TestAPIRequestBuilder(BuilderTestCase):
    """Test suite for APIRequestBuilder class."""

    def test_builder_initialization(self):
        """Test builder initialization."""
        builder = APIRequestBuilder(base_data={})
        self.assertIsNotNone(builder)

    def test_load_base_template(self):
        """Test loading base request template."""
        # Test that simple_request template can be loaded
        template = self.load_template("simple_request")
        if template:
            builder = APIRequestBuilder(base_data=template)
            self.assertIsNotNone(builder)
        else:
            self.skipTest("simple_request.json template not found")

    def test_update_nested_path(self):
        """Test updating nested paths with dot notation."""
        builder = APIRequestBuilder(base_data={})

        # Test basic nested path update
        builder.update('JobInfo.OtherRefNo', '6306')
        result = builder.build()

        self.assertIn('JobInfo', result)
        self.assertEqual(result['JobInfo'].get('OtherRefNo'), '6306')

    def test_update_items(self):
        """Test updating items in the builder data."""
        # Initialize the builder with an empty base_data dictionary.
        builder = APIRequestBuilder(base_data={})

        # Update a JobInfo field.
        builder.update('JobInfo.OtherRefNo', '6306')

        # Sample rows for items.
        rows = [
            {'lot_number': '1001', 'title': 'Widget A', 'amount': 10},
            {'lot_number': '1002', 'title': 'Widget B', 'amount': 20}
        ]

        # Example dimensions and weight.
        L = 5
        W = 10
        H = 15
        Wgt = 2.5

        # Update each item in the builder data.
        for idx, row in enumerate(rows):
            builder.update(f'Items.{idx}.L', str(L))
            builder.update(f'Items.{idx}.W', str(W))
            builder.update(f'Items.{idx}.H', str(H))
            builder.update(f'Items.{idx}.Wgt', str(Wgt))
            builder.update(f'Items.{idx}.Description', f"Lot {row['lot_number']} {row['title']}")
            builder.update(f'Items.{idx}.Value', row['amount'])

        # Build the final API request data.
        result = builder.build()

        # Validate that the result contains the updates.
        self.assertIn('JobInfo', result)
        self.assertEqual(result['JobInfo'].get('OtherRefNo'), '6306')

        self.assertIn('Items', result)
        self.assertEqual(len(result['Items']), len(rows))

        for idx, row in enumerate(rows):
            item = result['Items'][idx]
            self.assertEqual(item.get('L'), str(L))
            self.assertEqual(item.get('W'), str(W))
            self.assertEqual(item.get('H'), str(H))
            self.assertEqual(item.get('Wgt'), str(Wgt))
            self.assertEqual(item.get('Description'), f"Lot {row['lot_number']} {row['title']}")
            self.assertEqual(item.get('Value'), row['amount'])

    def test_job_type_handling(self):
        """Test handling of Regular vs 3PL job types."""
        self.skipTest("Not yet implemented")

    def test_extra_containers(self):
        """Test adding extra containers for 3PL."""
        self.skipTest("Not yet implemented")