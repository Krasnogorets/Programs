# простой блек джек
import random
import sys

bet = 1  # int значение ставки
deposit = 100  # int значение депозита
bet_min = 1  # значение минимальной ставки
bet_max = 100  # значение максимальной ставки
deposit_max = 1000  # значение максимального депозита
deposit_min = 100  # значение мнимального депозита
valid_deposit = [str(i) for i in range(deposit_min, deposit_max + 1, 1)]  # строка диапазона депозита для проверки ввода
valid_bet = [str(i) for i in range(bet_min, bet_max + 1, 1)]  # строка диапазона ставки для проверки ввода

text = ''  # промежуточная переменная для вывода значения карт
fullStack = []  # строка готового набора номеро карт к раздаче
playerCurrentCards = []  # строка текущая раздача набора карт игрока
dilerCurrentCards = []  # строка текущая раздача набора карт дилера

temp_card_picture = []  # промежуточная строка для соотношения карты и номера карты
temp_card = ''  # промежуточная переменная для вывода значения карт
player_points = 0
diler_points = 0

dictCardandPoints = {2: '2♥,2♦,2♣,2♠',
                     3: '3♥,3♦,3♣,3♠',
                     4: '4♥,4♦,4♣,4♠',
                     5: '5♥,5♦,5♣,5♠',
                     6: '6♥,6♦,6♣,6♠',
                     7: '7♥,7♦,7♣,7♠',
                     8: '8♥,8♦,8♣,8♠',
                     9: '9♥,9♦,9♣,9♠',
                     10: '10♥,10♦,10♣,10♠,J♥,J♦,J♣,J♠,D♥,D♦,D♣,D♠,K♥,K♦,K♣,K♠',
                     11: 'A♥,A♦,A♣,A♠'}  # словарь соответствия очков карт
dictCardNum = {1: '2♥', 2: '3♥', 3: '4♥', 4: '5♥', 5: '6♥',
               6: '7♥', 7: '8♥', 8: '9♥', 9: '10♥', 10: 'J♥', 11: 'D♥',
               12: 'K♥', 13: 'A♥', 14: '2♦', 15: '3♦',
               16: '4♦', 17: '5♦', 18: '6♦', 19: '7♦', 20: '8♦', 21: '9♦',
               22: '10♦', 23: 'J♦', 24: 'D♦', 25: 'K♦', 26: 'A♦',
               27: '2♣', 28: '3♣', 29: '4♣', 30: '5♣', 31: '6♣',
               32: '7♣', 33: '8♣', 34: '9♣', 35: '10♣', 36: 'J♣', 37: 'D♣',
               38: 'K♣', 39: 'A♣', 40: '2♠', 41: '3♠', 42: '4♠', 43: '5♠', 44: '6♠',
               45: '7♠', 46: '8♠', 47: '9♠', 48: '10♠', 49: 'J♠', 50: 'D♠',
               51: 'K♠', 52: 'A♠'}  # словарь соответствия номера карт и значений

dictCardColor = {
    1: '2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, D♥,K♥, A♥, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦,10♦, J♦, D♦, K♦, A♦',
    2: '2♣, 3♣, 4♣, 5♣, 6♣,7♣, 8♣, 9♣, 10♣, J♣, D♣, K♣, A♣, 2♠, 3♠, 4♠, 5♠, 6♠,7♠, 8♠, 9♠, 10♠, J♠, D♠, K♠, A♠'}


# methods
def out_red(text):
    print("\033[31m\033[47m{}\033[0m".format(*text))


def out_black(text):
    print("\033[30m\033[47m{}\033[0m".format(*text))


def fill_random_stack():
    temp_random = 0
    temp_rnd_str = []
    for k in range(0, 4):
        temp_rnd_str.append(int(random.randrange(1, 53)))
        i = 0
        while i < 51:
            temp_random = int(random.randrange(1, 53))
            if temp_random in temp_rnd_str:
                i -= 1
            else:
                temp_rnd_str.append(temp_random)
            i += 1
        fullStack.extend(temp_rnd_str)
        temp_rnd_str.clear()


def first_shuffle():  # первая раздача 4х карт

    for i in range(0, 4):
        card_number = 0

        if i == 0 or i == 2:
            card_number = int(fullStack.pop(0))
            playerCurrentCards.append(get_kard_picture(card_number))
        else:
            card_number = int(fullStack.pop(0))
            dilerCurrentCards.append((get_kard_picture(card_number)))


def print_card(temp_card_picture):
    for i in temp_card_picture:
        for k, j in dictCardColor.items():
            if i in j and k == 1:
                print(f"\033[31m\033[47m{i}\033[0m", sep=" ", end=' ')
            elif i in j and k == 2:
                print(f"\033[30m\033[47m{i}\033[0m", sep=" ", end=' ')


def bet_input():
    bet_user_input = []
    while bet_user_input not in valid_bet:
        bet_user_input = input(f'Введите вашу ставку от {bet_min} до {bet_max}: ')
    deposit = int(deposit_user_input)
    bet = int(bet_user_input)
    if bet > deposit:
        print(f'Ставка {bet} больше вашего остатка на депозите {deposit}')
    else:
        print(f'Ставка [{bet}] принята!')
    deposit -= bet
    print(f'Остаток на депозите : {deposit}')


def deposit_check():
    if deposit < bet_min:
        print('GAME OVER')
        # sys.exit()


def get_kard_picture(card_number):
    temp_card_picture.append(dictCardNum[card_number])
    return temp_card_picture.pop()


def count_points():

    for i in playerCurrentCards:
        print(i)
        for j, k in dictCardandPoints.items():
            if k == i:
                player_points += j
                print(j)

    for i in dilerCurrentCards:
        for j, k in dictCardandPoints.items():
            if k == i:
                diler_points += j


# end methods

deposit_user_input = []

# while deposit_user_input not in valid_deposit:
#     deposit_user_input = input(f'Введите размер депозита от {deposit_min} до {deposit_max}: ')
# bet_input()
# deposit_check()

if not fullStack:
    fill_random_stack()
first_shuffle()
count_points()
print_card(playerCurrentCards)
print(f'-карты игрока,  очки : {player_points}')
print_card(dilerCurrentCards)
print(f'-карты дилера,  очки : {diler_points}')
