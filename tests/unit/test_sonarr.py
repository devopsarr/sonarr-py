from unittest import TestCase
from unittest.mock import MagicMock
from devopsarr import sonarr
from devopsarr.sonarr_services import indexer_config
from devopsarr.base_services import tag
from devopsarr.adapter import Result


class TestSonarr(TestCase):
    def setUp(self) -> None:
        self.sonarr = sonarr.Client('127.0.0.1', 8989, 'test')
        self.sonarr.indexer_config._adapter = MagicMock()
        self.sonarr.tag._adapter = MagicMock()

    def test_get_tags(self):
        data = [{'id': 1, 'label': "test"}]
        self.sonarr.tag._adapter.get.return_value = Result(200, headers={}, data=data)
        tags = self.sonarr.tag.list()
        self.assertIsInstance(tags[0], tag.Tag)

    def test_get_indexer_config(self):
        data = {'minimumAge': 0, 'retention': 0, 'maximumSize': 0, 'rssSyncInterval': 15, 'id': 1}
        self.sonarr.indexer_config._adapter.get.return_value = Result(200, headers={}, data=data)
        config = self.sonarr.indexer_config.get()
        self.assertIsInstance(config, indexer_config.IndexerConfig)
