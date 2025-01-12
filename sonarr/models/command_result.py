# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.12.2823
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CommandResult(str, Enum):
    """
    CommandResult
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    SUCCESSFUL = 'successful'
    UNSUCCESSFUL = 'unsuccessful'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CommandResult from a JSON string"""
        return cls(json.loads(json_str))


