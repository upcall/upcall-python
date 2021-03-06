# coding: utf-8

"""
    Upcall API

    A RESTful API (json) to manage your human-powered outbound call campaigns.

    OpenAPI spec version: 2
    Contact: support@upcall.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2007(object):
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
        'webhooks': 'list[Webhook]'
    }

    attribute_map = {
        'webhooks': 'webhooks'
    }

    def __init__(self, webhooks=None):
        """
        InlineResponse2007 - a model defined in Swagger
        """

        self._webhooks = None

        if webhooks is not None:
          self.webhooks = webhooks

    @property
    def webhooks(self):
        """
        Gets the webhooks of this InlineResponse2007.

        :return: The webhooks of this InlineResponse2007.
        :rtype: list[Webhook]
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """
        Sets the webhooks of this InlineResponse2007.

        :param webhooks: The webhooks of this InlineResponse2007.
        :type: list[Webhook]
        """

        self._webhooks = webhooks

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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
