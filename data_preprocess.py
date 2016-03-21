import pandas as pd

trainset_path = "original_data/train.csv"
testset_path = "original_data/test.csv"

trainset = pd.read_csv(trainset_path)
testset = pd.read_csv(testset_path)

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]] / [4,13,4,13,4,13,4,13,4,13]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]] / [4,13,4,13,4,13,4,13,4,13]

# print trainset_target.head(6)
# print trainset_vars.head(6)
# print testset_ids.head(6)
# print testset_vars.head(6)

trainset_target.to_csv("cleaned_data/trainset_vars.csv")
trainset_vars.to_csv("cleaned_data/trainset_target.csv")
testset_ids.to_csv("cleaned_data/testset_ids.csv")
testset_vars.to_csv("cleaned_data/testset_vars.csv")
