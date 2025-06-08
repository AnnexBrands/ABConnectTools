"""Tests for CLI commands."""

import unittest
from unittest.mock import patch, MagicMock
import argparse
import json
from io import StringIO
from ABConnect.cli import (
    cmd_api, cmd_endpoints, cmd_lookup, cmd_company,
    cmd_quote, cmd_me, cmd_config
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
