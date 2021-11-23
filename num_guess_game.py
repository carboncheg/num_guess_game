from random import randint

print('Добро пожаловать в числовую угадайку =)')

hidden_num = randint(1, 100)

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

while True:
    input_num = input('Введите число от 1 до 100: ')
    if not is_valid(input_num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    input_num = int(input_num)

    if input_num > hidden_num:
        print('Слишком много, попробуйте еще раз')
    elif input_num < hidden_num:
        print('Слишком мало, попробуйте еще раз')
    elif input_num == hidden_num:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
