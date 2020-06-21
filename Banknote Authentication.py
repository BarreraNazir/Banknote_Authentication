#!/usr/bin/env python
# coding: utf-8

# # Banknote aunthentication

# In[18]:


# importing python data analysis toolkit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 


# In[19]:


# reading random points from xlsx file and storing results in data frame
data = pd.read_csv("data_banknote_authentication.csv")
data.head(5)


# Analyzing the data

# In[20]:


data.info() # missing values not found


# In[28]:


#number of instances (rows) that belong to each class. We can view this as an absolute count.
data['class'].value_counts()


# Visualizing the Class Column

# In[46]:


sns.heatmap(data.corr(), square=True, annot=True)


# In[54]:


columns = [f for f in data.columns if data.dtypes[f] != 'object']
values = pd.melt(data, value_vars = columns)
hist = sns.FacetGrid (values, col='variable', col_wrap=4, sharex=False, sharey = False)
hist = hist.map(sns.distplot, 'value')


# In[55]:


hist


# Splitting data into training and testing

# In[5]:


X5 = data.drop('class', axis=1)
X5.head()


# In[89]:


y5  = data['class']
y5.head()


# In[90]:


from sklearn.model_selection import train_test_split  
X5_train, X5_test, y5_train, y5_test = train_test_split(X5, y5, test_size = 0.20) 
print("Sample in traiing set:::", X5_train.shape)
print("Sample in testing set:::", X5_test.shape)
print("Sample of target in training set::", y5_train.shape)
print("Sample of target in testing set::", y5_test.shape)


# In[122]:


from sklearn.neural_network._stochastic_optimizers import SGDOptimizer


# In[177]:


gd = SGDOptimizer(params='0.1', learning_rate_init=0.1)


# In[184]:


gd.fit(X5_train, y5_train)


# In[193]:


from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y5_test,pred5.round()))  
print(classification_report(y5_test,pred5.round()))


# In[194]:


from sklearn.metrics import accuracy_score
accuracy5 = accuracy_score(y5_test, pred5.round())
print("Accuracy", accuracy5)

