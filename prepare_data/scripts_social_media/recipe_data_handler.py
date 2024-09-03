from prepare_data.read_excel_data import *
from prepare_data.sql_operations import *
from prepare_data.create_multiline_list_from_txt import *

class RecipeDataHandler:
    def __init__(self, recipe_id, param, config):
        self.recipe_id = recipe_id
        self.param = param
        self.config = config
        self.dataframes = {}

    def load_data(self, excel_table_name, db_table_name):
        # Load data from Execl into a DataFrame and store it in a given name
        excel_reader = ExcelDataReader(self.recipe_id, excel_table_name)
        self.dataframes[db_table_name] = excel_reader.fetch_data()

    def process_query(self, query_template, column_names):
        # Format query and execute SQL on loaded dataframes
        query = query_template.format(**column_names)
        sql_processor = SQLDataProcessor(self.dataframes, query, self.param)
        return sql_processor.process_data()
    
    def modify_text(self, path, search_text, replace_text):
        # Replace text in a file
        text_modifier = ReplaceStringsInTextFile(path, search_text, replace_text)
        text_modifier.replace_text()