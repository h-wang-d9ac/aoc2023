#!/usr/bin/env python
# coding: utf-8

# In[84]:


with open("num.txt") as f:
    txt = f.read()


# In[85]:


num = txt.split("\n")[:-1]


# In[86]:


nums = [f"{i}" for i in range(10)]


# In[87]:


z = ["".join([c for c in num[i] if c in nums]) for i in range(len(num))]

g = [int(a[0] + a[-1]) for a in z if len(a) > 0]


# In[88]:


sum(g)


# In[99]:


rep = {
    "one": "1e", 
    "two": "2o", 
    "three": "3e", 
    "four": "4r", 
    "five": "5e", 
    "six": "6x", 
    "seven": "7n", 
    "eight": "8t", 
    "nine": "9e"}


# In[100]:


import re


# In[101]:


numwords = "|".join(rep.keys())


# In[102]:


clean_num = []
for read_num in num:
    clean = read_num
    next = ""
    while next != clean:
        next = clean
        clean = re.sub(numwords, lambda m: str(rep[m.group(0)]), next)
    clean_num.append(clean)


# In[103]:


z1 = ["".join([c for c in clean_num[i] if c in nums]) for i in range(len(clean_num))]
g1 = [int(a[0] + a[-1]) for a in z1 if len(a) > 0]


# In[104]:


sum(g1)


# In[105]:


z1


# In[ ]:





# In[ ]:




