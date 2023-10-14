# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from sonarr.models.apply_tags import ApplyTags

class ImportListBulkResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    ids: Optional[List]
    tags: Optional[List]
    apply_tags: Optional[ApplyTags]
    enable_automatic_add: Optional[bool]
    root_folder_path: Optional[str]
    quality_profile_id: Optional[int]
    __properties = ["ids", "tags", "applyTags", "enableAutomaticAdd", "rootFolderPath", "qualityProfileId"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ImportListBulkResource:
        """Create an instance of ImportListBulkResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if ids (nullable) is None
        if self.ids is None:
            _dict['ids'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        # set to None if enable_automatic_add (nullable) is None
        if self.enable_automatic_add is None:
            _dict['enableAutomaticAdd'] = None

        # set to None if root_folder_path (nullable) is None
        if self.root_folder_path is None:
            _dict['rootFolderPath'] = None

        # set to None if quality_profile_id (nullable) is None
        if self.quality_profile_id is None:
            _dict['qualityProfileId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImportListBulkResource:
        """Create an instance of ImportListBulkResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ImportListBulkResource.parse_obj(obj)

        _obj = ImportListBulkResource.parse_obj({
            "ids": obj.get("ids"),
            "tags": obj.get("tags"),
            "apply_tags": obj.get("applyTags"),
            "enable_automatic_add": obj.get("enableAutomaticAdd"),
            "root_folder_path": obj.get("rootFolderPath"),
            "quality_profile_id": obj.get("qualityProfileId")
        })
        return _obj

