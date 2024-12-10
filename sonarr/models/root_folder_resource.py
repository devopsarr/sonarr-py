# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.11.2680
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.unmapped_folder import UnmappedFolder
from typing import Optional, Set
from typing_extensions import Self

class RootFolderResource(BaseModel):
    """
    RootFolderResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    accessible: Optional[StrictBool] = None
    free_space: Optional[StrictInt] = Field(default=None, alias="freeSpace")
    unmapped_folders: Optional[List[UnmappedFolder]] = Field(default=None, alias="unmappedFolders")
    __properties: ClassVar[List[str]] = ["id", "path", "accessible", "freeSpace", "unmappedFolders"]

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
        """Create an instance of RootFolderResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in unmapped_folders (list)
        _items = []
        if self.unmapped_folders:
            for _item_unmapped_folders in self.unmapped_folders:
                if _item_unmapped_folders:
                    _items.append(_item_unmapped_folders.to_dict())
            _dict['unmappedFolders'] = _items
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if free_space (nullable) is None
        # and model_fields_set contains the field
        if self.free_space is None and "free_space" in self.model_fields_set:
            _dict['freeSpace'] = None

        # set to None if unmapped_folders (nullable) is None
        # and model_fields_set contains the field
        if self.unmapped_folders is None and "unmapped_folders" in self.model_fields_set:
            _dict['unmappedFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RootFolderResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "accessible": obj.get("accessible"),
            "freeSpace": obj.get("freeSpace"),
            "unmappedFolders": [UnmappedFolder.from_dict(_item) for _item in obj["unmappedFolders"]] if obj.get("unmappedFolders") is not None else None
        })
        return _obj


