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
from sonarr.models.monitoring_options import MonitoringOptions
from sonarr.models.season_pass_series_resource import SeasonPassSeriesResource

class SeasonPassResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    series: Optional[List]
    monitoring_options: Optional[MonitoringOptions]
    __properties = ["series", "monitoringOptions"]

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
    def from_json(cls, json_str: str) -> SeasonPassResource:
        """Create an instance of SeasonPassResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in series (list)
        _items = []
        if self.series:
            for _item in self.series:
                if _item:
                    _items.append(_item.to_dict())
            _dict['series'] = _items
        # override the default output from pydantic by calling `to_dict()` of monitoring_options
        if self.monitoring_options:
            _dict['monitoringOptions'] = self.monitoring_options.to_dict()
        # set to None if series (nullable) is None
        if self.series is None:
            _dict['series'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeasonPassResource:
        """Create an instance of SeasonPassResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SeasonPassResource.parse_obj(obj)

        _obj = SeasonPassResource.parse_obj({
            "series": [SeasonPassSeriesResource.from_dict(_item) for _item in obj.get("series")] if obj.get("series") is not None else None,
            "monitoring_options": MonitoringOptions.from_dict(obj.get("monitoringOptions")) if obj.get("monitoringOptions") is not None else None
        })
        return _obj

