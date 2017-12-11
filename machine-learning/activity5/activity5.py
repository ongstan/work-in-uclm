#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:00:52 2017

@author: stan
"""

import pandas as pd

dengue_train = pd.read_csv('../dengue_features_train.csv')

dengue_labels = pd.read_csv('../dengue_labels_train.csv')

sj = dengue_train[dengue_train['city'] == 'sj']

iq = dengue_train[dengue_train['city'] == 'iq']

sj_label = dengue_labels[dengue_labels['city'] == 'sj' ]

iq_label = dengue_labels[dengue_labels['city'] == 'iq' ]

sj_combine = sj.merge(sj_label,how='outer',on = ['city','year', 'weekofyear'])

iq_combine = iq.merge(iq_label,how='outer', on= ['city','year', 'weekofyear'])

# fill na with mean
sj_combine = sj_combine.fillna(sj_combine.mean())
iq_combine = iq_combine.fillna(iq_combine.mean())

sj.corr

def getCorr(df, threshold = 0.8):
    s = set()
    t = []
    for i, j in df.corr().iterrows():
        for index, value in j.iteritems():
            if str(i) == str(index):
                continue
            if abs(value) >= threshold:
                t.append(i)
                t.append(index)
                s.add(tuple(sorted((str(i),str(index)))))
    return s,t

s,t = (getCorr(sj, 0.9))

from collections import Counter
Counter(t)

# print(getCorr(sj, 0.9))
#{('reanalysis_avg_temp_k', 'reanalysis_max_air_temp_k'),
# ('reanalysis_dew_point_temp_k', 'reanalysis_specific_humidity_g_per_kg'), 
# ('reanalysis_avg_temp_k', 'reanalysis_min_air_temp_k'), 
# ('reanalysis_air_temp_k', 'reanalysis_dew_point_temp_k'), 
# ('reanalysis_air_temp_k', 'reanalysis_max_air_temp_k'), 
# ('reanalysis_air_temp_k', 'reanalysis_specific_humidity_g_per_kg'), 
# ('precipitation_amt_mm', 'reanalysis_sat_precip_amt_mm'), 
# ('reanalysis_air_temp_k', 'reanalysis_min_air_temp_k'), 
# ('reanalysis_air_temp_k', 'reanalysis_avg_temp_k')}

# Counter in and select low frequences to remove

to_remove_sj = [
 'reanalysis_sat_precip_amt_mm',
 'reanalysis_avg_temp_k',
 'reanalysis_dew_point_temp_k'
 'reanalysis_max_air_temp_k',
 'reanalysis_min_air_temp_k',
 'reanalysis_specific_humidity_g_per_kg'
 ]

from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()

model.fit(sj_combine.iloc[:,4:-1], sj_combine.iloc[:,-1])

from collections import OrderedDict
from operator import itemgetter

sj_dic = {sj_combine.columns[4:-1][i]:model.feature_importances_[i] for i in range(20)}

sj_dic = OrderedDict(sorted(sj_dic.items(), key = itemgetter(1)))
# features importance
OrderedDict([('reanalysis_avg_temp_k', 0.042700440134622694),
             ('station_max_temp_c', 0.04404425961805318),
             ('reanalysis_dew_point_temp_k', 0.045742704119559295),
             ('precipitation_amt_mm', 0.045982823723034125),
             ('ndvi_se', 0.047315143673129452),
             ('reanalysis_sat_precip_amt_mm', 0.049159219710916705),
             ('reanalysis_precip_amt_kg_per_m2', 0.049427451296481996),
             ('station_precip_mm', 0.049512387821482831),
             ('station_min_temp_c', 0.049554543001562645),
             ('reanalysis_air_temp_k', 0.05028309517663735),
             ('reanalysis_specific_humidity_g_per_kg', 0.050728868919103408),
             ('ndvi_nw', 0.050975985157908944),
             ('reanalysis_min_air_temp_k', 0.051340204758025129),
             ('reanalysis_relative_humidity_percent', 0.051978769192855281),
             ('reanalysis_tdtr_k', 0.052299564844629665),
             ('station_diur_temp_rng_c', 0.052333072982541792),
             ('ndvi_ne', 0.052383628967761234),
             ('station_avg_temp_c', 0.053913627061074144),
             ('reanalysis_max_air_temp_k', 0.053989464462781592),
             ('ndvi_sw', 0.056334745377838488)])

# selection sj
{'ndvi_ne',
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
 'station_precip_mm'}

#
from sklearn.ensemble import ExtraTreesClassifier

s,t = (getCorr(iq, 0.9))

from collections import Counter
Counter(t)

{('precipitation_amt_mm', 'reanalysis_sat_precip_amt_mm'),
 ('reanalysis_air_temp_k', 'reanalysis_avg_temp_k'),
 ('reanalysis_dew_point_temp_k', 'reanalysis_specific_humidity_g_per_kg')}


to_remove_iq = [
 'reanalysis_sat_precip_amt_mm',
 'reanalysis_avg_temp_k',
 'reanalysis_specific_humidity_g_per_kg'
 ]

model.fit(iq_combine.iloc[:,4:-1], iq_combine.iloc[:,-1])

iq_dic = {iq_combine.columns[4:-1][i]:model.feature_importances_[i] for i in range(20)}

iq_dic = OrderedDict(sorted(iq_dic.items(), key = itemgetter(1)))

set(iq_combine.columns[4:-1]) - set(to_remove_iq)


set(iq_combine.columns[4:-1]) - set(to_remove_iq)
Out[366]: 
{'ndvi_ne',
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
 'station_precip_mm'}
