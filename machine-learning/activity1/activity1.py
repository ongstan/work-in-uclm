#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:06:32 2017

@author: stan wang
"""

import pandas as pd

# load features data
dengue_features_train = pd.read_csv('dengue_features_train.csv')

# calculate the correlation of features
correlation_of_features = dengue_features_train.corr()

THRESHOLD_OF_FEATURES = 0.9

# correlation list intial 
list_of_feature_correlation = []

for index,datarow in correlation_of_features.iterrows():
    for key,value in datarow.iteritems():
        if 1 > float(value) > THRESHOLD_OF_FEATURES:
            list_of_feature_correlation.append((index,key,value))
            
# sort by value
list_of_feature_correlation.sort(key=lambda x:x[2],reverse=True)

# format string
format_string_of_features_correlation = 'The feature %s and feature %s has'\
'correlation and its value is %s'

print('\n'.join([format_string_of_features_correlation % (i[0],i[1],i[2]) 
                            for i in list_of_feature_correlation]))
    
from sklearn.decomposition import PCA
from sklearn import preprocessing

# clean data

dengue_features_copy = dengue_features_train.copy()

del dengue_features_copy['city']
del dengue_features_copy['year']
del dengue_features_copy['weekofyear']
del dengue_features_copy['week_start_date']

dengue_features_copy = dengue_features_copy.dropna()

# nomalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
dengue = min_max_scaler.fit_transform(dengue_features_copy)

# PCA estimation

estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(dengue)

print(estimator.explained_variance_ratio_) 

# plot 
import numpy
import matplotlib.pyplot as plt

numbers = numpy.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i]) 
plt.xlim(-1, 2)
plt.ylim(-1, 1.5)
ax.grid(True)
fig.tight_layout()
plt.show()



