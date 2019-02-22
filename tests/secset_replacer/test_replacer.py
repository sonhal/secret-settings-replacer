from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from secset_replacer.replacer import Replacer
from secset_replacer.finder import FileResourceFinder

class TestReplacer(TestCase):

    filename = "testfile.txt"

    filecontent = '{"data":"${REPLACE1}","meta":{"sensitivityList": {"id": "quasi", "name": "quasi", "personnr": "sensitive"},"dataType": {"id": "int", "name": "${REPLACE2}"},"hirachy": {"id": "CSVstring", "name": "CSVString"}}}'

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        dir_path = Path(self.temp_dir.name)
        f = dir_path.joinpath(self.filename).open(mode="w")
        f.write(self.filecontent)
        f.close()

        self.filename_value_mapping = {"REPLACE1": "SECRET1", "REPLACE2": "SECRET2"}
        for filename, value in self.filename_value_mapping.items():
            f = dir_path.joinpath(filename).open(mode="w")
            f.write(value)
            f.close()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_parse_tokens_run(self):
        token1 = "TOKEN1"
        token2 = "TOKEN_2"
        token3 = "_/token3"

        test_string = f"${{{token1}}} ${{{token2}}} ${{{token3}}}"
        rep = Replacer(FileResourceFinder(""))
        resultat = rep._get_tokens(test_string)

        for token in token1, token2, token3:
            self.assertIn(token, resultat)

    def test_replace(self):
        rep = Replacer(FileResourceFinder(self.temp_dir.name))
        result =rep.get_filled_dict(self.filecontent)
        print(result)

