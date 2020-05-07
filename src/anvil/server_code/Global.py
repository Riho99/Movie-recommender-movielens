import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from io import BytesIO

import pandas as pd

from sklearn import *

import numpy as np

from sklearn.neighbors import KNeighborsClassifier


global table
table=app_tables.new_x.search().to_csv().get_bytes()
global new_x 
new_x= pd.read_csv(BytesIO(table))

global table2
table2=app_tables.new_y.search().to_csv().get_bytes()
global new_y 
new_y= pd.read_csv(BytesIO(table2))

if 'ID' in new_x.columns:
  new_x.drop(columns=['ID'],inplace=True)
if 'ID' in new_y.columns:  
  new_y.drop(columns=['ID'],inplace=True)    

global neigh
neigh= KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
neigh.fit(new_x, new_y)


@anvil.server.callable
def test(id1,id2,id3):
    return neigh.predict([[int(id1),int(id2),int(id3)]])
    #print(new_x.head())
  
  



  
  
  
  
  
  
  
  
  