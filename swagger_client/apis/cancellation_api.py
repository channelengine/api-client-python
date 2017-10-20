# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.0
    
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


class CancellationApi(object):
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

    def cancellation_create(self, cancellation, **kwargs):
        """
        Merchant: Create Cancellation
        For merchants.    Mark (part of) an order as cancelled.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancellation_create(cancellation, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MerchantCancellationRequest cancellation:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancellation_create_with_http_info(cancellation, **kwargs)
        else:
            (data) = self.cancellation_create_with_http_info(cancellation, **kwargs)
            return data

    def cancellation_create_with_http_info(self, cancellation, **kwargs):
        """
        Merchant: Create Cancellation
        For merchants.    Mark (part of) an order as cancelled.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancellation_create_with_http_info(cancellation, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MerchantCancellationRequest cancellation:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancellation']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancellation_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cancellation' is set
        if ('cancellation' not in params) or (params['cancellation'] is None):
            raise ValueError("Missing the required parameter `cancellation` when calling `cancellation_create`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cancellation' in params:
            body_params = params['cancellation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/cancellations', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cancellation_index(self, created_since, **kwargs):
        """
        Channel: Get Cancellations
        For channels.    Gets all cancellations created since the supplied date.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancellation_index(created_since, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime created_since:  (required)
        :return: CollectionOfChannelCancellationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancellation_index_with_http_info(created_since, **kwargs)
        else:
            (data) = self.cancellation_index_with_http_info(created_since, **kwargs)
            return data

    def cancellation_index_with_http_info(self, created_since, **kwargs):
        """
        Channel: Get Cancellations
        For channels.    Gets all cancellations created since the supplied date.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancellation_index_with_http_info(created_since, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime created_since:  (required)
        :return: CollectionOfChannelCancellationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancellation_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'created_since' is set
        if ('created_since' not in params) or (params['created_since'] is None):
            raise ValueError("Missing the required parameter `created_since` when calling `cancellation_index`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_since' in params:
            query_params.append(('createdSince', params['created_since']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api('/v2/cancellations', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CollectionOfChannelCancellationResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
