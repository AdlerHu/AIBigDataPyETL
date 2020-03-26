import jieba

jieba.load_userdict('./mydict.txt')
s = '大家好，我叫小賀，今天去中央大學大數據班上課，感覺非常開心'

# 全模式
s1_list = jieba.cut(s, cut_all=True)

# 精確模式
s2_list = jieba.cut(s, cut_all=False)

# 預設模式
s3_list = jieba.cut(s)

# 搜尋引擎模式
s4_list = jieba.cut_for_search(s)

print('|'.join(s1_list))
print('|'.join(s2_list))
print('|'.join(s3_list))
print('|'.join(s4_list))