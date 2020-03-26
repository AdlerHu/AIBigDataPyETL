import jieba
import os

path = './pttGossiping'
file_list = os.listdir(path)
jieba.load_userdict('./mydict.txt')

s = ''

for file_name in file_list:
    with open(path + '/' + file_name, 'r', encoding='utf-8') as f:
        s += f.read().split('---------------split--------------- \n')[0]

s_list = jieba.cut(s)

# 建立用詞字典，用來統計每個詞出現的次數
s_dict = {}
for w in s_list:
    # strip() 用來去掉左右兩邊的空白
    if len(w.strip()) < 2:
        continue

    if w in s_dict:
        s_dict[w] += 1
    else:
        s_dict[w] = 1

# print(s_dict)

tmp_list = []
for i in s_dict:
    tmp_list.append((i, s_dict[i]))

tmp_list.sort(key=lambda x: x[1], reverse=True)
print(tmp_list)
