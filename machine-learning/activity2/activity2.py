#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# load data
import pandas as pd
import numpy

dengue = pd.read_csv('../dengue_features_train.csv')

# normalization
dengue_subset = dengue.copy()

# temporary remove unused field and merge later
remove_field = ['city', 'year', 'weekofyear', 'week_start_date']
for i in remove_field:
    del dengue_subset[i]
    
from sklearn.preprocessing import MinMaxScaler,Imputer
min_max_scaler = MinMaxScaler()

imp = Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
dengue_subset_normalized = imp.fit_transform(dengue_subset)

features_norm = min_max_scaler.fit_transform(dengue_subset_normalized)

dengue_index = [i for i in dengue.columns if i not in remove_field]

dengue_normalized = pd.DataFrame(data=features_norm, columns=dengue_index)

for i in remove_field:
    dengue_normalized[i] = dengue[i]
    
# compute the similarity matrix
import sklearn.neighbors

dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(features_norm)
avSim = numpy.average(matsim)

# build dendrogram
from scipy import cluster
import matplotlib.pyplot as plt

clusters = cluster.hierarchy.linkage(matsim, method = 'complete')

cluster.hierarchy.dendrogram(clusters, color_threshold = 6)
plt.show()

# compare 
import

labels = cluster.hierarchy.fcluster(clusters, 23 , criterion = 'distance')

# create label dict
label_dic = {i:[] for i in range(1,7)}

for index,val in enumerate(labels):
    label_dic[val].append(index)

for i in range(1,5):
    print(str(i)+':')
    print(sum(dengue['station_avg_temp_c'][label_dic[i][:20]])/20)

# group info
# 1 fever 4 rash 2 muscle 3 joint pain
group_match = {1:'fever', 2: 'muscle', 3: 'joint pain', 4: 'rash'}
for i in range(1,5):
    print(group_match[i])
    print(label_dic[i][:20])