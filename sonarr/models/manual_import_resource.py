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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.episode_resource import EpisodeResource
from sonarr.models.import_rejection_resource import ImportRejectionResource
from sonarr.models.language import Language
from sonarr.models.quality_model import QualityModel
from sonarr.models.release_type import ReleaseType
from sonarr.models.series_resource import SeriesResource
from typing import Optional, Set
from typing_extensions import Self

class ManualImportResource(BaseModel):
    """
    ManualImportResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    relative_path: Optional[StrictStr] = Field(default=None, alias="relativePath")
    folder_name: Optional[StrictStr] = Field(default=None, alias="folderName")
    name: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    series: Optional[SeriesResource] = None
    season_number: Optional[StrictInt] = Field(default=None, alias="seasonNumber")
    episodes: Optional[List[EpisodeResource]] = None
    episode_file_id: Optional[StrictInt] = Field(default=None, alias="episodeFileId")
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    quality: Optional[QualityModel] = None
    languages: Optional[List[Language]] = None
    quality_weight: Optional[StrictInt] = Field(default=None, alias="qualityWeight")
    download_id: Optional[StrictStr] = Field(default=None, alias="downloadId")
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    indexer_flags: Optional[StrictInt] = Field(default=None, alias="indexerFlags")
    release_type: Optional[ReleaseType] = Field(default=None, alias="releaseType")
    rejections: Optional[List[ImportRejectionResource]] = None
    __properties: ClassVar[List[str]] = ["id", "path", "relativePath", "folderName", "name", "size", "series", "seasonNumber", "episodes", "episodeFileId", "releaseGroup", "quality", "languages", "qualityWeight", "downloadId", "customFormats", "customFormatScore", "indexerFlags", "releaseType", "rejections"]

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
        """Create an instance of ManualImportResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of series
        if self.series:
            _dict['series'] = self.series.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in episodes (list)
        _items = []
        if self.episodes:
            for _item_episodes in self.episodes:
                if _item_episodes:
                    _items.append(_item_episodes.to_dict())
            _dict['episodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item_custom_formats in self.custom_formats:
                if _item_custom_formats:
                    _items.append(_item_custom_formats.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item_rejections in self.rejections:
                if _item_rejections:
                    _items.append(_item_rejections.to_dict())
            _dict['rejections'] = _items
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if relative_path (nullable) is None
        # and model_fields_set contains the field
        if self.relative_path is None and "relative_path" in self.model_fields_set:
            _dict['relativePath'] = None

        # set to None if folder_name (nullable) is None
        # and model_fields_set contains the field
        if self.folder_name is None and "folder_name" in self.model_fields_set:
            _dict['folderName'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if season_number (nullable) is None
        # and model_fields_set contains the field
        if self.season_number is None and "season_number" in self.model_fields_set:
            _dict['seasonNumber'] = None

        # set to None if episodes (nullable) is None
        # and model_fields_set contains the field
        if self.episodes is None and "episodes" in self.model_fields_set:
            _dict['episodes'] = None

        # set to None if episode_file_id (nullable) is None
        # and model_fields_set contains the field
        if self.episode_file_id is None and "episode_file_id" in self.model_fields_set:
            _dict['episodeFileId'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if download_id (nullable) is None
        # and model_fields_set contains the field
        if self.download_id is None and "download_id" in self.model_fields_set:
            _dict['downloadId'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if rejections (nullable) is None
        # and model_fields_set contains the field
        if self.rejections is None and "rejections" in self.model_fields_set:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManualImportResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "relativePath": obj.get("relativePath"),
            "folderName": obj.get("folderName"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "series": SeriesResource.from_dict(obj["series"]) if obj.get("series") is not None else None,
            "seasonNumber": obj.get("seasonNumber"),
            "episodes": [EpisodeResource.from_dict(_item) for _item in obj["episodes"]] if obj.get("episodes") is not None else None,
            "episodeFileId": obj.get("episodeFileId"),
            "releaseGroup": obj.get("releaseGroup"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "qualityWeight": obj.get("qualityWeight"),
            "downloadId": obj.get("downloadId"),
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore"),
            "indexerFlags": obj.get("indexerFlags"),
            "releaseType": obj.get("releaseType"),
            "rejections": [ImportRejectionResource.from_dict(_item) for _item in obj["rejections"]] if obj.get("rejections") is not None else None
        })
        return _obj


