import pandas as pd
from sklearn.ensemble import RandomForestClassifier

trainset = pd.read_csv("original_data/train.csv")
testset = pd.read_csv("original_data/test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]


clf_rf = RandomForestClassifier(n_estimators = 500, verbose=6)
clf_rf.fit(trainset_vars, trainset_target)

rf_output = pd.DataFrame( clf_rf.predict(testset_vars), columns = ['hand'] )
rf_output['id'] = testset_ids
rf_output = rf_output[['id', 'hand']]

rf_output.to_csv("rf_output.csv", index=False, float_format='%.f')
