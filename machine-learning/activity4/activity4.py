#Dataset: the same of previous activities.

#1. Study the correlation between features and total cases. Extract some conclusions.

#2. Feature Selection: Select a subset of the available features. For this purpose you can use the knowledge in previous activities. Include in this subset the year and the week of the year to build your models.

#3. Build a Decision Tree Model using your data. Obtain the tree and the features relevancies. Perform a cross validation process in order to select the best max_depth parameter.

from sklearn import tree
import pandas as pd

# load data
dengue = pd.read_csv('../dengue_features_train.csv')
dengue_test = pd.read_csv('../dengue_features_test.csv')
dengue_label = pd.read_csv('../dengue_labels_train.csv')

dengue_copy = dengue.copy()
dengue_copy['total_cases'] = dengue_label['total_cases']
dengue_copy = dengue_copy.dropna()

labels = dengue_copy['total_cases']

remove_field = ['city', 'year', 'weekofyear', 'week_start_date']

#label_copy = dengue_label.copy()
#dengue_copy = dengue.copy()

for i in remove_field:
    #del dengue_test[i]
    del dengue_copy[i]

# normalization
from sklearn.feature_selection import VarianceThreshold

sel = VarianceThreshold()'

sel.fit(dengue_normalized.)

from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()

dengue_normalized = pd.DataFrame(min_max_scaler.fit_transform(dengue_copy.dropna()),columns=dengue_copy.columns)

dengue_normalized.corr()['total_cases']

# pick the field which abs(correlation cofficient ) in top rank
# 
picked_features = ['reanalysis_min_air_temp_k',
                   'reanalysis_max_air_temp_k',
                   'reanalysis_relative_humidity_percent',
                   'reanalysis_tdtr_k',
                   'station_diur_temp_rng_c']

dengue_normalized_copy = dengue_normalized.copy()
 
for i in dengue_normalized_copy:
    if i not in picked_features:
        del dengue_normalized_copy[i]


from sklearn import tree
import graphviz

clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=4,min_samples_leaf=100,max_features=5)


clf = clf.fit(dengue_normalized_copy, labels)

#for index, value in enumerate(clf.feature_importances_):
#    if value != 0:
#        print()
        
dot_data = tree.export_graphviz(clf, out_file=None,feature_names=picked_features) 
graph = graphviz.Source(dot_data) 
graph.render("dengue") 


clf.set_params(**{"criterion":'gini'})


dot_data = tree.export_graphviz(clf, out_file=None,feature_names=picked_features) 
graph = graphviz.Source(dot_data) 
graph.render("dengue_gini") 


