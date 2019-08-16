# file = open('C://Users/ssmd/Desktop/hello.txt','w')
# file.write('Hello World')

def text_create(name, msg):     #定义函数名text_create和两个参数
    desktop_path = 'C://Users/ssmd/Desktop/'     #桌面路径
    full_path  = desktop_path + name + '.txt'   #创建一个完整的文件路径
    file = open(full_path,'w')      #写入的模式 打开文件
    file.write(msg)         #写入传入的参数msg
    file.close()        #关闭文本文件
    print("Done")

text_create('Hello World','Hello World +2 ')    #调用函数

def text_filter(word,censord_word = 'lame',changeed_word = 'Awesome'):
    return word.replace(censord_word,changeed_word)

print(text_filter("Python is lame"))

def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)


censored_text_create('Try','lame! lame！lame!')
censored_text_create('Try2', 'lame! lame！lame!')
import os
print(os.getcwd())
print(os.listdir())
