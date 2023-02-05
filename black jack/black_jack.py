# простой блек джек
import random

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
               41: 'K♠', 52: 'A♠'}


# methods
def out_red(text):
    print("\033[31m\033[47m{}\033[0m".format(text))


def out_black(text):
    print("\033[30m\033[47m{}\033[0m".format(text))


temprnd = 0
tempRndstr = []


def fillRandomStack():
    for k in range(0, 4):
        tempRndstr.append(int(random.randrange(1, 53)))
        i = 0
        while i < 51:
            temprnd = int(random.randrange(1, 53))
            if temprnd in tempRndstr:
                i -= 1
            else:
                tempRndstr.append(temprnd)
            i += 1
        fullStack.extend(tempRndstr)
        tempRndstr.clear()


# cardHerts2 = '2    ♣ ♠ ♦ \n♥    \n  ♥  \n     \n     \n     \n     \n  ♥  \n    ♥\n     2'
# out_red(' K♥ ')
# out_black(' T♥ ')
# deposit = int(input('Введите размер депозита'))
if not fullStack:
    fillRandomStack()

print(fullStack)
