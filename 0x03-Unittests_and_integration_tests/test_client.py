#!/usr/bin/env python3
"""
A test for the client script
"""
import unittest
from typing import Dict
from unittest.mock import patch, MagicMock
from client import GithubOrgClient

from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    A class that test's the github
    org client
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock):
        """
        test that GithubOrgClient.org returns the correct value
        """
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
