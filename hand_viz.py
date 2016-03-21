import pandas as pd
from sklearn.ensemble import RandomForestClassifier


trainset = pd.read_csv("train.csv")
testset = pd.read_csv("test.csv")

trainset_target = trainset.hand
trainset_vars = trainset[trainset.columns[:10]]
testset_ids = testset.id
testset_vars = testset[testset.columns[1:]]

# test_hand = trainset.iloc[0]
test_hand = trainset[trainset.hand >= 8].iloc[1]
print test_hand


output = [[],[],[],[],[]]

output[test_hand.S1] += [test_hand.C1]
output[test_hand.S2] += [test_hand.C2]
output[test_hand.S3] += [test_hand.C3]
output[test_hand.S4] += [test_hand.C4]
output[test_hand.S5] += [test_hand.C5]

print output

rank = { 1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
        9:'9', 10:'10', 11:'J', 12:'Q', 13:'K', 14:'A' }

index = 0
pretty_print = ''
for s in output:
    if len(s) > 0:
        index = index + 1
        pretty_print += ( "  " + str(index) + ": ")
        s = [14 if x == 1 else x for x in s]
        s.sort(reverse=True)
        for c in s:
            pretty_print += rank[c] + ","

print pretty_print

# print("## \033[0;32m  1: A,K,Q,8  \033[0;35m 3: 7\033[00m .")





# test rules :  decision tree
#
# if all cards all in a row (straight)
#   if at least 4 cards are same suit:
#      if highest card is ace then 9
#         else 8
#     else 7

# if at least 4 cards are same suit then 6
#
# if three of kind
#     check if also full house then 5 else 4
#
# if pair
#    if two pair then 3 else 2
#
# else 1
