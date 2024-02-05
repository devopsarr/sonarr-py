# coding: utf-8

# flake8: noqa

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# x-release-please-start-version
__version__ = "0.10.0"
# x-release-please-end

# import apis into sdk package
from sonarr.api.api_info_api import ApiInfoApi
from sonarr.api.authentication_api import AuthenticationApi
from sonarr.api.auto_tagging_api import AutoTaggingApi
from sonarr.api.backup_api import BackupApi
from sonarr.api.blocklist_api import BlocklistApi
from sonarr.api.calendar_api import CalendarApi
from sonarr.api.calendar_feed_api import CalendarFeedApi
from sonarr.api.command_api import CommandApi
from sonarr.api.custom_filter_api import CustomFilterApi
from sonarr.api.custom_format_api import CustomFormatApi
from sonarr.api.cutoff_api import CutoffApi
from sonarr.api.delay_profile_api import DelayProfileApi
from sonarr.api.disk_space_api import DiskSpaceApi
from sonarr.api.download_client_api import DownloadClientApi
from sonarr.api.download_client_config_api import DownloadClientConfigApi
from sonarr.api.episode_api import EpisodeApi
from sonarr.api.episode_file_api import EpisodeFileApi
from sonarr.api.file_system_api import FileSystemApi
from sonarr.api.health_api import HealthApi
from sonarr.api.history_api import HistoryApi
from sonarr.api.host_config_api import HostConfigApi
from sonarr.api.import_list_api import ImportListApi
from sonarr.api.import_list_exclusion_api import ImportListExclusionApi
from sonarr.api.indexer_api import IndexerApi
from sonarr.api.indexer_config_api import IndexerConfigApi
from sonarr.api.language_api import LanguageApi
from sonarr.api.language_profile_api import LanguageProfileApi
from sonarr.api.language_profile_schema_api import LanguageProfileSchemaApi
from sonarr.api.localization_api import LocalizationApi
from sonarr.api.log_api import LogApi
from sonarr.api.log_file_api import LogFileApi
from sonarr.api.manual_import_api import ManualImportApi
from sonarr.api.media_cover_api import MediaCoverApi
from sonarr.api.media_management_config_api import MediaManagementConfigApi
from sonarr.api.metadata_api import MetadataApi
from sonarr.api.missing_api import MissingApi
from sonarr.api.naming_config_api import NamingConfigApi
from sonarr.api.notification_api import NotificationApi
from sonarr.api.parse_api import ParseApi
from sonarr.api.ping_api import PingApi
from sonarr.api.quality_definition_api import QualityDefinitionApi
from sonarr.api.quality_profile_api import QualityProfileApi
from sonarr.api.quality_profile_schema_api import QualityProfileSchemaApi
from sonarr.api.queue_api import QueueApi
from sonarr.api.queue_action_api import QueueActionApi
from sonarr.api.queue_details_api import QueueDetailsApi
from sonarr.api.queue_status_api import QueueStatusApi
from sonarr.api.release_api import ReleaseApi
from sonarr.api.release_profile_api import ReleaseProfileApi
from sonarr.api.release_push_api import ReleasePushApi
from sonarr.api.remote_path_mapping_api import RemotePathMappingApi
from sonarr.api.rename_episode_api import RenameEpisodeApi
from sonarr.api.root_folder_api import RootFolderApi
from sonarr.api.season_pass_api import SeasonPassApi
from sonarr.api.series_api import SeriesApi
from sonarr.api.series_editor_api import SeriesEditorApi
from sonarr.api.series_import_api import SeriesImportApi
from sonarr.api.series_lookup_api import SeriesLookupApi
from sonarr.api.static_resource_api import StaticResourceApi
from sonarr.api.system_api import SystemApi
from sonarr.api.tag_api import TagApi
from sonarr.api.tag_details_api import TagDetailsApi
from sonarr.api.task_api import TaskApi
from sonarr.api.ui_config_api import UiConfigApi
from sonarr.api.update_api import UpdateApi
from sonarr.api.update_log_file_api import UpdateLogFileApi

# import ApiClient
from sonarr.api_client import ApiClient
from sonarr.configuration import Configuration
from sonarr.exceptions import OpenApiException
from sonarr.exceptions import ApiTypeError
from sonarr.exceptions import ApiValueError
from sonarr.exceptions import ApiKeyError
from sonarr.exceptions import ApiAttributeError
from sonarr.exceptions import ApiException
# import models into sdk package
from sonarr.models.add_series_options import AddSeriesOptions
from sonarr.models.alternate_title_resource import AlternateTitleResource
from sonarr.models.apply_tags import ApplyTags
from sonarr.models.authentication_required_type import AuthenticationRequiredType
from sonarr.models.authentication_type import AuthenticationType
from sonarr.models.auto_tagging_resource import AutoTaggingResource
from sonarr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from sonarr.models.backup_resource import BackupResource
from sonarr.models.backup_type import BackupType
from sonarr.models.blocklist_bulk_resource import BlocklistBulkResource
from sonarr.models.blocklist_resource import BlocklistResource
from sonarr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from sonarr.models.certificate_validation_type import CertificateValidationType
from sonarr.models.command import Command
from sonarr.models.command_priority import CommandPriority
from sonarr.models.command_resource import CommandResource
from sonarr.models.command_result import CommandResult
from sonarr.models.command_status import CommandStatus
from sonarr.models.command_trigger import CommandTrigger
from sonarr.models.custom_filter_resource import CustomFilterResource
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from sonarr.models.database_type import DatabaseType
from sonarr.models.delay_profile_resource import DelayProfileResource
from sonarr.models.disk_space_resource import DiskSpaceResource
from sonarr.models.download_client_bulk_resource import DownloadClientBulkResource
from sonarr.models.download_client_config_resource import DownloadClientConfigResource
from sonarr.models.download_client_resource import DownloadClientResource
from sonarr.models.download_protocol import DownloadProtocol
from sonarr.models.episode_file_list_resource import EpisodeFileListResource
from sonarr.models.episode_file_resource import EpisodeFileResource
from sonarr.models.episode_history_event_type import EpisodeHistoryEventType
from sonarr.models.episode_resource import EpisodeResource
from sonarr.models.episode_resource_paging_resource import EpisodeResourcePagingResource
from sonarr.models.episode_title_required_type import EpisodeTitleRequiredType
from sonarr.models.episodes_monitored_resource import EpisodesMonitoredResource
from sonarr.models.field import Field
from sonarr.models.file_date_type import FileDateType
from sonarr.models.health_check_result import HealthCheckResult
from sonarr.models.health_resource import HealthResource
from sonarr.models.history_resource import HistoryResource
from sonarr.models.history_resource_paging_resource import HistoryResourcePagingResource
from sonarr.models.host_config_resource import HostConfigResource
from sonarr.models.import_list_bulk_resource import ImportListBulkResource
from sonarr.models.import_list_exclusion_resource import ImportListExclusionResource
from sonarr.models.import_list_resource import ImportListResource
from sonarr.models.import_list_type import ImportListType
from sonarr.models.indexer_bulk_resource import IndexerBulkResource
from sonarr.models.indexer_config_resource import IndexerConfigResource
from sonarr.models.indexer_resource import IndexerResource
from sonarr.models.language import Language
from sonarr.models.language_profile_item_resource import LanguageProfileItemResource
from sonarr.models.language_profile_resource import LanguageProfileResource
from sonarr.models.language_resource import LanguageResource
from sonarr.models.localization_language_resource import LocalizationLanguageResource
from sonarr.models.localization_resource import LocalizationResource
from sonarr.models.log_file_resource import LogFileResource
from sonarr.models.log_resource import LogResource
from sonarr.models.log_resource_paging_resource import LogResourcePagingResource
from sonarr.models.manual_import_reprocess_resource import ManualImportReprocessResource
from sonarr.models.manual_import_resource import ManualImportResource
from sonarr.models.media_cover import MediaCover
from sonarr.models.media_cover_types import MediaCoverTypes
from sonarr.models.media_info_resource import MediaInfoResource
from sonarr.models.media_management_config_resource import MediaManagementConfigResource
from sonarr.models.metadata_resource import MetadataResource
from sonarr.models.monitor_types import MonitorTypes
from sonarr.models.monitoring_options import MonitoringOptions
from sonarr.models.naming_config_resource import NamingConfigResource
from sonarr.models.new_item_monitor_types import NewItemMonitorTypes
from sonarr.models.notification_resource import NotificationResource
from sonarr.models.parse_resource import ParseResource
from sonarr.models.parsed_episode_info import ParsedEpisodeInfo
from sonarr.models.ping_resource import PingResource
from sonarr.models.privacy_level import PrivacyLevel
from sonarr.models.profile_format_item_resource import ProfileFormatItemResource
from sonarr.models.proper_download_types import ProperDownloadTypes
from sonarr.models.provider_message import ProviderMessage
from sonarr.models.provider_message_type import ProviderMessageType
from sonarr.models.proxy_type import ProxyType
from sonarr.models.quality import Quality
from sonarr.models.quality_definition_resource import QualityDefinitionResource
from sonarr.models.quality_model import QualityModel
from sonarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from sonarr.models.quality_profile_resource import QualityProfileResource
from sonarr.models.quality_source import QualitySource
from sonarr.models.queue_bulk_resource import QueueBulkResource
from sonarr.models.queue_resource import QueueResource
from sonarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from sonarr.models.queue_status_resource import QueueStatusResource
from sonarr.models.ratings import Ratings
from sonarr.models.rejection import Rejection
from sonarr.models.rejection_type import RejectionType
from sonarr.models.release_episode_resource import ReleaseEpisodeResource
from sonarr.models.release_profile_resource import ReleaseProfileResource
from sonarr.models.release_resource import ReleaseResource
from sonarr.models.remote_path_mapping_resource import RemotePathMappingResource
from sonarr.models.rename_episode_resource import RenameEpisodeResource
from sonarr.models.rescan_after_refresh_type import RescanAfterRefreshType
from sonarr.models.revision import Revision
from sonarr.models.root_folder_resource import RootFolderResource
from sonarr.models.runtime_mode import RuntimeMode
from sonarr.models.season_pass_resource import SeasonPassResource
from sonarr.models.season_pass_series_resource import SeasonPassSeriesResource
from sonarr.models.season_resource import SeasonResource
from sonarr.models.season_statistics_resource import SeasonStatisticsResource
from sonarr.models.select_option import SelectOption
from sonarr.models.series_editor_resource import SeriesEditorResource
from sonarr.models.series_resource import SeriesResource
from sonarr.models.series_statistics_resource import SeriesStatisticsResource
from sonarr.models.series_status_type import SeriesStatusType
from sonarr.models.series_title_info import SeriesTitleInfo
from sonarr.models.series_types import SeriesTypes
from sonarr.models.sort_direction import SortDirection
from sonarr.models.system_resource import SystemResource
from sonarr.models.tag_details_resource import TagDetailsResource
from sonarr.models.tag_resource import TagResource
from sonarr.models.task_resource import TaskResource
from sonarr.models.tracked_download_state import TrackedDownloadState
from sonarr.models.tracked_download_status import TrackedDownloadStatus
from sonarr.models.tracked_download_status_message import TrackedDownloadStatusMessage
from sonarr.models.ui_config_resource import UiConfigResource
from sonarr.models.unmapped_folder import UnmappedFolder
from sonarr.models.update_changes import UpdateChanges
from sonarr.models.update_mechanism import UpdateMechanism
from sonarr.models.update_resource import UpdateResource
