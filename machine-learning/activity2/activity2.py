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

clusters = cluster.hierarchy.fcluster(clusters, 4 , criterion = 'distance')

cluster.hierarchy.dendrogram(clusters, color_threshold = 4)
plt.show()