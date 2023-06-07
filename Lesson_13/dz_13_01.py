import random as r
from random_words import RandomWords
# 1
int_list = []
float_list = []
str_list = []

words = RandomWords()

for el in range(5000):
    int_list.append(r.randint(0, 1000))
    float_list.append(r.uniform(0.1, 100.0))
    str_list.append(words.random_word())

# print(int_list)
# print('*'*50)
# print(float_list)
# print('*'*50)
# print(str_list)

