import pandas as pd
from sklearn.linear_model import SGDClassifier

trainset = pd.read_csv("original_data/train.csv")
testset = pd.read_csv("original_data/test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]


clf_sgd = SGDClassifier(verbose=6)
clf_sgd.fit(trainset_vars, trainset_target)
print 'fit completed'

sgd_output = pd.DataFrame( clf_sgd.predict(testset_vars), columns = ['hand'] )
print 'predict completed'

sgd_output['id'] = testset_ids
sgd_output = sgd_output[['id', 'hand']]

sgd_output.to_csv("sgd_output.csv", index=False, float_format='%.f')
print 'output saved'
