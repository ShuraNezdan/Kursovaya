import mod.programm as programm
import mod.VkUser as yu
import mod.Addition as addit
from pydrive.auth import GoogleAuth
import sys
    
def main():
    # Считываем Токен ВК
    with open('token.txt', 'r') as file_object:
        token_vk = file_object.read().strip()
    
    # Вводимая человеком информация
    id_user_vk = '8398337'
    # id_user_vk = input('Введите id ВК: ')
    
    # Запрос на название альбомов для выбора
    album =  yu.VkUser(token_vk).get_albums_ad(id_user_vk)
    for key, value in album.items():
        print(f'{key}: {value[0]}, {value[2]} фотографий')

    # Выбор альбома и получение id альбома
    while True:
        id_album = addit.Addition().request_album_input(album)
        if id_album == 'q':
            sys.exit()
        else:
            break

    # Выбор колличества фотографий и название папки на диске
    number_of_photos = input('Введите колличество скачиваемых фотографий, по умолчанию - 5 шт.: ')
    name_folder = input('Введите название папки (в случае пустой строки, именем папки будет id ВК): ')
    if name_folder == '': name_folder = id_user_vk
    if number_of_photos == '': number_of_photos = 5
    
    # Выбор диска загрузки
    while True:
        print('''
        Выберите место загрузки.
        1: Yandex Disk
        2: Google Disk
        3: Отмена программы
            ''')
        disk_number = input('Номер: ')
            
        if disk_number == '1':    # Загрузка на Яндекс Диск
            disk = 1
            token_ya = ''
            # token_ya = input('Введите токен Яндекс Диска: ')
            
            vk = programm.Main(disk ,id_user_vk, id_album, token_vk, name_folder, number_of_photos, token_ya)
            vk.vk_to_disk()
         

        # Для загрузки на Google Disk необходимо создать файл client_secrets.json и скопировать его в корневой каталог
        # Описание создания можно прочиать тут: https://pythonhosted.org/PyDrive/
           
        elif disk_number == "2":           # Загрузка на Google Диск
            disk = 2
            # Проверка на аутентификацию
            gauth = GoogleAuth()
            gauth.LocalWebserverAuth() 
            
            vk = programm.Main(disk, id_user_vk, id_album, token_vk, name_folder, number_of_photos, gauth)
            vk.vk_to_disk()
        
            
        elif disk_number == '3':
            sys.exit()
        

if __name__ == '__main__':
    main()