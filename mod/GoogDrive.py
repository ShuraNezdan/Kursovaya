from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import io
import requests
import json


class GooglDrive:
    
    def __init__(self, gauth):
        self.gauth = gauth

    # Создаем папку в G Drive, на выход id папки, который используется для загрузки на диск
    def create_folder(self, new_folder_name):
        drive = GoogleDrive(self.gauth)
        
        folder_metadata = {
            'title': new_folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [{'id': 'root'}]
        }
        
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        return folder['id']

    # Загрузка данных на диск
    def upload(self, filename='', folder_id='', url=''):
        access_token = self.gauth.attr['credentials'].access_token
        metadata = {
            "name": filename,
            "parents": [folder_id]
        }

        # response.get.content возвращает содержимое в байтах
        # BytesIO загружает в память 
        files = {
            'data': ('metadata', json.dumps(metadata), 'application/json'),
            'file': io.BytesIO(requests.get(url).content)
        }
        
        response_up = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers={"Authorization": "Bearer " + access_token},
            files=files
        )
        return response_up.status_code