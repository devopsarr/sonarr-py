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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.language import Language
from sonarr.models.media_info_resource import MediaInfoResource
from sonarr.models.quality_model import QualityModel

class EpisodeFileResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    series_id: Optional[int]
    season_number: Optional[int]
    relative_path: Optional[str]
    path: Optional[str]
    size: Optional[int]
    date_added: Optional[datetime]
    scene_name: Optional[str]
    release_group: Optional[str]
    languages: Optional[List]
    quality: Optional[QualityModel]
    custom_formats: Optional[List]
    media_info: Optional[MediaInfoResource]
    quality_cutoff_not_met: Optional[bool]
    __properties = ["id", "seriesId", "seasonNumber", "relativePath", "path", "size", "dateAdded", "sceneName", "releaseGroup", "languages", "quality", "customFormats", "mediaInfo", "qualityCutoffNotMet"]

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
    def from_json(cls, json_str: str) -> EpisodeFileResource:
        """Create an instance of EpisodeFileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # set to None if relative_path (nullable) is None
        if self.relative_path is None:
            _dict['relativePath'] = None

        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if scene_name (nullable) is None
        if self.scene_name is None:
            _dict['sceneName'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EpisodeFileResource:
        """Create an instance of EpisodeFileResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EpisodeFileResource.parse_obj(obj)

        _obj = EpisodeFileResource.parse_obj({
            "id": obj.get("id"),
            "series_id": obj.get("seriesId"),
            "season_number": obj.get("seasonNumber"),
            "relative_path": obj.get("relativePath"),
            "path": obj.get("path"),
            "size": obj.get("size"),
            "date_added": obj.get("dateAdded"),
            "scene_name": obj.get("sceneName"),
            "release_group": obj.get("releaseGroup"),
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "media_info": MediaInfoResource.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None,
            "quality_cutoff_not_met": obj.get("qualityCutoffNotMet")
        })
        return _obj

