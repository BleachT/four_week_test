import random
# point1 = random.randrange(1,7)
# point2 = random.randrange(1,7)
# point3 = random.randrange(1,7)
# #
# # print(point1,point2,point3)
#
# def touzi():
#     print('<<<< GAME STARTS! >>>>')
#     big_or_small = input("Big or Small: ")
#     dianshu_list = []
#     for times in range(3):
#         dianshu_list.append(point1)
#         dianshu_list.append(point2)
#         dianshu_list.append(point3)
#         print('The points are [{},{},{}]'.format(point1,point2,point3))
#         sum_list = sum(dianshu_list())
#
#         if  sum_list < 11:
#             dian = "Small"
#         else:
#             dian = "Big"
#         if big_or_small ==dian:
#             print("win")
#         else:
#             print("lose")
#
# touzi()   # failed

def roll_dice(number = 3, points = None):
    print('<<<<< ROLL THE DICE >>>> ')
    if  points is None:
        points = []
    while number > 0:
        point = random.randrange(1,7)
        points.append(point)
        number = number - 1
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <=10
    if isBig:
        return "Big"
    elif isSmall:
        return  'Small'

def start_game():

    your_money = 1000

    while your_money > 0:
        print('<<<<< GAME STARTS! >>>>>')
        choice = ['Big', 'Small']
        your_choice = input('Big or Small :')

        if  your_choice in choice:
            your_bet = int(input('How much you wanna bet ? - '))
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:

                print('The points is',points,'You Win !')
                print('You gained {} ,you have {} now'.format(your_bet,your_money+your_bet))
                your_money = your_money + your_bet
            else:

                print('The points are',points,'You Lose !')
                print('You gained {} ,you have {} now'.format(your_bet,your_money-your_bet))
                your_money = your_money - your_bet

        else:
            print('Invalid Word')
            start_game()
    else:
        print('GAME OVER ')
start_game()


