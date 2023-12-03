#!/usr/bin/env python
# coding: utf-8

# In[2]:


#IMPORTS
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


#Read in Excel File
ddData = pd.read_excel('/Users/meme/Documents/InterviewDataAnalysis/Sephora.xlsx',sheet_name=1)
#Check Data Types
ddData.dtypes


# In[6]:


ddData.shape


# In[7]:


#check to make sure all duplicates were dropped
ddData.drop_duplicates()
ddData.shape


# In[8]:


ddData.head(5)


# In[9]:


ddData.describe()


# In[10]:


#count all unique vals in all cols
ddData.nunique()


# In[13]:


cor_matrix = ddData.corr()


# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt

# Create a heatmap
sns.heatmap(cor_matrix, annot=True, cmap='Purples', vmin=-1, vmax=1)
plt.show()


# In[50]:


import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(ddData,height=1)


# In[90]:


#MLM
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import style
import statsmodels.api as sm
X = ddData[["Paid Social Impressions", "Affiliate Clicks", "Display Impressions", "Paid Search Impressions"]]
y = ddData['SALES']
sm_X1_var = sm.add_constant(X)

mlr_model = sm.OLS(y, sm_X1_var)
mlr_reg = mlr_model.fit()
print(mlr_reg.summary())


# In[89]:


sb.distplot(yhat, hist = False, color = 'r', label = 'Predicted Values')
sb.distplot(y_test, hist = False, color = 'b', label = 'Actual Values')
plt.title('Actual vs Predicted Values', fontsize = 16)
plt.xlabel('Values', fontsize = 12)
plt.ylabel('Frequency', fontsize = 12)
plt.legend(loc = 'upper left', fontsize = 13)

plt.savefig('ap.png')

