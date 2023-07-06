#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter in File Explorer

# In[1]:


import os, shutil


# In[12]:


path = r"C:/Users/Admin/Desktop/JOBS/Cert/"


# In[15]:


file_name = os.listdir(path)


# In[17]:


folder_names = ['pdf files', 'image files', 'docx files']

for loop in range(0, 3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".docx" in file and not os.path.exists(path + "docx files/" + file):
        shutil.move(path + file, path + "docx files/" + file)


# In[16]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




