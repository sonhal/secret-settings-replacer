from unittest import TestCase
from tempfile import mkdtemp, TemporaryDirectory
from pathlib import Path

from secset_replacer.finder import FileResourceFinder


class TestFileResourceFinder(TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.filename_value_mapping = {"RESOURCE1": "SECRET1", "RESOURCE2": "SECRET2"}
        dir_path = Path(self.temp_dir.name)
        for filename, value in self.filename_value_mapping.items():
            f = dir_path.joinpath(value).open(mode="w")
            f.write(value)
            f.close()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_filled_resource(self):
        finder = FileResourceFinder(self.temp_dir.name)
        result = finder.create_filled_resource(self.filename_value_mapping)
        print(result)

    def test__fetch_resource_values(self):
        self.fail()
