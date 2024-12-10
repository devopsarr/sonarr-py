# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.11.2680
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from sonarr.models.episode_title_required_type import EpisodeTitleRequiredType
from sonarr.models.file_date_type import FileDateType
from sonarr.models.proper_download_types import ProperDownloadTypes
from sonarr.models.rescan_after_refresh_type import RescanAfterRefreshType
from typing import Optional, Set
from typing_extensions import Self

class MediaManagementConfigResource(BaseModel):
    """
    MediaManagementConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    auto_unmonitor_previously_downloaded_episodes: Optional[StrictBool] = Field(default=None, alias="autoUnmonitorPreviouslyDownloadedEpisodes")
    recycle_bin: Optional[StrictStr] = Field(default=None, alias="recycleBin")
    recycle_bin_cleanup_days: Optional[StrictInt] = Field(default=None, alias="recycleBinCleanupDays")
    download_propers_and_repacks: Optional[ProperDownloadTypes] = Field(default=None, alias="downloadPropersAndRepacks")
    create_empty_series_folders: Optional[StrictBool] = Field(default=None, alias="createEmptySeriesFolders")
    delete_empty_folders: Optional[StrictBool] = Field(default=None, alias="deleteEmptyFolders")
    file_date: Optional[FileDateType] = Field(default=None, alias="fileDate")
    rescan_after_refresh: Optional[RescanAfterRefreshType] = Field(default=None, alias="rescanAfterRefresh")
    set_permissions_linux: Optional[StrictBool] = Field(default=None, alias="setPermissionsLinux")
    chmod_folder: Optional[StrictStr] = Field(default=None, alias="chmodFolder")
    chown_group: Optional[StrictStr] = Field(default=None, alias="chownGroup")
    episode_title_required: Optional[EpisodeTitleRequiredType] = Field(default=None, alias="episodeTitleRequired")
    skip_free_space_check_when_importing: Optional[StrictBool] = Field(default=None, alias="skipFreeSpaceCheckWhenImporting")
    minimum_free_space_when_importing: Optional[StrictInt] = Field(default=None, alias="minimumFreeSpaceWhenImporting")
    copy_using_hardlinks: Optional[StrictBool] = Field(default=None, alias="copyUsingHardlinks")
    use_script_import: Optional[StrictBool] = Field(default=None, alias="useScriptImport")
    script_import_path: Optional[StrictStr] = Field(default=None, alias="scriptImportPath")
    import_extra_files: Optional[StrictBool] = Field(default=None, alias="importExtraFiles")
    extra_file_extensions: Optional[StrictStr] = Field(default=None, alias="extraFileExtensions")
    enable_media_info: Optional[StrictBool] = Field(default=None, alias="enableMediaInfo")
    __properties: ClassVar[List[str]] = ["id", "autoUnmonitorPreviouslyDownloadedEpisodes", "recycleBin", "recycleBinCleanupDays", "downloadPropersAndRepacks", "createEmptySeriesFolders", "deleteEmptyFolders", "fileDate", "rescanAfterRefresh", "setPermissionsLinux", "chmodFolder", "chownGroup", "episodeTitleRequired", "skipFreeSpaceCheckWhenImporting", "minimumFreeSpaceWhenImporting", "copyUsingHardlinks", "useScriptImport", "scriptImportPath", "importExtraFiles", "extraFileExtensions", "enableMediaInfo"]

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
        """Create an instance of MediaManagementConfigResource from a JSON string"""
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
        # set to None if recycle_bin (nullable) is None
        # and model_fields_set contains the field
        if self.recycle_bin is None and "recycle_bin" in self.model_fields_set:
            _dict['recycleBin'] = None

        # set to None if chmod_folder (nullable) is None
        # and model_fields_set contains the field
        if self.chmod_folder is None and "chmod_folder" in self.model_fields_set:
            _dict['chmodFolder'] = None

        # set to None if chown_group (nullable) is None
        # and model_fields_set contains the field
        if self.chown_group is None and "chown_group" in self.model_fields_set:
            _dict['chownGroup'] = None

        # set to None if script_import_path (nullable) is None
        # and model_fields_set contains the field
        if self.script_import_path is None and "script_import_path" in self.model_fields_set:
            _dict['scriptImportPath'] = None

        # set to None if extra_file_extensions (nullable) is None
        # and model_fields_set contains the field
        if self.extra_file_extensions is None and "extra_file_extensions" in self.model_fields_set:
            _dict['extraFileExtensions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaManagementConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "autoUnmonitorPreviouslyDownloadedEpisodes": obj.get("autoUnmonitorPreviouslyDownloadedEpisodes"),
            "recycleBin": obj.get("recycleBin"),
            "recycleBinCleanupDays": obj.get("recycleBinCleanupDays"),
            "downloadPropersAndRepacks": obj.get("downloadPropersAndRepacks"),
            "createEmptySeriesFolders": obj.get("createEmptySeriesFolders"),
            "deleteEmptyFolders": obj.get("deleteEmptyFolders"),
            "fileDate": obj.get("fileDate"),
            "rescanAfterRefresh": obj.get("rescanAfterRefresh"),
            "setPermissionsLinux": obj.get("setPermissionsLinux"),
            "chmodFolder": obj.get("chmodFolder"),
            "chownGroup": obj.get("chownGroup"),
            "episodeTitleRequired": obj.get("episodeTitleRequired"),
            "skipFreeSpaceCheckWhenImporting": obj.get("skipFreeSpaceCheckWhenImporting"),
            "minimumFreeSpaceWhenImporting": obj.get("minimumFreeSpaceWhenImporting"),
            "copyUsingHardlinks": obj.get("copyUsingHardlinks"),
            "useScriptImport": obj.get("useScriptImport"),
            "scriptImportPath": obj.get("scriptImportPath"),
            "importExtraFiles": obj.get("importExtraFiles"),
            "extraFileExtensions": obj.get("extraFileExtensions"),
            "enableMediaInfo": obj.get("enableMediaInfo")
        })
        return _obj


