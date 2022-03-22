import pandas as pd

url = 'https://touch-sp.hatenablog.com/entry/2021/03/07/234555'
dfs = pd.read_html(url, encoding='utf-8')
df = dfs[0]

df = df.drop_duplicates()

words_list = list(df['英単語'].unique())

words_dict = {}
for word in words_list:
    words_dict[word] = list(df[df['英単語']==word]['意味'])

import pickle

with open('words_dict.pkl', 'wb') as f:
    pickle.dump(words_dict, f)