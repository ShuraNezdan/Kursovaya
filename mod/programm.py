import mod.YaDisk as yd
import mod.VkUser as yu
import mod.GoogDrive as gd
import mod.Addition as addit



class Main:
    # Класс для основной работы закачки с соц сетей на облачные диски

    def __init__(self, disk, id: str, id_album, token_vk, name_folder, number_of_photos, token_or_gauth = ''):
        self.disk = disk
        self.id = id
        self.ad_album = id_album
        self.token_vk = token_vk
        self.token_or_gauth = token_or_gauth
        self.number_of_photos = number_of_photos
        self.name_folder = name_folder

    # Выполняет закачку с ВК на Яндекс Диск
    def vk_to_disk(self):
        json_file_logs = []

        # Загрузка,  идентификатор disk служит для разделения вариантов загрузки, можно без него, но так появляется возможность дополнить другие обл.диски.
        # Загрузка на Яндекс 
        if self.disk == 1:
            vk_client = yu.VkUser(self.token_vk)
            uploader_ya = yd.YaDisk(self.token_or_gauth)
            add = addit.Addition()

            uploader_ya.create_folder(self.name_folder)             # Создаем папку на диске
            dict_photo = vk_client.get_url_photo(self.id, self.number_of_photos, self.ad_album)    # Создаем словарь для загрузки
            
            # Перебераем словарь со ссылками и названиями фото, загружаем и пополняем log
            for key, value in dict_photo.items():
                result = uploader_ya.upload(value[0], self.name_folder, key)
                if result == 202:
                    print(f'Файл {key}.jpg загрузился')
                    json_file_logs.append(add.create_json(key, value[1]))
            
        # Загрузка на Google
        elif self.disk == 2:
            vk_client = yu.VkUser(self.token_vk)
            uploader_gl = gd.GooglDrive(self.token_or_gauth)
            add = addit.Addition()

            id_folder = uploader_gl.create_folder(self.name_folder)             # Создаем папку на диске
            dict_photo = vk_client.get_url_photo(self.id, self.number_of_photos, self.ad_album)    # Создаем словарь для загрузки

            # Перебераем словарь со ссылками и названиями фото, загружаем и пополняем log
            for key, value in dict_photo.items():
                result = uploader_gl.upload(key, id_folder, value[0])
                if result == 200:
                    print(f'Файл {key}.jpg загрузился')
                    json_file_logs.append(add.create_json(key, value[1]))

        # Сохрание log
        add.save_json(json_file_logs)
        print(json_file_logs)
        
