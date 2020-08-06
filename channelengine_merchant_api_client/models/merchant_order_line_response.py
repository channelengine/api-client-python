# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from channelengine_merchant_api_client.configuration import Configuration


class MerchantOrderLineResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'OrderStatusView',
        'is_fulfillment_by_marketplace': 'bool',
        'merchant_product_no': 'str',
        'gtin': 'str',
        'description': 'str',
        'unit_vat': 'float',
        'line_total_incl_vat': 'float',
        'line_vat': 'float',
        'original_unit_price_incl_vat': 'float',
        'original_unit_vat': 'float',
        'original_line_total_incl_vat': 'float',
        'original_line_vat': 'float',
        'original_fee_fixed': 'float',
        'bundle_product_merchant_product_no': 'str',
        'extra_data': 'list[MerchantOrderLineExtraDataResponse]',
        'channel_product_no': 'str',
        'quantity': 'int',
        'cancellation_requested_quantity': 'int',
        'unit_price_incl_vat': 'float',
        'fee_fixed': 'float',
        'fee_rate': 'float',
        'condition': 'Condition',
        'expected_delivery_date': 'datetime'
    }

    attribute_map = {
        'status': 'Status',
        'is_fulfillment_by_marketplace': 'IsFulfillmentByMarketplace',
        'merchant_product_no': 'MerchantProductNo',
        'gtin': 'Gtin',
        'description': 'Description',
        'unit_vat': 'UnitVat',
        'line_total_incl_vat': 'LineTotalInclVat',
        'line_vat': 'LineVat',
        'original_unit_price_incl_vat': 'OriginalUnitPriceInclVat',
        'original_unit_vat': 'OriginalUnitVat',
        'original_line_total_incl_vat': 'OriginalLineTotalInclVat',
        'original_line_vat': 'OriginalLineVat',
        'original_fee_fixed': 'OriginalFeeFixed',
        'bundle_product_merchant_product_no': 'BundleProductMerchantProductNo',
        'extra_data': 'ExtraData',
        'channel_product_no': 'ChannelProductNo',
        'quantity': 'Quantity',
        'cancellation_requested_quantity': 'CancellationRequestedQuantity',
        'unit_price_incl_vat': 'UnitPriceInclVat',
        'fee_fixed': 'FeeFixed',
        'fee_rate': 'FeeRate',
        'condition': 'Condition',
        'expected_delivery_date': 'ExpectedDeliveryDate'
    }

    def __init__(self, status=None, is_fulfillment_by_marketplace=None, merchant_product_no=None, gtin=None, description=None, unit_vat=None, line_total_incl_vat=None, line_vat=None, original_unit_price_incl_vat=None, original_unit_vat=None, original_line_total_incl_vat=None, original_line_vat=None, original_fee_fixed=None, bundle_product_merchant_product_no=None, extra_data=None, channel_product_no=None, quantity=None, cancellation_requested_quantity=None, unit_price_incl_vat=None, fee_fixed=None, fee_rate=None, condition=None, expected_delivery_date=None, local_vars_configuration=None):  # noqa: E501
        """MerchantOrderLineResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._is_fulfillment_by_marketplace = None
        self._merchant_product_no = None
        self._gtin = None
        self._description = None
        self._unit_vat = None
        self._line_total_incl_vat = None
        self._line_vat = None
        self._original_unit_price_incl_vat = None
        self._original_unit_vat = None
        self._original_line_total_incl_vat = None
        self._original_line_vat = None
        self._original_fee_fixed = None
        self._bundle_product_merchant_product_no = None
        self._extra_data = None
        self._channel_product_no = None
        self._quantity = None
        self._cancellation_requested_quantity = None
        self._unit_price_incl_vat = None
        self._fee_fixed = None
        self._fee_rate = None
        self._condition = None
        self._expected_delivery_date = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if is_fulfillment_by_marketplace is not None:
            self.is_fulfillment_by_marketplace = is_fulfillment_by_marketplace
        self.merchant_product_no = merchant_product_no
        self.gtin = gtin
        self.description = description
        self.unit_vat = unit_vat
        self.line_total_incl_vat = line_total_incl_vat
        self.line_vat = line_vat
        self.original_unit_price_incl_vat = original_unit_price_incl_vat
        self.original_unit_vat = original_unit_vat
        self.original_line_total_incl_vat = original_line_total_incl_vat
        self.original_line_vat = original_line_vat
        if original_fee_fixed is not None:
            self.original_fee_fixed = original_fee_fixed
        self.bundle_product_merchant_product_no = bundle_product_merchant_product_no
        self.extra_data = extra_data
        self.channel_product_no = channel_product_no
        self.quantity = quantity
        if cancellation_requested_quantity is not None:
            self.cancellation_requested_quantity = cancellation_requested_quantity
        self.unit_price_incl_vat = unit_price_incl_vat
        if fee_fixed is not None:
            self.fee_fixed = fee_fixed
        if fee_rate is not None:
            self.fee_rate = fee_rate
        if condition is not None:
            self.condition = condition
        self.expected_delivery_date = expected_delivery_date

    @property
    def status(self):
        """Gets the status of this MerchantOrderLineResponse.  # noqa: E501


        :return: The status of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: OrderStatusView
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MerchantOrderLineResponse.


        :param status: The status of this MerchantOrderLineResponse.  # noqa: E501
        :type status: OrderStatusView
        """

        self._status = status

    @property
    def is_fulfillment_by_marketplace(self):
        """Gets the is_fulfillment_by_marketplace of this MerchantOrderLineResponse.  # noqa: E501

        Is the order fulfilled by the marketplace (amazon: FBA, bol: LVB, etc.)?.  # noqa: E501

        :return: The is_fulfillment_by_marketplace of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_fulfillment_by_marketplace

    @is_fulfillment_by_marketplace.setter
    def is_fulfillment_by_marketplace(self, is_fulfillment_by_marketplace):
        """Sets the is_fulfillment_by_marketplace of this MerchantOrderLineResponse.

        Is the order fulfilled by the marketplace (amazon: FBA, bol: LVB, etc.)?.  # noqa: E501

        :param is_fulfillment_by_marketplace: The is_fulfillment_by_marketplace of this MerchantOrderLineResponse.  # noqa: E501
        :type is_fulfillment_by_marketplace: bool
        """

        self._is_fulfillment_by_marketplace = is_fulfillment_by_marketplace

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this MerchantOrderLineResponse.  # noqa: E501

        The unique product reference used by the Merchant (sku).  # noqa: E501

        :return: The merchant_product_no of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this MerchantOrderLineResponse.

        The unique product reference used by the Merchant (sku).  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this MerchantOrderLineResponse.  # noqa: E501
        :type merchant_product_no: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def gtin(self):
        """Gets the gtin of this MerchantOrderLineResponse.  # noqa: E501

        Either the GTIN (EAN, ISBN, UPC etc) provided by the channel, or the the GTIN belonging to the MerchantProductNo in ChannelEngine.  # noqa: E501

        :return: The gtin of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this MerchantOrderLineResponse.

        Either the GTIN (EAN, ISBN, UPC etc) provided by the channel, or the the GTIN belonging to the MerchantProductNo in ChannelEngine.  # noqa: E501

        :param gtin: The gtin of this MerchantOrderLineResponse.  # noqa: E501
        :type gtin: str
        """

        self._gtin = gtin

    @property
    def description(self):
        """Gets the description of this MerchantOrderLineResponse.  # noqa: E501

        The product description (or title) provided by the channel.  # noqa: E501

        :return: The description of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MerchantOrderLineResponse.

        The product description (or title) provided by the channel.  # noqa: E501

        :param description: The description of this MerchantOrderLineResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def unit_vat(self):
        """Gets the unit_vat of this MerchantOrderLineResponse.  # noqa: E501

        The total amount of VAT charged over the value of a single unit of the ordered product  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :return: The unit_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._unit_vat

    @unit_vat.setter
    def unit_vat(self, unit_vat):
        """Sets the unit_vat of this MerchantOrderLineResponse.

        The total amount of VAT charged over the value of a single unit of the ordered product  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :param unit_vat: The unit_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type unit_vat: float
        """

        self._unit_vat = unit_vat

    @property
    def line_total_incl_vat(self):
        """Gets the line_total_incl_vat of this MerchantOrderLineResponse.  # noqa: E501

        The total value of the order line (quantity * unit price) including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :return: The line_total_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._line_total_incl_vat

    @line_total_incl_vat.setter
    def line_total_incl_vat(self, line_total_incl_vat):
        """Sets the line_total_incl_vat of this MerchantOrderLineResponse.

        The total value of the order line (quantity * unit price) including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :param line_total_incl_vat: The line_total_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type line_total_incl_vat: float
        """

        self._line_total_incl_vat = line_total_incl_vat

    @property
    def line_vat(self):
        """Gets the line_vat of this MerchantOrderLineResponse.  # noqa: E501

        The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :return: The line_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._line_vat

    @line_vat.setter
    def line_vat(self, line_vat):
        """Sets the line_vat of this MerchantOrderLineResponse.

        The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :param line_vat: The line_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type line_vat: float
        """

        self._line_vat = line_vat

    @property
    def original_unit_price_incl_vat(self):
        """Gets the original_unit_price_incl_vat of this MerchantOrderLineResponse.  # noqa: E501

        The value of a single unit of the ordered product including VAT  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :return: The original_unit_price_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._original_unit_price_incl_vat

    @original_unit_price_incl_vat.setter
    def original_unit_price_incl_vat(self, original_unit_price_incl_vat):
        """Sets the original_unit_price_incl_vat of this MerchantOrderLineResponse.

        The value of a single unit of the ordered product including VAT  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :param original_unit_price_incl_vat: The original_unit_price_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type original_unit_price_incl_vat: float
        """

        self._original_unit_price_incl_vat = original_unit_price_incl_vat

    @property
    def original_unit_vat(self):
        """Gets the original_unit_vat of this MerchantOrderLineResponse.  # noqa: E501

        The total amount of VAT charged over the value of a single unit of the ordered product  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :return: The original_unit_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._original_unit_vat

    @original_unit_vat.setter
    def original_unit_vat(self, original_unit_vat):
        """Sets the original_unit_vat of this MerchantOrderLineResponse.

        The total amount of VAT charged over the value of a single unit of the ordered product  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :param original_unit_vat: The original_unit_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type original_unit_vat: float
        """

        self._original_unit_vat = original_unit_vat

    @property
    def original_line_total_incl_vat(self):
        """Gets the original_line_total_incl_vat of this MerchantOrderLineResponse.  # noqa: E501

        The total value of the order line (quantity * unit price) including VAT  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :return: The original_line_total_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._original_line_total_incl_vat

    @original_line_total_incl_vat.setter
    def original_line_total_incl_vat(self, original_line_total_incl_vat):
        """Sets the original_line_total_incl_vat of this MerchantOrderLineResponse.

        The total value of the order line (quantity * unit price) including VAT  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :param original_line_total_incl_vat: The original_line_total_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type original_line_total_incl_vat: float
        """

        self._original_line_total_incl_vat = original_line_total_incl_vat

    @property
    def original_line_vat(self):
        """Gets the original_line_vat of this MerchantOrderLineResponse.  # noqa: E501

        The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :return: The original_line_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._original_line_vat

    @original_line_vat.setter
    def original_line_vat(self, original_line_vat):
        """Sets the original_line_vat of this MerchantOrderLineResponse.

        The total amount of VAT charged over the total value of the order line (quantity * unit price)  (in the currency in which the order was paid for, see CurrencyCode).  # noqa: E501

        :param original_line_vat: The original_line_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type original_line_vat: float
        """

        self._original_line_vat = original_line_vat

    @property
    def original_fee_fixed(self):
        """Gets the original_fee_fixed of this MerchantOrderLineResponse.  # noqa: E501

        A percentage fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of client  This field is optional, send 0 if not applicable.  # noqa: E501

        :return: The original_fee_fixed of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._original_fee_fixed

    @original_fee_fixed.setter
    def original_fee_fixed(self, original_fee_fixed):
        """Sets the original_fee_fixed of this MerchantOrderLineResponse.

        A percentage fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of client  This field is optional, send 0 if not applicable.  # noqa: E501

        :param original_fee_fixed: The original_fee_fixed of this MerchantOrderLineResponse.  # noqa: E501
        :type original_fee_fixed: float
        """

        self._original_fee_fixed = original_fee_fixed

    @property
    def bundle_product_merchant_product_no(self):
        """Gets the bundle_product_merchant_product_no of this MerchantOrderLineResponse.  # noqa: E501

        If the product is ordered part of a bundle, this field contains the MerchantProductNo of  the product bundle.  # noqa: E501

        :return: The bundle_product_merchant_product_no of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._bundle_product_merchant_product_no

    @bundle_product_merchant_product_no.setter
    def bundle_product_merchant_product_no(self, bundle_product_merchant_product_no):
        """Sets the bundle_product_merchant_product_no of this MerchantOrderLineResponse.

        If the product is ordered part of a bundle, this field contains the MerchantProductNo of  the product bundle.  # noqa: E501

        :param bundle_product_merchant_product_no: The bundle_product_merchant_product_no of this MerchantOrderLineResponse.  # noqa: E501
        :type bundle_product_merchant_product_no: str
        """

        self._bundle_product_merchant_product_no = bundle_product_merchant_product_no

    @property
    def extra_data(self):
        """Gets the extra_data of this MerchantOrderLineResponse.  # noqa: E501


        :return: The extra_data of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: list[MerchantOrderLineExtraDataResponse]
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this MerchantOrderLineResponse.


        :param extra_data: The extra_data of this MerchantOrderLineResponse.  # noqa: E501
        :type extra_data: list[MerchantOrderLineExtraDataResponse]
        """

        self._extra_data = extra_data

    @property
    def channel_product_no(self):
        """Gets the channel_product_no of this MerchantOrderLineResponse.  # noqa: E501

        The unique product reference used by the channel.  # noqa: E501

        :return: The channel_product_no of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """Sets the channel_product_no of this MerchantOrderLineResponse.

        The unique product reference used by the channel.  # noqa: E501

        :param channel_product_no: The channel_product_no of this MerchantOrderLineResponse.  # noqa: E501
        :type channel_product_no: str
        """
        if self.local_vars_configuration.client_side_validation and channel_product_no is None:  # noqa: E501
            raise ValueError("Invalid value for `channel_product_no`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                channel_product_no is not None and len(channel_product_no) > 50):
            raise ValueError("Invalid value for `channel_product_no`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                channel_product_no is not None and len(channel_product_no) < 0):
            raise ValueError("Invalid value for `channel_product_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._channel_product_no = channel_product_no

    @property
    def quantity(self):
        """Gets the quantity of this MerchantOrderLineResponse.  # noqa: E501

        The number of items of the product.  # noqa: E501

        :return: The quantity of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this MerchantOrderLineResponse.

        The number of items of the product.  # noqa: E501

        :param quantity: The quantity of this MerchantOrderLineResponse.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def cancellation_requested_quantity(self):
        """Gets the cancellation_requested_quantity of this MerchantOrderLineResponse.  # noqa: E501

        The number of items for which cancellation was requested by the customer.  Some channels allow a customer to cancel an order until it has been shipped.  When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation.  Use this field to check whether it is still possible to cancel the order. If this is the case, submit a cancellation to ChannelEngine.  # noqa: E501

        :return: The cancellation_requested_quantity of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: int
        """
        return self._cancellation_requested_quantity

    @cancellation_requested_quantity.setter
    def cancellation_requested_quantity(self, cancellation_requested_quantity):
        """Sets the cancellation_requested_quantity of this MerchantOrderLineResponse.

        The number of items for which cancellation was requested by the customer.  Some channels allow a customer to cancel an order until it has been shipped.  When an order has already been acknowledged in ChannelEngine, it can only be cancelled by creating a cancellation.  Use this field to check whether it is still possible to cancel the order. If this is the case, submit a cancellation to ChannelEngine.  # noqa: E501

        :param cancellation_requested_quantity: The cancellation_requested_quantity of this MerchantOrderLineResponse.  # noqa: E501
        :type cancellation_requested_quantity: int
        """

        self._cancellation_requested_quantity = cancellation_requested_quantity

    @property
    def unit_price_incl_vat(self):
        """Gets the unit_price_incl_vat of this MerchantOrderLineResponse.  # noqa: E501

        The value of a single unit of the ordered product including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :return: The unit_price_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._unit_price_incl_vat

    @unit_price_incl_vat.setter
    def unit_price_incl_vat(self, unit_price_incl_vat):
        """Sets the unit_price_incl_vat of this MerchantOrderLineResponse.

        The value of a single unit of the ordered product including VAT  (in the shop's base currency calculated using the exchange rate at the time of ordering).  # noqa: E501

        :param unit_price_incl_vat: The unit_price_incl_vat of this MerchantOrderLineResponse.  # noqa: E501
        :type unit_price_incl_vat: float
        """
        if self.local_vars_configuration.client_side_validation and unit_price_incl_vat is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price_incl_vat`, must not be `None`")  # noqa: E501

        self._unit_price_incl_vat = unit_price_incl_vat

    @property
    def fee_fixed(self):
        """Gets the fee_fixed of this MerchantOrderLineResponse.  # noqa: E501

        A fixed fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of the Channel  This field is optional, send 0 if not applicable.  # noqa: E501

        :return: The fee_fixed of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._fee_fixed

    @fee_fixed.setter
    def fee_fixed(self, fee_fixed):
        """Sets the fee_fixed of this MerchantOrderLineResponse.

        A fixed fee that is charged by the Channel for this orderline.  This fee rate is based on the currency of the Channel  This field is optional, send 0 if not applicable.  # noqa: E501

        :param fee_fixed: The fee_fixed of this MerchantOrderLineResponse.  # noqa: E501
        :type fee_fixed: float
        """

        self._fee_fixed = fee_fixed

    @property
    def fee_rate(self):
        """Gets the fee_rate of this MerchantOrderLineResponse.  # noqa: E501

        A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.  # noqa: E501

        :return: The fee_rate of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this MerchantOrderLineResponse.

        A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.  # noqa: E501

        :param fee_rate: The fee_rate of this MerchantOrderLineResponse.  # noqa: E501
        :type fee_rate: float
        """

        self._fee_rate = fee_rate

    @property
    def condition(self):
        """Gets the condition of this MerchantOrderLineResponse.  # noqa: E501


        :return: The condition of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this MerchantOrderLineResponse.


        :param condition: The condition of this MerchantOrderLineResponse.  # noqa: E501
        :type condition: Condition
        """

        self._condition = condition

    @property
    def expected_delivery_date(self):
        """Gets the expected_delivery_date of this MerchantOrderLineResponse.  # noqa: E501

        Expected delivery date from channels, empty if channels not support this value  # noqa: E501

        :return: The expected_delivery_date of this MerchantOrderLineResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expected_delivery_date

    @expected_delivery_date.setter
    def expected_delivery_date(self, expected_delivery_date):
        """Sets the expected_delivery_date of this MerchantOrderLineResponse.

        Expected delivery date from channels, empty if channels not support this value  # noqa: E501

        :param expected_delivery_date: The expected_delivery_date of this MerchantOrderLineResponse.  # noqa: E501
        :type expected_delivery_date: datetime
        """

        self._expected_delivery_date = expected_delivery_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, MerchantOrderLineResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MerchantOrderLineResponse):
            return True

        return self.to_dict() != other.to_dict()
