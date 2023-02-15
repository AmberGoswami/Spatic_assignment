#!/usr/bin/env python
# coding: utf-8

# In[273]:


#importing libraries
import pandas as pd                    #for working with data sets
from difflib import SequenceMatcher    #provides classes and functions for comparing sequences.
from geopy.distance import geodesic    #to locate the coordinates


# In[274]:


#importing data
Data= pd.read_csv('E:/assignment_data.csv') #data(csv) location


# In[275]:


#Storing names and (lat,long) in variables
X=Data.iloc[:,0].values               #Storing names in X
y=Data.iloc[:,1:].values              #Storing lat and long in y 


# In[276]:


#Creating an empty list of the same length as of dataset
temp=[None]*len(X)


# In[277]:


#First element of the list (compares first and second name on the basis of similarity score and distance from each other (in metres))
if SequenceMatcher(None, X[0], X[1]).ratio()>0.6 and geopy.distance.geodesic(y[0], y[1]).m<=200:  
    temp[0]=1
else:
    temp[0]=0
    
#middle elements of the list (compares the names on the basis of similarity score and distance from the previous or the next name (in metres) in the loop)
for i in range(0,len(X)-2):
    if (SequenceMatcher(None, X[i+1], X[i]).ratio()>0.6 and geopy.distance.geodesic(y[i+1], y[i]).m<=200) or (SequenceMatcher(None, X[i+1], X[i+2]).ratio()>0.6 and geopy.distance.geodesic(y[i+1], y[i+2]).m<=200):
        temp[i+1]=1                                                                  
    else:
        temp[i+1]=0 
        
#last element of the list (compares last and second last name on the basis of similarity score and distance from each other (in metres))
if SequenceMatcher(None, X[len(X)-1], X[len(X)-2]).ratio()>0.6 and geopy.distance.geodesic(y[len(X)-1], y[len(X)-2]).m<=200:
    temp[len(X)-1]=1
else:
    temp[len(X)-1]=0


# In[278]:


#NOTE:
#1) SequenceMatcher class of difflib module is used to compare the similarity in the name of the strings. This class can be 
#   used to compare two input sequences or strings. In other words, this class is useful to use when finding similarities 
#   between two strings on the character level. It returns the similarity index in the ratio which follows the formula:  
#   2.0*M/T, where M=matches, T=total number of elements in both sequences. For our assignment the satisfying condition
#   for similarity is set up as similarity ratio>=0.6 which is optimum for considering names similarity.

#2) geopy locates the coordinates of addresses, cities, countries, and landmarks across the globe. It can calculate 
#   geodesic distance between two points (shortest path between two points) on the basis of there latitude and
#   longitude co-ordinates. For our assignment the satisfying condition for distance is set up as distance<=200 metres.


# In[279]:


#Necessary dataframes
df1=pd.DataFrame({'name':X})                         #names
df2=pd.DataFrame({'lat':y[:,0]})                     #latitude
df3=pd.DataFrame({'long':y[:,1]})                    #longitude
df4=pd.DataFrame({'is_similar':temp})                #is_similar (conditional results)
Result_data=pd.concat([df1,df2,df3,df4],axis=1)      #Joined result dataframe


# In[280]:


#cisualization of the result dataframe
Result_data


# In[281]:


#Conerting and exporting dataframe to excel file(.xlsx)
Result_data.to_csv("Result_assignment.csv",index=False)

