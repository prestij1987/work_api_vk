

TOKEN = 
token = 'TOKEN'

VK_api = 58eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008
vk_token = VK_api 


class Vk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }    

    def upload(self, file_path: str):
      upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
      headers = self.get_headers()
      params = {"path": file_path, "overwrite": "true"}



class Vk_foto:
    def __init__(self, token: str):





    json-файл с информацией по файлу:

    [{
    "file_name": "34.jpg",
    "size": "z"
    }] 
