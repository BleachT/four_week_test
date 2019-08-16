'''
1、列表中的每一个元素都是可变的；可以增删改
2、列表中的元素是有序的，每个元素都有一个位置 可查询位置对应的值
3、列表可容纳Python中的任何对象
'''
all_in_list = [
        1,                          #整数
        1.2,                        #浮点型
        'a word',                   #字符串
        print(1),                   #函数
        True,                       #布尔值
        [1,2],                      #列表嵌套列表
        (1,2),                      #元祖
        {'key': 'value'}            #字典

    ]

fruit = ['pineapple','pear']
fruit.insert(2,'grape2')
print(fruit)
fruit[0:0] = ['Orange']
print(fruit)
fruit.remove('grape2')             #删除grape2
print(fruit)
fruit[0] = "Apple"                 #Orange 替换成 Apple
print(fruit)
del fruit[0:2]                      # 删除方法2 del来声明
print(fruit)
