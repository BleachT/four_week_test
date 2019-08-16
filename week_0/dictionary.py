"""
1、字典是键值对的形式出现
2、键不能重复，值可以
3、键不可改变，值可以改变 可以是任何对象
4、字典不能切片
"""
NASDAQ_code = {
    'BIDU': 'Baidu',
    'SINA': 'Sina',
    'YOKU': 'Youku'

}
NASDAQ_code['YOKU'] = 'youku'
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print(NASDAQ_code)
del NASDAQ_code['FB']
print(NASDAQ_code)

a = {'key':123,'key':123}   # 不重复，相同键值只出现一次
print(a)

import time

a = []
t0 = time.time()
for i in range(1,20000):
    a.append(i)
print(time.time() - t0,'Seconds process.time')

t0 = time.time()
b = [i for i in range(1,20000)]
print(time.time() - t0,'Seconds process time')

a = [i**2 for i in range(1,10)]
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n % 2 ==0]
z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']

print(a,'\n',c,'\n',k,'\n',z)

d = {i:i+1 for i in range(4)}
g = {i:j for i,j in zip(range(1,6),'abcde')}
h = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(d,'\n',g,'\n',h,'\n' '*********')
letters = ['a','b','c','e','f','g']
for num,letter in enumerate(letters):
    print(letter,'is',num + 1)
