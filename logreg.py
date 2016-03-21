import pandas as pd
from sklearn.linear_model import LogisticRegression

trainset = pd.read_csv("original_data/train.csv")
testset = pd.read_csv("original_data/test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]

clf_logreg = LogisticRegression(verbose=6)
clf_logreg.fit(trainset_vars, trainset_target)

logreg_output = pd.DataFrame( clf_logreg.predict(testset_vars), columns = ['hand'] )
logreg_output['id'] = testset_ids
logreg_output = logreg_output[['id', 'hand']]

logreg_output.to_csv("logreg_output.csv", index=False, float_format='%.f')
