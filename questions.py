#!/usr/bin/env python
# coding: utf-8

# In[29]:


get_ipython().system('pip install pyPDF2')
get_ipython().system('pip install regex')


# In[30]:


import re
import PyPDF2 as pdf


# In[3]:


file=open('C:\\Users\\Maria sanjai\\Desktop\\The_Living_World.pdf','rb')


# In[4]:


file


# In[5]:


pdf_reader=pdf.PdfFileReader(file)


# In[6]:


pdf_reader


# In[7]:


pdf_reader.getIsEncrypted()


# In[8]:


pdf_reader.getNumPages()


# In[47]:


text1=" "


# In[48]:


for x in range(0,17):
    page=pdf_reader.getPage(x)
    text=page.extractText()
    text1=text1+text
print(text1)


# In[50]:


question=re.compile("\d{1,2}.[A-Za-z]")


# In[51]:


for line in text1.split('\n'):
    if question.match(line):
        print(line)


# In[74]:


options=re.compile("\(\d{1}\)[A-Z]{1}[a-z]{1,30}")


# In[75]:


for line in text1.split('\n'):
    if options.match(line):
        print(line)


# In[63]:


answer=re.compile("Sol.[A-Za-z]")


# In[64]:


for line in text1.split('\n'):
    if answer.match(line):
        print(line)


# In[ ]:




