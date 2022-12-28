import logging
from devopsarr.sonarr_services.indexer_config import IndexerConfigClient
from devopsarr.sonarr_services.system_status import SystemStatusClient
from devopsarr.base_services.tag import TagClient
from devopsarr.adapter import RestAdapter


class Client():
    def __init__(
        self,
        hostname: str,
        port: int,
        api_key: str,
        protocol: str = 'http',
        ver: str = 'v3',
        ssl_verify: bool = True,
        logger: logging.Logger = None
    ):
        adapter = RestAdapter(hostname, port, api_key, protocol, ver, ssl_verify, logger)
        self.tag = TagClient(adapter)
        self.system_status = SystemStatusClient(adapter)
        self.indexer_config = IndexerConfigClient(adapter)
