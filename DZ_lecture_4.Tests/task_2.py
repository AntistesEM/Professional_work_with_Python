import os

import requests


class YandexFolder:
    def __init__(self):
        self.host = "https://cloud-api.yandex.net"
        self.url = "/v1/disk/resources/"

    @staticmethod
    def get_headers(folder_):
        token_file = os.path.join(os.path.dirname(__file__), folder_)
        with open(token_file) as token:
            token = token.read()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": token,
        }
        return headers

    def add_folder(self, folder):
        response = requests.put(
            self.host + self.url,
            headers=self.get_headers("token_ya.txt"),
            params={"path": folder},
        )
        return response.status_code

    def delete_folder(self, folder):
        response = requests.delete(
            self.host + self.url,
            headers=self.get_headers("token_ya.txt"),
            params={"path": folder, "permanently": True},
        )
        return response.status_code


if __name__ == "__main__":
    folder = YandexFolder()
    print(folder.add_folder("task_2"))
    print(folder.delete_folder("task_2"))
