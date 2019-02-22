from secset_replacer.replacer import Replacer
from secset_replacer.finder import FileResourceFinder
from pprint import pprint as pp
from pathlib import Path

f = open("settings.json", "rt")
settings_str = f.read()

replacer = Replacer(FileResourceFinder(Path("secrets").absolute()))

filled_settings_dict = replacer.get_filled_dict(settings_str)

pp(filled_settings_dict)

#Prints
"""
{'data': 'SOME_SECRET_VALUE',
 'meta': {'dataType': {'id': 'int', 'name': 'SOME_OTHER_SECRET_VALUE'},
          'hierachy': {'id': 'someid', 'name': 'CSVString'},
          'sensitivityList': {'id': 'quasi',
                              'name': 'quasi',
                              'personnr': 'sensitive'}}}
"""