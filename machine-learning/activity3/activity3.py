#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:35:44 2017

@author: stan
"""

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# load data
dengue = pd.read_csv('../dengue_features_train.csv')
dengue_test = pd.read_csv('../dengue_features_test.csv')

dengue_subset = dengue.dropna()

remove_field = ['city', 'year', 'weekofyear', 'week_start_date']

remove_data = pd.DataFrame()

for i in remove_field:
    remove_data[i] = dengue_subset[i]
    del dengue_subset[i]

# normalization
from sklearn.preprocessing import MinMaxScaler,Imputer
min_max_scaler = MinMaxScaler()

imp = Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
dengue_subset_normalized = imp.fit_transform(dengue_subset)

from collections import Counter

for i in range(1,9):
    cluster = KMeans(n_clusters=i)
    cluster.fit(dengue_subset_normalized)
    arr = cluster.predict(dengue_subset.dropna().values)
    
    print(Counter(arr))
    

for i in range(1,9):
    cluster = KMeans(n_clusters=i, init='random')
    cluster.fit(dengue_subset_normalized)
    arr = cluster.predict(dengue_subset.dropna().values)
    
    print(Counter(arr))

import hypertools as hyp
hyp.plot(dengue_subset_normalized, '.', n_clusters=4)

hyp.plot(dengue_subset_normalized, '.', n_clusters=5)

hyp.tools.describe_pca(dengue_subset_normalized)


cluster = KMeans(n_clusters=4)
cluster.fit(dengue_subset_normalized)
arr = cluster.predict(dengue_subset.dropna().values)
    
print(Counter(arr))

arr_dic = {i:[] for i in set(arr)}

for index,value in enumerate(final_labels):
    #if value > 100:
    #    value = 100    
    arr_dic[arr[index]].append(value)
    
    
[sum(arr_dic[i])/len(arr_dic[i]) for i in arr_dic.keys()]