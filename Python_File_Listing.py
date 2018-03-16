
# coding: utf-8

# In[1]:


import os,glob

os.chdir("/Users/user/Downloads")

for file in glob.glob("*.jpg"):
    print(file)

