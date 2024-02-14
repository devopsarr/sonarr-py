# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.1.929
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from typing import Optional, Set
from typing_extensions import Self

class CustomFormatResource(BaseModel):
    """
    CustomFormatResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    include_custom_format_when_renaming: Optional[StrictBool] = Field(default=None, alias="includeCustomFormatWhenRenaming")
    specifications: Optional[List[CustomFormatSpecificationSchema]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "includeCustomFormatWhenRenaming", "specifications"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CustomFormatResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in specifications (list)
        _items = []
        if self.specifications:
            for _item in self.specifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specifications'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if include_custom_format_when_renaming (nullable) is None
        # and model_fields_set contains the field
        if self.include_custom_format_when_renaming is None and "include_custom_format_when_renaming" in self.model_fields_set:
            _dict['includeCustomFormatWhenRenaming'] = None

        # set to None if specifications (nullable) is None
        # and model_fields_set contains the field
        if self.specifications is None and "specifications" in self.model_fields_set:
            _dict['specifications'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomFormatResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "includeCustomFormatWhenRenaming": obj.get("includeCustomFormatWhenRenaming"),
            "specifications": [CustomFormatSpecificationSchema.from_dict(_item) for _item in obj["specifications"]] if obj.get("specifications") is not None else None
        })
        return _obj


