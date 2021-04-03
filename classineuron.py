#!/usr/bin/env python
# coding: utf-8

# In[66]:


import os
os.getcwd()
os.mkdir('/Users/akhilsonga/Desktop/ineuron')
os.mkdir('/Users/akhilsonga/Desktop/ineuron/one')
os.mkdir('/Users/akhilsonga/Desktop/ineuron/two')
os.mkdir('/Users/akhilsonga/Desktop/ineuron/temp')
os.chdir('/Users/akhilsonga/Desktop/ineuron/one')
os.getcwd()
for i in range(10):
    s = str(i) + '.txt'
    print(s)
    f = open(s,"w")
    f.write("akhilsongafile ")
    f.close()
os.getcwd()
os.getcwd()
os.listdir()
list = []
for i in os.listdir():
    f = open(i,"r")
    list.append(f.read())
    f.close()
os.chdir('/Users/akhilsonga/Desktop/ineuron/temp')
f = open("result.txt", "w")
f.write(str(list))
f.close()
import shutil
os.chdir('/Users/akhilsonga/Desktop/ineuron/one')
sl = []
for i in range(10):
    sl.append(str(i) + '.txt')
print(sl)
for i in range(10):
    sd = '/Users/akhilsonga/Desktop/ineuron/one/' + sl[i]
    shutil.move(sd,'/Users/akhilsonga/Desktop/ineuron/two')
    print("moved")
shutil.move('/Users/akhilsonga/Desktop/ineuron/temp/result.txt','/Users/akhilsonga/Desktop/ineuron/one')
os.rmdir('/Users/akhilsonga/Desktop/ineuron/temp')
  



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




