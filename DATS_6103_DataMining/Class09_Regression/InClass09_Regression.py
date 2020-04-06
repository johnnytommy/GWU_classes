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
# First read in the datasets. One Graduate school admission dataset, one Titanic survival dataset
import os
os.chdir('../Class09_Regression')  
# filepath = os.path.join( os.getcwd() ,'gradAdmit.csv')
import pandas as pd
dfadmit = pd.read_csv('gradAdmit.csv')
dfChkBasics(dfadmit, True)



#%%
# quick plots
import matplotlib.pyplot as plt
# add color
import numpy as np
admitcolors = np.where(dfadmit['admit']==1,'g','r')
# admitcolors[dfadmit['admit']==0] = 'r'
# admitcolors[dfadmit['admit']==1] = 'g'

#%% 
# Plot, Pandas style (or seaborn sns)
dfadmit.plot(x="gre", y="gpa", kind="scatter", color=admitcolors)
plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()


#%%
# OR 
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
# easier to add jittering
fig, axis = plt.subplots()
axis.plot(dfadmit.gre + np.random.uniform(0,10, size=dfadmit.shape[0] ), dfadmit.gpa, color='g', linestyle="", marker="o", markersize=3, alpha=0.3)
plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()

#%% 
# seaborn sns
import seaborn as sns
sns.scatterplot('gre', 'gpa', data=dfadmit)
sns.despine()


#%% 
# seaborn sns
# import seaborn as sns
sns.regplot('gre', 'gpa', data=dfadmit, fit_reg = False, x_jitter=10, scatter_kws={'alpha': 0.3, 's': 3 } )
sns.despine()
# easy
# lack some minor control such as what distribution to use
# can also use subplots, with different set of syntax

#%% 
# seaborn sns
# import seaborn as sns
sns.regplot('gre', 'gpa', data=dfadmit, fit_reg = True, x_jitter=10, scatter_kws={'alpha': 0.3, 's': 3 }, line_kws = {'color':'red', 'label':'LM fit'})
sns.despine()

#%% 
# seaborn sns
# import seaborn as sns
sns.lmplot('gre', 'gpa', data=dfadmit, hue='admit', fit_reg = False, x_jitter=10, scatter_kws={'alpha': 0.3, 's': 3 })
sns.despine()

#%% 
# seaborn sns
# import seaborn as sns
sns.lmplot('gre', 'gpa', data=dfadmit, hue='admit', markers=["o", "x"], fit_reg = True, x_jitter=10, scatter_kws={'alpha': 0.4, 's': 8 })
sns.despine()


#%% 
# seaborn sns
# color by rank
# import seaborn as sns
sns.lmplot('gre', 'gpa', data=dfadmit, hue='rank', markers=['o', 'x', '^', 's'], fit_reg = False, x_jitter=10, scatter_kws={'alpha': 0.4, 's': 8 })
# markers=['o', 'x', 's','^','p','+','d']
sns.despine()

#%%
# Question, 
# How many dimensions we can visualize?



#%% 
# color by rank
# Let try pandas, 
# need to create the color label for each data point ourselves, 
# but we can have color and shape separate
rankcolors = np.where(dfadmit['rank']==1,'r','-') # initialize the vector as well
# rankcolors[dfadmit['rank']==1] = 'r'
rankcolors[dfadmit['rank']==2] = 'g'
rankcolors[dfadmit['rank']==3] = 'b'
rankcolors[dfadmit['rank']==4] = 'yellow'

# and use different shape for admit 0 and 1
ax1 = dfadmit[dfadmit.admit==0].plot(x="gre", y="gpa", kind="scatter", color=rankcolors[dfadmit.admit==0], marker='o', label='rejected')
dfadmit[dfadmit.admit==1].plot(x="gre", y="gpa", kind="scatter", color=rankcolors[dfadmit.admit==1], marker='+', label='admitted', ax = ax1)
# dfadmit.plot(x="gre", y="gpa", kind="scatter", color=rankcolors, marker='+')
plt.legend(loc='upper left')
plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()


#%% 
# color by rank
# Try Matplotlib, so we can add jittering
fig, axis = plt.subplots()
for admitval, markerval in { 0: "o" , 1: "+" }.items() : # rejected (admit==0), use 'o', admitted (admit==1), use '+'
  for cindex, cvalue in {1: 'r', 2: 'g', 3: 'b', 4: 'yellow' }.items() : # the ranks and colors
    thisdf = dfadmit[dfadmit.admit==admitval] # first filter out admitted or rejected
    thisdf = thisdf[thisdf['rank'] == cindex] # then filter out one rank at a time.
    print(thisdf.shape)
    axis.plot(thisdf.gre + np.random.uniform(0,10, size=thisdf.shape[0] ), 
              thisdf.gpa, 
              color=cvalue, 
              linestyle="", 
              marker=markerval, 
              markersize=3, 
              alpha=0.3
    )

plt.xlabel("GRE score")
plt.ylabel("GPA")
plt.title("GPA vs GRE")
# plt.savefig(filepath, dpi=96)
plt.show()


#%%
# Now, your turn. Try some sensible plots with the Titanic dataset. 
# How would you visualize the relations between survived, age, sex, fare, embarked? 
# You do not need to use all of them in a single plot. What variables make the most sense to you, 
# in terms of finding out who survived, and who didn't.
#

# filepath = os.path.join( os.getcwd(), 'Titanic_clean.csv')
dftitan = pd.read_csv('Titanic_clean.csv')
# dfChkBasics(dftitan, True) # later



#%% 
# Now LINEAR REGRESSION
# 1. Describe the model → ols()
# 2. Fit the model → .fit()
# 3. Summarize the model → .summary()
# 4. Make model predictions → .predict()


#%%
# FORMULA based
from statsmodels.formula.api import ols
modelGreGpa = ols(formula='gre ~ gpa', data=dfadmit)
print( type(modelGreGpa) )

#%%
modelGreGpaFit = modelGreGpa.fit()
print( type(modelGreGpaFit) )
print( modelGreGpaFit.summary() )

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
modelpredicitons = pd.DataFrame( columns=['gre_GpaLM'], data= modelGreGpaFit.predict(dfadmit.gpa)) 
# use the original dataset gpa data to find the expected model values
print(modelpredicitons.shape)
print( modelpredicitons.head() )

#%%
# Next let us try more variables, and do it in a combined step
modelGreGpaRankFit = ols(formula='gre ~ gpa + rank', data=dfadmit).fit()

print( type(modelGreGpaRankFit) )
print( modelGreGpaRankFit.summary() )

modelpredicitons['gre_GpaRankLM'] = modelGreGpaRankFit.predict(dfadmit)
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
modelGreGpaCRankFit = ols(formula='gre ~ gpa + C(rank)', data=dfadmit).fit()
print( modelGreGpaCRankFit.summary() )
modelpredicitons['gre_GpaCRankLM'] = modelGreGpaCRankFit.predict(dfadmit)
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

modelGreGpaXCRankFit = ols(formula='gre ~ gpa * C(rank)', data=dfadmit).fit()
print( modelGreGpaXCRankFit.summary() )
modelpredicitons['gre_GpaXCRankLM'] = modelGreGpaXCRankFit.predict(dfadmit)
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

modelAdmitGreLogitFit = glm(formula='admit ~ gre', data=dfadmit, family=sm.families.Binomial()).fit()
print( modelAdmitGreLogitFit.summary() )
modelpredicitons['admit_GreGpaLogit'] = modelAdmitGreLogitFit.predict(dfadmit)
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
print(-2*modelAdmitGreLogitFit.llf)
# Compare to the null deviance
print(modelAdmitGreLogitFit.null_deviance)
# 499.98
# A decrease of 14 with just one variable. That's not bad. 

#%%
# Now with more predictors
modelAdmitAllLogitFit = glm(formula='admit ~ gre+gpa+C(rank)', data=dfadmit, family=sm.families.Binomial()).fit()
print( modelAdmitAllLogitFit.summary() )
modelpredicitons['admit_GreAllLogit'] = modelAdmitAllLogitFit.predict(dfadmit)
# print(modelpredicitons.head())
dfChkBasics(modelpredicitons)

# QUESTION: Is this model separable into four models for each rank with the 
# same "intercept" or "slopes"? 
# How can you generalize it to a more general case?

#%%
# To interpret the model properly, it is handy to have the exponentials of the coefficients
np.exp(modelAdmitAllLogitFit.params)
np.exp(modelAdmitAllLogitFit.conf_int())

#%%
# Confusion matrix
# Define cut-off value
cut_off = 0.3
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
# Now try the Titanic Dataset, and find out the survival chances from different predictors.

