# coding: utf-8

"""
    Sonarr

    Sonarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MonitorTypes(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    UNKNOWN = 'unknown'
    ALL = 'all'
    FUTURE = 'future'
    MISSING = 'missing'
    EXISTING = 'existing'
    FIRST_SEASON = 'firstSeason'
    LATEST_SEASON = 'latestSeason'
    PILOT = 'pilot'
    var_NONE = 'none'

