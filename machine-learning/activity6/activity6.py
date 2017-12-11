#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:01:19 2017

@author: stan
"""

import pandas as pd

dengue_train = pd.read_csv('../dengue_features_train.csv')

dengue_labels = pd.read_csv('../dengue_labels_train.csv')

dengue_test = pd.read_csv('../dengue_features_test.csv')

dengue_test = dengue_test.fillna(dengue_test.mean())

sj_test = dengue_test[dengue_test['city'] == 'sj']

iq_test = dengue_test[dengue_test['city'] == 'iq']

sj = dengue_train[dengue_train['city'] == 'sj']

iq = dengue_train[dengue_train['city'] == 'iq']

sj_label = dengue_labels[dengue_labels['city'] == 'sj' ]

iq_label = dengue_labels[dengue_labels['city'] == 'iq' ]

sj_combine = sj.merge(sj_label,how='outer',on = ['city','year', 'weekofyear'])

iq_combine = iq.merge(iq_label,how='outer', on= ['city','year', 'weekofyear'])


# fill na with mean
sj_combine = sj_combine.fillna(sj_combine.mean())
iq_combine = iq_combine.fillna(iq_combine.mean())


sj_columns = ['ndvi_ne',
 'ndvi_nw',
 'ndvi_se',
 'ndvi_sw',
 'precipitation_amt_mm',
 'reanalysis_dew_point_temp_k',
 'reanalysis_max_air_temp_k',
 'reanalysis_precip_amt_kg_per_m2',
 'reanalysis_relative_humidity_percent',
 'reanalysis_tdtr_k',
 'station_avg_temp_c',
 'station_diur_temp_rng_c',
 'station_max_temp_c',
 'station_min_temp_c',
 'station_precip_mm']

iq_columns = ['ndvi_ne',
 'ndvi_nw',
 'ndvi_se',
 'ndvi_sw',
 'precipitation_amt_mm',
 'reanalysis_air_temp_k',
 'reanalysis_dew_point_temp_k',
 'reanalysis_max_air_temp_k',
 'reanalysis_min_air_temp_k',
 'reanalysis_precip_amt_kg_per_m2',
 'reanalysis_relative_humidity_percent',
 'reanalysis_tdtr_k',
 'station_avg_temp_c',
 'station_diur_temp_rng_c',
 'station_max_temp_c',
 'station_min_temp_c',
 'station_precip_mm']


from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors


knn = KNeighborsClassifier()

knn.fit(sj_combine.iloc[:,4:-1], sj_combine.iloc[:,-1])

## sj

knn.fit(pd.DataFrame(sj_combine, columns = sj_columns), sj_combine.iloc[:,-1])

sj_res = knn.predict(pd.DataFrame(sj_test, columns = sj_columns))

## iq



knn.fit(pd.DataFrame(iq_combine, columns = iq_columns), iq_combine.iloc[:,-1])

iq_res = knn.predict(pd.DataFrame(iq_test, columns = iq_columns))

import numpy as np

res = np.concatenate((sj_res, iq_res))



keep_fields = ['city', 'year', 'weekofyear', 'total_cases']

res = np.concatenate((sj_res, iq_res))

dengue_test['total_cases'] = pd.DataFrame(res, columns=['total_cases'])

output = pd.DataFrame(dengue_test, columns = keep_fields)

output.to_csv('result.csv' , index= False)

# normalization and retry

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()

sj_normalized = pd.DataFrame(min_max_scaler.fit_transform(sj_combine.iloc[:,4:-1]),columns=sj_combine.columns[4:-1])
iq_normalized = pd.DataFrame(min_max_scaler.fit_transform(iq_combine.iloc[:,4:-1]),columns=iq_combine.columns[4:-1])

sj_test_normalized = pd.DataFrame(min_max_scaler.fit_transform(sj_test.iloc[:,4:]),columns=sj_test.columns[4:])
iq_test_normalized = pd.DataFrame(min_max_scaler.fit_transform(iq_test.iloc[:,4:]),columns=iq_test.columns[4:])

knn.fit(pd.DataFrame(sj_normalized, columns = sj_columns), sj_combine.iloc[:,-1])
sj_res = knn.predict(pd.DataFrame(sj_test_normalized, columns = sj_columns))

knn.fit(pd.DataFrame(iq_normalized, columns = iq_columns), iq_combine.iloc[:,-1])
iq_res = knn.predict(pd.DataFrame(iq_test_normalized, columns = iq_columns))


res = np.concatenate((sj_res, iq_res))

dengue_test['total_cases'] = pd.DataFrame(res, columns=['total_cases'])

output = pd.DataFrame(dengue_test, columns = keep_fields)

output.to_csv('result.csv' , index= False)

# cross validation 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

sj_train_list = train_test_split(sj_combine)

sj_normalized.merge(sj_label,on = keep_fields[:-1])

def cross_validation(train, label,k=10):
    m = []
    for i in range(k):
        X_train, X_test, y_train, y_test = train_test_split(train, label,test_size = 0.3, random_state=0)
        knn.fit(X_train, y_train)
        t = knn.predict(X_test)
        m.append(mean_absolute_error(y_test, t))
    print(sum(m)/len(m))
    
cross_validation(sj_combine.iloc[:,4:-1], sj_combine.iloc[:,-1])
26.2633451957

cross_validation(iq_combine.iloc[:,4:-1], iq_combine.iloc[:,-1])
7.42307692308

# parameter choosem, # k for sj is 11 25.3
for i in range(1,15):
    knn.set_params(**{'n_neighbors':i})
    print(i)
    cross_validation(sj_combine.iloc[:,4:-1], sj_combine.iloc[:,-1])


# k for iq is 9 7.13
for i in range(3,15):
    knn.set_params(**{'n_neighbors':i})
    print(i)
    cross_validation(iq_combine.iloc[:,4:-1], iq_combine.iloc[:,-1])

# test normalized data ,sq without norm k = 13 25.15
for i in range(3,15):
    knn.set_params(**{'n_neighbors':i})
    print(i)
    cross_validation(sj_normalized.iloc[:], sj_combine.iloc[:,-1])

# sq with norm k with 13 6.53
for i in range(3,15):
    knn.set_params(**{'n_neighbors':i})
    print(i)
    cross_validation(iq_normalized.iloc[:], iq_combine.iloc[:,-1])

# sj
# metric to eucli k = 11 ,24.86 without norm
# k=13 25.15
knn.set_params(**{'metric':'euclidean'})

# iq 
# k = 6.53 with norm

# weights distance , worse
knn.set_params(**{'p':'4'})

