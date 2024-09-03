import traceback

import prepare_data.config as config_prepare_data
from prepare_data.text_extractor import *
from prepare_data.scripts_social_media.recipe_data_handler import *

config = {
    "path_file_output": config_prepare_data.path_file_output,
    "path_folder_recipies": config_prepare_data.path_folder_recipies,
    "file_name_beginning_recipe": config_prepare_data.file_name_beginning_recipe,
    "file_extension_md": config_prepare_data.file_extension_md,
    "table_recipies": config_prepare_data.table_recipies,
    "table_recipe_ingredients": config_prepare_data.table_recipe_ingredients,
    "filtered_col": config_prepare_data.filtered_col,
    "col_dish_name": config_prepare_data.col_dish_name,
    "col_general_dish_type": config_prepare_data.col_general_dish_type,
    "col_dish_no_id": config_prepare_data.col_dish_no_id,
    "col_ingredient_id": config_prepare_data.col_ingredient_id,
    "replace_text_recipe_title": config_prepare_data.replace_text_recipe_title,
    "replace_text_recipe_number": config_prepare_data.replace_text_recipe_number,
    "replace_text_ingredients": config_prepare_data.replace_text_ingredients,
    "replace_text_recipe": config_prepare_data.replace_text_recipe,
    "extract_recipe_start_delimiter": config_prepare_data.extract_recipe_start_delimiter,
    "extract_recipe_end_delimiter": config_prepare_data.extract_recipe_end_delimiter
}

class SocialMediaPrompts:
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id

    def prepare_social_media_prompts(self):
        try:
            recipe_id = self.recipe_id
            param = [recipe_id]      
            handler = RecipeDataHandler(recipe_id, param, config)

            # Load data from excel
            handler.load_data(config['table_recipies'], 'recipies')
            handler.load_data(config['table_recipe_ingredients'], 'recipe_ingredients')

            # Get _TEXT_TITLE (recipe title)
            result_str = handler.process_query("SELECT [{col_dish_name}] FROM [{table_recipies}] WHERE [{filtered_col}] = ?",
                    {"col_dish_name": config['col_dish_name'], "table_recipies": config['table_recipies'], "filtered_col": config['filtered_col']})
            handler.modify_text(config["path_file_output"], config["replace_text_recipe_title"], result_str)

            # Get _TEXT_RECIPE_NO (number of recipe preceded #)
            result_str = handler.process_query(
                    """SELECT 
                        UPPER(SUBSTR([{col_general_dish_type}], 1, 1)) || SUBSTR([{col_general_dish_type}], 2) || ' #' || CAST([{col_dish_no_id}] AS INTEGER) 
                        FROM [{table_recipies}] 
                        WHERE [{filtered_col}] = ?""",
                    {
                        "col_general_dish_type": config['col_general_dish_type'],
                        "col_dish_no_id": config['col_dish_no_id'],
                        "table_recipies": config['table_recipies'],
                        "filtered_col": config['filtered_col']
                    }
            )
            handler.modify_text(config["path_file_output"], config["replace_text_recipe_number"], result_str)

            # Get _TEXT_INGREDIENTS (list of recipe ingredients)
            result_str = handler.process_query(
                    "SELECT [{col_ingredient_id}] FROM [{table_recipe_ingredients}] WHERE [{filtered_col}] = ?",
                    {
                        "col_ingredient_id": config['col_ingredient_id'],
                        "table_recipe_ingredients": config['table_recipe_ingredients'],
                        "filtered_col": config['filtered_col']
                    }
            )
            handler.modify_text(config["path_file_output"], config["replace_text_ingredients"], result_str)

            # Get _TEXT_RECIPE (recipe description)
            full_file_name = config["path_folder_recipies"] + config["file_name_beginning_recipe"] + recipe_id + config["file_extension_md"]
            file_manager = FileTextManager(full_file_name)
            oryginal_recipe = file_manager.read_data()

            extract_text = TextExtractor(config["extract_recipe_start_delimiter"], config["extract_recipe_end_delimiter"])
            extract_recipe = extract_text.extract_text(oryginal_recipe)

            handler.modify_text(config["path_file_output"], config["replace_text_recipe"], extract_recipe)

            # Prepare OUTPUT DATA = FULL READY PROMPT
            output_manager = FileTextManager(config["path_file_output"])
            output_data = output_manager.read_data()

            return output_data
        
        except Exception as e:
            error_message = f"Error preparing social media parts of description: {str(e)}"
            trace = traceback.format_exc()
            print(error_message)
            print("Traceback details:")
            print(trace)
            return None