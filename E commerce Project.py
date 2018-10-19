
# coding: utf-8

# # Ecommerce Purchases Project¶
# 
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.

# In[27]:


# Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.

import pandas as pd


# In[28]:


# Importing the file

ecom = pd.read_csv('Ecommerce Purchases')


# In[29]:


# Check the head of the DataFrame.

ecom.head()


# In[30]:


ecom.info()


# #### What is the average Purchase Price?

# In[31]:


ecom['Purchase Price'].mean()


# #### What were the highest and lowest purchase prices?

# In[32]:


ecom['Purchase Price'].max()


# In[33]:


ecom['Purchase Price'].min()


# #### How many people have English 'en' as their Language of choice on the website?

# In[34]:


ecom[ecom['Language']=='en'].count()


# #### How many people have the job title of "Lawyer" ?

# In[35]:


ecom[ecom['Job']=='Lawyer'].info()


# #### How many people made the purchase during the AM and how many people made the purchase during PM ?

# In[36]:


ecom['AM or PM'].value_counts()


# In[37]:


get_ipython().set_next_input('What are the 5 most common Job Titles');get_ipython().run_line_magic('pinfo', 'Titles')


# In[ ]:


What are the 5 most common Job Titles


# #### What are the 5 most common Job Titles

# In[38]:


ecom['Job'].value_counts().head(5)


# #### Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?

# In[39]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# #### What is the email of the person with the following Credit Card Number: 4926535242672853

# In[40]:


ecom[ecom["Credit Card"] == 4926535242672853]['Email'] 


# #### How many people have American Express as their Credit Card Provider and made a purchase above $95 ?

# In[41]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# #### How many people have a credit card that expires in 2025?

# In[42]:


sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# #### What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)

# In[43]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

