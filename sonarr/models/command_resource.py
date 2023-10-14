# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sonarr.models.command import Command
from sonarr.models.command_priority import CommandPriority
from sonarr.models.command_result import CommandResult
from sonarr.models.command_status import CommandStatus
from sonarr.models.command_trigger import CommandTrigger

class CommandResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    command_name: Optional[str]
    message: Optional[str]
    body: Optional[Command]
    priority: Optional[CommandPriority]
    status: Optional[CommandStatus]
    result: Optional[CommandResult]
    queued: Optional[datetime]
    started: Optional[datetime]
    ended: Optional[datetime]
    duration: Optional[str]
    exception: Optional[str]
    trigger: Optional[CommandTrigger]
    client_user_agent: Optional[str]
    state_change_time: Optional[datetime]
    send_updates_to_client: Optional[bool]
    update_scheduled_task: Optional[bool]
    last_execution_time: Optional[datetime]
    __properties = ["id", "name", "commandName", "message", "body", "priority", "status", "result", "queued", "started", "ended", "duration", "exception", "trigger", "clientUserAgent", "stateChangeTime", "sendUpdatesToClient", "updateScheduledTask", "lastExecutionTime"]

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
    def from_json(cls, json_str: str) -> CommandResource:
        """Create an instance of CommandResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of body
        if self.body:
            _dict['body'] = self.body.to_dict()
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if command_name (nullable) is None
        if self.command_name is None:
            _dict['commandName'] = None

        # set to None if message (nullable) is None
        if self.message is None:
            _dict['message'] = None

        # set to None if started (nullable) is None
        if self.started is None:
            _dict['started'] = None

        # set to None if ended (nullable) is None
        if self.ended is None:
            _dict['ended'] = None

        # set to None if exception (nullable) is None
        if self.exception is None:
            _dict['exception'] = None

        # set to None if client_user_agent (nullable) is None
        if self.client_user_agent is None:
            _dict['clientUserAgent'] = None

        # set to None if state_change_time (nullable) is None
        if self.state_change_time is None:
            _dict['stateChangeTime'] = None

        # set to None if last_execution_time (nullable) is None
        if self.last_execution_time is None:
            _dict['lastExecutionTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommandResource:
        """Create an instance of CommandResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CommandResource.parse_obj(obj)

        _obj = CommandResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "command_name": obj.get("commandName"),
            "message": obj.get("message"),
            "body": Command.from_dict(obj.get("body")) if obj.get("body") is not None else None,
            "priority": obj.get("priority"),
            "status": obj.get("status"),
            "result": obj.get("result"),
            "queued": obj.get("queued"),
            "started": obj.get("started"),
            "ended": obj.get("ended"),
            "duration": obj.get("duration"),
            "exception": obj.get("exception"),
            "trigger": obj.get("trigger"),
            "client_user_agent": obj.get("clientUserAgent"),
            "state_change_time": obj.get("stateChangeTime"),
            "send_updates_to_client": obj.get("sendUpdatesToClient"),
            "update_scheduled_task": obj.get("updateScheduledTask"),
            "last_execution_time": obj.get("lastExecutionTime")
        })
        return _obj

