#%%
# Standard quick checks
def dfChkBasics(dframe): 
  cnt = 1  
  try:
    print(str(cnt)+': info(): ')
    print(dframe.info())
  except: pass

  cnt+=1
  print(str(cnt)+': describe(): ')
  print(dframe.describe())

  cnt+=1
  print(str(cnt)+': dtypes: ')
  print(dframe.dtypes)

  try:
    cnt+=1
    print(str(cnt)+': columns: ')
    print(dframe.columns)
  except: pass

  cnt+=1
  print(str(cnt)+': head() -- ')
  print(dframe.head())

  cnt+=1
  print(str(cnt)+': shape: ')
  print(dframe.shape)

  # cnt+=1
  # print(str(cnt)+': columns.value_counts(): ')
  # print(dframe.columns.value_counts())

def dfChkValueCnts(dframe):
  cnt = 1
  for i in dframe.columns :
    print(str(cnt)+':', i, 'value_counts(): ')
    print(dframe[i].value_counts())
    cnt +=1

#%%
# First read in the datasets. 
# First read in the datasets. One Graduate school admission dataset, one Titanic survival dataset
import os
dirpath = os.getcwd() # print("current directory is : " + dirpath)
path2add = 'GWU_classes/DATS_6103_DataMining/Class11_Trees_SVM'
filepath = os.path.join( dirpath, path2add ,'gradAdmit.csv')
import numpy as np
import pandas as pd
dfadmit = pd.read_csv(filepath)
dfChkBasics(dfadmit)
# dfChkValueCnts(dfadmit)

# filepath = os.path.join( dirpath, path2add ,'Titanic.csv')
filepath = os.path.join( dirpath, path2add ,'Titanic_clean.csv')
dftitan = pd.read_csv(filepath)
# dfChkBasics(dftitan) # later
# dfChkValueCnts(dftitan) # later 

#%%
# Prepare our X data (features, predictors, regressors) and y data (target, dependent variable)
# xadmit = dfadmit[['gre', 'gpa']]
xadmit = dfadmit[['gre', 'gpa', 'rank']]
yadmit = dfadmit['admit']
# print(ydfadmit.head())
# These xdfadmit and ydfadmit are dataframes


#%%
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
# Import train_test_split
from sklearn.model_selection import train_test_split
# Import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report

# Split dataset into 80% train, 20% test
X_train, X_test, y_train, y_test= train_test_split(xadmit, yadmit, test_size=0.2, stratify=yadmit,random_state=1)

#%%
# Instantiate dtree
dtree_admit1 = DecisionTreeClassifier(max_depth=4, random_state=1)
# Fit dt to the training set
dtree_admit1.fit(X_train,y_train)
# Predict test set labels
y_pred = dtree_admit1.predict(X_test)
# Evaluate test-set accuracy
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#                         predicted 
#                   0                  1
# Actual 0   True Negative  TN      False Positive FP
# Actual 1   False Negative FN      True Positive  TP
# 
# Accuracy    = (TP + TN) / Total
# Precision   = TP / (TP + FP)
# Recall rate = TP / (TP + FN) = Sensitivity
# Specificity = TN / (TN + FP)
# F1_score is the "harmonic mean" of precision and recall
#          F1 = 2 (precision)(recall)/(precision + recall)

#%% [markdown]
#
# Considering the original dataset has 273 rejections and 127 acceptances out of 400 (68.25% and 31.75%) 
# respectively, the model accuracy here is really terrible. 
# From the scatterplot, one most likely will see admitted/rejected are scattered very close to each other 
# and have very little pattern to work with. 

#%% 
# Let us try different citeria...
# Instantiate dtree, try criterion='gini'  or 'entropy'
dtree_admit2 = DecisionTreeClassifier(criterion='entropy', random_state=1)
# Fit dt to the training set
dtree_admit2.fit(X_train,y_train)
# Predict test set labels
y_pred = dtree_admit2.predict(X_test)
# Evaluate test-set accuracy
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


#%%
# Instantiate dtree, try criterion='gini'  or 'entropy'
dtree_admit3 = DecisionTreeClassifier(criterion='entropy', max_depth=8, random_state=1)
# Fit dt to the training set
dtree_admit3.fit(X_train,y_train)
# Predict test set labels
y_pred = dtree_admit3.predict(X_test)
# Evaluate test-set accuracy
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


#%% 
# compare with logistic regression result
# Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import LogisticRegression

# Instatiate logitreg_admit
logitreg_admit = LogisticRegression(random_state=1)

# Fit logitreg_admit to the training set
logitreg_admit.fit(X_train, y_train)


#%%

# Use this plot function plot_labeled_decision_regions() defined in datacamp 
# which requires function plot_decision_regions from mlxtend.plotting
#
# !pip3 install mlxtend 
#

#%%
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt



#%%
# Now plot
# Review the decision regions of the two classifiers

#%%
# Plotting decision regions
plot_decision_regions(X_test.values, y_test.values, clf=logitreg_admit, legend=3, filler_feature_values={2:1} , filler_feature_ranges={2: 3} )
# filler_feature_values is used when you have more than 2 predictors, then 
# you need to specify the ones not shown in the 2-D plot. For us, 
# the rank is at poition 2, and the value can be 1, 2, 3, or 4.
# also need to specify the filler_feature_ranges for +/-, otherwise only data points with that feature value will be shown.

# Adding axes annotations
plt.xlabel(X_test.columns[0])
plt.ylabel(X_test.columns[1])
plt.title(logitreg_admit.__class__.__name__)
plt.show()

# And the decision tree result
plot_decision_regions(X_test.values, y_test.values, clf=dtree_admit1, legend=3, filler_feature_values={2:1} , filler_feature_ranges={2: 3} )
plt.xlabel(X_test.columns[0])
plt.ylabel(X_test.columns[1])
plt.title(dtree_admit1.__class__.__name__)
plt.show()


#%% [markdown]
# Notice that decision trees only make orthogonal cuts. 
# Try to change the depth of the tree, and see what happens. You can also try the gini and entropy criteria


#%%
# regression tree
import os
dirpath = os.getcwd() # print("current directory is : " + dirpath)
path2add = 'GWU_classes/DATS_6103_DataMining/Class11_Trees_SVM'
filepath = os.path.join( dirpath, path2add ,'Pizza.csv')
dfpizza = pd.read_csv(filepath)
import numpy as np
import pandas as pd
dfpizza = pd.read_csv(filepath)
# dfChkBasics(dfpizza)
# fChkValueCnts(dfpizza)


#%%
# Prepare our X data (features, predictors, regressors) and y data (target, dependent variable)
# xpizza = dfpizza[['mois', 'prot', 'fat', 'ash', 'sodium', 'carb']]
xpizza = dfpizza[['prot', 'fat', 'sodium']]
# xpizza = dfpizza[['prot', 'fat', 'carb']]
# xpizza = dfpizza[['fat', 'carb', 'sodium']]
# xpizza = dfpizza[['fat', 'carb']]
# print(xdfpizza.head())
ypizza = dfpizza['cal']
# print(ydfpizza.head())
# print(type(xpizza))
# print(type(ypizza))
# These xdfpizza and ydfpizza are dataframes

#%%
# Or try seaborn
import seaborn as sns
sns.set()
sns.pairplot(dfpizza)

#%%
# Regression Trees

from sklearn.tree import DecisionTreeRegressor  # Import DecisionTreeRegressor
from sklearn.model_selection import train_test_split  # Import train_test_split
from sklearn.metrics import mean_squared_error as MSE  # Import mean_squared_error as MSE
# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test= train_test_split(xpizza, ypizza, test_size=0.2,random_state=1)
# Instantiate a DecisionTreeRegressor 'regtree0'
regtree0 = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.1,random_state=22) # set minimum leaf to contain at least 10% of data points
# DecisionTreeRegressor(criterion='mse', max_depth=8, max_features=None,
#     max_leaf_nodes=None, min_impurity_decrease=0.0,
#     min_impurity_split=None, min_samples_leaf=0.13,
#     min_samples_split=2, min_weight_fraction_leaf=0.0,
#     presort=False, random_state=3, splitter='best')


regtree0.fit(X_train, y_train)  # Fit regtree0 to the training set
# Import mean_squared_error from sklearn.metrics as MSE
from sklearn.metrics import mean_squared_error as MSE

# evaluation
y_pred = regtree0.predict(X_test)  # Compute y_pred
mse_regtree0 = MSE(y_test, y_pred)  # Compute mse_regtree0
rmse_regtree0 = mse_regtree0 ** (.5) # Compute rmse_regtree0
print("Test set RMSE of regtree0: {:.2f}".format(rmse_regtree0))

#%%
# Let us compare the performance with OLS
from sklearn import linear_model
olspizza = linear_model.LinearRegression() 
olspizza.fit( X_train, y_train )

y_pred_ols = olspizza.predict(X_test)  # Predict test set labels/values

mse_ols = MSE(y_test, y_pred_ols)  # Compute mse_ols
rmse_ols = mse_ols**(0.5)  # Compute rmse_ols

print('Linear Regression test set RMSE: {:.2f}'.format(rmse_ols))
print('Regression Tree test set RMSE: {:.2f}'.format(rmse_regtree0))

# You can try to include different ingredients, and see how the two compare. 
# If you include both 'carb' and 'fat', the OLS model is almost perfect. Reg Tree cannot compete there. 
# In most other combinations, Reg Tree is measured up against OLS pretty good.

#%% [markdown]
#
# #  Bias-variance tradeoff  
#
# high bias: underfitting  
#
# high variance: overfitting, too much complexity  
#
# Generalization Error = (bias)^2 + Variance + irreducible error  
# 
# Solution: Use CV  
# 
# 1. If CV error (average of 10- or 5-fold) > training set error  
#   - high variance
#   - overfitting the training set
#   - try to decrease model complexity
#   - decrease max depth
#   - increase min samples per leaf
#   - get more data
# 2. If CV error approximates the training set error, and greater than desired error
#   - high bias
#   - underfitting the training set
#   - increase max depth
#   - decrease min samples per leaf
#   - use or gather more relevant features


#%%
# We already have train-test split at 75-25%, let us compare the result with 10-fold CV average
# Split the data into 70% train and 30% test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Instantiate a DecisionTreeRegressor dt
SEED = 28
regtree1 = DecisionTreeRegressor(max_depth=5, min_samples_leaf=0.13, random_state=SEED)

# Evaluate the list of MSE ontained by 10-fold CV
from sklearn.model_selection import cross_val_score
# Set n_jobs to -1 in order to exploit all CPU cores in computation
MSE_CV = - cross_val_score(regtree1, X_train, y_train, cv= 10, scoring='neg_mean_squared_error', n_jobs = -1)
regtree1.fit(X_train, y_train)  # Fit 'regtree1' to the training set
y_predict_train = regtree1.predict(X_train)  # Predict the labels of training set
y_predict_test = regtree1.predict(X_test)  # Predict the labels of test set

print('CV RMSE:', MSE_CV.mean()**(0.5) )  #CV MSE 
print('Training set RMSE:', MSE(y_train, y_predict_train)**(0.5) )   # Training set MSE
print('Test set RMSE:', MSE(y_test, y_predict_test)**(0.5) )   # Test set MSE 

#%%
# Is it high bias? high variance? 
# If so, change some parameters and try?

# Other topics:
# bagging
# boosting
# tuning, pruning


#%%
# Graphing the tree
from sklearn.tree import export_graphviz  
  
# export the decision tree to a tree.dot file 
# for visualizing the plot easily anywhere 
# import os
# dirpath = os.getcwd() # print("current directory is : " + dirpath)
# path2add = 'GWU_classes/DATS_6103_DataMining/Class11_Trees_SVM'
filepath = os.path.join( dirpath, path2add ,'tree1')
export_graphviz(regtree1, out_file = filepath+'.dot' , feature_names =['prot', 'fat', 'sodium']) 

# can't get it to work yet
# pip3 install pydot
# https://graphviz.gitlab.io/download/
# import pydot

# (graph,) = pydot.graph_from_dot_file(filepath)
# graph.write_png(filepath+'.png')



#%% 
#  SVM - Support Vector Machines

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# import plot_iris_svc python functions
# import classifierPlots.py

clf1 = LogisticRegression()
clf2 = LinearSVC()
clf3 = SVC(kernel="linear")
clf4 = SVC()
clf5 = DecisionTreeClassifier()
clf6 = KNeighborsClassifier(n_neighbors=3) 
classifiers = [clf1,clf2] # use even numbers to avoid issue for now
# classifiers.append(clf3)
classifiers.append(clf4)
classifiers.append(clf5)
# classifiers.append(clf6)
# You can try adding clf3 and clf6, but KNN takes a long time to render.

xadmit2 = dfadmit[['gre', 'gpa']]  # just two features so that we can plot 2-D easily
# yadmit = dfadmit['admit']

# Fit the classifiers
for c in classifiers:
    c.fit(xadmit2,yadmit)

# Plot the classifiers
plot_classifiers(xadmit2.values, yadmit.values, classifiers)
# plt.show()


#%% 
#  SVM - Support Vector Machines
#  SVC - Support Vector Classifier
# (SVR - Support Vector Regressor)
# Concepts: 
# Loss function
# Linear SVC  ( SVC(kernel='linear')   or linearSVC  )
# classifier that are linear separable
# (non-linear) SVC
# transformed features might be linearly separable
# Kernel SVM
# RBF  Radial Basis Function
# gamma small - smooth. (default=1)



#%%


