# coding: utf-8

"""
    Upcall API

    A RESTful API (json) to manage your human-powered outbound call campaigns.

    OpenAPI spec version: 2
    Contact: support@upcall.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AnswersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def fetch_contact_answers(self, id, **kwargs):
        """
        Get contact's answers
        Fetching answers for contact
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fetch_contact_answers(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of contact (required)
        :param int limit: Amount of records to return. 25 by default.
        :param int start_id: Object ID to fetch next page
        :param int end_id: Object ID to fetch previous page
        :param str result: Filter. Filter collection by result
        :param str sort: Sort field. Available fields: answer_type, created_at
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.fetch_contact_answers_with_http_info(id, **kwargs)
        else:
            (data) = self.fetch_contact_answers_with_http_info(id, **kwargs)
            return data

    def fetch_contact_answers_with_http_info(self, id, **kwargs):
        """
        Get contact's answers
        Fetching answers for contact
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fetch_contact_answers_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of contact (required)
        :param int limit: Amount of records to return. 25 by default.
        :param int start_id: Object ID to fetch next page
        :param int end_id: Object ID to fetch previous page
        :param str result: Filter. Filter collection by result
        :param str sort: Sort field. Available fields: answer_type, created_at
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'start_id', 'end_id', 'result', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_contact_answers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `fetch_contact_answers`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'start_id' in params:
            query_params.append(('start_id', params['start_id']))
        if 'end_id' in params:
            query_params.append(('end_id', params['end_id']))
        if 'result' in params:
            query_params.append(('result', params['result']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'oauth2']

        return self.api_client.call_api('/contacts/{id}/answers', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2005',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def fetch_question_answers(self, id, **kwargs):
        """
        Get question's answers
        Fetching answers for question
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fetch_question_answers(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of question (required)
        :param int limit: Amount of records to return. 25 by default.
        :param int start_id: Object ID to fetch next page
        :param int end_id: Object ID to fetch previous page
        :param str result: Filter. Filter collection by result
        :param str sort: Sort field. Available fields: created_at
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.fetch_question_answers_with_http_info(id, **kwargs)
        else:
            (data) = self.fetch_question_answers_with_http_info(id, **kwargs)
            return data

    def fetch_question_answers_with_http_info(self, id, **kwargs):
        """
        Get question's answers
        Fetching answers for question
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fetch_question_answers_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID of question (required)
        :param int limit: Amount of records to return. 25 by default.
        :param int start_id: Object ID to fetch next page
        :param int end_id: Object ID to fetch previous page
        :param str result: Filter. Filter collection by result
        :param str sort: Sort field. Available fields: created_at
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'start_id', 'end_id', 'result', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_question_answers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `fetch_question_answers`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'start_id' in params:
            query_params.append(('start_id', params['start_id']))
        if 'end_id' in params:
            query_params.append(('end_id', params['end_id']))
        if 'result' in params:
            query_params.append(('result', params['result']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'oauth2']

        return self.api_client.call_api('/questions/{id}/answers', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2005',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
