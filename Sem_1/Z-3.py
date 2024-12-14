#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10
i = 0
while i < count:
    i += 1
    user = int(input("Введите число больше 0 и меньше 1000: "))
    if user > randintnum:
        print(f"Число больше\nОсталось попыток {count - i}")
    elif user < randintnum:
        print(f"Число меньше\nОсталось попыток {count - i}")
    else:
        print("Вы выиграли")
        break