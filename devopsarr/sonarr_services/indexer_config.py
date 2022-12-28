from devopsarr.adapter import RestAdapter
from devopsarr.models import ArrModel


class IndexerConfig(ArrModel):
    maximum_size: int
    minimum_age: int
    retention: int
    rss_sync_interval: int
    id: int


class IndexerConfigClient(dict):
    base_path = '/config/indexer/'

    def __init__(self, adapter: RestAdapter):
        self._adapter = adapter
        # set default values
        self._maximum_size = 0
        self._minimum_age = 0
        self._retention = 0
        self._rss_sync_interval = 15

    # get indexer config
    def get(self) -> IndexerConfig:
        response = self._adapter.get(f'{self.base_path}')
        return IndexerConfig(**response.data)

    # update indexer config
    def update(self) -> IndexerConfig:
        config = IndexerConfig(
            maximum_size=self.maximum_size,
            minimum_age=self.minimum_age,
            retention=self.retention,
            rss_sync_interval=self.rss_sync_interval,
            id=self.id,
        )
        response = self._adapter.put(f'{self.base_path}', data=config.dict(by_alias=True))
        return IndexerConfig(**response.data)

    @property
    def maximum_size(self):
        """Retrieve maximum_size config.
        :rtype: int.
        :returns: maximum size.
        """
        return self._maximum_size

    @maximum_size.setter
    def maximum_size(self, value):
        """Set maximum_size config.
        :type value: int.
        :param value: maximum size.
        """
        self._maximum_size = value

    @property
    def minimum_age(self):
        """Retrieve minimum_age config.
        :rtype: int.
        :returns: minimum age.
        """
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, value):
        """Set minimum_age config.
        :type value: int.
        :param value: minimum age.
        """
        self._minimum_age = value

    @property
    def retention(self):
        """Retrieve retention config.
        :rtype: int.
        :returns: retention.
        """
        return self._retention

    @retention.setter
    def retention(self, value):
        """Set retention config.
        :type value: int.
        :param value: retention.
        """
        self._retention = value

    @property
    def rss_sync_interval(self):
        """Retrieve rss_sync_interval config.
        :rtype: int.
        :returns: rss sync interval.
        """
        return self._rss_sync_interval

    @rss_sync_interval.setter
    def rss_sync_interval(self, value):
        """Set rss_sync_interval config.
        :type value: int.
        :param value: rss sync interval.
        """
        self._rss_sync_interval = value

    @property
    def id(self):
        """Retrieve tag ID.
        :rtype: int.
        :returns: The indexer config ID.
        """
        return 1
