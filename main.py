import pandas as pd                  
from difflib import SequenceMatcher    
from geopy.distance import geodesic 
import geopy.distance 

Data= pd.read_csv('E:/assignment_data.csv')
X=Data.iloc[:,0].values              
y=Data.iloc[:,1:].values  
temp=[None]*len(X)

if SequenceMatcher(None, X[0], X[1]).ratio()>0.6 and geopy.distance.geodesic(y[0], y[1]).m<=200:  
    temp[0]=1
else:
    temp[0]=0

for i in range(0,len(X)-2):
    if (SequenceMatcher(None, X[i+1], X[i]).ratio()>0.6 and geopy.distance.geodesic(y[i+1], y[i]).m<=200) or (SequenceMatcher(None, X[i+1], X[i+2]).ratio()>0.6 and geopy.distance.geodesic(y[i+1], y[i+2]).m<=200):
        temp[i+1]=1                                                                  
    else:
        temp[i+1]=0 

if SequenceMatcher(None, X[len(X)-1], X[len(X)-2]).ratio()>0.6 and geopy.distance.geodesic(y[len(X)-1], y[len(X)-2]).m<=200:
    temp[len(X)-1]=1
else:
    temp[len(X)-1]=0

df1=pd.DataFrame({'name':X})                        
df2=pd.DataFrame({'lat':y[:,0]})                     
df3=pd.DataFrame({'long':y[:,1]})                    
df4=pd.DataFrame({'is_similar':temp})                
Result_data=pd.concat([df1,df2,df3,df4],axis=1)

Result_data.to_csv("Result_assignment.csv",index=False)