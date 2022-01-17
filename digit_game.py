import random

num = random.randint(1,100)

def is_valid(usr_resp):
    return usr_resp.isdigit() and 1<int(usr_resp)<100

def start_game():
    while True:
        print("Введите число от 1 до 100")
        usr_resp=input()
    
        if is_valid(usr_resp):
            usr_resp=int(usr_resp)
        else: 
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if usr_resp==num:
            print('Вы угадали, поздравляем!')
            break;
        if usr_resp<num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Ваше число больше загаданного, попробуйте еще разок')

def menu():
    print('Добро пожаловать в числовую угадайку')
    start_game()

menu()