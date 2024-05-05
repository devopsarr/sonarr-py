# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.4.1491
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.add_series_options import AddSeriesOptions
from sonarr.models.alternate_title_resource import AlternateTitleResource
from sonarr.models.language import Language
from sonarr.models.media_cover import MediaCover
from sonarr.models.new_item_monitor_types import NewItemMonitorTypes
from sonarr.models.ratings import Ratings
from sonarr.models.season_resource import SeasonResource
from sonarr.models.series_statistics_resource import SeriesStatisticsResource
from sonarr.models.series_status_type import SeriesStatusType
from sonarr.models.series_types import SeriesTypes
from typing import Optional, Set
from typing_extensions import Self

class SeriesResource(BaseModel):
    """
    SeriesResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    alternate_titles: Optional[List[AlternateTitleResource]] = Field(default=None, alias="alternateTitles")
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    status: Optional[SeriesStatusType] = None
    ended: Optional[StrictBool] = None
    profile_name: Optional[StrictStr] = Field(default=None, alias="profileName")
    overview: Optional[StrictStr] = None
    next_airing: Optional[datetime] = Field(default=None, alias="nextAiring")
    previous_airing: Optional[datetime] = Field(default=None, alias="previousAiring")
    network: Optional[StrictStr] = None
    air_time: Optional[StrictStr] = Field(default=None, alias="airTime")
    images: Optional[List[MediaCover]] = None
    original_language: Optional[Language] = Field(default=None, alias="originalLanguage")
    remote_poster: Optional[StrictStr] = Field(default=None, alias="remotePoster")
    seasons: Optional[List[SeasonResource]] = None
    year: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    season_folder: Optional[StrictBool] = Field(default=None, alias="seasonFolder")
    monitored: Optional[StrictBool] = None
    monitor_new_items: Optional[NewItemMonitorTypes] = Field(default=None, alias="monitorNewItems")
    use_scene_numbering: Optional[StrictBool] = Field(default=None, alias="useSceneNumbering")
    runtime: Optional[StrictInt] = None
    tvdb_id: Optional[StrictInt] = Field(default=None, alias="tvdbId")
    tv_rage_id: Optional[StrictInt] = Field(default=None, alias="tvRageId")
    tv_maze_id: Optional[StrictInt] = Field(default=None, alias="tvMazeId")
    first_aired: Optional[datetime] = Field(default=None, alias="firstAired")
    last_aired: Optional[datetime] = Field(default=None, alias="lastAired")
    series_type: Optional[SeriesTypes] = Field(default=None, alias="seriesType")
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    title_slug: Optional[StrictStr] = Field(default=None, alias="titleSlug")
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    folder: Optional[StrictStr] = None
    certification: Optional[StrictStr] = None
    genres: Optional[List[StrictStr]] = None
    tags: Optional[List[StrictInt]] = None
    added: Optional[datetime] = None
    add_options: Optional[AddSeriesOptions] = Field(default=None, alias="addOptions")
    ratings: Optional[Ratings] = None
    statistics: Optional[SeriesStatisticsResource] = None
    episodes_changed: Optional[StrictBool] = Field(default=None, alias="episodesChanged")
    language_profile_id: Optional[StrictInt] = Field(default=None, alias="languageProfileId")
    __properties: ClassVar[List[str]] = ["id", "title", "alternateTitles", "sortTitle", "status", "ended", "profileName", "overview", "nextAiring", "previousAiring", "network", "airTime", "images", "originalLanguage", "remotePoster", "seasons", "year", "path", "qualityProfileId", "seasonFolder", "monitored", "monitorNewItems", "useSceneNumbering", "runtime", "tvdbId", "tvRageId", "tvMazeId", "firstAired", "lastAired", "seriesType", "cleanTitle", "imdbId", "titleSlug", "rootFolderPath", "folder", "certification", "genres", "tags", "added", "addOptions", "ratings", "statistics", "episodesChanged", "languageProfileId"]

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
        """Create an instance of SeriesResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "ended",
            "language_profile_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in alternate_titles (list)
        _items = []
        if self.alternate_titles:
            for _item in self.alternate_titles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alternateTitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of original_language
        if self.original_language:
            _dict['originalLanguage'] = self.original_language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in seasons (list)
        _items = []
        if self.seasons:
            for _item in self.seasons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['seasons'] = _items
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if alternate_titles (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_titles is None and "alternate_titles" in self.model_fields_set:
            _dict['alternateTitles'] = None

        # set to None if sort_title (nullable) is None
        # and model_fields_set contains the field
        if self.sort_title is None and "sort_title" in self.model_fields_set:
            _dict['sortTitle'] = None

        # set to None if profile_name (nullable) is None
        # and model_fields_set contains the field
        if self.profile_name is None and "profile_name" in self.model_fields_set:
            _dict['profileName'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if next_airing (nullable) is None
        # and model_fields_set contains the field
        if self.next_airing is None and "next_airing" in self.model_fields_set:
            _dict['nextAiring'] = None

        # set to None if previous_airing (nullable) is None
        # and model_fields_set contains the field
        if self.previous_airing is None and "previous_airing" in self.model_fields_set:
            _dict['previousAiring'] = None

        # set to None if network (nullable) is None
        # and model_fields_set contains the field
        if self.network is None and "network" in self.model_fields_set:
            _dict['network'] = None

        # set to None if air_time (nullable) is None
        # and model_fields_set contains the field
        if self.air_time is None and "air_time" in self.model_fields_set:
            _dict['airTime'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if remote_poster (nullable) is None
        # and model_fields_set contains the field
        if self.remote_poster is None and "remote_poster" in self.model_fields_set:
            _dict['remotePoster'] = None

        # set to None if seasons (nullable) is None
        # and model_fields_set contains the field
        if self.seasons is None and "seasons" in self.model_fields_set:
            _dict['seasons'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if first_aired (nullable) is None
        # and model_fields_set contains the field
        if self.first_aired is None and "first_aired" in self.model_fields_set:
            _dict['firstAired'] = None

        # set to None if last_aired (nullable) is None
        # and model_fields_set contains the field
        if self.last_aired is None and "last_aired" in self.model_fields_set:
            _dict['lastAired'] = None

        # set to None if clean_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_title is None and "clean_title" in self.model_fields_set:
            _dict['cleanTitle'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdbId'] = None

        # set to None if title_slug (nullable) is None
        # and model_fields_set contains the field
        if self.title_slug is None and "title_slug" in self.model_fields_set:
            _dict['titleSlug'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        # set to None if folder (nullable) is None
        # and model_fields_set contains the field
        if self.folder is None and "folder" in self.model_fields_set:
            _dict['folder'] = None

        # set to None if certification (nullable) is None
        # and model_fields_set contains the field
        if self.certification is None and "certification" in self.model_fields_set:
            _dict['certification'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if episodes_changed (nullable) is None
        # and model_fields_set contains the field
        if self.episodes_changed is None and "episodes_changed" in self.model_fields_set:
            _dict['episodesChanged'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeriesResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "alternateTitles": [AlternateTitleResource.from_dict(_item) for _item in obj["alternateTitles"]] if obj.get("alternateTitles") is not None else None,
            "sortTitle": obj.get("sortTitle"),
            "status": obj.get("status"),
            "ended": obj.get("ended"),
            "profileName": obj.get("profileName"),
            "overview": obj.get("overview"),
            "nextAiring": obj.get("nextAiring"),
            "previousAiring": obj.get("previousAiring"),
            "network": obj.get("network"),
            "airTime": obj.get("airTime"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "originalLanguage": Language.from_dict(obj["originalLanguage"]) if obj.get("originalLanguage") is not None else None,
            "remotePoster": obj.get("remotePoster"),
            "seasons": [SeasonResource.from_dict(_item) for _item in obj["seasons"]] if obj.get("seasons") is not None else None,
            "year": obj.get("year"),
            "path": obj.get("path"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "seasonFolder": obj.get("seasonFolder"),
            "monitored": obj.get("monitored"),
            "monitorNewItems": obj.get("monitorNewItems"),
            "useSceneNumbering": obj.get("useSceneNumbering"),
            "runtime": obj.get("runtime"),
            "tvdbId": obj.get("tvdbId"),
            "tvRageId": obj.get("tvRageId"),
            "tvMazeId": obj.get("tvMazeId"),
            "firstAired": obj.get("firstAired"),
            "lastAired": obj.get("lastAired"),
            "seriesType": obj.get("seriesType"),
            "cleanTitle": obj.get("cleanTitle"),
            "imdbId": obj.get("imdbId"),
            "titleSlug": obj.get("titleSlug"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "folder": obj.get("folder"),
            "certification": obj.get("certification"),
            "genres": obj.get("genres"),
            "tags": obj.get("tags"),
            "added": obj.get("added"),
            "addOptions": AddSeriesOptions.from_dict(obj["addOptions"]) if obj.get("addOptions") is not None else None,
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "statistics": SeriesStatisticsResource.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "episodesChanged": obj.get("episodesChanged"),
            "languageProfileId": obj.get("languageProfileId")
        })
        return _obj


