import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

trainset = pd.read_csv("original_data/train.csv")
testset = pd.read_csv("original_data/test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]


clf_knn = KNeighborsClassifier(weights = 'distance')
clf_knn.fit(trainset_vars, trainset_target)
print 'fit completed'

knn_output = pd.DataFrame( clf_knn.predict(testset_vars), columns = ['hand'] )
print 'predict completed'

knn_output['id'] = testset_ids
knn_output = knn_output[['id', 'hand']]

knn_output.to_csv("knn_output.csv", index=False, float_format='%.f')
print 'output saved'
