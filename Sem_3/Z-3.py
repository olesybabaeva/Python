#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

things = {'спички': 1, 'компас': 2, 'термос': 5, 'аптечка': 4, 'палатка': 8, 'спальный мешок': 7, 'ложка': 2, 'тарелка': 2}

def backpack_capacity(capacity: int, things: dict):
    packaging_option = []
    summary = []
    for key, value in things.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(backpack_capacity(13, things))