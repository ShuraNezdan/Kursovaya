import mod.main as main
    
    
if __name__ == '__main__':
    
    # Вводимая человеком информация
    # id_user_vk = '8398337'
    # token_ya = ''
    # number_of_photos = 8
    # name_folder = 'Фото из ВК'
    
    
    id_user_vk = input('Введите id ВК: ')
    token_ya = input('Введите токен Яндекс Диска: ')
    number_of_photos = int(input('Введите колличество скачиваемых фотографий: '))
    name_folder = input('Введите название папки (в случае пустой строки, именем папки будет id ВК): ')
    
    
    
    if name_folder == '': name_folder = id_user_vk
    
   
    
    vk = main.Main(id_user_vk, token_ya, name_folder, number_of_photos)
    vk.vk_to_ya()