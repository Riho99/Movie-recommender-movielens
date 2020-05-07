from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    #call server module
    #anvil.server.call('module_init')
    self.label_3.bold=True
    self.label_3.font_size=18
    
    
    # Any code you write here will run when the form opens.
    #self.drop_down_1.items= [(r['title'],r['movieId']) for r in app_tables.movies.search()]
    #self.drop_down_2.items= [(r['title'],r['movieId']) for r in app_tables.movies.search()]
    #self.drop_down_3.items= [(r['title'],r['movieId']) for r in app_tables.movies.search()]
    
  def file_loader_1_change(self, file, **event_args):
    anvil.server.call('store_data',file)
    
    

  def button_1_click(self, **event_args):
    if self.drop_down_1.selected_value is None or  self.drop_down_2.selected_value is None or self.drop_down_3.selected_value is None:
      alert('Please select 3 movies')
    else:  
      #print(self.drop_down_1.selected_value)
      list=tuple(anvil.server.call('test',self.drop_down_1.selected_value,self.drop_down_2.selected_value,self.drop_down_3.selected_value)[0])
    
      self.data_grid_1.visible=True;
      self.data_grid_1.clear()
      self.data_grid_1.columns = [
      { "id": "A", "title": "Title", "data_key": "title" },
      { "id": "B", "title": "Genre", "data_key": "genres" },
      ]
      
      rp = RepeatingPanel(item_template=DataRowPanel)
      
      m_row = app_tables.movies.search(movieId =q.any_of(*list))
      
      rp.items =[({'title':r['title'],'genres': r['genres']}) for r in m_row]
      # Add the repeating panel to your data grid
    
      self.data_grid_1.add_component(rp)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_1_change(self, **event_args):
      if len(self.text_box_1.text)>2:
        self.drop_down_1.enabled=True
        self.drop_down_1.items=[(r['title'],r['movieId']) for r in app_tables.movies.search(tables.order_by('title'),title=q.ilike("%"+self.text_box_1.text+"%"))]
        #self.drop_down_1.
        
      pass

  def text_box_2_change(self, **event_args):
      if len(self.text_box_2.text)>2:
        self.drop_down_2.enabled=True
        self.drop_down_2.items=[(r['title'],r['movieId']) for r in app_tables.movies.search(tables.order_by('title'),title=q.ilike("%"+self.text_box_2.text+"%"))]
      pass

  def text_box_3_change(self, **event_args):
    if len(self.text_box_3.text)>2:
        self.drop_down_3.enabled=True
        self.drop_down_3.items=[(r['title'],r['movieId']) for r in app_tables.movies.search(tables.order_by('title'),title=q.ilike("%"+self.text_box_3.text+"%"))]
    pass






  
  

