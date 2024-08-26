# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.9.2244
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.apply_tags import ApplyTags
from typing import Optional, Set
from typing_extensions import Self

class IndexerBulkResource(BaseModel):
    """
    IndexerBulkResource
    """ # noqa: E501
    ids: Optional[List[StrictInt]] = None
    tags: Optional[List[StrictInt]] = None
    apply_tags: Optional[ApplyTags] = Field(default=None, alias="applyTags")
    enable_rss: Optional[StrictBool] = Field(default=None, alias="enableRss")
    enable_automatic_search: Optional[StrictBool] = Field(default=None, alias="enableAutomaticSearch")
    enable_interactive_search: Optional[StrictBool] = Field(default=None, alias="enableInteractiveSearch")
    priority: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["ids", "tags", "applyTags", "enableRss", "enableAutomaticSearch", "enableInteractiveSearch", "priority"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndexerBulkResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if enable_rss (nullable) is None
        # and model_fields_set contains the field
        if self.enable_rss is None and "enable_rss" in self.model_fields_set:
            _dict['enableRss'] = None

        # set to None if enable_automatic_search (nullable) is None
        # and model_fields_set contains the field
        if self.enable_automatic_search is None and "enable_automatic_search" in self.model_fields_set:
            _dict['enableAutomaticSearch'] = None

        # set to None if enable_interactive_search (nullable) is None
        # and model_fields_set contains the field
        if self.enable_interactive_search is None and "enable_interactive_search" in self.model_fields_set:
            _dict['enableInteractiveSearch'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndexerBulkResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ids": obj.get("ids"),
            "tags": obj.get("tags"),
            "applyTags": obj.get("applyTags"),
            "enableRss": obj.get("enableRss"),
            "enableAutomaticSearch": obj.get("enableAutomaticSearch"),
            "enableInteractiveSearch": obj.get("enableInteractiveSearch"),
            "priority": obj.get("priority")
        })
        return _obj


