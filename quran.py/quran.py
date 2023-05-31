import requests
import json
import html2text
import string

"""THIS IS THE SIMPLIFIED VERSION OF MY QURAN.PY PACKAGE; SEE IBNALEEM/QURAN.PY FOR THE FULL PACKAGE"""

class Chapters:
    def __init__(self):
        self.__version__ = 1.0

    def all_complex_order(self):

        """Returns a list of all chapter names in the QurAn in complex notation, in order"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            name_complex = []
            chapters = parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            for chapter in sorted_chapters:
                name_complex.append(chapter["name_complex"])

            return name_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_arabic(self):
        """Returns a list of all chapter names in the QurAn in Arabic"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            name_arabic = []
            for chapter in parsed_data["chapters"]:
                name_arabic.append(chapter["name_arabic"])

            return name_arabic

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")