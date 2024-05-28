# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:46:40 2023

@author: geron
"""

#  an dimportant step to measure the models predictive power we must calculate common evaluation metrics for classification
#  problems.  We do so by split data into training, validation and test sets.  Using TP, TN, FP, FN
#  A common way to visualize the true positive, true negative, false positive, false negative is witha  confusion matrix
#  in a confusion matrix the predicted classes are represented as columns and the actuall classes are represented as rows

from sklearn.metrics import confusion_matrix

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  if actual[i] == 1 and predicted[i] == 1:
    true_positives += 1
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1


print(true_positives,true_negatives,false_positives,false_negatives)

conf_matrix = confusion_matrix(actual,predicted)
print(conf_matrix)



#  determin accuracy    Accuracy = (TP + TN) / (TP +FP + TN + FN)  - defined as number of correct classifications out of
#  all classifications

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  #True Positives
  if actual[i] == 1 and predicted[i] == 1:
    true_positives += 1
  #True Negatives
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1 
  #False Positives
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1
  #False Negatives
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1
  
accuracy = (true_positives + true_negatives) / (true_positives + false_positives + true_negatives + false_negatives)
print(accuracy)




#  Recall    Recall = TP / (TP + FN)

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  if actual[i] == 1 and predicted[i] == 1:
    true_positives += 1
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1

recall = true_positives / (true_positives + false_negatives)
print(recall)



#  precision   Precision = TP / (TP + FP) - defined as the number of relevant items out of all items

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  if actual[i] == 1 and predicted[i] == 1:
    true_positives += 1
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1

precision = true_positives / (true_positives + false_positives)
print(precision)



#f1 score   F1 Score - weighted average of precision and recall
#  f1 = 2 * precision * recall / precision + recall
#  harmonic mean for f1 score - makes the f1 score low when either precision or recall is low

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  if actual[i] == 1 and predicted[i] == 1:
    true_positives += 1
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1

precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)

f_1 = 2*precision*recall/(precision+recall)

print(f_1)



from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

print(accuracy_score(actual,predicted))

print(recall_score(actual,predicted))
print(precision_score(actual,predicted))
print(f1_score(actual,predicted))







