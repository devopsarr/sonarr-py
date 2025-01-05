# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.12.2823
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from typing import Optional, Set
from typing_extensions import Self

class AutoTaggingResource(BaseModel):
    """
    AutoTaggingResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    remove_tags_automatically: Optional[StrictBool] = Field(default=None, alias="removeTagsAutomatically")
    tags: Optional[List[StrictInt]] = None
    specifications: Optional[List[AutoTaggingSpecificationSchema]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "removeTagsAutomatically", "tags", "specifications"]

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
        """Create an instance of AutoTaggingResource from a JSON string"""
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
            for _item_specifications in self.specifications:
                if _item_specifications:
                    _items.append(_item_specifications.to_dict())
            _dict['specifications'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if specifications (nullable) is None
        # and model_fields_set contains the field
        if self.specifications is None and "specifications" in self.model_fields_set:
            _dict['specifications'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoTaggingResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "removeTagsAutomatically": obj.get("removeTagsAutomatically"),
            "tags": obj.get("tags"),
            "specifications": [AutoTaggingSpecificationSchema.from_dict(_item) for _item in obj["specifications"]] if obj.get("specifications") is not None else None
        })
        return _obj


