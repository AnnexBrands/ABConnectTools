#!/usr/bin/env python3
"""Test the new jobs CLI structure."""

import unittest
from unittest.mock import patch, MagicMock
import argparse
import json
from io import StringIO
from ABConnect.cli import cmd_jobs


class TestJobsCLI(unittest.TestCase):
    """Test the jobs command structure."""

    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_jobs_help(self, mock_stdout, mock_api_class):
        """Test jobs command without submodule shows help."""
        # Create args without submodule
        args = argparse.Namespace(submodule=None)

        # Run command
        cmd_jobs(args)

        # Check output shows help
        output = mock_stdout.getvalue()
        self.assertIn('JOBS PACKAGE', output)
        self.assertIn('agent', output)
        self.assertIn('OA/DA changes', output)
        self.assertIn('ab jobs agent oa', output)

    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.exit')
    def test_jobs_agent_oa(self, mock_exit, mock_stdout, mock_api_class):
        """Test jobs agent oa command."""
        # Mock API instance
        mock_api = MagicMock()
        mock_agent = MagicMock()
        mock_agent.oa.return_value = {'success': True, 'jobId': 2000000}
        mock_api.jobs.agent = mock_agent
        mock_api_class.return_value = mock_api

        # Create args for oa method
        args = argparse.Namespace(
            submodule='agent',
            method='oa',
            params=['2000000', 'JM']
        )

        # Run command
        cmd_jobs(args)

        # Check oa method was called correctly
        mock_agent.oa.assert_called_once_with(2000000, 'JM')

        # Check output
        output = mock_stdout.getvalue()
        self.assertIn('Executing jobs.agent.oa(2000000, JM)', output)
        self.assertIn('Method executed successfully', output)

    @patch('ABConnect.cli.ABConnectAPI')
    @patch('sys.stdout', new_callable=StringIO)
    def test_jobs_agent_help(self, mock_stdout, mock_api_class):
        """Test jobs agent submodule help."""
        # Mock API instance
        mock_api = MagicMock()
        mock_agent = MagicMock()
        # Add some methods to the agent
        mock_agent.oa = MagicMock()
        mock_agent.da = MagicMock()
        mock_agent.change = MagicMock()
        mock_api.jobs.agent = mock_agent
        mock_api_class.return_value = mock_api

        # Create args for agent submodule without method
        args = argparse.Namespace(
            submodule='agent',
            method=None,
            params=[]
        )

        # Run command
        cmd_jobs(args)

        # Check output shows methods
        output = mock_stdout.getvalue()
        self.assertIn('jobs.agent endpoint', output)
        self.assertIn('Available methods:', output)


if __name__ == '__main__':
    unittest.main()