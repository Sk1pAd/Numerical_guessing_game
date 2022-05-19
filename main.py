import random # Подключаем модуль random

def is_valid(num): # Создаем функцию для проверки введённого числа
    if 1 <= int(num) <= 100 and num.isdigit():
        return True
    else:
        return False

print('Добрый день! Хотите сыграть со мной в одну игру?')
answer = input('(д / н)')
while answer == 'д': # Игра начинается :)
    print('Прекрасно! Сыграем в числовую угадайку!')
    print(f'Я загадала число от 1 до 100, попробуйте его угадать :)')
    puzzle = random.randint(1, 100) # Генерируем случайное число от 1 до 100
    while True:
        x = input('Ваше число... ')
        if is_valid(x) == True:
            x = int(x)
            if x == puzzle:
                print('Вы угадали, поздравляем!')
                break
            elif x < puzzle:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            else:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
        else:
            print(f'А может быть все-таки введем целое число от 1 до 100?')
            continue
    print('Хотите сыграть ещё раз?')
    answer = input('(д / н)')
else:
    print('Было приятно поиграть с Вами, досвидания и удачи!')