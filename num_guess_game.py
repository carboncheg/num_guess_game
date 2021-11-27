print('Привет! \nЯ - числовая угадайка =)')

def launch_game():

    from random import randint

    hidden_num = randint(1, 100)

    def is_valid(s):
        return s.isdigit() and 1 <= int(s) <= 100

    def incline_word():
        a = attempt
        if a % 10 == 1 and a % 100 != 11:
            result = f'{a} попытку'
        elif 2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14:
            result = f'{a} попытки'
        else:
            result = f'{a} попыток'
        return result

    attempt = 0

    while True:
        input_num = input('Введи число от 1 до 100: ')
        attempt += 1
        if not is_valid(input_num):
            print('Это не целое число от 1 до 100 :-|')
            continue
        input_num = int(input_num)

        if input_num > hidden_num:
            print('Слишком много, попробуй еще раз')
        elif input_num < hidden_num:
            print('Слишком мало, попробуй еще раз')
        elif input_num == hidden_num:
            incl = incline_word()
            print(f'Ура! Ты угадал число за {incl}, поздравляю!')
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
        print('Я тебя не понял :-/')
