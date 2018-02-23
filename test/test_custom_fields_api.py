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
from swagger_client.apis.custom_fields_api import CustomFieldsApi


class TestCustomFieldsApi(unittest.TestCase):
    """ CustomFieldsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.custom_fields_api.CustomFieldsApi()

    def tearDown(self):
        pass

    def test_fetch_custom_fields(self):
        """
        Test case for fetch_custom_fields

        Get custom fields
        """
        pass


if __name__ == '__main__':
    unittest.main()
