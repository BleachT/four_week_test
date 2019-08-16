# path = 'C://Users/ssmd/Desktop/p/Walden.txt'
# with open(path,'r',encoding= 'gbk',errors='ignore') as text:
#     words = text.read().split()
#     print(words)
#     for word in words:
#         print('{} - {} times'.format(word,words.count(word)))
import string
import time
t0 = time.time()
print(t0)
path = 'C://Users/ssmd/Desktop/p/Walden.txt'

with open(path,'r',encoding= 'gbk',errors='ignore') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}

for word in sorted(counts_dict,key = lambda x: counts_dict[x],reverse=True):
    print('{} -- {} times'.format(word,counts_dict[word]))

print("*******")
print(time.time())
print(time.time() - t0 ,'S')
