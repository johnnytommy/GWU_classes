

#%%
#Intro to Data Mining
#Homework Assignment #8
#Johnny Thomas

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

import numpy as np
import matplotlib.pyplot as plt

# examples:
# dfChkBasics(df)

#%%
# First read in the dataset.
import os
os.chdir('../Class09_Regression')  
# filepath = os.path.join( os.getcwd() ,'gradAdmit.csv')
import pandas as pd
titanic = pd.read_csv('Titanic.csv')
dfChkBasics(titanic, True)




#%%
#Q1: With the Titanic dataset, perform some summary statistics. 

#a) Histogram on age. Maybe a stacked histogram on age with male-female as two series if possible

x1 = titanic.age[titanic.sex == 'male']
x2 = titanic.age[titanic.sex == 'female']
legend = ['Men', 'Women']
plt.figure()
plt.title('Scores by Age and gender')
plt.hist([x1,x2], stacked=True, density=True)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.legend(legend)
plt.show()

#%%

#b) proportion summary of male-female, survived-dead

x3 = len(titanic[titanic.sex == 'male'])/len(titanic.sex)
x4 = len(titanic[titanic.sex == 'female'])/len(titanic.sex)

print('proportion of male: '"{:.2f}".format(x3))
print('proportion of female: '"{:.2f}".format(x4))

x5 = len(titanic[titanic.survived == 0])/len(titanic.survived)
x6 = len(titanic[titanic.survived == 1])/len(titanic.survived)

print('proportion of dead: ',"{:.2f}".format(x5))
print('proportion of survived: ',"{:.2f}".format(x6))

#%%
#c) pie chart for “Ticket class”
tix = titanic['pclass'].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(tix, labels=tix.index, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()

#%%
#d) A single visualization chart that shows info of survival, age, pclass, and sex.
# color by rank


import plotly_express as px

px.scatter(titanic, x='age', y="survived",color="pclass", animation_frame = "sex")




# %%!
# Question 2
# Build a logistic regression model for survival. As we did before, include the features that you find plausible. Make sure categorical variables are use properly. If the coefficient(s) turns out insignificant, drop it and re-build.


import statsmodels.api as sm 
from statsmodels.formula.api import glm
#Predictors: pclass, sex, age
model1 = glm(formula='survived ~ age + + sibsp + C(pclass) + C(sex)', data=titanic, family=sm.families.Binomial()).fit()

print(model1.summary())


#%%
print("The deviance of the model was:", -2*model1.llf)

print("The null deviance is:",model1.null_deviance)

print("Thus, our model is better!")

#%%
# Question 3 Interpret your result. What are the factors and how do they affect the chance of survival (or the survival odds ratio)? What is the predicted probability of survival for a 30-year-old female with a second class ticket, no siblings, 3 parents/children on the trip? Use whatever variables that are relevant in your model.

print('The best variables are age, sex, sibsp, and pclass.')

predict1 = pd.DataFrame( columns=['Survived_AgePclassSexSibspLogit'], data= model1.predict(titanic[titanic.sex == 'female'][titanic.age == 30][titanic.pclass == 2][titanic.sibsp == 0]))
print(predict1.head() )

print('We see that a woman with these characteristics on the Titanic has a 82% chance of survival!')



#%%
#Try three different cut-off values at 0.3, 0.5, and 0.7. What are the a) Total accuracy of the model b) The precision of the model and c) The recall rate

# Confusion matrix
# Define cut-off value
cut_off = 0.3
# Compute class predictions
predict1['classLogitAll'] = np.where(predict1['Survived_AgePclassSexSibspLogit'] > cut_off, 1, 0)
print(predict1.classLogitAll.head())
#
# Make a cross table
print("cut_off = 0.3")
print(pd.crosstab(titanic.survived, predict1.classLogitAll,
rownames=['Actual'], colnames=['Predicted'],
margins = True))

# cut-off value = 0.3
accuracy = (240+425)/891
precision = 240/(240+124)
recall  = 240/(240+102)

print("\n cut off value = %s: \n Total accuracy of the model: %s \n The precision of the model: %s \n The recall rate: %s" %(cut_off, accuracy, precision, recall))

# Confusion matrix
# Define cut-off value
cut_off = 0.5
# Compute class predictions
predict1['classLogitAll'] = np.where(predict1['Survived_AgePclassSexSibspLogit'] > cut_off, 1, 0)
print(predict1.classLogitAll.head())
#
# Make a cross table
print("cut_off = 0.5")
print(pd.crosstab(titanic.survived, predict1.classLogitAll,
rownames=['Actual'], colnames=['Predicted'],
margins = True))

# cut-off value = 0.5
accuracy = (212+486)/891
precision = 212/(212+63)
recall  = 212/(212+130)

print("\n cut off value = %s: \n Total accuracy of the model: %s \n The precision of the model: %s \n The recall rate: %s" %(cut_off, accuracy, precision, recall))

# Confusion matrix
# Define cut-off value
cut_off = 0.7
# Compute class predictions
print("cut_off = 0.7")
predict1['classLogitAll'] = np.where(predict1['Survived_AgePclassSexSibspLogit'] > cut_off, 1, 0)
print(predict1.classLogitAll.head())
#
# Make a cross table
print(pd.crosstab(titanic.survived, predict1.classLogitAll,
rownames=['Actual'], colnames=['Predicted'],
margins = True))

# cut-off value = 0.5
accuracy = (160+534)/891
precision = 160/(160+15)
recall  = 160/(160+182)

print("\n cut off value = %s: \n Total accuracy of the model: %s \n The precision of the model: %s \n The recall rate: %s" %(cut_off, accuracy, precision, recall))


###NFL DATA

#%%
# NFL field goal data dataset
nfl = pd.read_csv('nfl2008_fga.csv')
newnfl = nfl[['HomeTeam','AwayTeam','qtr','min','sec','kickteam','distance','timerem','GOOD','Missed','Blocked']]

dfChkBasics(newnfl, True)



#%%
#Question 5 Build a model overall (not individual team or kicker) to predict the chances of a successful field goal. What variables do you have in your model?

# %%
# Model by 5 predictors (Quarter, Min, Sec, Distance, Time)
nfl_model1 = glm(formula='GOOD ~ C(qtr)+min+sec+distance+timerem', data=newnfl, family=sm.families.Binomial()).fit()
print( nfl_model1.summary() )

print("Based on p-value, only distance is relevant.") 

#%%
#Just keep distance  
nfl_dist_model = glm(formula='GOOD ~ distance', data=newnfl, family=sm.families.Binomial()).fit()
print( nfl_dist_model.summary())

#%%
#Make a GOOD prediction
newnfl['GOOD_predicted'] = nfl_dist_model.predict(newnfl)
print(newnfl)

# %%
#Question 6 Someone has a feeling that home teams are more relaxed and have a friendly crowd, they should kick better field goals. Can you build two different models, one for all home teams, and one for road teams, of their chances of making a successful field goal?
nfl_dist_modelHome = glm(formula='GOOD ~ distance + HomeTeam', data=newnfl, family=sm.families.Binomial()).fit()
print( nfl_dist_modelHome.summary())

#%%
nfl_dist_modelAway = glm(formula='GOOD ~ distance + AwayTeam', data=newnfl, family=sm.families.Binomial()).fit()
print( nfl_dist_modelAway.summary())

#%%
# Question 7 From what you found, do home teams and road teams have different chances of making a successful field goal? If one does, is that true for all distances, or only with a certain range?

"You can see by both above models that with such high p-values, the status of Home/Away doesn't really contribute to a sucessful field goal. A great addition to this would be if the player was on the NE Patriots or not; would contribute largely and negatively to lowering the chance of a field goal made. GO BIRDS."

# %%
