# 创建一个函数在指定文件夹下创建10个文件
# def creat_file():
#     path = "C://Users/ssmd/Desktop/p/"
#     # for name in range(1,11):
#     #     full_path = path + str(name) + '.txt'
#     #     file = open(full_path,'w')
#     #     file.write(str(name))
#     #     file.close()
#     for name in range(1,11):
#         full_path = path + str(name) + '.txt'
#         with open(full_path,'w') as file:
#             file.write(str(name))
#
#
# creat_file()

#复利函数
def invest(amount,rate,time):
    print("principal amount: {}".format(amount))
    for year in range(1,time+1):
        amount = amount * (rate + 1)    # 累乘
        print('year {}: $ {}'.format(time,round(amount,2)))

invest(100,0.05,8)
print("********")
invest(2000,0.025,8)


def oushu(number):
    for i in range(1,number+1):
        if i % 2 == 0:
            print(i)

oushu(100)