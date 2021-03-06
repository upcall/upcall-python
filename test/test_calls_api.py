# coding: utf-8

"""
    Upcall API

    A RESTful API (json) to manage your human-powered outbound call campaigns.

    OpenAPI spec version: 2
    Contact: support@upcall.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.calls_api import CallsApi


class TestCallsApi(unittest.TestCase):
    """ CallsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.calls_api.CallsApi()

    def tearDown(self):
        pass

    def test_fetch_calls(self):
        """
        Test case for fetch_calls

        Get all calls
        """
        pass

    def test_fetch_calls_for_campaign(self):
        """
        Test case for fetch_calls_for_campaign

        Get all calls for a campaign
        """
        pass


if __name__ == '__main__':
    unittest.main()
