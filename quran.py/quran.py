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

    def all_translated_names(self):
        """Returns a list of all translated names of chapters in the QurAn"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            name_translated = []
            for chapter in parsed_data["chapters"]:
                ch = chapter["translated_name"]
                name_translated.append(ch["name"])

            return name_translated

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_mecca_complex(self):
        """Returns a list of all chapters revealed in Mecca (complex notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            name_complex = []
            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    name_complex.append(chapter["name_complex"])
                else:
                    pass

            return name_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_madinah_complex(self):
        """Returns a list of all chapters revealed in Mecca (complex notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            name_complex = []
            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "madinah":
                    name_complex.append(chapter["name_complex"])
                else:
                    pass

            return name_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_translated_name(self, name: str):
        """Returns the translation of a chapter name (simple or complex name) as a string"""

        if type(name) is not str:
            raise TypeError("Name must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)

            name_translated = []
            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] == name or chapter["name_complex"] == name:
                    ch = chapter["translated_name"]
                    name_translated.append(ch["name"])
                else:
                    pass

            return ''.join(name_translated)

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_arabic(self, name: str):
        """Returns the Arabic translation of a simple or complex name as a string"""

        if type(name) is not str:
            raise TypeError("Name must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return chapter["name_arabic"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_revelation_place(self, name: str):
        """Returns the revelation place of chapter from a simple or complex name as a string"""

        if type(name) is not str:
            raise TypeError("Name must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return chapter["revelation_place"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_revelation_order(self, name: str):
        """Returns the revelation order of chapter from a simple or complex name as an integer"""

        if type(name) is not str:
            raise TypeError("Name must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return chapter["revelation_order"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")


    def get_verse_count(self, name: str):
        """Returns the number of verses in a given chapter from a simple or complex name as an integer"""

        if type(name) is not str:
            raise TypeError("Name must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] or chapter["name_complex"] == name:
                    return chapter["verses_count"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")
