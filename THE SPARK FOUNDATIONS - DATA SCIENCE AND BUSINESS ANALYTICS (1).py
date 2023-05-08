#!/usr/bin/env python
# coding: utf-8

# # Retail Superstore
# 

# A retail sale occurs when a business sells a product or service to an individual consumer for his or her own use. The transaction itself can occur through a number of different sales channels, such as online, in a brick-and-mortar storefront, through direct sales, or direct mail. The aspect of the sale that qualifies it as a retail transaction is that the end user is the buyer.

# # Problem Statement

# 1.As a business manager, try to find out the weak areas where you can work to make more profit.
# 
# 2.What all business problems you can derive by exploring the data?

# # 'Exploratory Data Analysis' on dataset 'SampleSuperstore'

# In[1]:


import numpy as np # for numeric data 
import pandas as pd # for dataframe and analysis
import matplotlib.pyplot as plt # for plots 
import seaborn as sns #for Advance plots
import warnings


# In[2]:


df = pd.read_csv("SampleSuperstore.csv")
df.head()


# In[3]:


df.shape


# In[4]:


#There are total 13 attributes about orders at superstore.


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


df.isna().sum()


# In[8]:


df.describe()


# # OBSERVATIONS
# #Retail Superstore is making average profit of 28.65 overall on each order.
# #Maximum loss incured is of around 6599.97 and profit of around 8399.97.
# #On an average superstore is doing sales of around 229 per order.
# #Max discount offered by superstore ia around 80%.

# # Univariate Analysis#
# 

# In[11]:


fig, axis = plt.subplots(nrows = 2 , ncols = 2 , figsize = (15 , 7))
sns.countplot(data = df , x = df["Ship Mode"] , ax = axis[0 , 0])  
sns.countplot(data = df , x = df["Segment"] , ax = axis[0 , 1])  
sns.countplot(data = df , x = df["Region"] , ax = axis[1, 0])  
sns.countplot(data = df , x = df["Category"] , ax = axis[1, 1])
plt.tight_layout()
plt.show()


# # OBSERVATIONS
# #Most of the orders have ship mode as Standard Class and least for the Same Day.
# #Majority of the orders are Consumer segment while least for Home Office.
# #Highest number of orders are from West and East Region while least from South.
# #Majorily the category of order are of Office supplies as compared to other categories

# In[13]:


fig, axis = plt.subplots(nrows = 4 , ncols = 1 , figsize = (15 , 7))
sns.boxplot(data = df , x = df["Sales"] , ax = axis[0],color = "g")  
sns.boxplot(data = df , x = df["Quantity"] , ax = axis[1],color = "r")  
sns.boxplot(data = df , x = df["Discount"] , ax = axis[2],color = "b")  
sns.boxplot(data = df , x = df["Profit"] , ax = axis[3],color = "y")
plt.tight_layout()
plt.show()


# # OBSERVATIONS
# #There are many outliers in Sales attribute and all of them are in positive side i.e higher side.
# #Majority of the Quantity lies between 3 to 9 orders with some outliers on higher side.
# #Discount majorily ranges from 0 to 50% with 60%,70% and 80% as an outlier.
# #Profit has highest number of outliers and seems to incur losses too.

# # Bi-Variate Analysis

# In[16]:


df.head()


# In[17]:


pd.DataFrame(df.groupby('Ship Mode').sum()[['Sales','Profit']]).plot(kind='bar',figsize=(6,3))
pd.DataFrame(df.groupby('Region').sum()[['Sales','Profit']]).plot(kind='bar',figsize=(6,3))
pd.DataFrame(df.groupby('Segment').sum()[['Sales','Profit']]).plot(kind='bar',figsize=(6,3))
pd.DataFrame(df.groupby('Category').sum()[['Sales','Profit']]).plot(kind='bar',figsize=(6,3))
plt.tight_layout()
plt.show()


# # OBSERVATIONS
# #The profit is far less as compared to the sales that have been made through Standard Class ship mode that infers that some good amount of losses have been incurred.
# #The sales are lowest from south region.
# #Profits in central region are not upto the mark as compared to other regions.
# #Sales and Profit both are highest for consumer segment and lowest for Home office.
# #Profit made in furniture category are extremely low as compared to other categories.

# In[19]:


pd.DataFrame(df.groupby('Sub-Category').sum()[['Profit']]).plot(kind='bar',color='r',figsize=(6,4))


# In[20]:


pd.DataFrame(df.groupby('Sub-Category').sum()[['Sales']]).plot(kind='bar',color = 'g',figsize=(6,4))


# # OBSERVATIONS
# #Most profitable sub category is copiers and most loss making is Tables.
# #Chairs and Phones are highest selling sub category while Fasteners,Labels,Envelopes have least sales.

# In[22]:


sns.heatmap(df.corr(),annot=True,cmap='Blues')


# In[23]:


#By Heatmap we confirm two obvious logical arguments:

#Discount is negatively correlated with profit.
#Sales has strong positive correlation with profit.


# # What impact discount is making on Sales?

# From the heatmap we got a an interesting observation, Discount should have a positive impact on sales but on inferring it seem to not having any great impact on Sales infact it is having negative correlation that is a major problem.
# 
# 

# In[25]:


df.head()


# # Which state are on top and bottom in terms of profit?

# In[26]:


df_state = pd.DataFrame(df.groupby('State').sum()[["Sales","Profit"]]).reset_index()
df_state.head()


# In[27]:


df_state.columns


# In[28]:


df_state[df_state['Profit']==max(df_state['Profit'])]


# In[29]:


df_state[df_state['Profit']==min(df_state['Profit'])]


# # Which state are top and bottom in terms of sales?
# 

# In[30]:


df_state[df_state['Sales']==max(df_state['Sales'])]


# In[31]:


df_state[df_state['Sales']==min(df_state['Sales'])]


# State with highest sales is "California" with a sales of 457687.
# State with lowest sales is "North Dakota" with a loss of 919.

# In[34]:


plt.figure(figsize=(25,20))
sns.pairplot(df)
plt.show()


# # RECOMMENDATIONS

# 1.Superstore should focus more on improving sells in South region,South Dakota state and Texas state as by giving more discount on selected items that are more in demand in these regions and also improve delivery facilities.
# 
# 2.We should either minimize selling or reduce discount on Furniture category as it is providing least profit especially Tables sub-category which is incurring huge losses.
# 
# 3.The sales of Fasteners,Envelops,Labels and Art are extremely low, to improve this condition more discounted offers should be provided for a short interval of time to give boost to the sales.
# 
# 4.The discount is observed to have negatively impacting sales somehow that is a major problem, planning for amount of discount on different products should be restructured such as the in demand products have a moderate discount while heavy discount offers should be provided for less sold products.

# In[ ]:




