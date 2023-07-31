#!/usr/bin/env python3
"""A module for testing the utils module.
"""
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]
                               ) -> None:
        """
        tests the access_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
