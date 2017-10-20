# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MerchantReturnResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'merchant_order_no': 'str',
        'lines': 'list[MerchantReturnLineResponse]',
        'reason': 'str',
        'customer_comment': 'str',
        'merchant_comment': 'str',
        'refund_incl_vat': 'float',
        'refund_excl_vat': 'float'
    }

    attribute_map = {
        'merchant_order_no': 'MerchantOrderNo',
        'lines': 'Lines',
        'reason': 'Reason',
        'customer_comment': 'CustomerComment',
        'merchant_comment': 'MerchantComment',
        'refund_incl_vat': 'RefundInclVat',
        'refund_excl_vat': 'RefundExclVat'
    }

    def __init__(self, merchant_order_no=None, lines=None, reason=None, customer_comment=None, merchant_comment=None, refund_incl_vat=None, refund_excl_vat=None):
        """
        MerchantReturnResponse - a model defined in Swagger
        """

        self._merchant_order_no = None
        self._lines = None
        self._reason = None
        self._customer_comment = None
        self._merchant_comment = None
        self._refund_incl_vat = None
        self._refund_excl_vat = None

        if merchant_order_no is not None:
          self.merchant_order_no = merchant_order_no
        if lines is not None:
          self.lines = lines
        if reason is not None:
          self.reason = reason
        if customer_comment is not None:
          self.customer_comment = customer_comment
        if merchant_comment is not None:
          self.merchant_comment = merchant_comment
        if refund_incl_vat is not None:
          self.refund_incl_vat = refund_incl_vat
        if refund_excl_vat is not None:
          self.refund_excl_vat = refund_excl_vat

    @property
    def merchant_order_no(self):
        """
        Gets the merchant_order_no of this MerchantReturnResponse.

        :return: The merchant_order_no of this MerchantReturnResponse.
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """
        Sets the merchant_order_no of this MerchantReturnResponse.

        :param merchant_order_no: The merchant_order_no of this MerchantReturnResponse.
        :type: str
        """

        self._merchant_order_no = merchant_order_no

    @property
    def lines(self):
        """
        Gets the lines of this MerchantReturnResponse.

        :return: The lines of this MerchantReturnResponse.
        :rtype: list[MerchantReturnLineResponse]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this MerchantReturnResponse.

        :param lines: The lines of this MerchantReturnResponse.
        :type: list[MerchantReturnLineResponse]
        """

        self._lines = lines

    @property
    def reason(self):
        """
        Gets the reason of this MerchantReturnResponse.

        :return: The reason of this MerchantReturnResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this MerchantReturnResponse.

        :param reason: The reason of this MerchantReturnResponse.
        :type: str
        """
        allowed_values = ["PRODUCT_DEFECT", "PRODUCT_UNSATISFACTORY", "REFUSED", "REFUSED_DAMAGED", "WRONG_ADDRESS", "NOT_COLLECTED", "OTHER"]
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def customer_comment(self):
        """
        Gets the customer_comment of this MerchantReturnResponse.

        :return: The customer_comment of this MerchantReturnResponse.
        :rtype: str
        """
        return self._customer_comment

    @customer_comment.setter
    def customer_comment(self, customer_comment):
        """
        Sets the customer_comment of this MerchantReturnResponse.

        :param customer_comment: The customer_comment of this MerchantReturnResponse.
        :type: str
        """
        if customer_comment is not None and len(customer_comment) > 4001:
            raise ValueError("Invalid value for `customer_comment`, length must be less than or equal to `4001`")
        if customer_comment is not None and len(customer_comment) < 0:
            raise ValueError("Invalid value for `customer_comment`, length must be greater than or equal to `0`")

        self._customer_comment = customer_comment

    @property
    def merchant_comment(self):
        """
        Gets the merchant_comment of this MerchantReturnResponse.

        :return: The merchant_comment of this MerchantReturnResponse.
        :rtype: str
        """
        return self._merchant_comment

    @merchant_comment.setter
    def merchant_comment(self, merchant_comment):
        """
        Sets the merchant_comment of this MerchantReturnResponse.

        :param merchant_comment: The merchant_comment of this MerchantReturnResponse.
        :type: str
        """
        if merchant_comment is not None and len(merchant_comment) > 4001:
            raise ValueError("Invalid value for `merchant_comment`, length must be less than or equal to `4001`")
        if merchant_comment is not None and len(merchant_comment) < 0:
            raise ValueError("Invalid value for `merchant_comment`, length must be greater than or equal to `0`")

        self._merchant_comment = merchant_comment

    @property
    def refund_incl_vat(self):
        """
        Gets the refund_incl_vat of this MerchantReturnResponse.

        :return: The refund_incl_vat of this MerchantReturnResponse.
        :rtype: float
        """
        return self._refund_incl_vat

    @refund_incl_vat.setter
    def refund_incl_vat(self, refund_incl_vat):
        """
        Sets the refund_incl_vat of this MerchantReturnResponse.

        :param refund_incl_vat: The refund_incl_vat of this MerchantReturnResponse.
        :type: float
        """

        self._refund_incl_vat = refund_incl_vat

    @property
    def refund_excl_vat(self):
        """
        Gets the refund_excl_vat of this MerchantReturnResponse.

        :return: The refund_excl_vat of this MerchantReturnResponse.
        :rtype: float
        """
        return self._refund_excl_vat

    @refund_excl_vat.setter
    def refund_excl_vat(self, refund_excl_vat):
        """
        Sets the refund_excl_vat of this MerchantReturnResponse.

        :param refund_excl_vat: The refund_excl_vat of this MerchantReturnResponse.
        :type: float
        """

        self._refund_excl_vat = refund_excl_vat

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, MerchantReturnResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
