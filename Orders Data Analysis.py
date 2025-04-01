#!/usr/bin/env python
# coding: utf-8

# # Overview
# 
# 

# In this Project I am do an end to end data analytics project using python and SQL. I will use Kaggle API to download the dataset and to data processing and cleaning using pandas and load the data into sql server. Lastly we will answer some interesting questions using SQL.

# # Library

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import kaggle
import warnings
warnings.filterwarnings('ignore')


# # Data Collection from Kaggle API

# In[17]:


get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# ## Extract file from ZIP file 

# In[24]:


get_ipython().system('pip install zipfile')


# In[6]:


import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() 


# In[7]:


df = pd.read_csv('orders.csv')
df


# ## Understanding Data 

# In[29]:


# to check the first 5 rows 
df.head(5)


# In[30]:


# to check the last 5 rows 
df.tail(5)


# In[31]:


# to see the data types: 
df.info()


# # Data Cleaning & Processing 

# In[32]:


# check duplicate values: 
df.duplicated().sum()


# In[33]:


# check for null values: 
df.isnull().sum()


# In[34]:


# drop null values: 
df.dropna(inplace=True)


# In[37]:


df.isnull().sum()


# In[8]:


df.rename(columns={'Order Id':'order_id','Order Date':'order_date','Postal Code':'postal_code','Sub Category':'sub_category'},inplace=True)
df


# In[9]:


df.rename(columns={'Product Id':'product_id','cost price':'cost_price','List Price':'list_price','Discount Percent':'discount_price'},inplace=True)
df


# In[11]:


# derive new columns discount, sale price and profit
df['discount'] = df['list_price']*df['discount_price']*.01


# In[13]:


df['sale_price'] = df['list_price'] - df['discount']


# In[14]:


df['profit'] = df['sale_price'] - df['cost_price']


# In[15]:


df


# In[17]:


# conver order date from object data type to datetime
df.dtypes


# In[18]:


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[19]:


df.dtypes


# In[21]:


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_price'],inplace=True)


# # Load Data to SQL server

# In[23]:


#load the data into sql server using replace option
import sqlalchemy as sal
#create a connection to sql server
engine = sal.create_engine('mssql://DESKTOP-VI84P2U/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[24]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'replace')


# In[ ]:




