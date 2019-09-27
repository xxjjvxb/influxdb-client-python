# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb_client.api_client import ApiClient


class ChecksService(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_check(self, check, **kwargs):  # noqa: E501
        """Add new check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_check(check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Check check: check to create (required)
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_check_with_http_info(check, **kwargs)  # noqa: E501
        else:
            (data) = self.create_check_with_http_info(check, **kwargs)  # noqa: E501
            return data

    def create_check_with_http_info(self, check, **kwargs):  # noqa: E501
        """Add new check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_check_with_http_info(check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Check check: check to create (required)
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_check" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check' is set
        if ('check' not in local_var_params or
                local_var_params['check'] is None):
            raise ValueError("Missing the required parameter `check` when calling `create_check`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'check' in local_var_params:
            body_params = local_var_params['check']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Check',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_checks_id(self, check_id, **kwargs):  # noqa: E501
        """Delete a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_checks_id_with_http_info(check_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_checks_id_with_http_info(check_id, **kwargs)  # noqa: E501
            return data

    def delete_checks_id_with_http_info(self, check_id, **kwargs):  # noqa: E501
        """Delete a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_checks_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `delete_checks_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_checks_id_labels_id(self, check_id, label_id, **kwargs):  # noqa: E501
        """delete label from a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id_labels_id(check_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of the check (required)
        :param str label_id: the label id to delete (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_checks_id_labels_id_with_http_info(check_id, label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_checks_id_labels_id_with_http_info(check_id, label_id, **kwargs)  # noqa: E501
            return data

    def delete_checks_id_labels_id_with_http_info(self, check_id, label_id, **kwargs):  # noqa: E501
        """delete label from a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_checks_id_labels_id_with_http_info(check_id, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of the check (required)
        :param str label_id: the label id to delete (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'label_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_checks_id_labels_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `delete_checks_id_labels_id`")  # noqa: E501
        # verify the required parameter 'label_id' is set
        if ('label_id' not in local_var_params or
                local_var_params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `delete_checks_id_labels_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501
        if 'label_id' in local_var_params:
            path_params['labelID'] = local_var_params['label_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}/labels/{labelID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_checks(self, org_id, **kwargs):  # noqa: E501
        """Get all checks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: only show checks belonging to specified organization (required)
        :param int offset:
        :param int limit:
        :return: Checks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_checks_with_http_info(org_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_checks_with_http_info(org_id, **kwargs)  # noqa: E501
            return data

    def get_checks_with_http_info(self, org_id, **kwargs):  # noqa: E501
        """Get all checks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_id: only show checks belonging to specified organization (required)
        :param int offset:
        :param int limit:
        :return: Checks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['org_id', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_checks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if ('org_id' not in local_var_params or
                local_var_params['org_id'] is None):
            raise ValueError("Missing the required parameter `org_id` when calling `get_checks`")  # noqa: E501

        if 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_checks`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_checks`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_checks`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Checks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_checks_id(self, check_id, **kwargs):  # noqa: E501
        """Get a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_checks_id_with_http_info(check_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_checks_id_with_http_info(check_id, **kwargs)  # noqa: E501
            return data

    def get_checks_id_with_http_info(self, check_id, **kwargs):  # noqa: E501
        """Get a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_checks_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `get_checks_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Check',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_checks_id_labels(self, check_id, **kwargs):  # noqa: E501
        """list all labels for a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_labels(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of the check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_checks_id_labels_with_http_info(check_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_checks_id_labels_with_http_info(check_id, **kwargs)  # noqa: E501
            return data

    def get_checks_id_labels_with_http_info(self, check_id, **kwargs):  # noqa: E501
        """list all labels for a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_labels_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of the check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_checks_id_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `get_checks_id_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}/labels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_checks_id_query(self, check_id, **kwargs):  # noqa: E501
        """Get an check query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_query(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_checks_id_query_with_http_info(check_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_checks_id_query_with_http_info(check_id, **kwargs)  # noqa: E501
            return data

    def get_checks_id_query_with_http_info(self, check_id, **kwargs):  # noqa: E501
        """Get an check query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_checks_id_query_with_http_info(check_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param str zap_trace_span: OpenTracing span context
        :return: FluxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_checks_id_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `get_checks_id_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}/query', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FluxResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_checks_id(self, check_id, check, **kwargs):  # noqa: E501
        """Update a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_checks_id(check_id, check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param Check check: check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_checks_id_with_http_info(check_id, check, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_checks_id_with_http_info(check_id, check, **kwargs)  # noqa: E501
            return data

    def patch_checks_id_with_http_info(self, check_id, check, **kwargs):  # noqa: E501
        """Update a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_checks_id_with_http_info(check_id, check, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of check (required)
        :param Check check: check update to apply (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Check
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'check', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_checks_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `patch_checks_id`")  # noqa: E501
        # verify the required parameter 'check' is set
        if ('check' not in local_var_params or
                local_var_params['check'] is None):
            raise ValueError("Missing the required parameter `check` when calling `patch_checks_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'check' in local_var_params:
            body_params = local_var_params['check']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Check',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_checks_id_labels(self, check_id, label_mapping, **kwargs):  # noqa: E501
        """add a label to a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_checks_id_labels(check_id, label_mapping, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of the check (required)
        :param LabelMapping label_mapping: label to add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_checks_id_labels_with_http_info(check_id, label_mapping, **kwargs)  # noqa: E501
        else:
            (data) = self.post_checks_id_labels_with_http_info(check_id, label_mapping, **kwargs)  # noqa: E501
            return data

    def post_checks_id_labels_with_http_info(self, check_id, label_mapping, **kwargs):  # noqa: E501
        """add a label to a check  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_checks_id_labels_with_http_info(check_id, label_mapping, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_id: ID of the check (required)
        :param LabelMapping label_mapping: label to add (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['check_id', 'label_mapping', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_checks_id_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'check_id' is set
        if ('check_id' not in local_var_params or
                local_var_params['check_id'] is None):
            raise ValueError("Missing the required parameter `check_id` when calling `post_checks_id_labels`")  # noqa: E501
        # verify the required parameter 'label_mapping' is set
        if ('label_mapping' not in local_var_params or
                local_var_params['label_mapping'] is None):
            raise ValueError("Missing the required parameter `label_mapping` when calling `post_checks_id_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'check_id' in local_var_params:
            path_params['checkID'] = local_var_params['check_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'label_mapping' in local_var_params:
            body_params = local_var_params['label_mapping']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/checks/{checkID}/labels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)