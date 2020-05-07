import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import csv
import anvil.media
from io import BytesIO

import pandas as pd
import anvil.media

import Global


@anvil.server.callable
def store_data(file):
  filedata = file.get_bytes()
  df = pd.read_csv(BytesIO(filedata))
  anvil.server.launch_background_task('server_store', df.to_dict(orient="records"))
  
@anvil.server.callable
def get_entries(list):
  print(list[0],list[1],list[2])
      
@anvil.server.background_task    
def server_store(dict_df):
  print(dict_df[0])
  for d in dict_df:
    print(d)
    # d is now a dict of {columnname -> value} for this row
    # We use Python's **kwargs syntax to pass the whole dict as
    # keyword arguments
    app_tables.new_y.add_row(**d)






      

        
        
        