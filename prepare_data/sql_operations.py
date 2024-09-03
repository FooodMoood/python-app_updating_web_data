import sqlite3
import pandas as pd

class SQLDataProcessor1:
    def __init__(self, data, query, params):
        self.data = data
        self.query = query
        self.params = params if params is not None else[]

    def process_data(self):
        # Ensure params is a tuple
        if not isinstance(self.params, (list, tuple)):
            self.params = [self.params]

        conn = sqlite3.connect(':memory:')
        self.data.to_sql('data', conn, index=False, if_exists='replace')
        cursor = conn.cursor()
        cursor.execute(self.query, self.params)
        result = cursor.fetchall()
        conn.close()

        result_str = '\n'.join([' '.join(map(str, row)) for row in result])
        return result_str
    
class SQLDataProcessor:
    def __init__(self, dataframes, query, params):
        """
        :param dataframes: A dictionary of dataframes to be loaded into the SQL database.
                            Keys are table names and values are the dataframes.
        :param query: SQL query string
        :param params: List of tuple of parameters to use with the SQL query
        """
        self.dataframes = dataframes
        self.query = query
        self.params = params if params is not None else []

    def process_data(self):
        # Ensure params is a tuple
        if not isinstance(self.params, (list,tuple)):
            self.params = [self.params]

        # Connect to a SQLite in-memoty database
        conn = sqlite3.connect(':memory:')

        # Load each dataframe into the database as a separate table
        for table_name, df in self.dataframes.items():
            # print(f"Loading table {table_name} into database.")
            df.to_sql(table_name, conn, index=False, if_exists='replace')

        # Execute the query
        cursor = conn.cursor()
        cursor.execute(self.query, self.params)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Format the result into a string
        result_str = '\n'.join([' '.join(map(str, row)) for row in result])
        return result_str