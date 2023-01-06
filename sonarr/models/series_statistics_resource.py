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

class SeriesStatisticsResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    season_count: Optional[int]
    episode_file_count: Optional[int]
    episode_count: Optional[int]
    total_episode_count: Optional[int]
    size_on_disk: Optional[int]
    release_groups: Optional[List]
    percent_of_episodes: Optional[float]
    __properties = ["seasonCount", "episodeFileCount", "episodeCount", "totalEpisodeCount", "sizeOnDisk", "releaseGroups", "percentOfEpisodes"]

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
    def from_json(cls, json_str: str) -> SeriesStatisticsResource:
        """Create an instance of SeriesStatisticsResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "percent_of_episodes",
                          },
                          exclude_none=True)
        # set to None if release_groups (nullable) is None
        if self.release_groups is None:
            _dict['releaseGroups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeriesStatisticsResource:
        """Create an instance of SeriesStatisticsResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SeriesStatisticsResource.parse_obj(obj)

        _obj = SeriesStatisticsResource.parse_obj({
            "season_count": obj.get("seasonCount"),
            "episode_file_count": obj.get("episodeFileCount"),
            "episode_count": obj.get("episodeCount"),
            "total_episode_count": obj.get("totalEpisodeCount"),
            "size_on_disk": obj.get("sizeOnDisk"),
            "release_groups": obj.get("releaseGroups"),
            "percent_of_episodes": obj.get("percentOfEpisodes")
        })
        return _obj
