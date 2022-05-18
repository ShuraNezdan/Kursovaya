import mod.YaDisk as yd
import mod.VkUser as yu
import mod.Addition as addit



class Main:
    # Класс для основной работы закачки с соц сетей на облачные диски

    def __init__(self, id: str, token_ya: str, name_folder, number_of_photos = 5):
        self.id = id
        self.token_ya = token_ya
        self.number_of_photos = number_of_photos
        self.name_folder = name_folder

    # Выполняет закачку с ВК на Яндекс Диск
    def vk_to_ya(self):

        # Считываем Токен ВК
        with open('token.txt', 'r') as file_object:
            token = file_object.read().strip()

        json_file_logs = []


        vk_client = yu.VkUser(token)
        uploader = yd.YaDisk(self.token_ya)
        add = addit.Addition()

        uploader.create_folder(self.name_folder)             # Создаем папку на диске
        dict_photo = vk_client.get_url_photo(self.id, self.number_of_photos)    # Создаем словарь для загрузки

        for key, value in dict_photo.items():
            result = uploader.upload(value[0], self.name_folder, key)
            if result == 202:
                print(f'Файл {key}.jpg загрузился')
                json_file_logs.append(add.create_json(key, value[1]))
            


        add.save_json(json_file_logs)
        print(json_file_logs)