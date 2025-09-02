# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
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
    from sonarr.api.import_list_config_api import ImportListConfigApi
    from sonarr.api.import_list_exclusion_api import ImportListExclusionApi
    from sonarr.api.indexer_api import IndexerApi
    from sonarr.api.indexer_config_api import IndexerConfigApi
    from sonarr.api.indexer_flag_api import IndexerFlagApi
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
    from sonarr.api.series_folder_api import SeriesFolderApi
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
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
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
from sonarr.api.import_list_config_api import ImportListConfigApi
from sonarr.api.import_list_exclusion_api import ImportListExclusionApi
from sonarr.api.indexer_api import IndexerApi
from sonarr.api.indexer_config_api import IndexerConfigApi
from sonarr.api.indexer_flag_api import IndexerFlagApi
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
from sonarr.api.series_folder_api import SeriesFolderApi
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

""",
            name=__name__,
            doc=__doc__,
        )
    )
