#%%
# Logistic Regression
import os
os.chdir('../Class10_SciKitLearn')
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath ,'Titanic_clean.csv')
import pandas as pd
titanic = pd.read_csv(filepath)


# %%
# Prepare our X data (features, predictors, regressors) and y data (target, dependent variable)
#We are only including variables we found significant last week
xTin = titanic[['pclass', 'sex', 'age', 'sibsp']]
yTin = titanic['survived']

xTin['sex'] = xTin['sex'].astype('category')
#TODO HOW TO change sex and pclass to categorical...

# %%
#Quick Plots
import seaborn as sns
sns.set()
sns.pairplot(xTin)

# %%
#QUESTION 1: Split Data into Train and Test
from sklearn.model_selection import train_test_split

x_trainTin, x_testTin, y_trainTin, y_testTin = train_test_split(xTin, yTin, random_state=1 )

# %%
#QUESTION 2: Build a Logistic Regression using the chosen variables from last week, score on Test

from sklearn.linear_model import LogisticRegression

Tinlogit = LogisticRegression()  # instantiate
Tinlogit.fit(x_trainTin, y_trainTin)
print('Logit model accuracy (with the test set):', Tinlogit.score(x_testTin, y_testTin))

#%%
print(Tinlogit.predict(x_testTin))

#%%
print(Tinlogit.predict_proba(x_trainTin[:8]))
print(Tinlogit.predict_proba(x_testTin[:8]))

#%%
test = Tinlogit.predict_proba(x_testTin)
type(test)



# %%
#QUESTION 3: Model survived using KNN, pick best 'k'.


#%%
#QUESTION 4: Try cutoffs of .3 and .7 Report Findings!
def predictcutoff(arr, cutoff):
  arrbool = arr[:,1]>cutoff
  arr= arr[:,1]*arrbool
  arr.apply()

predictcutoff(test, 0.5)


#%%
#QUESTION 5: Also try to score and plot the KNN model and logit model with ROC-AUC.

# Receiver Operator Characteristics (ROC)
# Area Under the Curve (AUC)
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt


#%%
###LOGIT MODEL
# generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(y_testTin))]
# predict probabilities
lr_probs = Tinlogit.predict_proba(x_testTin)
# keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]
# calculate scores
ns_auc = roc_auc_score(y_testTin, ns_probs)
lr_auc = roc_auc_score(y_testTin, lr_probs)
# summarize scores
print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Logistic: ROC AUC=%.3f' % (lr_auc))
# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_testTin, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_testTin, lr_probs)
# plot the roc curve for the model
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')
# axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# show the legend
plt.legend()
# show the plot
plt.show()


#%% 
#KNN

