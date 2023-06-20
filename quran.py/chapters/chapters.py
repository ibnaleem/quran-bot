import json, requests, html2text
from quran import QurAn

class Chapters(QurAn):
    def __init__(self):
        self.all_simples = []
        self.all_simples_order = []
        self.all_complexes = []
        self.all_complexes_order = []
        self.arabic_names = []
        self.translated_name = []
        self.mecca_simples = []
        self.mecca_complex = []
        self.madinah_simples = []
        self.madinah_complex = []
        self.translated_conversion = []
        self.chapter_id = 0
        self.arabic_name = ""
        self.revelation_place = ""
        self.revelation_order = 0
        self.verse_count = 0
        self.chapter_from_id = ""
        self.rev_ord_from_id = 0
        self.name_from_trans_name = ""
        self.chapter_from_rev_ord = ""


    def all_simple(self) -> list:
        """Returns a list of all chapter names in the Qur'An in simple notation"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                self.all_simples.append(chapter["name_simple"])

            return self.all_simples

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_simple_order(self) -> list:

        """Returns a list of all chapter names in the Qur'An in simple notation, in order"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            chapters = parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            for chapter in sorted_chapters:
                self.all_simples_order.append(chapter["name_simple"])

            return self.all_simples_order

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_complex(self) -> list:
        """Returns a list of all chapter names in the Qur'An in complex notation"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                self.all_complexes.append(chapter["name_complex"])

            return self.all_complexes

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    
    def all_complex_order(self) -> list:

        """Returns a list of all chapter names in the Qur'An, arranged in the order they were revealed, and presented in complex notation"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            chapters = parsed_data["chapters"]
            sorted_chapters = sorted(chapters, key=lambda x: x["revelation_order"])
            for chapter in sorted_chapters:
                self.all_complexes_order.append(chapter["name_complex"])

            return self.all_complexes_order

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_arabic(self) -> list:
        """Returns a list of all chapter names in the Qur'An written in Arabic"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                self.arabic_names.append(chapter["name_arabic"])

            return self.arabic_names

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_translated_names(self) -> list:
        """Returns a list of all translated chapter names in the Qur'An"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                ch = chapter["translated_name"]
                self.translated_name.append(ch["name"])

            return self.translated_name

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_mecca_simple(self) -> list:
        """Returns a list of all chapters revealed in Mecca (simple notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    self.mecca_simples.append(chapter["name_simple"])
                else:
                    pass

            return self.mecca_simples

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_mecca_complex(self) -> list:
        """Returns a list of all chapters revealed in Mecca (complex notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "makkah":
                    self.mecca_complex.append(chapter["name_complex"])
                else:
                    pass

            return self.mecca_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_madinah_simple(self) -> list:
        """Returns a list of all chapters revealed in Madinah (simple notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "madinah":
                    self.madinah_simples.append(chapter["name_simple"])
                else:
                    pass

            return self.madinah_simples

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def all_madinah_complex(self) -> list:
        """Returns a list of all chapters revealed in Madinah (complex notation)"""

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)

            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_place"] == "madinah":
                    self.madinah_complex.append(chapter["name_complex"])
                else:
                    pass

            return self.madinah_complex

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_translated_name(self, name: str) -> str:
        """Returns the translated chapter name (simple or complex name) as a string"""

        if type(name) is not str:
            raise TypeError("'Name' must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] == name or chapter["name_complex"] == name:
                    ch = chapter["translated_name"]
                    self.translated_conversion.append(ch["name"])
                else:
                    pass

            return ''.join(self.translated_conversion)

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_id(self, name: str) -> int:
        """Returns the ID of a simple or complex name as an integer"""

        if type(name) is not str:
            raise TypeError("Name must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["name_simple"] == name or chapter["name_complex"] == name:
                    return self.chapter_id + int(chapter["id"])
                else:
                    pass
        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_arabic(self, name: str) -> str:
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
                    return self.arabic_name + chapter["name_arabic"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_revelation_place(self, name: str) -> str:
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
                    return self.revelation_place + chapter["revelation_place"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_revelation_order(self, name: str) -> int:
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
                    return self.revelation_order + chapter["revelation_order"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_verse_count(self, name: str) -> int:
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
                    return self.verse_count + chapter["verses_count"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_chapter_from_id(self, id: int) -> tuple:
        """Returns the simple and complex name of a chapter from an ID as a tuple"""

        if type(id) is not int:
            raise TypeError("ID must be an integer")


        url = f'https://api.quran.com/api/v4/chapters/{id}?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)
            chapter = parsed_data["chapter"]
            return self.chapter_from_id + chapter["name_simple"], chapter["name_complex"]

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def revelation_order_from_id(self, id: int) -> int:
        """Returns the revelation order of a chapter from an ID as an integer"""

        if type(id) is not int:
            raise TypeError("ID must be an integer")

        url = f'https://api.quran.com/api/v4/chapters/{id}?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)
            chapter = parsed_data["chapter"]
            return self.rev_ord_from_id + int(chapter["revelation_order"])

        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_name_from_trans_name(self, translated_name: str) -> tuple:
        """Returns the original chapter name (simple & complex name) from translated name as a tuple"""

        if type(translated_name) is not str:
            raise TypeError("'translated_name' must be a string")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                ch = chapter["translated_name"]
                if ch["name"] == translated_name:
                    return self.name_from_trans_name + chapter["name_simple"], chapter["name_complex"]
                else:
                    pass
        else:
            print(f"The API is currently down. Response Code: {response.status_code}")

    def get_chapter_from_rev_ord(self, order: int) -> tuple:
        """Returns the chapter name (name simple & complex) that belongs to the given revelation order, as a tuple"""

        if type(order) is not int:
            raise TypeError("Order must be an integer")

        url = 'https://api.quran.com/api/v4/chapters?language=en'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            dumped_data = json.dumps(data)
            parsed_data = json.loads(dumped_data)

            for chapter in parsed_data["chapters"]:
                if chapter["revelation_order"] == order:
                    return self.chapter_from_rev_ord + chapter["name_simple"], chapter["name_complex"]
                else:
                    if order > 114:
                        print("Out of Scope Error: The Qur'An has 114 chapters, you provided an integer greater than "
                              "that")
                        break
                    elif 0 > order:
                        print("Invalid Integer: A book cannot have negative chapters, check your integer input")
                        break
                    elif order == 0:
                        print("Invalid Integer: A book cannot have zero chapters, provide an integer between 1 and "
                              "114 (Chapters in the QurAn)")
                        break
        else:
            print(f"The API is currently down. Response Code: {response.status_code}")