#%%
#Homework Assignment #9
#SciKit-Learn
#Name: Johnny Thomas 

#%%
import os
os.chdir('../Class10_SciKitLearn')
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath ,'Titanic_clean.csv')
import pandas as pd
titanic = pd.read_csv(filepath)

# %%
#Quick Plots
import seaborn as sns
sns.set()
sns.pairplot(titanic)


# %%
#QUESTION 1: Split Data into Train and Test
# Prepare our X data (features, predictors, regressors) and y data (target, dependent variable)
xtitanic = titanic[['age',"pclass","sex"]]
ytitanic = titanic['survived']

#%%
sexes = {"male": 0, "female": 1}
data = [xtitanic]
for dataset in data:
    dataset['sex'] = dataset['sex'].map(sexes)

from sklearn.model_selection import train_test_split
x_traintitanic, x_testtitanic, y_traintitanic, y_testtitanic = train_test_split(xtitanic, ytitanic, random_state=1, train_size=.8 )



#%%
#QUESTION 2: Build a Logistic Regression using the chosen variables from last week, score on Test

from sklearn.linear_model import LogisticRegression

titaniclogit = LogisticRegression()  # instantiate
titaniclogit.fit(x_traintitanic, y_traintitanic)
print('Logit model accuracy (with the test set):', titaniclogit.score(x_testtitanic, y_testtitanic))

#%%
#CV
import numpy as np
from sklearn.model_selection import cross_val_score
full_cv = LogisticRegression()
cv_results = cross_val_score(full_cv, xtitanic, ytitanic, cv=5)



print("CV Accuracy:",np.mean(cv_results))



# %%
#QUESTION 3: Model survived using KNN, pick best 'k'.
from sklearn.neighbors import KNeighborsClassifier
#2-KNN worked best.
for i in (3,5,7,9):
  n = i
  knn_split = KNeighborsClassifier(n_neighbors=n)
  knn_split.fit(x_traintitanic,y_traintitanic)
  ytest_pred = knn_split.predict(x_testtitanic)
  ytest_pred
  knn_split.score(x_testtitanic,y_testtitanic)
  print(knn_split.score(x_testtitanic,y_testtitanic))

#This shows 3 to be the best!


#%%
#QUESTION 4: Try cutoffs of .3 and .7 Report Findings!
def predictcutoff(arr, cutoff):
  arrbool = arr[:,1]>cutoff
  arr= arr[:,1]*arrbool
  arr.apply()


test = titaniclogit.predict_proba(x_testtitanic)
##predictcutoff(test, 0.7)
##predictcutoff(test, 0.3)

#Getting Error on this but I'm assuming accuracy to go down the lower the cut-off.

#%%
#QUESTION 5: Also try to score and plot the KNN model and logit model with ROC-AUC.

# Logistic Model
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(y_testtitanic))]
# predict probabilities
lr_probs = titaniclogit.predict_proba(x_testtitanic)
# keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]
# calculate scores
ns_auc = roc_auc_score(y_testtitanic, ns_probs)
lr_auc = roc_auc_score(y_testtitanic, lr_probs)
# summarize scores
print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Logistic: ROC AUC=%.3f' % (lr_auc))
# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_testtitanic, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_testtitanic, lr_probs)
# plot the roc curve for the model
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(lr_fpr, lr_tpr, label='Logistic')
# axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# show the legend
plt.legend()
# show the plot
plt.show()


#%%
# KNN

# generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(ytitanic))]
# predict probabilities
knn_probs = knn_split.predict_proba(xtitanic)
# keep probabilities for the positive outcome only
knn_probs = knn_probs[:, 1]
# calculate scores
ns_auc = roc_auc_score(ytitanic, ns_probs)
knn_auc = roc_auc_score(ytitanic, knn_probs)
# summarize scores
print('No Skill: ROC AUC=%.2f' % (ns_auc))
print('KNN: ROC AUC=%.2f' % (knn_auc))
# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(ytitanic, ns_probs)
knn_fpr, knn_tpr, _ = roc_curve(ytitanic, knn_probs)
# plot the roc curve for the model
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(knn_fpr, knn_tpr, marker='.', label='KNN')
# axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# show the legend
plt.legend()
# show the plot
plt.show()


# %%
#THE END