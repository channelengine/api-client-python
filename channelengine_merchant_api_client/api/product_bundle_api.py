# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_merchant_api_client.api_client import ApiClient
from channelengine_merchant_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ProductBundleApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def product_bundle_get_by_filter(self, **kwargs):  # noqa: E501
        """Get product bundles.  You can get the full product information on bundles from the regular /products endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.product_bundle_get_by_filter(async_req=True)
        >>> result = thread.get()

        :param search: Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters.
        :type search: str
        :param ean_list: Search products by submitting a list of EAN's.
        :type ean_list: list[str]
        :param merchant_product_no_list: Search products by submitting a list of MerchantProductNo's.
        :type merchant_product_no_list: list[str]
        :param page: The page to filter on. Starts at 1.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CollectionOfMerchantProductBundleResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.product_bundle_get_by_filter_with_http_info(**kwargs)  # noqa: E501

    def product_bundle_get_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Get product bundles.  You can get the full product information on bundles from the regular /products endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.product_bundle_get_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param search: Search product(s) by Name, MerchantProductNo, Ean or Brand<br />This search is applied to the result after applying the other filters.
        :type search: str
        :param ean_list: Search products by submitting a list of EAN's.
        :type ean_list: list[str]
        :param merchant_product_no_list: Search products by submitting a list of MerchantProductNo's.
        :type merchant_product_no_list: list[str]
        :param page: The page to filter on. Starts at 1.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CollectionOfMerchantProductBundleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'search',
            'ean_list',
            'merchant_product_no_list',
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_bundle_get_by_filter" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'ean_list' in local_var_params and local_var_params['ean_list'] is not None:  # noqa: E501
            query_params.append(('eanList', local_var_params['ean_list']))  # noqa: E501
            collection_formats['eanList'] = 'multi'  # noqa: E501
        if 'merchant_product_no_list' in local_var_params and local_var_params['merchant_product_no_list'] is not None:  # noqa: E501
            query_params.append(('merchantProductNoList', local_var_params['merchant_product_no_list']))  # noqa: E501
            collection_formats['merchantProductNoList'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/productbundles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantProductBundleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
