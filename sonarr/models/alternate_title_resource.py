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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class AlternateTitleResource(BaseModel):
    """
    AlternateTitleResource
    """ # noqa: E501
    title: Optional[StrictStr] = None
    season_number: Optional[StrictInt] = Field(default=None, alias="seasonNumber")
    scene_season_number: Optional[StrictInt] = Field(default=None, alias="sceneSeasonNumber")
    scene_origin: Optional[StrictStr] = Field(default=None, alias="sceneOrigin")
    comment: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["title", "seasonNumber", "sceneSeasonNumber", "sceneOrigin", "comment"]

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
        """Create an instance of AlternateTitleResource from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if season_number (nullable) is None
        # and model_fields_set contains the field
        if self.season_number is None and "season_number" in self.model_fields_set:
            _dict['seasonNumber'] = None

        # set to None if scene_season_number (nullable) is None
        # and model_fields_set contains the field
        if self.scene_season_number is None and "scene_season_number" in self.model_fields_set:
            _dict['sceneSeasonNumber'] = None

        # set to None if scene_origin (nullable) is None
        # and model_fields_set contains the field
        if self.scene_origin is None and "scene_origin" in self.model_fields_set:
            _dict['sceneOrigin'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlternateTitleResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "seasonNumber": obj.get("seasonNumber"),
            "sceneSeasonNumber": obj.get("sceneSeasonNumber"),
            "sceneOrigin": obj.get("sceneOrigin"),
            "comment": obj.get("comment")
        })
        return _obj


