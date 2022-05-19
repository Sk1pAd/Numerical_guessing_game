import random # Подключаем модуль random

def is_valid(num, right): # Создаем функцию для проверки введённого числа
    if 1 <= int(num) <= right and num.isdigit():
        return True
    else:
        return False

print('Добрый день! Хотите сыграть со мной в одну игру?')
answer = input('(д / н)')
while answer == 'д': # Игра начинается :)
    print('Прекрасно! Сыграем в числовую угадайку!')
    n = int(input('До какой правой границы вы хотите со мной сыграть?: '))
    print(f'Я загадала число от 1 до {n}, попробуйте его угадать :)')
    puzzle = random.randint(1, n) # Генерируем случайное число от 1 до n
    count = 0 # Создаём счётчик кол-ва попыток
    while True:
        x = input('Ваше число... ')
        if is_valid(x, n) == True:
            x = int(x)
            if x == puzzle:
                count += 1
                print('Вы угадали, поздравляем!')
                print(f'Количество Ваших попыток: {count}')
                break
            elif x < puzzle:
                count += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            else:
                count += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            continue
    print('Хотите сыграть ещё раз?')
    answer = input('(д / н)')
else:
    print('Было приятно поиграть с Вами, досвидания и удачи!')