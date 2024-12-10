# coding: utf-8

# flake8: noqa
"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.11.2680
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
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
from sonarr.models.contract_field import ContractField
from sonarr.models.custom_filter_resource import CustomFilterResource
from sonarr.models.custom_format_bulk_resource import CustomFormatBulkResource
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
from sonarr.models.file_date_type import FileDateType
from sonarr.models.health_check_result import HealthCheckResult
from sonarr.models.health_resource import HealthResource
from sonarr.models.history_resource import HistoryResource
from sonarr.models.history_resource_paging_resource import HistoryResourcePagingResource
from sonarr.models.host_config_resource import HostConfigResource
from sonarr.models.import_list_bulk_resource import ImportListBulkResource
from sonarr.models.import_list_config_resource import ImportListConfigResource
from sonarr.models.import_list_exclusion_bulk_resource import ImportListExclusionBulkResource
from sonarr.models.import_list_exclusion_resource import ImportListExclusionResource
from sonarr.models.import_list_exclusion_resource_paging_resource import ImportListExclusionResourcePagingResource
from sonarr.models.import_list_resource import ImportListResource
from sonarr.models.import_list_type import ImportListType
from sonarr.models.indexer_bulk_resource import IndexerBulkResource
from sonarr.models.indexer_config_resource import IndexerConfigResource
from sonarr.models.indexer_flag_resource import IndexerFlagResource
from sonarr.models.indexer_resource import IndexerResource
from sonarr.models.language import Language
from sonarr.models.language_profile_item_resource import LanguageProfileItemResource
from sonarr.models.language_profile_resource import LanguageProfileResource
from sonarr.models.language_resource import LanguageResource
from sonarr.models.list_sync_level_type import ListSyncLevelType
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
from sonarr.models.quality_definition_limits_resource import QualityDefinitionLimitsResource
from sonarr.models.quality_definition_resource import QualityDefinitionResource
from sonarr.models.quality_model import QualityModel
from sonarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from sonarr.models.quality_profile_resource import QualityProfileResource
from sonarr.models.quality_source import QualitySource
from sonarr.models.queue_bulk_resource import QueueBulkResource
from sonarr.models.queue_resource import QueueResource
from sonarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from sonarr.models.queue_status import QueueStatus
from sonarr.models.queue_status_resource import QueueStatusResource
from sonarr.models.ratings import Ratings
from sonarr.models.rejection import Rejection
from sonarr.models.rejection_type import RejectionType
from sonarr.models.release_episode_resource import ReleaseEpisodeResource
from sonarr.models.release_profile_resource import ReleaseProfileResource
from sonarr.models.release_resource import ReleaseResource
from sonarr.models.release_type import ReleaseType
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
