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
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.episode_resource import EpisodeResource
from sonarr.models.language import Language
from sonarr.models.quality_model import QualityModel
from sonarr.models.rejection import Rejection
from sonarr.models.series_resource import SeriesResource

class ManualImportResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    relative_path: Optional[str]
    folder_name: Optional[str]
    name: Optional[str]
    size: Optional[int]
    series: Optional[SeriesResource]
    season_number: Optional[int]
    episodes: Optional[List]
    episode_file_id: Optional[int]
    release_group: Optional[str]
    quality: Optional[QualityModel]
    languages: Optional[List]
    quality_weight: Optional[int]
    download_id: Optional[str]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    rejections: Optional[List]
    __properties = ["id", "path", "relativePath", "folderName", "name", "size", "series", "seasonNumber", "episodes", "episodeFileId", "releaseGroup", "quality", "languages", "qualityWeight", "downloadId", "customFormats", "customFormatScore", "rejections"]

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
    def from_json(cls, json_str: str) -> ManualImportResource:
        """Create an instance of ManualImportResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of series
        if self.series:
            _dict['series'] = self.series.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in episodes (list)
        _items = []
        if self.episodes:
            for _item in self.episodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['episodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item in self.rejections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rejections'] = _items
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if relative_path (nullable) is None
        if self.relative_path is None:
            _dict['relativePath'] = None

        # set to None if folder_name (nullable) is None
        if self.folder_name is None:
            _dict['folderName'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if season_number (nullable) is None
        if self.season_number is None:
            _dict['seasonNumber'] = None

        # set to None if episodes (nullable) is None
        if self.episodes is None:
            _dict['episodes'] = None

        # set to None if episode_file_id (nullable) is None
        if self.episode_file_id is None:
            _dict['episodeFileId'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualImportResource:
        """Create an instance of ManualImportResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ManualImportResource.parse_obj(obj)

        _obj = ManualImportResource.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "relative_path": obj.get("relativePath"),
            "folder_name": obj.get("folderName"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "series": SeriesResource.from_dict(obj.get("series")) if obj.get("series") is not None else None,
            "season_number": obj.get("seasonNumber"),
            "episodes": [EpisodeResource.from_dict(_item) for _item in obj.get("episodes")] if obj.get("episodes") is not None else None,
            "episode_file_id": obj.get("episodeFileId"),
            "release_group": obj.get("releaseGroup"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "quality_weight": obj.get("qualityWeight"),
            "download_id": obj.get("downloadId"),
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore"),
            "rejections": [Rejection.from_dict(_item) for _item in obj.get("rejections")] if obj.get("rejections") is not None else None
        })
        return _obj

