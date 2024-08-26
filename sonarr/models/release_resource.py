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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from sonarr.models.alternate_title_resource import AlternateTitleResource
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.download_protocol import DownloadProtocol
from sonarr.models.language import Language
from sonarr.models.quality_model import QualityModel
from sonarr.models.release_episode_resource import ReleaseEpisodeResource
from typing import Optional, Set
from typing_extensions import Self

class ReleaseResource(BaseModel):
    """
    ReleaseResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    guid: Optional[StrictStr] = None
    quality: Optional[QualityModel] = None
    quality_weight: Optional[StrictInt] = Field(default=None, alias="qualityWeight")
    age: Optional[StrictInt] = None
    age_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageHours")
    age_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageMinutes")
    size: Optional[StrictInt] = None
    indexer_id: Optional[StrictInt] = Field(default=None, alias="indexerId")
    indexer: Optional[StrictStr] = None
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    sub_group: Optional[StrictStr] = Field(default=None, alias="subGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    title: Optional[StrictStr] = None
    full_season: Optional[StrictBool] = Field(default=None, alias="fullSeason")
    scene_source: Optional[StrictBool] = Field(default=None, alias="sceneSource")
    season_number: Optional[StrictInt] = Field(default=None, alias="seasonNumber")
    languages: Optional[List[Language]] = None
    language_weight: Optional[StrictInt] = Field(default=None, alias="languageWeight")
    air_date: Optional[StrictStr] = Field(default=None, alias="airDate")
    series_title: Optional[StrictStr] = Field(default=None, alias="seriesTitle")
    episode_numbers: Optional[List[StrictInt]] = Field(default=None, alias="episodeNumbers")
    absolute_episode_numbers: Optional[List[StrictInt]] = Field(default=None, alias="absoluteEpisodeNumbers")
    mapped_season_number: Optional[StrictInt] = Field(default=None, alias="mappedSeasonNumber")
    mapped_episode_numbers: Optional[List[StrictInt]] = Field(default=None, alias="mappedEpisodeNumbers")
    mapped_absolute_episode_numbers: Optional[List[StrictInt]] = Field(default=None, alias="mappedAbsoluteEpisodeNumbers")
    mapped_series_id: Optional[StrictInt] = Field(default=None, alias="mappedSeriesId")
    mapped_episode_info: Optional[List[ReleaseEpisodeResource]] = Field(default=None, alias="mappedEpisodeInfo")
    approved: Optional[StrictBool] = None
    temporarily_rejected: Optional[StrictBool] = Field(default=None, alias="temporarilyRejected")
    rejected: Optional[StrictBool] = None
    tvdb_id: Optional[StrictInt] = Field(default=None, alias="tvdbId")
    tv_rage_id: Optional[StrictInt] = Field(default=None, alias="tvRageId")
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    rejections: Optional[List[StrictStr]] = None
    publish_date: Optional[datetime] = Field(default=None, alias="publishDate")
    comment_url: Optional[StrictStr] = Field(default=None, alias="commentUrl")
    download_url: Optional[StrictStr] = Field(default=None, alias="downloadUrl")
    info_url: Optional[StrictStr] = Field(default=None, alias="infoUrl")
    episode_requested: Optional[StrictBool] = Field(default=None, alias="episodeRequested")
    download_allowed: Optional[StrictBool] = Field(default=None, alias="downloadAllowed")
    release_weight: Optional[StrictInt] = Field(default=None, alias="releaseWeight")
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    scene_mapping: Optional[AlternateTitleResource] = Field(default=None, alias="sceneMapping")
    magnet_url: Optional[StrictStr] = Field(default=None, alias="magnetUrl")
    info_hash: Optional[StrictStr] = Field(default=None, alias="infoHash")
    seeders: Optional[StrictInt] = None
    leechers: Optional[StrictInt] = None
    protocol: Optional[DownloadProtocol] = None
    indexer_flags: Optional[StrictInt] = Field(default=None, alias="indexerFlags")
    is_daily: Optional[StrictBool] = Field(default=None, alias="isDaily")
    is_absolute_numbering: Optional[StrictBool] = Field(default=None, alias="isAbsoluteNumbering")
    is_possible_special_episode: Optional[StrictBool] = Field(default=None, alias="isPossibleSpecialEpisode")
    special: Optional[StrictBool] = None
    series_id: Optional[StrictInt] = Field(default=None, alias="seriesId")
    episode_id: Optional[StrictInt] = Field(default=None, alias="episodeId")
    episode_ids: Optional[List[StrictInt]] = Field(default=None, alias="episodeIds")
    download_client_id: Optional[StrictInt] = Field(default=None, alias="downloadClientId")
    download_client: Optional[StrictStr] = Field(default=None, alias="downloadClient")
    should_override: Optional[StrictBool] = Field(default=None, alias="shouldOverride")
    __properties: ClassVar[List[str]] = ["id", "guid", "quality", "qualityWeight", "age", "ageHours", "ageMinutes", "size", "indexerId", "indexer", "releaseGroup", "subGroup", "releaseHash", "title", "fullSeason", "sceneSource", "seasonNumber", "languages", "languageWeight", "airDate", "seriesTitle", "episodeNumbers", "absoluteEpisodeNumbers", "mappedSeasonNumber", "mappedEpisodeNumbers", "mappedAbsoluteEpisodeNumbers", "mappedSeriesId", "mappedEpisodeInfo", "approved", "temporarilyRejected", "rejected", "tvdbId", "tvRageId", "imdbId", "rejections", "publishDate", "commentUrl", "downloadUrl", "infoUrl", "episodeRequested", "downloadAllowed", "releaseWeight", "customFormats", "customFormatScore", "sceneMapping", "magnetUrl", "infoHash", "seeders", "leechers", "protocol", "indexerFlags", "isDaily", "isAbsoluteNumbering", "isPossibleSpecialEpisode", "special", "seriesId", "episodeId", "episodeIds", "downloadClientId", "downloadClient", "shouldOverride"]

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
        """Create an instance of ReleaseResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mapped_episode_info (list)
        _items = []
        if self.mapped_episode_info:
            for _item_mapped_episode_info in self.mapped_episode_info:
                if _item_mapped_episode_info:
                    _items.append(_item_mapped_episode_info.to_dict())
            _dict['mappedEpisodeInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item_custom_formats in self.custom_formats:
                if _item_custom_formats:
                    _items.append(_item_custom_formats.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of scene_mapping
        if self.scene_mapping:
            _dict['sceneMapping'] = self.scene_mapping.to_dict()
        # set to None if guid (nullable) is None
        # and model_fields_set contains the field
        if self.guid is None and "guid" in self.model_fields_set:
            _dict['guid'] = None

        # set to None if indexer (nullable) is None
        # and model_fields_set contains the field
        if self.indexer is None and "indexer" in self.model_fields_set:
            _dict['indexer'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if sub_group (nullable) is None
        # and model_fields_set contains the field
        if self.sub_group is None and "sub_group" in self.model_fields_set:
            _dict['subGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if air_date (nullable) is None
        # and model_fields_set contains the field
        if self.air_date is None and "air_date" in self.model_fields_set:
            _dict['airDate'] = None

        # set to None if series_title (nullable) is None
        # and model_fields_set contains the field
        if self.series_title is None and "series_title" in self.model_fields_set:
            _dict['seriesTitle'] = None

        # set to None if episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.episode_numbers is None and "episode_numbers" in self.model_fields_set:
            _dict['episodeNumbers'] = None

        # set to None if absolute_episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.absolute_episode_numbers is None and "absolute_episode_numbers" in self.model_fields_set:
            _dict['absoluteEpisodeNumbers'] = None

        # set to None if mapped_season_number (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_season_number is None and "mapped_season_number" in self.model_fields_set:
            _dict['mappedSeasonNumber'] = None

        # set to None if mapped_episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_episode_numbers is None and "mapped_episode_numbers" in self.model_fields_set:
            _dict['mappedEpisodeNumbers'] = None

        # set to None if mapped_absolute_episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_absolute_episode_numbers is None and "mapped_absolute_episode_numbers" in self.model_fields_set:
            _dict['mappedAbsoluteEpisodeNumbers'] = None

        # set to None if mapped_series_id (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_series_id is None and "mapped_series_id" in self.model_fields_set:
            _dict['mappedSeriesId'] = None

        # set to None if mapped_episode_info (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_episode_info is None and "mapped_episode_info" in self.model_fields_set:
            _dict['mappedEpisodeInfo'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdbId'] = None

        # set to None if rejections (nullable) is None
        # and model_fields_set contains the field
        if self.rejections is None and "rejections" in self.model_fields_set:
            _dict['rejections'] = None

        # set to None if comment_url (nullable) is None
        # and model_fields_set contains the field
        if self.comment_url is None and "comment_url" in self.model_fields_set:
            _dict['commentUrl'] = None

        # set to None if download_url (nullable) is None
        # and model_fields_set contains the field
        if self.download_url is None and "download_url" in self.model_fields_set:
            _dict['downloadUrl'] = None

        # set to None if info_url (nullable) is None
        # and model_fields_set contains the field
        if self.info_url is None and "info_url" in self.model_fields_set:
            _dict['infoUrl'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if magnet_url (nullable) is None
        # and model_fields_set contains the field
        if self.magnet_url is None and "magnet_url" in self.model_fields_set:
            _dict['magnetUrl'] = None

        # set to None if info_hash (nullable) is None
        # and model_fields_set contains the field
        if self.info_hash is None and "info_hash" in self.model_fields_set:
            _dict['infoHash'] = None

        # set to None if seeders (nullable) is None
        # and model_fields_set contains the field
        if self.seeders is None and "seeders" in self.model_fields_set:
            _dict['seeders'] = None

        # set to None if leechers (nullable) is None
        # and model_fields_set contains the field
        if self.leechers is None and "leechers" in self.model_fields_set:
            _dict['leechers'] = None

        # set to None if series_id (nullable) is None
        # and model_fields_set contains the field
        if self.series_id is None and "series_id" in self.model_fields_set:
            _dict['seriesId'] = None

        # set to None if episode_id (nullable) is None
        # and model_fields_set contains the field
        if self.episode_id is None and "episode_id" in self.model_fields_set:
            _dict['episodeId'] = None

        # set to None if episode_ids (nullable) is None
        # and model_fields_set contains the field
        if self.episode_ids is None and "episode_ids" in self.model_fields_set:
            _dict['episodeIds'] = None

        # set to None if download_client_id (nullable) is None
        # and model_fields_set contains the field
        if self.download_client_id is None and "download_client_id" in self.model_fields_set:
            _dict['downloadClientId'] = None

        # set to None if download_client (nullable) is None
        # and model_fields_set contains the field
        if self.download_client is None and "download_client" in self.model_fields_set:
            _dict['downloadClient'] = None

        # set to None if should_override (nullable) is None
        # and model_fields_set contains the field
        if self.should_override is None and "should_override" in self.model_fields_set:
            _dict['shouldOverride'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReleaseResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "guid": obj.get("guid"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "qualityWeight": obj.get("qualityWeight"),
            "age": obj.get("age"),
            "ageHours": obj.get("ageHours"),
            "ageMinutes": obj.get("ageMinutes"),
            "size": obj.get("size"),
            "indexerId": obj.get("indexerId"),
            "indexer": obj.get("indexer"),
            "releaseGroup": obj.get("releaseGroup"),
            "subGroup": obj.get("subGroup"),
            "releaseHash": obj.get("releaseHash"),
            "title": obj.get("title"),
            "fullSeason": obj.get("fullSeason"),
            "sceneSource": obj.get("sceneSource"),
            "seasonNumber": obj.get("seasonNumber"),
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "languageWeight": obj.get("languageWeight"),
            "airDate": obj.get("airDate"),
            "seriesTitle": obj.get("seriesTitle"),
            "episodeNumbers": obj.get("episodeNumbers"),
            "absoluteEpisodeNumbers": obj.get("absoluteEpisodeNumbers"),
            "mappedSeasonNumber": obj.get("mappedSeasonNumber"),
            "mappedEpisodeNumbers": obj.get("mappedEpisodeNumbers"),
            "mappedAbsoluteEpisodeNumbers": obj.get("mappedAbsoluteEpisodeNumbers"),
            "mappedSeriesId": obj.get("mappedSeriesId"),
            "mappedEpisodeInfo": [ReleaseEpisodeResource.from_dict(_item) for _item in obj["mappedEpisodeInfo"]] if obj.get("mappedEpisodeInfo") is not None else None,
            "approved": obj.get("approved"),
            "temporarilyRejected": obj.get("temporarilyRejected"),
            "rejected": obj.get("rejected"),
            "tvdbId": obj.get("tvdbId"),
            "tvRageId": obj.get("tvRageId"),
            "imdbId": obj.get("imdbId"),
            "rejections": obj.get("rejections"),
            "publishDate": obj.get("publishDate"),
            "commentUrl": obj.get("commentUrl"),
            "downloadUrl": obj.get("downloadUrl"),
            "infoUrl": obj.get("infoUrl"),
            "episodeRequested": obj.get("episodeRequested"),
            "downloadAllowed": obj.get("downloadAllowed"),
            "releaseWeight": obj.get("releaseWeight"),
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore"),
            "sceneMapping": AlternateTitleResource.from_dict(obj["sceneMapping"]) if obj.get("sceneMapping") is not None else None,
            "magnetUrl": obj.get("magnetUrl"),
            "infoHash": obj.get("infoHash"),
            "seeders": obj.get("seeders"),
            "leechers": obj.get("leechers"),
            "protocol": obj.get("protocol"),
            "indexerFlags": obj.get("indexerFlags"),
            "isDaily": obj.get("isDaily"),
            "isAbsoluteNumbering": obj.get("isAbsoluteNumbering"),
            "isPossibleSpecialEpisode": obj.get("isPossibleSpecialEpisode"),
            "special": obj.get("special"),
            "seriesId": obj.get("seriesId"),
            "episodeId": obj.get("episodeId"),
            "episodeIds": obj.get("episodeIds"),
            "downloadClientId": obj.get("downloadClientId"),
            "downloadClient": obj.get("downloadClient"),
            "shouldOverride": obj.get("shouldOverride")
        })
        return _obj


