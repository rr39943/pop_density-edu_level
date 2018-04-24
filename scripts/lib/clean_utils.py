import os
import json
import re
import unicodedata

class cleanUtils:
    """
    Class used to clean datafames. Tables used to clean data are json files
    located at the same folder (for example "abbreviated_cantons.json").
    """

    # Set class variables to use local files
    module_file = os.path.abspath(__file__)
    module_dir = os.path.dirname(module_file)


    @classmethod
    def _read_json(cls, file_name):
        """
        Return object from a local json file.
        """

        json_file = os.path.join(cls.module_dir, file_name)

        with open(json_file, 'r', encoding='utf8') as f:
            return json.load(f)


    @classmethod
    def canton_name_to_abbreviation(cls, canton_name):
        """
        Return the abbreviated form of the canton name.
        """
        if not(hasattr(cls, 'cantons')):
            cls.cantons = cls._read_json('abbreviated_cantons.json')

        # Remove parentheses and useless spaces
        canton_name = cls.normalize_txt(re.split(r'[(/]', canton_name)[0].strip())
        return cls.cantons[canton_name]

    @staticmethod
    def normalize_txt(txt):
        """
        Remove accents et set in lower case.
        """
        return unicodedata.normalize('NFD', txt).encode('ascii', 'ignore').decode('utf-8', 'ignoree').lower()

    @staticmethod
    def convert_ha_to_km2(nb):
        """
        Convert hectares to square kilometers.
        """
        return nb / 100
