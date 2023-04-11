#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import Entrez
from Bio import SeqIO
Entrez.email = "Your.Name.Here@example.org"


# In[2]:


import pandas as pd


# In[20]:


handle = Entrez.esearch(db="protein", term='lycopene cyclase',retmax="100")
rec_list = Entrez.read(handle)
handle.close()
rec_list['Count']


# In[21]:


len(rec_list['IdList'])


# In[22]:


rec_list['IdList']


# In[23]:


id_list = rec_list['IdList']
handle = Entrez.efetch(db='protein', id=id_list, rettype='gb') 


# In[24]:


handle


# In[25]:


#print(handle.read())


# In[26]:


recs = list(SeqIO.parse(handle, 'gb'))
handle.close()


# In[27]:


# Open a file called 'data.txt' for writing
with open('data1.txt', 'w') as file:
    # Write the contents of the GenBank string to the file
    file.write(str(recs))

print("Data saved to 'data1.txt'")


# In[28]:


recs


# In[109]:


x= 'WP_205819985'
for rec in recs: 
    print(rec.name,'/',end=" ")
    if rec.name == x:
            print('\n==========================================================================================') 
            print(rec.name)
            print(rec.description) 
            break
if rec.name != x:
    print('\n==========================================================================================') 
    print('\n')
    print('\n')
    print("***not exist, please search other name***")


# In[112]:


if rec.name != x:
    print("***not exist, please search other name***")
else:
    print(str(rec.seq))


# In[ ]:




