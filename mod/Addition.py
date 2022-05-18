import json
from datetime import date


class Addition:

    # Проверка на одинаковые имена и переименование с датой.
    # Сделано отдельно, на вероятность подключения других соц сетей
    def same_values(self, new_dict_photo, like, url_max_size, type_max_size, data):

        if like not in new_dict_photo:
            new_dict_photo[like] = [url_max_size, type_max_size]
        else:
            new_key = str(like) + "_" + str(date.fromtimestamp(data))
            new_dict_photo[new_key] = [url_max_size, type_max_size]
        return new_dict_photo
    
    
    # Создание списка со словарем внутри
    def create_json(self, file_name, type):
        dict_to_file = {}
        new_file_name = f'{file_name}.jpg'
        dict_to_file['file_name'] = str(new_file_name)
        dict_to_file['size'] = type
        return dict_to_file
    
    
    # Запись списка в файл json
    def save_json(self, dict_to_file):
        with open('LOG_download.json', 'w') as f:
            json.dump(dict_to_file, f, ensure_ascii=False, indent=4)