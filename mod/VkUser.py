import requests
from datetime import date
import mod.Addition as Add
from pprint import pprint

class VkUser:

    URL_MAIN = 'http://api.vk.com/method/'
    
    # Вводим ТОКЕН
    def __init__(self, token):
        self.params = {
            'access_token': token,
            'v': '5.131'
        }

    # Возвращаем словарь с сылками на фото, лайками и т.п.
    def get_dict_photos(self, owner_id, id_album):
        url = self.URL_MAIN + 'photos.get'
        photo_params = {
            'owner_id': owner_id,
            'album_id': id_album,
            'extended': 1,
            'photo_size': 1
        }
        response = requests.get(url, params={**self.params, **photo_params}).json()
        
        return response['response']
    
    
    # Создать словарь, ключ это название файла, значение это ссылка на файл и буквенный тип размера файла, дата и 
    def get_url_photo(self, owner_id, number, id_album):
        index = 1
        new_dict_photo = {}
        dict_photos = self.get_dict_photos(owner_id, id_album)['items']
        
        for item in dict_photos:
            
            if index > number:    # Проверка на колличество нужных ссылок для закачки
                break
                
            # Ищем максимальный размер фото
            type_max_size = self.filter_type(item['sizes'])

            # Проверяем на одинаковое колличество лайков и меняем имя если такие есть
            Add.Addition().same_values(new_dict_photo, item['likes']['count'], type_max_size[1], type_max_size[0], item['date'], index)
            index += 1
            
        return new_dict_photo
    


    # Запрос на альбомы. Создается словарь "порядковым номером альбома": Название и id
    def get_albums_ad(self, owner_id):
        dict_album = {}
        number_album = 2

        url = self.URL_MAIN + 'photos.getAlbums'
        photo_params = {
            'owner_id': owner_id
        }

        # Создется первый ключ для выбора фото из профиля (аватарки)
        response_profile = self.get_dict_photos(owner_id, 'profile')['count']
        dict_album[1] = ['Фото с аватаров', 'profile', response_profile]

        # Далее создаются ключи (со 2го) для выбора фото из альбомов
        response = requests.get(url, params={**self.params, **photo_params}).json()
        
        for item in response['response']['items']:
            dict_album[number_album] = [item['title'], item['id'], item['size']]
            number_album += 1
        
        return dict_album


    # Поиск самой большой фотографии
    def filter_type(self, sizes):
        type = {'w': [1,'w'], 'z': [2,'z'], 'y': [3,'y'], 'x': [4,'x'], 'm': [5,'m'], 's': [6,'s']}
        type_key = 7
        url_max_size = ''

        for size in sizes:
            if size['type'] in type:
                if type_key > type[size['type']][0]:
                    type_key = type[size['type']][0]
                    max_type_key = type[size['type']][1]
                    url_max_size = size['url']
    
        return [max_type_key, url_max_size] 