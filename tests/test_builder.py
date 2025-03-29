import unittest
from ABConnect import APIRequestBuilder

class TestAPIRequestBuilder(unittest.TestCase):
    def test_update_items(self):
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

if __name__ == '__main__':
    unittest.main()
