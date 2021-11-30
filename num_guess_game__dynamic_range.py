print('Привет! \nЯ - числовая угадайка =)')

def launch_game():

    from random import randint

    while True:
        input_range = input('Введи диапазон чисел через пробел: ').split()
        if len(input_range) != 2:
            print('Нужно ввести 2 числа')
            continue
        if input_range[0][0] == '-':
            if not input_range[0][1:].isdigit():
                print('Это не числовой диапазон')
                continue
        if input_range[0][0] != '-':
            if not input_range[0].isdigit():
                print('Это не числовой диапазон')
                continue
        if input_range[1][0] == '-':
            if not input_range[1][1:].isdigit():
                print('Это не числовой диапазон')
                continue
        if input_range[1][0] != '-':
            if not input_range[1].isdigit():
                print('Это не числовой диапазон')
                continue
            else:
                break
        else:
            break

    num_range = [int(n) for n in input_range]
    min_num = min(num_range)
    max_num = max(num_range)

    hidden_num = randint(min_num, max_num)

    def is_valid(s):
        num = input_num[1:]
        if s.isdigit() and min_num <= int(s) <= max_num:
            result = True
        elif input_num[0] == '-' and num.isdigit() and min_num <= int(input_num) <= max_num:
            result = True
        else:
            result = False
        return result

    attempt = 0

    while True:
        input_num = input(f'Введи число от {min_num} до {max_num}: ')
        attempt += 1
        if not is_valid(input_num):
            print(f'Это не целое число от {min_num} до {max_num}')
            continue
        input_num = int(input_num)

        if input_num > hidden_num:
            print('Слишком много, попробуй еще раз')
        elif input_num < hidden_num:
            print('Слишком мало, попробуй еще раз')
        elif input_num == hidden_num:
            print(f'Ура! Ты угадал число, поздравляю! \nКоличество потраченных попыток: {attempt}')
            break

launch_game()

positive_answers = ['д', 'да', 'конечно', 'ага', 'угу']
negative_answers = ['н', 'не', 'нет', 'неа']
while True:
    again = input('Хочешь сыграть ещё раз? =) \n').lower()
    if again in positive_answers:
        launch_game()
    elif again in negative_answers:
        break
    else:
        print('Я тебя не понял')
