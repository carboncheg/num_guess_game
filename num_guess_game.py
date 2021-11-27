from random import randint

print('Добро пожаловать в числовую угадайку =)')

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
    input_num = input('Введите число от 1 до 100: ')
    attempt += 1
    if not is_valid(input_num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    input_num = int(input_num)

    if input_num > hidden_num:
        print('Слишком много, попробуйте еще раз')
    elif input_num < hidden_num:
        print('Слишком мало, попробуйте еще раз')
    elif input_num == hidden_num:
        incl = incline_word()
        print(f'Ура! Вы угадали число за {incl}, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
