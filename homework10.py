# -*- coding: utf-8 -*-
"""Homework10

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CX_2BxlvbBULk0FtGk4vUz5U7EpeSS-T
"""

import pandas as pd

import seaborn as snas

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

import random



lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data1 = pd.get_dummies(data, columns=['whoAmI'])
data1.head()

"""Возможно перевести его в one hot вид без использования get_dummies, код будет слишком массивным. Необходимо будет создать нумерацию строк, выделить критерии (будующие столбцы), а затем пробежаться по изначальному дата фрейму столько раз сколько критериев ища совпадения"""

