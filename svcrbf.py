import pandas as pd
from sklearn.svm import SVC

trainset = pd.read_csv("original_data/train.csv")
testset = pd.read_csv("original_data/test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]


clf_svcrbf = SVC(verbose=6)
clf_svcrbf.fit(trainset_vars, trainset_target)
print 'fit completed'

svcrbf_output = pd.DataFrame( clf_svcrbf.predict(testset_vars), columns = ['hand'] )
print 'predict completed'

svcrbf_output['id'] = testset_ids
svcrbf_output = svcrbf_output[['id', 'hand']]

svcrbf_output.to_csv("svcrbf_output.csv", index=False, float_format='%.f')
print 'output saved'
