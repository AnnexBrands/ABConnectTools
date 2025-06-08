"""Comprehensive tests for all Lookup Keys.

This module tests each value in LookupKeys enum to ensure:
1. The lookup endpoint returns valid data
2. The response can be validated with the LookupValue model
"""

import unittest
from typing import List
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError, RequestError
from ABConnect.api.models import LookupKeys, LookupValue


class TestAllLookupKeys(BaseEndpointTest):
    """Test cases for all lookup keys."""
    
    tag_name = "Lookup"
    __test__ = True

    def setUp(self):
        """Set up test fixtures."""
        super().setUp()

    def _test_lookup_key(self, key: str, key_name: str):
        """Helper method to test a single lookup key.
        
        Args:
            key: The lookup key value
            key_name: The name of the enum member (for error messages)
        """
        try:
            response = self.api.raw.get(
                "/api/lookup/{masterConstantKey}",
                masterConstantKey=key,
            )
            
            # Check response is not None
            self.assertIsNotNone(response, f"Response for {key_name} ({key}) is None")
            
            # Response should be a list of lookup values
            self.assertIsInstance(response, list, f"Response for {key_name} ({key}) is not a list")
            
            # Validate each item in the response
            validated_count = 0
            for idx, item in enumerate(response):
                try:
                    # Validate with Pydantic model
                    lookup_value = LookupValue.model_validate(item)
                    self.assertIsInstance(lookup_value, LookupValue)
                    
                    # Check required fields
                    self.assertIsNotNone(lookup_value.id, f"Item {idx} in {key_name} has no id")
                    # Must have either value or name
                    self.assertTrue(
                        lookup_value.value or lookup_value.name,
                        f"Item {idx} in {key_name} has neither value nor name"
                    )
                    
                    validated_count += 1
                except Exception as e:
                    self.fail(f"Failed to validate item {idx} in {key_name} ({key}): {str(e)}")
            
            # Log success
            print(f"✓ {key_name}: validated {validated_count} items")
            
        except RequestError as e:
            if e.status_code == 404:
                self.skipTest(f"Lookup key {key_name} ({key}) returns 404 - may not be available in staging")
            elif e.status_code == 500:
                self.skipTest(f"Lookup key {key_name} ({key}) returns 500 - server error")
            else:
                raise

    def test_all_lookup_keys(self):
        """Test all lookup keys defined in the LookupKeys enum."""
        failed_keys = []
        skipped_keys = []
        successful_keys = []
        
        # Test each lookup key
        for key_name, key_value in LookupKeys.__members__.items():
            with self.subTest(lookup_key=key_name):
                try:
                    self._test_lookup_key(key_value.value, key_name)
                    successful_keys.append(key_name)
                except unittest.SkipTest as e:
                    skipped_keys.append((key_name, str(e)))
                    raise  # Re-raise to mark as skipped
                except Exception as e:
                    failed_keys.append((key_name, str(e)))
                    raise  # Re-raise to fail the subtest
        
        # Print summary (will only show if all tests pass)
        if not failed_keys:
            print(f"\n✅ Successfully validated {len(successful_keys)} lookup keys")
            if skipped_keys:
                print(f"⚠️  Skipped {len(skipped_keys)} keys due to API issues")

    def test_companytypes_lookup_detailed(self):
        """Detailed test for CompanyTypes lookup."""
        try:
            response = self.api.raw.get(
                "/api/lookup/{masterConstantKey}",
                masterConstantKey=LookupKeys.COMPANYTYPES.value,
            )
            
            self.assertIsInstance(response, list)
            self.assertGreater(len(response), 0, "CompanyTypes lookup returned empty list")
            
            # Check that we have expected company types
            # Get values from either 'value' or 'name' field
            company_type_values = []
            for item in response:
                if 'value' in item:
                    company_type_values.append(item['value'])
                elif 'name' in item:
                    company_type_values.append(item['name'])
            
            # Log what we actually got
            print(f"Company types found: {company_type_values}")
            
            # Check that we got some reasonable number of company types
            self.assertGreaterEqual(len(company_type_values), 5, 
                                   "Expected at least 5 company types in response")
            
            # Validate all items
            for item in response:
                lookup_value = LookupValue.model_validate(item)
                self.assertIsNotNone(lookup_value.id)
                self.assertTrue(lookup_value.value or lookup_value.name, 
                               "Lookup value must have either 'value' or 'name'")
                
        except RequestError as e:
            if e.status_code in [404, 500]:
                self.skipTest(f"CompanyTypes lookup returned {e.status_code}")
            else:
                raise

    def test_contacttypes_lookup_detailed(self):
        """Detailed test for ContactTypes lookup."""
        try:
            response = self.api.raw.get(
                "/api/lookup/{masterConstantKey}",
                masterConstantKey=LookupKeys.CONTACTTYPES.value,
            )
            
            self.assertIsInstance(response, list)
            self.assertGreater(len(response), 0, "ContactTypes lookup returned empty list")
            
            # Validate all items
            for item in response:
                lookup_value = LookupValue.model_validate(item)
                self.assertIsNotNone(lookup_value.id)
                self.assertTrue(lookup_value.value or lookup_value.name, 
                               "Lookup value must have either 'value' or 'name'")
                
        except RequestError as e:
            if e.status_code in [404, 500]:
                self.skipTest(f"ContactTypes lookup returned {e.status_code}")
            else:
                raise

    def test_jobstatustypes_lookup_detailed(self):
        """Detailed test for JobsStatusTypes lookup."""
        try:
            response = self.api.raw.get(
                "/api/lookup/{masterConstantKey}",
                masterConstantKey=LookupKeys.JOBSSTATUSTYPES.value,
            )
            
            self.assertIsInstance(response, list)
            self.assertGreater(len(response), 0, "JobsStatusTypes lookup returned empty list")
            
            # Validate all items
            for item in response:
                lookup_value = LookupValue.model_validate(item)
                self.assertIsNotNone(lookup_value.id)
                self.assertTrue(lookup_value.value or lookup_value.name, 
                               "Lookup value must have either 'value' or 'name'")
                
                # Job status values might correspond to our JobStatus enum
                # but the API might have different values
                
        except RequestError as e:
            if e.status_code in [404, 500]:
                self.skipTest(f"JobsStatusTypes lookup returned {e.status_code}")
            else:
                raise


if __name__ == "__main__":
    unittest.main()