# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from channelengine_merchant_api_client.configuration import Configuration


class MerchantProductRequest(object):
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
        'merchant_product_no': 'str',
        'parent_merchant_product_no': 'str',
        'parent_merchant_product_no2': 'str',
        'extra_data': 'list[MerchantProductExtraDataItemRequest]',
        'name': 'str',
        'description': 'str',
        'brand': 'str',
        'size': 'str',
        'color': 'str',
        'ean': 'str',
        'manufacturer_product_number': 'str',
        'stock': 'int',
        'price': 'float',
        'msrp': 'float',
        'purchase_price': 'float',
        'vat_rate_type': 'VatRateType',
        'shipping_cost': 'float',
        'shipping_time': 'str',
        'url': 'str',
        'image_url': 'str',
        'extra_image_url1': 'str',
        'extra_image_url2': 'str',
        'extra_image_url3': 'str',
        'extra_image_url4': 'str',
        'extra_image_url5': 'str',
        'extra_image_url6': 'str',
        'extra_image_url7': 'str',
        'extra_image_url8': 'str',
        'extra_image_url9': 'str',
        'category_trail': 'str'
    }

    attribute_map = {
        'merchant_product_no': 'MerchantProductNo',
        'parent_merchant_product_no': 'ParentMerchantProductNo',
        'parent_merchant_product_no2': 'ParentMerchantProductNo2',
        'extra_data': 'ExtraData',
        'name': 'Name',
        'description': 'Description',
        'brand': 'Brand',
        'size': 'Size',
        'color': 'Color',
        'ean': 'Ean',
        'manufacturer_product_number': 'ManufacturerProductNumber',
        'stock': 'Stock',
        'price': 'Price',
        'msrp': 'MSRP',
        'purchase_price': 'PurchasePrice',
        'vat_rate_type': 'VatRateType',
        'shipping_cost': 'ShippingCost',
        'shipping_time': 'ShippingTime',
        'url': 'Url',
        'image_url': 'ImageUrl',
        'extra_image_url1': 'ExtraImageUrl1',
        'extra_image_url2': 'ExtraImageUrl2',
        'extra_image_url3': 'ExtraImageUrl3',
        'extra_image_url4': 'ExtraImageUrl4',
        'extra_image_url5': 'ExtraImageUrl5',
        'extra_image_url6': 'ExtraImageUrl6',
        'extra_image_url7': 'ExtraImageUrl7',
        'extra_image_url8': 'ExtraImageUrl8',
        'extra_image_url9': 'ExtraImageUrl9',
        'category_trail': 'CategoryTrail'
    }

    def __init__(self, merchant_product_no=None, parent_merchant_product_no=None, parent_merchant_product_no2=None, extra_data=None, name=None, description=None, brand=None, size=None, color=None, ean=None, manufacturer_product_number=None, stock=None, price=None, msrp=None, purchase_price=None, vat_rate_type=None, shipping_cost=None, shipping_time=None, url=None, image_url=None, extra_image_url1=None, extra_image_url2=None, extra_image_url3=None, extra_image_url4=None, extra_image_url5=None, extra_image_url6=None, extra_image_url7=None, extra_image_url8=None, extra_image_url9=None, category_trail=None, local_vars_configuration=None):  # noqa: E501
        """MerchantProductRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._merchant_product_no = None
        self._parent_merchant_product_no = None
        self._parent_merchant_product_no2 = None
        self._extra_data = None
        self._name = None
        self._description = None
        self._brand = None
        self._size = None
        self._color = None
        self._ean = None
        self._manufacturer_product_number = None
        self._stock = None
        self._price = None
        self._msrp = None
        self._purchase_price = None
        self._vat_rate_type = None
        self._shipping_cost = None
        self._shipping_time = None
        self._url = None
        self._image_url = None
        self._extra_image_url1 = None
        self._extra_image_url2 = None
        self._extra_image_url3 = None
        self._extra_image_url4 = None
        self._extra_image_url5 = None
        self._extra_image_url6 = None
        self._extra_image_url7 = None
        self._extra_image_url8 = None
        self._extra_image_url9 = None
        self._category_trail = None
        self.discriminator = None

        self.merchant_product_no = merchant_product_no
        self.parent_merchant_product_no = parent_merchant_product_no
        self.parent_merchant_product_no2 = parent_merchant_product_no2
        self.extra_data = extra_data
        self.name = name
        self.description = description
        self.brand = brand
        self.size = size
        self.color = color
        self.ean = ean
        self.manufacturer_product_number = manufacturer_product_number
        if stock is not None:
            self.stock = stock
        if price is not None:
            self.price = price
        self.msrp = msrp
        self.purchase_price = purchase_price
        if vat_rate_type is not None:
            self.vat_rate_type = vat_rate_type
        self.shipping_cost = shipping_cost
        self.shipping_time = shipping_time
        self.url = url
        self.image_url = image_url
        self.extra_image_url1 = extra_image_url1
        self.extra_image_url2 = extra_image_url2
        self.extra_image_url3 = extra_image_url3
        self.extra_image_url4 = extra_image_url4
        self.extra_image_url5 = extra_image_url5
        self.extra_image_url6 = extra_image_url6
        self.extra_image_url7 = extra_image_url7
        self.extra_image_url8 = extra_image_url8
        self.extra_image_url9 = extra_image_url9
        self.category_trail = category_trail

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this MerchantProductRequest.  # noqa: E501

        A unique identifier of the product. (sku).  # noqa: E501

        :return: The merchant_product_no of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this MerchantProductRequest.

        A unique identifier of the product. (sku).  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this MerchantProductRequest.  # noqa: E501
        :type merchant_product_no: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def parent_merchant_product_no(self):
        """Gets the parent_merchant_product_no of this MerchantProductRequest.  # noqa: E501

        If this product is a different version of another  product (for example, all fields are the same except  size), then this field should contain  the 'MerchantProductNo' of the parent. The parent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the parent is behind the child in the list).  # noqa: E501

        :return: The parent_merchant_product_no of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_merchant_product_no

    @parent_merchant_product_no.setter
    def parent_merchant_product_no(self, parent_merchant_product_no):
        """Sets the parent_merchant_product_no of this MerchantProductRequest.

        If this product is a different version of another  product (for example, all fields are the same except  size), then this field should contain  the 'MerchantProductNo' of the parent. The parent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the parent is behind the child in the list).  # noqa: E501

        :param parent_merchant_product_no: The parent_merchant_product_no of this MerchantProductRequest.  # noqa: E501
        :type parent_merchant_product_no: str
        """

        self._parent_merchant_product_no = parent_merchant_product_no

    @property
    def parent_merchant_product_no2(self):
        """Gets the parent_merchant_product_no2 of this MerchantProductRequest.  # noqa: E501

        If this product is a different version of another  product (for example, all fields are the same except  color) and itself is a parent with child products (e.g. of sizes),  then this field should contain the 'MerchantProductNo' of the grandparent. The grandparent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the grandparent is behind the child in the list).  When you set this field, the ParentMerchantProductNo should be left empty.                Use this field in case of three level product hierarchy,  e.g. model - color - size.  This is required for channels like Otto.  # noqa: E501

        :return: The parent_merchant_product_no2 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_merchant_product_no2

    @parent_merchant_product_no2.setter
    def parent_merchant_product_no2(self, parent_merchant_product_no2):
        """Sets the parent_merchant_product_no2 of this MerchantProductRequest.

        If this product is a different version of another  product (for example, all fields are the same except  color) and itself is a parent with child products (e.g. of sizes),  then this field should contain the 'MerchantProductNo' of the grandparent. The grandparent  should already exist (or be present between the products  in the content of the API call, it does not matter whether  the grandparent is behind the child in the list).  When you set this field, the ParentMerchantProductNo should be left empty.                Use this field in case of three level product hierarchy,  e.g. model - color - size.  This is required for channels like Otto.  # noqa: E501

        :param parent_merchant_product_no2: The parent_merchant_product_no2 of this MerchantProductRequest.  # noqa: E501
        :type parent_merchant_product_no2: str
        """

        self._parent_merchant_product_no2 = parent_merchant_product_no2

    @property
    def extra_data(self):
        """Gets the extra_data of this MerchantProductRequest.  # noqa: E501

        An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products.  # noqa: E501

        :return: The extra_data of this MerchantProductRequest.  # noqa: E501
        :rtype: list[MerchantProductExtraDataItemRequest]
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this MerchantProductRequest.

        An optional list of key-value pairs containing  extra data about this product. This data can be  sent to channels or used for filtering products.  # noqa: E501

        :param extra_data: The extra_data of this MerchantProductRequest.  # noqa: E501
        :type extra_data: list[MerchantProductExtraDataItemRequest]
        """

        self._extra_data = extra_data

    @property
    def name(self):
        """Gets the name of this MerchantProductRequest.  # noqa: E501

        The name of the product.  # noqa: E501

        :return: The name of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MerchantProductRequest.

        The name of the product.  # noqa: E501

        :param name: The name of this MerchantProductRequest.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this MerchantProductRequest.  # noqa: E501

        A description of the product. Can contain these HTML tags:  div, span, pre, p, br, hr, hgroup, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, strong, em, b, i, u, img, a, abbr, address, blockquote, area, audio, video, caption, table, tbody, td, tfoot, th, thead, tr.  # noqa: E501

        :return: The description of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MerchantProductRequest.

        A description of the product. Can contain these HTML tags:  div, span, pre, p, br, hr, hgroup, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, strong, em, b, i, u, img, a, abbr, address, blockquote, area, audio, video, caption, table, tbody, td, tfoot, th, thead, tr.  # noqa: E501

        :param description: The description of this MerchantProductRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def brand(self):
        """Gets the brand of this MerchantProductRequest.  # noqa: E501

        The brand of the product.  # noqa: E501

        :return: The brand of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this MerchantProductRequest.

        The brand of the product.  # noqa: E501

        :param brand: The brand of this MerchantProductRequest.  # noqa: E501
        :type brand: str
        """

        self._brand = brand

    @property
    def size(self):
        """Gets the size of this MerchantProductRequest.  # noqa: E501

        Optional. The size of the product (variant). E.g. fashion size (S-XL, 46-56, etc), width of the watch, etc..  # noqa: E501

        :return: The size of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MerchantProductRequest.

        Optional. The size of the product (variant). E.g. fashion size (S-XL, 46-56, etc), width of the watch, etc..  # noqa: E501

        :param size: The size of this MerchantProductRequest.  # noqa: E501
        :type size: str
        """

        self._size = size

    @property
    def color(self):
        """Gets the color of this MerchantProductRequest.  # noqa: E501

        Optional. The color of the product (variant).  # noqa: E501

        :return: The color of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this MerchantProductRequest.

        Optional. The color of the product (variant).  # noqa: E501

        :param color: The color of this MerchantProductRequest.  # noqa: E501
        :type color: str
        """

        self._color = color

    @property
    def ean(self):
        """Gets the ean of this MerchantProductRequest.  # noqa: E501

        The EAN of GTIN of the product.  # noqa: E501

        :return: The ean of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this MerchantProductRequest.

        The EAN of GTIN of the product.  # noqa: E501

        :param ean: The ean of this MerchantProductRequest.  # noqa: E501
        :type ean: str
        """

        self._ean = ean

    @property
    def manufacturer_product_number(self):
        """Gets the manufacturer_product_number of this MerchantProductRequest.  # noqa: E501

        The unique product reference used by the manufacturer/vendor of the product.  # noqa: E501

        :return: The manufacturer_product_number of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_product_number

    @manufacturer_product_number.setter
    def manufacturer_product_number(self, manufacturer_product_number):
        """Sets the manufacturer_product_number of this MerchantProductRequest.

        The unique product reference used by the manufacturer/vendor of the product.  # noqa: E501

        :param manufacturer_product_number: The manufacturer_product_number of this MerchantProductRequest.  # noqa: E501
        :type manufacturer_product_number: str
        """

        self._manufacturer_product_number = manufacturer_product_number

    @property
    def stock(self):
        """Gets the stock of this MerchantProductRequest.  # noqa: E501

        The number of items in stock.  # noqa: E501

        :return: The stock of this MerchantProductRequest.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this MerchantProductRequest.

        The number of items in stock.  # noqa: E501

        :param stock: The stock of this MerchantProductRequest.  # noqa: E501
        :type stock: int
        """

        self._stock = stock

    @property
    def price(self):
        """Gets the price of this MerchantProductRequest.  # noqa: E501

        Price, including VAT.  # noqa: E501

        :return: The price of this MerchantProductRequest.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MerchantProductRequest.

        Price, including VAT.  # noqa: E501

        :param price: The price of this MerchantProductRequest.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def msrp(self):
        """Gets the msrp of this MerchantProductRequest.  # noqa: E501

        Manufacturer's suggested retail price.  # noqa: E501

        :return: The msrp of this MerchantProductRequest.  # noqa: E501
        :rtype: float
        """
        return self._msrp

    @msrp.setter
    def msrp(self, msrp):
        """Sets the msrp of this MerchantProductRequest.

        Manufacturer's suggested retail price.  # noqa: E501

        :param msrp: The msrp of this MerchantProductRequest.  # noqa: E501
        :type msrp: float
        """

        self._msrp = msrp

    @property
    def purchase_price(self):
        """Gets the purchase_price of this MerchantProductRequest.  # noqa: E501

        Optional. The purchase price of the product. Useful for repricing.  # noqa: E501

        :return: The purchase_price of this MerchantProductRequest.  # noqa: E501
        :rtype: float
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this MerchantProductRequest.

        Optional. The purchase price of the product. Useful for repricing.  # noqa: E501

        :param purchase_price: The purchase_price of this MerchantProductRequest.  # noqa: E501
        :type purchase_price: float
        """

        self._purchase_price = purchase_price

    @property
    def vat_rate_type(self):
        """Gets the vat_rate_type of this MerchantProductRequest.  # noqa: E501


        :return: The vat_rate_type of this MerchantProductRequest.  # noqa: E501
        :rtype: VatRateType
        """
        return self._vat_rate_type

    @vat_rate_type.setter
    def vat_rate_type(self, vat_rate_type):
        """Sets the vat_rate_type of this MerchantProductRequest.


        :param vat_rate_type: The vat_rate_type of this MerchantProductRequest.  # noqa: E501
        :type vat_rate_type: VatRateType
        """

        self._vat_rate_type = vat_rate_type

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this MerchantProductRequest.  # noqa: E501

        Shipping cost of the product.  # noqa: E501

        :return: The shipping_cost of this MerchantProductRequest.  # noqa: E501
        :rtype: float
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this MerchantProductRequest.

        Shipping cost of the product.  # noqa: E501

        :param shipping_cost: The shipping_cost of this MerchantProductRequest.  # noqa: E501
        :type shipping_cost: float
        """

        self._shipping_cost = shipping_cost

    @property
    def shipping_time(self):
        """Gets the shipping_time of this MerchantProductRequest.  # noqa: E501

        A textual representation of the shippingtime.  For example, in Dutch: 'Op werkdagen voor 22:00 uur besteld, morgen in huis'.  # noqa: E501

        :return: The shipping_time of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._shipping_time

    @shipping_time.setter
    def shipping_time(self, shipping_time):
        """Sets the shipping_time of this MerchantProductRequest.

        A textual representation of the shippingtime.  For example, in Dutch: 'Op werkdagen voor 22:00 uur besteld, morgen in huis'.  # noqa: E501

        :param shipping_time: The shipping_time of this MerchantProductRequest.  # noqa: E501
        :type shipping_time: str
        """

        self._shipping_time = shipping_time

    @property
    def url(self):
        """Gets the url of this MerchantProductRequest.  # noqa: E501

        A URL pointing to the merchant's webpage  which displays this product.  # noqa: E501

        :return: The url of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MerchantProductRequest.

        A URL pointing to the merchant's webpage  which displays this product.  # noqa: E501

        :param url: The url of this MerchantProductRequest.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def image_url(self):
        """Gets the image_url of this MerchantProductRequest.  # noqa: E501

        A URL at which an image of this product  can be found.  # noqa: E501

        :return: The image_url of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this MerchantProductRequest.

        A URL at which an image of this product  can be found.  # noqa: E501

        :param image_url: The image_url of this MerchantProductRequest.  # noqa: E501
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def extra_image_url1(self):
        """Gets the extra_image_url1 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (1).  # noqa: E501

        :return: The extra_image_url1 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url1

    @extra_image_url1.setter
    def extra_image_url1(self, extra_image_url1):
        """Sets the extra_image_url1 of this MerchantProductRequest.

        Url to an additional image of product (1).  # noqa: E501

        :param extra_image_url1: The extra_image_url1 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url1: str
        """

        self._extra_image_url1 = extra_image_url1

    @property
    def extra_image_url2(self):
        """Gets the extra_image_url2 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (2).  # noqa: E501

        :return: The extra_image_url2 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url2

    @extra_image_url2.setter
    def extra_image_url2(self, extra_image_url2):
        """Sets the extra_image_url2 of this MerchantProductRequest.

        Url to an additional image of product (2).  # noqa: E501

        :param extra_image_url2: The extra_image_url2 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url2: str
        """

        self._extra_image_url2 = extra_image_url2

    @property
    def extra_image_url3(self):
        """Gets the extra_image_url3 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (3).  # noqa: E501

        :return: The extra_image_url3 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url3

    @extra_image_url3.setter
    def extra_image_url3(self, extra_image_url3):
        """Sets the extra_image_url3 of this MerchantProductRequest.

        Url to an additional image of product (3).  # noqa: E501

        :param extra_image_url3: The extra_image_url3 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url3: str
        """

        self._extra_image_url3 = extra_image_url3

    @property
    def extra_image_url4(self):
        """Gets the extra_image_url4 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (4).  # noqa: E501

        :return: The extra_image_url4 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url4

    @extra_image_url4.setter
    def extra_image_url4(self, extra_image_url4):
        """Sets the extra_image_url4 of this MerchantProductRequest.

        Url to an additional image of product (4).  # noqa: E501

        :param extra_image_url4: The extra_image_url4 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url4: str
        """

        self._extra_image_url4 = extra_image_url4

    @property
    def extra_image_url5(self):
        """Gets the extra_image_url5 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (5).  # noqa: E501

        :return: The extra_image_url5 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url5

    @extra_image_url5.setter
    def extra_image_url5(self, extra_image_url5):
        """Sets the extra_image_url5 of this MerchantProductRequest.

        Url to an additional image of product (5).  # noqa: E501

        :param extra_image_url5: The extra_image_url5 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url5: str
        """

        self._extra_image_url5 = extra_image_url5

    @property
    def extra_image_url6(self):
        """Gets the extra_image_url6 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (6).  # noqa: E501

        :return: The extra_image_url6 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url6

    @extra_image_url6.setter
    def extra_image_url6(self, extra_image_url6):
        """Sets the extra_image_url6 of this MerchantProductRequest.

        Url to an additional image of product (6).  # noqa: E501

        :param extra_image_url6: The extra_image_url6 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url6: str
        """

        self._extra_image_url6 = extra_image_url6

    @property
    def extra_image_url7(self):
        """Gets the extra_image_url7 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (7).  # noqa: E501

        :return: The extra_image_url7 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url7

    @extra_image_url7.setter
    def extra_image_url7(self, extra_image_url7):
        """Sets the extra_image_url7 of this MerchantProductRequest.

        Url to an additional image of product (7).  # noqa: E501

        :param extra_image_url7: The extra_image_url7 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url7: str
        """

        self._extra_image_url7 = extra_image_url7

    @property
    def extra_image_url8(self):
        """Gets the extra_image_url8 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (8).  # noqa: E501

        :return: The extra_image_url8 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url8

    @extra_image_url8.setter
    def extra_image_url8(self, extra_image_url8):
        """Sets the extra_image_url8 of this MerchantProductRequest.

        Url to an additional image of product (8).  # noqa: E501

        :param extra_image_url8: The extra_image_url8 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url8: str
        """

        self._extra_image_url8 = extra_image_url8

    @property
    def extra_image_url9(self):
        """Gets the extra_image_url9 of this MerchantProductRequest.  # noqa: E501

        Url to an additional image of product (9).  # noqa: E501

        :return: The extra_image_url9 of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._extra_image_url9

    @extra_image_url9.setter
    def extra_image_url9(self, extra_image_url9):
        """Sets the extra_image_url9 of this MerchantProductRequest.

        Url to an additional image of product (9).  # noqa: E501

        :param extra_image_url9: The extra_image_url9 of this MerchantProductRequest.  # noqa: E501
        :type extra_image_url9: str
        """

        self._extra_image_url9 = extra_image_url9

    @property
    def category_trail(self):
        """Gets the category_trail of this MerchantProductRequest.  # noqa: E501

        The category to which this product belongs.  Please supply this field in the following format:  'maincategory > category > subcategory'  For example:  'vehicles > bikes > mountainbike'.  # noqa: E501

        :return: The category_trail of this MerchantProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._category_trail

    @category_trail.setter
    def category_trail(self, category_trail):
        """Sets the category_trail of this MerchantProductRequest.

        The category to which this product belongs.  Please supply this field in the following format:  'maincategory > category > subcategory'  For example:  'vehicles > bikes > mountainbike'.  # noqa: E501

        :param category_trail: The category_trail of this MerchantProductRequest.  # noqa: E501
        :type category_trail: str
        """

        self._category_trail = category_trail

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
        if not isinstance(other, MerchantProductRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MerchantProductRequest):
            return True

        return self.to_dict() != other.to_dict()
