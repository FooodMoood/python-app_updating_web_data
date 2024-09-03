import traceback
import prepare_data.config as config_prepare_data
from prepare_data.scripts_wordpress.wp_recipe_data_handler import *
from prepare_data.scripts_wordpress.prepare_wordpress_post_code import *

config = {
    "table_recipies": config_prepare_data.table_recipies,
    "table_recipe_category": config_prepare_data.table_recipe_category,
    "col_dish_name": config_prepare_data.col_dish_name,
    "col_dish_no_id": config_prepare_data.col_dish_no_id,
    "col_general_dish_type": config_prepare_data.col_general_dish_type,
    "col_wp_category_id": config_prepare_data.col_wp_category_id,
    "filtered_col": config_prepare_data.filtered_col,
}

class GetAllDataForWordpressApi():
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id

    def all_wp_data_for_api(self):
        recipe_id = self.recipe_id
        param = [recipe_id]      
        handler = WordpressDataHandler(recipe_id, param, config)

        # Load datatables from excel
        handler.load_data(config['table_recipies'], 'recipies')
        handler.load_data(config['table_recipe_category'], 'recipe_category')

        # Get data for Wordpress API
        ## POST TITLE example: Chicken Wrap with Garlic Sauce [Recipe #28]
        wp_post_title = handler.process_query("""
                    SELECT [{col_dish_name}] || ' [' || UPPER(SUBSTR([{col_general_dish_type}], 1, 1)) || SUBSTR([{col_general_dish_type}], 2) || ' #' || CAST([{col_dish_no_id}] AS INTEGER) || ']' 
                    FROM [{table_recipies}] WHERE [{filtered_col}] = ?""",
                {"col_dish_name": config['col_dish_name'], 
                 "col_general_dish_type": config['col_general_dish_type'], 
                 "col_dish_no_id": config['col_dish_no_id'], 
                 "table_recipies": config['table_recipies'], 
                 "filtered_col": config['filtered_col']})

        ## POST SLUG example: recipe-28
        wp_post_slug = handler.process_query("""
                    SELECT [{col_general_dish_type}] || '-' || CAST([{col_dish_no_id}] AS INTEGER) 
                    FROM [{table_recipies}] WHERE [{filtered_col}] = ?""",
                {"col_general_dish_type": config['col_general_dish_type'], 
                 "col_dish_no_id": config['col_dish_no_id'], 
                 "table_recipies": config['table_recipies'], 
                 "filtered_col": config['filtered_col']})

        ## POST LIST CATEGORIES example: [27, 67, 52]
        wp_post_categories = handler.process_query("SELECT [{col_wp_category_id}] FROM [{table_recipe_category}] WHERE [{filtered_col}] = ?",
                {"col_wp_category_id": config['col_wp_category_id'], 
                 "table_recipe_category": config['table_recipe_category'], 
                 "filtered_col": config['filtered_col']})
        wp_post_categories_list = [int(num) for num in wp_post_categories.split()]

        ## POST CODE
        wp_post_code = WordpressPost(self.recipe_id).prepare_wordpress_post()

        return wp_post_code, wp_post_title, wp_post_slug, wp_post_categories_list