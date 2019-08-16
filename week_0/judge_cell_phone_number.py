def number_test():
    CN_mobile = \
    [134,135,137,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
    CN_union = [130,131,132,155,156,185,186,145,176,1709]
    CN_telecom = [133,153,180,181,189,177,1700]

    print('Enter Your number :')
    number = input()

    len_memober = len(number)
    while len_memober == 11:
        top3 = int(number[:3])
        # print(top3,type(top3))
        if top3 in CN_mobile:
            print('Operator : China Mobile')
        elif top3 in CN_telecom:
            print('Operator : China Telecom')
        elif top3 in CN_union:
            print('Operator : China Union')
        else:
            print("Can't find ")
        break

    else:
        print("Invalid number length! ,your number should be in 11 digtis")

number_test()