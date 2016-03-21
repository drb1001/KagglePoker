import pandas as pd
from sklearn.svm import LinearSVC

trainset = pd.read_csv("original_data/train.csv")
testset = pd.read_csv("original_data/test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]


clf_svclinear = LinearSVC(verbose=6)
clf_svclinear.fit(trainset_vars, trainset_target)

svclinear_output = pd.DataFrame( clf_svclinear.predict(testset_vars), columns = ['hand'] )
svclinear_output['id'] = testset_ids
svclinear_output = svclinear_output[['id', 'hand']]

svclinear_output.to_csv("svclinear_output.csv", index=False, float_format='%.f')
