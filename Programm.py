import mod.main as main
    
    
if __name__ == '__main__':
    
    # Вводимая человеком информация
    id_user_vk = '8398337'
    token_ya = ''
    number_of_photos = 8
    name_folder = 'sdfdg'
    
    if name_folder == '': name_folder = id_user_vk
    
   
    
    vk = main.Main(id_user_vk, token_ya, name_folder, number_of_photos)
    vk.vk_to_ya()