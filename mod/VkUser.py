import requests
from datetime import date
import mod.Addition as Add

class VkUser:

    URL_MAIN = 'http://api.vk.com/method/'
    
    # Вводим ТОКЕН
    def __init__(self, token):
        self.params = {
            'access_token': token,
            'v': '5.131'
        }

    # Возвращаем словарь с сылками на фото, лайками и т.п.
    def get_dict_photos(self, owner_id):
        url = self.URL_MAIN + 'photos.get'
        photo_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': 1,
            'photo_size': 1
        }
        response = requests.get(url, params={**self.params, **photo_params}).json()
        return response['response']['items']
    
    
    # Создать словарь, ключ это название файла, значение это ссылка на файл и буквенный тип размера файла
    def get_url_photo(self, owner_id, number):
        index = 1
        new_dict_photo = {}
        dict_photos = self.get_dict_photos(owner_id)

        for item in dict_photos:
            
            if index > number:    # Проверка на колличество нужных ссылок для закачки
                break
            
            max_heigth = 1
            url_max_size = ''
            type_max_size = ''
            
            # Находим самое большое фото, так сделано потому что они находятся не порядке возрастания размера.
            for size in item['sizes']:
                if max_heigth < size['height']:
                    max_heigth = size['height']
                    url_max_size = size['url']
                    type_max_size = size['type']

            # Проверяем на одинаковое колличество лайков и меняем имя если такие есть
            Add.Addition().same_values(new_dict_photo, item['likes']['count'], url_max_size, type_max_size, item['date'])
            index += 1

        return new_dict_photo