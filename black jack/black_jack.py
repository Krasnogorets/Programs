# простой блек джек
import random

bet = 0
bet_min = 1
bet_max = 100
deposit_max = 1000
deposit_min = 100
valid_deposit = [str(i) for i in range(deposit_min, deposit_max+1, 1)]
valid_bet = [str(i) for i in range(bet_min, bet_max+1, 1)]
deposit = 0
fullStack = []
dictCardandPoints = {2: '2♥,2♦,2♣,2♠',
                     3: '3♥,3♦,3♣,3♠',
                     4: '4♥,4♦,4♣,4♠',
                     5: '5♥,5♦,5♣,5♠',
                     6: '6♥,6♦,6♣,6♠',
                     7: '7♥,7♦,7♣,7♠',
                     8: '8♥,8♦,8♣,8♠',
                     9: '9♥,9♦,9♣,9♠',
                     10: '10♥,10♦,10♣,10♠,J♥,J♦,J♣,J♠,D♥,D♦,D♣,D♠,K♥,K♦,K♣,K♠',
                     11: 'A♥,A♦,A♣,A♠'}
dictCardNum = {1: '2♥', 2: '3♥', 3: '4♥', 4: '5♥', 5: '6♥',
               6: '7♥', 7: '8♥', 8: '9♥', 9: '10♥', 10: 'J♥', 11: 'D♥',
               12: 'K♥', 13: 'A♥', 14: '2♦', 15: '3♦',
               16: '4♦', 17: '5♦', 18: '6♦', 19: '7♦', 20: '8♦', 21: '9♦',
               22: '10♦', 23: 'J♦', 24: 'D♦', 25: 'K♦', 26: 'A♦',
               27: '2♣', 28: '3♣', 29: '4♣', 30: '5♣', 31: '6♣',
               32: '7♣', 33: '8♣', 34: '9♣', 35: '10♣', 36: 'J♣', 37: 'D♣',
               38: 'K♣', 39: 'A♣', 40: '2♠', 41: '3♠', 42: '4♠', 43: '5♠', 44: '6♠',
               45: '7♠', 46: '8♠', 47: '9♠', 48: '10♠', 49: 'J♠', 50: 'D♠',
               51: 'K♠', 52: 'A♠'}


# methods
def out_red(text):
    print("\033[31m\033[47m{}\033[0m".format(text))


def out_black(text):
    print("\033[30m\033[47m{}\033[0m".format(text))


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


while deposit not in valid_deposit:
    deposit = input(f'Введите размер депозита от {deposit_min} до {deposit_max}: ')

if not fullStack:
    fill_random_stack()
while bet not in valid_bet:
    bet = input(f'Введите вашу ставку от {bet_min} до {bet_max}: ')

print(f'Ставка [{bet}] принята!')
