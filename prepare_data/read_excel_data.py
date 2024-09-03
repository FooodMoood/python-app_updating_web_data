import pandas as pd
import prepare_data.config as config_prepare_data

class ExcelDataReader:
    def __init__(self, recipe_id, table):
        self.recipe_id = recipe_id
        self.table= table
    
    def fetch_data(self):
        df = pd.read_excel(config_prepare_data.path_file_excel, sheet_name=self.table)
        return df
    
    def get_memory_table_name(self):
        return 'data'