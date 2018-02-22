# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from channelengine_merchant_api_client.models.merchant_cancellation_line_request import MerchantCancellationLineRequest  # noqa: F401,E501


class MerchantCancellationRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'merchant_cancellation_no': 'str',
        'merchant_order_no': 'str',
        'lines': 'list[MerchantCancellationLineRequest]',
        'reason': 'str'
    }

    attribute_map = {
        'merchant_cancellation_no': 'MerchantCancellationNo',
        'merchant_order_no': 'MerchantOrderNo',
        'lines': 'Lines',
        'reason': 'Reason'
    }

    def __init__(self, merchant_cancellation_no=None, merchant_order_no=None, lines=None, reason=None):  # noqa: E501
        """MerchantCancellationRequest - a model defined in Swagger"""  # noqa: E501

        self._merchant_cancellation_no = None
        self._merchant_order_no = None
        self._lines = None
        self._reason = None
        self.discriminator = None

        self.merchant_cancellation_no = merchant_cancellation_no
        self.merchant_order_no = merchant_order_no
        self.lines = lines
        if reason is not None:
            self.reason = reason

    @property
    def merchant_cancellation_no(self):
        """Gets the merchant_cancellation_no of this MerchantCancellationRequest.  # noqa: E501


        :return: The merchant_cancellation_no of this MerchantCancellationRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_cancellation_no

    @merchant_cancellation_no.setter
    def merchant_cancellation_no(self, merchant_cancellation_no):
        """Sets the merchant_cancellation_no of this MerchantCancellationRequest.


        :param merchant_cancellation_no: The merchant_cancellation_no of this MerchantCancellationRequest.  # noqa: E501
        :type: str
        """
        if merchant_cancellation_no is None:
            raise ValueError("Invalid value for `merchant_cancellation_no`, must not be `None`")  # noqa: E501

        self._merchant_cancellation_no = merchant_cancellation_no

    @property
    def merchant_order_no(self):
        """Gets the merchant_order_no of this MerchantCancellationRequest.  # noqa: E501


        :return: The merchant_order_no of this MerchantCancellationRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """Sets the merchant_order_no of this MerchantCancellationRequest.


        :param merchant_order_no: The merchant_order_no of this MerchantCancellationRequest.  # noqa: E501
        :type: str
        """
        if merchant_order_no is None:
            raise ValueError("Invalid value for `merchant_order_no`, must not be `None`")  # noqa: E501

        self._merchant_order_no = merchant_order_no

    @property
    def lines(self):
        """Gets the lines of this MerchantCancellationRequest.  # noqa: E501


        :return: The lines of this MerchantCancellationRequest.  # noqa: E501
        :rtype: list[MerchantCancellationLineRequest]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this MerchantCancellationRequest.


        :param lines: The lines of this MerchantCancellationRequest.  # noqa: E501
        :type: list[MerchantCancellationLineRequest]
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def reason(self):
        """Gets the reason of this MerchantCancellationRequest.  # noqa: E501


        :return: The reason of this MerchantCancellationRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MerchantCancellationRequest.


        :param reason: The reason of this MerchantCancellationRequest.  # noqa: E501
        :type: str
        """

        self._reason = reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MerchantCancellationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
