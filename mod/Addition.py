import json
from datetime import date


class Addition:

    # Проверка на одинаковые имена и переименование с датой.
    # Сделано отдельно, на вероятность подключения других соц сетей
    # Внимание! Есть особенность, когда фото с одинаковым колво лайков более 2, то предыдущие переписываются, это из за того что словарь. По этому добавил в конец названия индекс загрузки.
    def same_values(self, new_dict_photo, like, url_max_size, type_max_size, data, index):    
        # print(like, ' ', url_max_size)
        if like not in new_dict_photo:
            new_dict_photo[like] = [url_max_size, type_max_size]
        else:
            new_key = f'{str(like)}_{str(date.fromtimestamp(data))}_фото№_{str(index)}'
            new_dict_photo[new_key] = [url_max_size, type_max_size]
        return new_dict_photo
    
    
    # Создание списка со словарем внутри, для записи в LOG
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

    
    # Возвращает id выбранного альбома
    def request_album_input(self, dict_album):

        while True:
            self.number_album = input('Введите номер альбома, "q" выход: ')

            if self.number_album == "q":
                id_album = 'q'
                break
            elif int(self.number_album) in dict_album:
                id_album = dict_album[int(self.number_album)][1]
                print(f'Вы выбрали "{dict_album[int(self.number_album)][0]}"')
                break
            else:
                print('Вы ошиблись номером альбома, выход "q"')

        return id_album