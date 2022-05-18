import requests

class YaDisk:
    
    
    HOST = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    # Создание новой папки на диске
    def create_folder(self, name_new_folder: str):
        url = f'{self.HOST}/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': name_new_folder}
        response = requests.put(url, params=params, headers=headers)
        


        # Загрузка файла на диск
    def upload(self, url_photo: str, name_folder: str, new_file: str):
        url = f'{self.HOST}/v1/disk/resources/upload/'
        headers = self.get_headers()  
        
        
        # соединяем путь, даем имя файлу на Ядиске
        file_path = f'{name_folder}/{new_file}'


        # Загрузка
        params_upload = {'path': file_path, 'url': url_photo}
        response_up = requests.post(url, params=params_upload, headers=headers)
        # if response_up.status_code == 202:
        #     print('Ваш файл загрузился')
        return response_up.status_code