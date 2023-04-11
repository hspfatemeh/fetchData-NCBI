#!/usr/bin/env python
# coding: utf-8

# In[2]:

# 113 بودن داده های دریافت شده بهترین ساختمان داده استک میباشد؟؟ --از خط order به دلیل

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "Your.Name.Here@example.org"


# In[3]:


import pandas as pd


# In[4]:


handle = Entrez.esearch(db="protein", term='lycopene cyclase',retmax="20")
rec_list = Entrez.read(handle)
handle.close()
rec_list['Count']


# In[5]:


len(rec_list['IdList'])


# In[6]:


rec_list['IdList']


# In[7]:


id_list = rec_list['IdList']
handle = Entrez.efetch(db='protein', id=id_list, rettype='gb') 


# In[8]:


handle


# In[9]:


#print(handle.read())


# In[10]:


recs = list(SeqIO.parse(handle, 'gb'))
handle.close()


# In[11]:


# Open a file called 'data.txt' for writing
with open('data1.txt', 'w') as file:
    # Write the contents of the GenBank string to the file
    file.write(str(recs))

print("Data saved to 'data1.txt'")


# In[12]:


recs


# In[15]:


x= 'WP_277898193'
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


# In[16]:


if rec.name != x:
    print("***not exist, please search other name***")
else:
    print(str(rec.seq))


# In[ ]:


#stack  به دلیل اینکه داده های بدست آمده orderهستند
#از استک برای ذخیره سازی استفاده کرده ام


# In[68]:


from collections import deque
 
stack = deque()
for recc in rec.seq:
    stack.append(recc)
      
print('Initial stack:')
print(stack)

print(stack.pop())
print('\nStack after elements are popped:')
print(stack)


# In[32]:


import csv


# In[48]:


with open("WP_277898193.csv", 'w',newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(stack)
    print("data store was succesfull")


# In[63]:


import pandas as pd
data= pd.read_csv("WP_277898193.csv")


# In[62]:


pd.set_option("max_rows", None)
data


# In[ ]:




