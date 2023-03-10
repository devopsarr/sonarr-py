# coding: utf-8

"""
    Sonarr

    Sonarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel
from sonarr.models.unmapped_folder import UnmappedFolder

class RootFolderResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    accessible: Optional[bool]
    free_space: Optional[int]
    unmapped_folders: Optional[List]
    __properties = ["id", "path", "accessible", "freeSpace", "unmappedFolders"]

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
    def from_json(cls, json_str: str) -> RootFolderResource:
        """Create an instance of RootFolderResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in unmapped_folders (list)
        _items = []
        if self.unmapped_folders:
            for _item in self.unmapped_folders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['unmappedFolders'] = _items
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if free_space (nullable) is None
        if self.free_space is None:
            _dict['freeSpace'] = None

        # set to None if unmapped_folders (nullable) is None
        if self.unmapped_folders is None:
            _dict['unmappedFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RootFolderResource:
        """Create an instance of RootFolderResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RootFolderResource.parse_obj(obj)

        _obj = RootFolderResource.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "accessible": obj.get("accessible"),
            "free_space": obj.get("freeSpace"),
            "unmapped_folders": [UnmappedFolder.from_dict(_item) for _item in obj.get("unmappedFolders")] if obj.get("unmappedFolders") is not None else None
        })
        return _obj

