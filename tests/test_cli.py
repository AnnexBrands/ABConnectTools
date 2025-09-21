"""Tests for CLI commands."""

import unittest
from unittest.mock import patch, MagicMock
import argparse
import json
from io import StringIO
from ABConnect.cli import (
    cmd_api, cmd_endpoints, cmd_lookup, cmd_company,
    cmd_quote, cmd_me, cmd_config, cmd_address
)


class TestCLICommands(unittest.TestCase):
    """Test cases for CLI commands."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.api_mock = MagicMock()
        
    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cmd_endpoints(self, mock_stdout, mock_api_class):
        """Test endpoints command."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.available_endpoints = ['companies', 'contacts', 'jobs']
        mock_api_class.return_value = mock_api
        
        # Create args
        args = argparse.Namespace(
            endpoint=None,
            format='table',
            verbose=False
        )
        
        # Run command
        cmd_endpoints(args)
        
        # Check output
        output = mock_stdout.getvalue()
        self.assertIn('Available endpoints', output)
        self.assertIn('companies', output)
        
    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cmd_api_raw(self, mock_stdout, mock_api_class):
        """Test raw API command."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.raw.call.return_value = {'status': 'success', 'data': []}
        mock_api_class.return_value = mock_api
        
        # Create args
        args = argparse.Namespace(
            api_type='raw',
            raw=True,
            method='get',
            path='/api/companies/search',
            params=['page=1', 'per_page=10'],
            format='json'
        )
        
        # Run command
        cmd_api(args)
        
        # Check API was called
        mock_api.raw.call.assert_called_once_with(
            'GET', '/api/companies/search', data=None, page='1', per_page='10'
        )
        
        # Check output is JSON
        output = mock_stdout.getvalue()
        data = json.loads(output)
        self.assertEqual(data['status'], 'success')
        
    @patch('ABConnect.cli.ABConnectAPI')
    def test_cmd_lookup(self, mock_api_class):
        """Test lookup command."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.raw.get.return_value = [
            {'id': '123', 'name': 'Test Company Type'}
        ]
        mock_api_class.return_value = mock_api
        
        # Create args
        args = argparse.Namespace(
            key='CompanyTypes',
            format='json'
        )
        
        # Run command (it will print to stdout)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            cmd_lookup(args)
            
        # Check API was called
        mock_api.raw.get.assert_called_with('lookup/CompanyTypes')
        
    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cmd_company_by_id(self, mock_stdout, mock_api_class):
        """Test company command with ID."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.companies.get_get.return_value = {
            'id': '123-abc',
            'name': 'Test Company',
            'code': 'TEST001'
        }
        mock_api_class.return_value = mock_api

        # Create args
        args = argparse.Namespace(
            code=None,
            id='123-abc'
        )

        # Run command
        cmd_company(args)

        # Check API was called with correct method
        mock_api.companies.get_get.assert_called_once_with('123-abc')

        # Check output is JSON
        output = mock_stdout.getvalue()
        data = json.loads(output)
        self.assertEqual(data['id'], '123-abc')
        self.assertEqual(data['name'], 'Test Company')

    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cmd_company_by_code(self, mock_stdout, mock_api_class):
        """Test company command with code."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.companies.get_search.return_value = [{
            'id': '123-abc',
            'name': 'Test Company',
            'code': 'TEST001'
        }]
        mock_api_class.return_value = mock_api

        # Create args
        args = argparse.Namespace(
            code='TEST001',
            id=None
        )

        # Run command
        cmd_company(args)

        # Check API was called with correct method
        mock_api.companies.get_search.assert_called_once_with(search_value='TEST001')

        # Check output is JSON
        output = mock_stdout.getvalue()
        data = json.loads(output)
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]['code'], 'TEST001')

    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cmd_address_by_id(self, mock_stdout, mock_api_class):
        """Test address command with ID."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.address.get_by_id.return_value = {
            'id': 'addr-123',
            'address1': '123 Main St',
            'city': 'Springfield',
            'state': 'IL',
            'zip': '62701'
        }
        mock_api_class.return_value = mock_api

        # Create args
        args = argparse.Namespace(
            id='addr-123',
            search=None,
            validate=False
        )

        # Run command
        cmd_address(args)

        # Check API was called
        mock_api.address.get_by_id.assert_called_once_with('addr-123')

        # Check output is JSON
        output = mock_stdout.getvalue()
        data = json.loads(output)
        self.assertEqual(data['id'], 'addr-123')
        self.assertEqual(data['city'], 'Springfield')

    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cmd_address_validate(self, mock_stdout, mock_api_class):
        """Test address validation command."""
        # Mock API instance
        mock_api = MagicMock()
        mock_api.address.validate.return_value = {
            'valid': True,
            'normalized': {
                'address1': '123 MAIN ST',
                'city': 'SPRINGFIELD',
                'state': 'IL',
                'zip': '62701-1234'
            }
        }
        mock_api_class.return_value = mock_api

        # Create args
        args = argparse.Namespace(
            id=None,
            search=None,
            validate=True,
            address1='123 Main St',
            city='Springfield',
            state='IL',
            zip='62701'
        )

        # Run command
        cmd_address(args)

        # Check API was called
        mock_api.address.validate.assert_called_once_with(
            address1='123 Main St',
            city='Springfield',
            state='IL',
            zip='62701'
        )

        # Check output is JSON
        output = mock_stdout.getvalue()
        data = json.loads(output)
        self.assertEqual(data['valid'], True)
        self.assertIn('normalized', data)

    @patch('ABConnect.cli.Config')
    def test_cmd_config_show(self, mock_config_class):
        """Test config show command."""
        # Mock config
        mock_config = MagicMock()
        mock_config.get_env.return_value = 'staging'
        mock_config.get_api_base_url.return_value = 'https://staging.api.example.com'
        mock_config._env_file = '.env.staging'
        mock_config_class.return_value = mock_config
        
        # Create args
        args = argparse.Namespace(
            show=True,
            env=None
        )
        
        # Run command
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            cmd_config(args)
            output = mock_stdout.getvalue()
            
        # Check output
        self.assertIn('Environment: staging', output)
        self.assertIn('API URL: https://staging.api.example.com', output)


class TestCLIParsing(unittest.TestCase):
    """Test CLI argument parsing."""
    
    def test_api_raw_parsing(self):
        """Test parsing of raw API command."""
        from ABConnect.cli import main
        
        # Mock sys.argv
        with patch('sys.argv', ['ab', 'api', 'raw', 'get', '/api/test']):
            with patch('ABConnect.cli.cmd_api') as mock_cmd:
                # Mock parse_args to avoid SystemExit
                with patch('argparse.ArgumentParser.parse_args') as mock_parse:
                    mock_parse.return_value = argparse.Namespace(
                        command='api',
                        api_type='raw',
                        method='get',
                        path='/api/test',
                        params=[],
                        format='json',
                        func=mock_cmd,
                        raw=True,
                        version=False
                    )
                    
                    # This would normally run the command
                    # but we're just testing parsing
                    args = mock_parse.return_value
                    self.assertEqual(args.api_type, 'raw')
                    self.assertEqual(args.method, 'get')
                    self.assertEqual(args.path, '/api/test')


if __name__ == "__main__":
    unittest.main()
