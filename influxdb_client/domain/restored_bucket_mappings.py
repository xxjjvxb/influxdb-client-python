# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RestoredBucketMappings(object):
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
        'id': 'str',
        'name': 'str',
        'shard_mappings': 'list[BucketShardMapping]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'shard_mappings': 'shardMappings'
    }

    def __init__(self, id=None, name=None, shard_mappings=None):  # noqa: E501,D401,D403
        """RestoredBucketMappings - a model defined in OpenAPI."""  # noqa: E501
        self._id = None
        self._name = None
        self._shard_mappings = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.shard_mappings = shard_mappings

    @property
    def id(self):
        """Get the id of this RestoredBucketMappings.

        New ID of the restored bucket

        :return: The id of this RestoredBucketMappings.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this RestoredBucketMappings.

        New ID of the restored bucket

        :param id: The id of this RestoredBucketMappings.
        :type: str
        """  # noqa: E501
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id

    @property
    def name(self):
        """Get the name of this RestoredBucketMappings.

        :return: The name of this RestoredBucketMappings.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this RestoredBucketMappings.

        :param name: The name of this RestoredBucketMappings.
        :type: str
        """  # noqa: E501
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def shard_mappings(self):
        """Get the shard_mappings of this RestoredBucketMappings.

        :return: The shard_mappings of this RestoredBucketMappings.
        :rtype: list[BucketShardMapping]
        """  # noqa: E501
        return self._shard_mappings

    @shard_mappings.setter
    def shard_mappings(self, shard_mappings):
        """Set the shard_mappings of this RestoredBucketMappings.

        :param shard_mappings: The shard_mappings of this RestoredBucketMappings.
        :type: list[BucketShardMapping]
        """  # noqa: E501
        if shard_mappings is None:
            raise ValueError("Invalid value for `shard_mappings`, must not be `None`")  # noqa: E501
        self._shard_mappings = shard_mappings

    def to_dict(self):
        """Return the model properties as a dict."""
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, RestoredBucketMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other