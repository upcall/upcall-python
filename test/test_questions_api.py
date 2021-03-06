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
from swagger_client.apis.questions_api import QuestionsApi


class TestQuestionsApi(unittest.TestCase):
    """ QuestionsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.questions_api.QuestionsApi()

    def tearDown(self):
        pass

    def test_fetch_campaign_questions(self):
        """
        Test case for fetch_campaign_questions

        Get campaign's questions
        """
        pass


if __name__ == '__main__':
    unittest.main()
