# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

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
# First read in the datasets. One Graduate school admission dataset, one Titanic survival dataset
import os
dirpath = os.getcwd() # print("current directory is : " + dirpath)
path2add = 'GWU_classes/DATS_6103_DataMining/Class09_Regression'
filepath = os.path.join( dirpath, path2add ,'gradAdmit.csv')
import pandas as pd
dfadmit = pd.read_csv(filepath)
dfChkBasics(dfadmit)
dfChkValueCnts(dfadmit)

# filepath = os.path.join( dirpath, path2add ,'Titanic.csv')
filepath = os.path.join( dirpath, path2add ,'Titanic_clean.csv')
dftitan = pd.read_csv(filepath)
# dfChkBasics(dftitan) # later
# dfChkValueCnts(dftitan) # later 

#%%
# dftitan_clean = dftitan[dftitan.age > 0]
# print(dftitan_clean.shape)
# dftitan_clean.to_csv(os.path.join( dirpath, path2add ,'Titanic_clean.csv'))
# dfChkBasics(dftitan_clean)

#%%
# quick plots
import matplotlib.pyplot as plt
# add color
import numpy as np
admitcolors = np.where(dfadmit['admit']==1,'g','r')
# admitcolors[dfadmit['admit']==0] = 'r'
# admitcolors[dfadmit['admit']==1] = 'g'

#%%
# plt.plot(x,y, 'r-o')  # red, solid line, circle dots
# OR
# more object-oriented
fig, axis = plt.subplots()
axis.plot(dfadmit.gre, dfadmit.gpa, color='g', linestyle="", marker="o", markersize=3)
plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()

#%% 
# OR Pandas style (or seaborn sns)
dfadmit.plot(x="gre", y="gpa", kind="scatter", color=admitcolors)
plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()

#%% 
# color by rank
rankcolors = np.where(dfadmit['rank']==1,'r','-') # initialize the vector as well
# rankcolors[dfadmit['rank']==1] = 'r'
rankcolors[dfadmit['rank']==2] = 'g'
rankcolors[dfadmit['rank']==3] = 'b'
rankcolors[dfadmit['rank']==4] = 'yellow'

# and use different shape for admit 0 and 1
ax1 = dfadmit[dfadmit.admit==0].plot(x="gre", y="gpa", kind="scatter", color=rankcolors[dfadmit.admit==0], marker='+', label='rejected')
dfadmit[dfadmit.admit==1].plot(x="gre", y="gpa", kind="scatter", color=rankcolors[dfadmit.admit==1], marker='o', label='admitted', ax = ax1)
# dfadmit.plot(x="gre", y="gpa", kind="scatter", color=rankcolors, marker='+')
plt.legend(loc='upper left')
plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()

#%%
# Let us also try using seaborn to make some quick plots
import seaborn as sns

sns.regplot('gre', 'gpa', data = dfadmit, x_jitter = 5,fit_reg = True, line_kws = {'color':'red', 'label':'LM fit'})

#%% 
# Now LINEAR REGRESSION
# 1. Describe the model → ols()
# 2. Fit the model → .fit()
# 3. Summarize the model → .summary()
# 4. Make model predictions → .predict()


# FORMULA based
from statsmodels.formula.api import ols
modelGreGpa = ols(formula='gre ~ gpa', data=dfadmit).fit()
print( modelGreGpa.summary() )

# From the summary, try to get as much info as we can
# Df Residuals (# total observations minus Df Model minus 1)
# Df Model (# of x variables)
# R-squared, what does that mean?
# Adj R-squared
# F-statistics
# Prob (F-statistics), ie. p-value for F-statistics
# Log-Likelihood
# AIC (model eval)
# BIC (model eval)

# coef
# std err
# t
# P>|t|, aka p-value for the coefficient significance
# 95% confidence intervals

# Omnibus - close to zero means residuals are normally distributed
# Prob(Omnibus) - close to 1 means residuals are normally distributed
# skew (positive is right tailed, negative is left)
# Kurtosis (tailedness, normal dist = 3, less than 3 is fatter tail, and flat top.)

#%% 
modelpredicitons = pd.DataFrame( columns=['gre_GpaLM'], data= modelGreGpa.predict(dfadmit.gpa)) 
# use the original dataset gpa data to find the expected model values
print(modelpredicitons.shape)
print( modelpredicitons.head() )

#%%
# Next let us try more variables
modelGreGpaRank = ols(formula='gre ~ gpa + rank', data=dfadmit).fit()
print( modelGreGpaRank.summary() )
modelpredicitons['gre_GpaRankLM'] = modelGreGpaRank.predict(dfadmit)
print(modelpredicitons.head())

#%%
# And let us check the VIF value (watch out for multicollinearity issues)
# Import functions
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Get variables for which to compute VIF and add intercept term
X = dfadmit[['gpa', 'rank']]
X['Intercept'] = 1

# Compute and view VIF
vif = pd.DataFrame()
vif["variables"] = X.columns
vif["VIF"] = [ variance_inflation_factor(X.values, i) for i in range(X.shape[1]) ] # list comprehension

# View results using print
print(vif)


#%% [markdown]
# But rank really should be categorical. 
# 
# # Patsy coding
# 
# * Strings and booleans are automatically coded
# * Numerical → categorical
#   * C() function
#   * level 0 → (0,0,0,...)
#   * level 1 → (1,0,0,...)
#   * level 2 → (0,1,0,...)
# * Reference group
#   * Default: first group
#   * Treatment
#   * levels

#%%
modelGreGpaCRank = ols(formula='gre ~ gpa + C(rank)', data=dfadmit).fit()
print( modelGreGpaCRank.summary() )
modelpredicitons['gre_GpaCRankLM'] = modelGreGpaCRank.predict(dfadmit)
print(modelpredicitons.head())


#%%
# Next try some interaction terms
# 
# formula = 'y ~ x1 + x2'
# C(x1) : treat x1 as categorical variable
# -1 : remove intercept
# x1:x2 : an interaction term between x1 and x2
# x1*x2 : an interaction term between x1 and x2 and the individual variables
# np.log(x1) : apply vectorized functions to model variables

modelGreGpaXCRank = ols(formula='gre ~ gpa * C(rank)', data=dfadmit).fit()
print( modelGreGpaXCRank.summary() )
modelpredicitons['gre_GpaXCRankLM'] = modelGreGpaXCRank.predict(dfadmit)
print(modelpredicitons.head())

# This is essentially four different models for the four ranks of schools.

# QUESTION: Can you build a model which encompass four models for the four different schools 
# with the same slope (for gpa) but allow for different intercepts?


#%% [markdown]
# # Logistic Regressions
#
# link function in glm
# https://www.statsmodels.org/stable/glm.html#families
# Gaussian(link = sm.families.links.identity) → the default family
# Binomial(link = sm.families.links.logit)
# probit, cauchy, log, and cloglog
# Poisson(link = sm.families.links.log)
# identity and sqrt


#%% [markdown]
#
# # Maximum Likelihood Estimation
#
# Likelihood vs Probability
# Conditional Probability: P (outcome A∣given B)
# Probability: P (data∣model)
# Likelihood: L(model∣data)
#
# If the error distribution is normal, and we chose to use a square (Euclidean) 
# distance metric, then OLS and MLE produces the same result.


#%%
import statsmodels.api as sm  # Importing statsmodels
# import statsmodels.formula.api as smf  # Support for formulas
# from statsmodels.formula.api import glm   # Use glm() directly

# 1. Describe the model → glm()
# 2. Fit the model → .fit()
# 3. Summarize the model → .summary()
# 4. Make model predictions → .predict()

# 1. Describe the model → glm()

# Two of the available styles:
# ARRAY based
# import statsmodels.api as sm
# X = sm.add_constant(X)
# model = sm.glm(y, X, family)

# FORMULA based (we had been using this for ols)
from statsmodels.formula.api import glm
# model = glm(formula, data, family)

modelAdmitGreLogit = glm(formula='admit ~ gre', data=dfadmit, family=sm.families.Binomial()).fit()
print( modelAdmitGreLogit.summary() )
modelpredicitons['admit_GreGpaLogit'] = modelAdmitGreLogit.predict(dfadmit)
# print(modelpredicitons.head())
dfChkBasics(modelpredicitons)

#%% [markdown]
# # Deviance
# Formula
# D = −2LL(β)
# * Measure of error
# * Lower deviance → better model fit
# * Benchmark for comparison is the null deviance → intercept-only model / constant model
# * Evaluate
#   * Adding a random noise variable would, on average, decrease deviance by 1
#   * Adding k predictors to the model deviance should decrease by more than k

#%%
# The deviance of the model was 486.06 (or negative two times Log-Likelihood-function)
print(-2*modelAdmitGreLogit.llf)
# Compare to the null deviance
print(modelAdmitGreLogit.null_deviance)
# 499.98
# A decrease of 14 with just one variable. That's not bad. 

#%%
# Now with more predictors
modelAdmitAllLogit = glm(formula='admit ~ gre+gpa+C(rank)', data=dfadmit, family=sm.families.Binomial()).fit()
print( modelAdmitAllLogit.summary() )
modelpredicitons['admit_GreAllLogit'] = modelAdmitAllLogit.predict(dfadmit)
# print(modelpredicitons.head())
dfChkBasics(modelpredicitons)

# QUESTION: Is this model separable into four models for each rank with the 
# same "intercept" or "slopes"? 
# How can you generalize it to a more general case?

#%%
# To interpret the model properly, it is handy to have the exponentials of the coefficients
np.exp(modelAdmitAllLogit.params)
np.exp(modelAdmitAllLogit.conf_int())

#%%
# Confusion matrix
# Define cut-off value
cut_off = 0.7
# Compute class predictions
modelpredicitons['classLogitAll'] = np.where(modelpredicitons['admit_GreAllLogit'] > cut_off, 1, 0)
print(modelpredicitons.classLogitAll.head())
#
# Make a cross table
print(pd.crosstab(dfadmit.admit, modelpredicitons.classLogitAll,
rownames=['Actual'], colnames=['Predicted'],
margins = True))
#
#
#                         predicted 
#                   0                  1
# Actual 0   True Negative        False Positive
# Actual 1   False Negative       True Positive
# 
# Accuracy    = (TP + TN) / Total
# Precision   = TP / (TP + FP)
# Recall rate = TP / (TP + FN)


#%%
# Now try the Titanic Dataset, and find out the survival chances from different predictors.

