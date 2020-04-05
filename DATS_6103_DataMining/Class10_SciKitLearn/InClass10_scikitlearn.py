#%% [markdown]
# shell install scikit-learn
# https://scikit-learn.org/stable/install.html  
#
# Scikit-learn requires:
# * Python (>= 3.5)
# * NumPy (>= 1.11.0)
# * SciPy (>= 0.17.0)
# * joblib (>= 0.11)
#
# You can check what is installed on your system by shell command
# pip list 
# pip freeze
# 
# Since we already have scipy and numpy installed, simply do this
# pip3 install -U scikit-learn
# pip install -U scikit-learn
# OR
# conda install scikit-learn 


#%%
# Standard quick checks
def dfChkBasics(dframe, valCnt = False): 
  cnt = 1
  print('\ndataframe Basic Check function -')
  
  try:
    print(f'\n{cnt}: info(): ')
    cnt+=1
    print(dframe.info())
  except: pass

  print(f'\n{cnt}: describe(): ')
  cnt+=1
  print(dframe.describe())

  print(f'\n{cnt}: dtypes: ')
  cnt+=1
  print(dframe.dtypes)

  try:
    print(f'\n{cnt}: columns: ')
    cnt+=1
    print(dframe.columns)
  except: pass

  print(f'\n{cnt}: head() -- ')
  cnt+=1
  print(dframe.head())

  print(f'\n{cnt}: shape: ')
  cnt+=1
  print(dframe.shape)

  if (valCnt):
    print('\nValue Counts for each feature -')
    for colname in dframe.columns :
      print(f'\n{cnt}: {colname} value_counts(): ')
      print(dframe[colname].value_counts())
      cnt +=1

# examples:
# dfChkBasics(df)

#%%
# First read in the datasets. 
import os
os.chdir('../Class10_SciKitLearn')
dirpath = os.getcwd() # print("current directory is : " + dirpath)
# path2add = 'GWU_classes_p/DATS_6103_DataMining/Class10_SciKitLearn'
filepath = os.path.join( dirpath,'Pizza.csv')
import pandas as pd
dfpizza = pd.read_csv(filepath)
dfChkBasics(dfpizza)
# fChkValueCnts(dfpizza)

#%% [markdown]
# The dataset is clean. No missing values.  

# Pizza.csv
# from data.world (ret 11/8/2019) 
# @sdhilip

# Nutrient analysis of pizzas

# brand -- Pizza brand (class label)  
# id -- Sample analysed  
# mois -- Amount of water per 100 grams in the sample  
# prot -- Amount of protein per 100 grams in the sample  
# fat -- Amount of fat per 100 grams in the sample  
# ash -- Amount of ash per 100 grams in the sample  
# sodium -- Amount of sodium per 100 grams in the sample  
# carb -- Amount of carbohydrates per 100 grams in the sample  
# cal -- Amount of calories per 100 grams in the sample  


#%%
# Last time we were using the statsmodel library and the functions there, 
# let us try scikit-learn this time.

#%%
# Prepare our X data (features, predictors, regressors) and y data (target, dependent variable)
xpizza = dfpizza[['mois', 'prot', 'fat', 'ash', 'sodium', 'carb']]
# print(xdfpizza.head())
ypizza = dfpizza['cal']
# print(ydfpizza.head())
print(type(xpizza))
print(type(ypizza))
# These xdfpizza and ydfpizza are dataframes

#%%
# quick plots
import matplotlib.pyplot as plt
# add color
import numpy as np

plt.scatter(xpizza.iloc[:,1].values,ypizza.values)

#%%
# Or try pandas
from pandas.plotting import scatter_matrix
scatter_matrix(xpizza, alpha = 0.2, figsize = (7, 7), diagonal = 'hist')
# scatter_matrix(dfpizza.iloc[:,2:], alpha = 0.2, figsize = (7, 7), diagonal = 'kde')
# the first twol exluded columns are brand and id

#%%
# Or try seaborn
import seaborn as sns
sns.set()
sns.pairplot(xpizza)




#%%
# There are a lot of interesting relationships shown here. 
# But let us first try the basic linear regression using sklearn
import numpy as np
from sklearn import linear_model
fatcalfit = linear_model.LinearRegression()  # instantiate the object, with full functionality

xfat = dfpizza.iloc[:,4].values.reshape(-1,1)
ycal = dfpizza.iloc[:,-1].values.reshape(-1,1)
# check
print('xfat type is ',type(xfat))
print('ycal type is ',type(ycal))

fatcalfit.fit( xfat , ycal )
fatcalfit.score( xfat, ycal)
# .score is the generic method of evaluating models in sklearn
# for linear regression, it is R^2 value. 
# This is a simple linear model with one predictor we have.

#%%
print(fatcalfit.intercept_)
print(fatcalfit.coef_)
# intercept_ , coef_ , predict, and score are the most common methods we use with the lm object

#%% [markdown]
# # sklearn does not give p-values for each regressor's coefficient
# 
# nor other statistics such as skewness, etc. The statsmodel library handle those as we 
# learned last time. You can find some get-around solutions...
# 
#%%
# plot, and regression line
prediction_grid = np.linspace(min(xfat),max(xfat)).reshape(-1,1)

plt.scatter(xfat,ycal, color="blue")
plt.plot(prediction_grid, fatcalfit.predict(prediction_grid), color="red", linewidth = 3)

#%%
# Let us now try multiple regression
# We can actually use the full dataframe in the linearRegression function.
# Just when you have only one column, then it is not a pd dataframe, it is a pd series, 
# which requires some extra attention.

fullfit = linear_model.LinearRegression()  # a new instance of the object
fullfit.fit( xpizza , ycal )
print('score:', fullfit.score( xpizza, ycal )) # 0.9993590486296579
print('intercept:', fullfit.intercept_)  # [6.17023085]
print('coef_:', fullfit.coef_)  # [[-0.06179035 -0.0215788   0.0284689  -0.06169822 -0.0031912  -0.02162895]]

#%%
# You can make a small df to store the coef_ and print them out.
coeff_df = pd.DataFrame(fullfit.coef_ , columns=xpizza.columns )  
coeff_df['notes'] = ['linear model full fit']
coeff_df



#%%
# Let us also do the model evaluation using train and test sets from the early on
from sklearn.model_selection import train_test_split

X_train1, X_test1, y_train1, y_test1 = train_test_split(xpizza, ypizza, test_size = 0.25, random_state=2020)
full_split1 = linear_model.LinearRegression() # new instancew
full_split1.fit(X_train1, y_train1)
y_pred1 = full_split1.predict(X_test1)
full_split1.score(X_test1, y_test1)

print('score:', full_split1.score(X_test1, y_test1)) # 0.9980384387631105
print('intercept:', full_split1.intercept_) # 5.4722114861507745
print('coef_:', full_split1.coef_)  # [-0.05476668 -0.01457834  0.03529162 -0.05513429  0.00136433 -0.01472148]




#%% 
# Try other split test_size at 0.20, 0.10, and 0.05

# Add the new results to the coeff_df


#%%

# Add the new results to the coeff_df


#%%


# Add the new results to the coeff_df



#%% 
from sklearn.model_selection import cross_val_score
full_cv = linear_model.LinearRegression()
cv_results = cross_val_score(full_cv, xpizza, ypizza, cv=5)
print(cv_results) # [0.99982467 0.99014869 0.98341804 0.99957296 0.99898658]
np.mean(cv_results) # 0.9943901862799376


#%%
# Logistic Regression
import os
os.chdir('../Class10_SciKitLearn');
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath ,'gradAdmit.csv')
import pandas as pd
dfadmit = pd.read_csv(filepath)

#%%
# From last week, we used statsmodels.api
import statsmodels.api as sm  # Importing statsmodels
# import statsmodels.formula.api as smf  # Support for formulas
# from statsmodels.formula.api import glm   # Use glm() directly

# FORMULA based (we had been using this for ols)
from statsmodels.formula.api import glm
# model = glm(formula, data, family)

modelAdmitGreLogitFit = glm(formula='admit ~ gre', data=dfadmit, family=sm.families.Binomial()).fit()
print( modelAdmitGreLogitFit.summary() )
modelpredicitons = pd.DataFrame( columns=['admit_GreGpaLogit'], data= modelAdmitGreLogitFit.predict(dfadmit)) 
print(modelpredicitons.head())
dfChkBasics(modelpredicitons)


#%% 
# Let's try logistic regression again with sklearn instead of statsmodel

# Prepare our X data (features, predictors, regressors) and y data (target, dependent variable)
xadmit = dfadmit[['gre', 'gpa', 'rank']]
yadmit = dfadmit['admit']
print(type(xadmit))
print(type(yadmit))
# These xdfadmit and ydfadmit are dataframes


#from sklearn.model_selection import train_test_split
x_trainAdmit, x_testAdmit, y_trainAdmit, y_testAdmit = train_test_split(xadmit, yadmit, random_state=1 )

print('x_trainAdmit type',type(x_trainAdmit))
print('x_trainAdmit shape',x_trainAdmit.shape)
print('x_testAdmit type',type(x_testAdmit))
print('x_testAdmit shape',x_testAdmit.shape)
print('y_trainAdmit type',type(y_trainAdmit))
print('y_trainAdmit shape',y_trainAdmit.shape)
print('y_testAdmit type',type(y_testAdmit))
print('y_testAdmit shape',y_testAdmit.shape)

#%%
# Logit
from sklearn.linear_model import LogisticRegression

admitlogit = LogisticRegression()  # instantiate
admitlogit.fit(x_trainAdmit, y_trainAdmit)
print('Logit model accuracy (with the test set):', admitlogit.score(x_testAdmit, y_testAdmit))

#%%
# Bonus 5 points for your HW scores (added to your total HW scores.
# #
# 

#%%
# Classification Report
#
from sklearn.metrics import classification_report
y_true, y_pred = y_testAdmit, admitlogit.predict(x_testAdmit)
print(classification_report(y_true, y_pred))

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


#%%
# Precision-Recall vs Threshold

y_pred=admitlogit.predict(x_testAdmit)

y_pred_probs=admitlogit.predict_proba(x_testAdmit) 
  # probs_y is a 2-D array of probability of being labeled as 0 (first 
  # column of array) vs 1 (2nd column in array)

from sklearn import metrics
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = precision_recall_curve(y_testAdmit, y_pred_probs[:, 1]) 
   #retrieve probability of being 1(in second column of probs_y)
pr_auc = metrics.auc(recall, precision)

plt.title("Precision-Recall vs Threshold Chart")
plt.plot(thresholds, precision[: -1], "b--", label="Precision")
plt.plot(thresholds, recall[: -1], "r--", label="Recall")
plt.ylabel("Precision, Recall")
plt.xlabel("Threshold")
plt.legend(loc="lower left")
plt.ylim([0,1])


#%%
# Receiver Operator Characteristics (ROC)
# Area Under the Curve (AUC)
from sklearn.metrics import roc_auc_score, roc_curve

# generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(y_testAdmit))]
# predict probabilities
lr_probs = admitlogit.predict_proba(x_testAdmit)
# keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]
# calculate scores
ns_auc = roc_auc_score(y_testAdmit, ns_probs)
lr_auc = roc_auc_score(y_testAdmit, lr_probs)
# summarize scores
print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Logistic: ROC AUC=%.3f' % (lr_auc))
# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_testAdmit, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_testAdmit, lr_probs)
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
# Another standard (built-in) example
# this classifier target has 3 possible outcomes
import sklearn.datasets
wine = sklearn.datasets.load_wine()
print(wine)

#%%
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(wine.data, wine.target)
lr.score(wine.data, wine.target) # accuracy score

# We can also get the probability for each row, or being class0, class1, or class2
lr.predict_proba(wine.data[:10]) # predicted 




#%%
# KNN   on  admissions data
# number of neighbors
mrroger = 7

 #%%
# KNN algorithm
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=mrroger) # instantiate with n value given
knn.fit(xadmit,yadmit)
y_pred = knn.predict(xadmit)
print(y_pred)
knn.score(xadmit,yadmit)

#%%
# 2-KNN algorithm
# The better way
# from sklearn.neighbors import KNeighborsClassifier
knn_split = KNeighborsClassifier(n_neighbors=mrroger) # instantiate with n value given
knn_split.fit(x_trainAdmit,y_trainAdmit)
ytest_pred = knn_split.predict(x_testAdmit)
ytest_pred
knn_split.score(x_testAdmit,y_testAdmit)

# Try different n values


#%%
# 3-KNN algorithm
# The best way
from sklearn.neighbors import KNeighborsClassifier
knn_cv = KNeighborsClassifier(n_neighbors=mrroger) # instantiate with n value given

from sklearn.model_selection import cross_val_score
cv_results = cross_val_score(knn_cv, xadmit, yadmit, cv=5)
print(cv_results) 
np.mean(cv_results) 



#%%
# 4-KNN algorithm
# Scale first? better or not?

# Re-do our darta with scale on X
from sklearn.preprocessing import scale
xsadmit = pd.DataFrame( scale(xadmit), columns=xadmit.columns )  # reminder: xadmit = dfadmit[['gre', 'gpa', 'rank']]
# Note that scale( ) coerce the object from pd.dataframe to np.array  
# Need to reconstruct the pandas df with column names
# xsadmit.rank = xadmit.rank
ysadmit = yadmit.copy()  # no need to scale y, but make a true copy to be safe

#%%
# from sklearn.neighbors import KNeighborsClassifier
knn_scv = KNeighborsClassifier(n_neighbors=mrroger) # instantiate with n value given

# from sklearn.model_selection import cross_val_score
scv_results = cross_val_score(knn_scv, xsadmit, ysadmit, cv=5)
print(scv_results) 
np.mean(scv_results) 


#%%
# Your turn. 
# (1) Use the admit dataset to predict survival of the titanic passenger?
# (2) Use the admit dataset to classify the pclass of the titanic passenger?
# (3) Use the wine dataset to classify the target class ['class_0', 'class_1', 'class_2']
# Try both unscaled and scaled data, 
# Only need to do the CV method for in all cases. 
# (4) Now we have logit and KNN models to predict admit in the first dataset, and 
# the class for the wine dataset, compare the accuracies of these results 
# with the logit regression results.





#%%
# K-means 
# 
from sklearn.cluster import KMeans

km_xpizza = KMeans( n_clusters=3, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0 )
y_km = km_xpizza.fit_predict(xpizza)

#%%
# plot
# plot the 3 clusters
index1 = 2
index2 = 3

plt.scatter( xpizza[y_km==0].iloc[:,index1], xpizza[y_km==0].iloc[:,index2], s=50, c='lightgreen', marker='s', edgecolor='black', label='cluster 1' )

plt.scatter( xpizza[y_km==1].iloc[:,index1], xpizza[y_km==1].iloc[:,index2], s=50, c='orange', marker='o', edgecolor='black', label='cluster 2' )

plt.scatter( xpizza[y_km==2].iloc[:,index1], xpizza[y_km==2].iloc[:,index2], s=50, c='lightblue', marker='v', edgecolor='black', label='cluster 3' )

# plot the centroids
plt.scatter( km_xpizza.cluster_centers_[:, index1], km_xpizza.cluster_centers_[:, index2], s=250, marker='*', c='red', edgecolor='black', label='centroids' )
plt.legend(scatterpoints=1)
plt.xlabel(str(index1) + " : " + xpizza.columns[index1])
plt.ylabel(str(index2) + " : " + xpizza.columns[index2])
plt.grid()
plt.show()



  
#%%
