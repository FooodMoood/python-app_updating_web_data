# The order of creating descriptions for the post
# _IMG_SRC_FOOD_PHOTO (single) - not used now
# _TEXT_DIETARY_CURIOSITY (single)
# _INSERT_INGREDIENTS_LIST
# _INSERT_RECIPE_STEPS
# _INSERT_TIP_STEPS
# _VALUE_KCAL (single)
# _VALUE_CARBS (single)
# _VALUE_PROTEIN (single)
# _VALUE_FATS (single)
# _HREF_YOUTUBE (single)

import traceback
import prepare_data.config as config_prepare_data
from prepare_data.scripts_wordpress.wp_recipe_data_handler import *
from prepare_data.text_manager import *

config = {
    "path_file_output": config_prepare_data.path_file_output,   
    "path_file_wp_output_recipe_steps": config_prepare_data.path_file_wp_output_recipe_steps,
    "path_file_wp_output_recipe_tips": config_prepare_data.path_file_wp_output_recipe_tips,
    "path_file_wp_output_ingredients_list": config_prepare_data.path_file_wp_output_ingredients_list,
    "path_file_wp_temp_file": config_prepare_data.path_file_wp_temp_file,     
    "path_file_wp_template_ingredients_list": config_prepare_data.path_file_wp_template_ingredients_list,
    "path_file_wp_template_recipe_steps": config_prepare_data.path_file_wp_template_recipe_steps,
    "path_file_wp_temp_template_recipe_steps": config_prepare_data.path_file_wp_temp_template_recipe_steps,
    "path_file_wp_template_recipe_tips": config_prepare_data.path_file_wp_template_recipe_tips,
    "path_folder_dietary_curiosity": config_prepare_data.path_folder_dietary_curiosity, 
    "path_folder_recipies": config_prepare_data.path_folder_recipies,
    "file_name_beginning_dietary_curiosity": config_prepare_data.file_name_beginning_dietary_curiosity,  
    "file_name_beginning_recipe": config_prepare_data.file_name_beginning_recipe,
    "file_extension_md": config_prepare_data.file_extension_md,          
    "table_recipies": config_prepare_data.table_recipies,
    "table_recipe_ingredients": config_prepare_data.table_recipe_ingredients,
    "table_ingredients": config_prepare_data.table_ingredients,
    "table_recipe_category": config_prepare_data.table_recipe_category,
    "col_wp_category_id": config_prepare_data.col_wp_category_id,
    "col_ingredient_id": config_prepare_data.col_ingredient_id,
    "col_ingredient_wp_url": config_prepare_data.col_ingredient_wp_url,
    "col_ingredient_name": config_prepare_data.col_ingredient_name,
    "col_dietary_curiosity_id": config_prepare_data.col_dietary_curiosity_id,
    "col_dish_name": config_prepare_data.col_dish_name,
    "col_dish_no_id": config_prepare_data.col_dish_no_id,
    "col_general_dish_type": config_prepare_data.col_general_dish_type,
    "col_wp_portion": config_prepare_data.col_wp_portion,
    "col_kcal": config_prepare_data.col_kcal,
    "col_carbs": config_prepare_data.col_carbs,
    "col_protein": config_prepare_data.col_protein,
    "col_fat": config_prepare_data.col_fat,
    "filtered_col": config_prepare_data.filtered_col,
    "replace_text_amount_x": config_prepare_data.replace_text_amount_x,
    "replace_text_ingredient_x": config_prepare_data.replace_text_ingredient_x,
    "replace_text_food_photo": config_prepare_data.replace_text_food_photo,
    "replace_text_insert_ingredients_lists": config_prepare_data.replace_text_insert_ingredients_lists,
    "replace_text_insert_recipe_steps": config_prepare_data.replace_text_insert_recipe_steps,
    "replace_text_insert_output_recipe_steps": config_prepare_data.replace_text_insert_output_recipe_steps,
    "replace_text_insert_tip_steps": config_prepare_data.replace_text_insert_tip_steps,
    "replace_text_recipe_step_x": config_prepare_data.replace_text_recipe_step_x,
    "replace_text_tip_x": config_prepare_data.replace_text_tip_x,
    "replace_text_dietary_curiosity": config_prepare_data.replace_text_dietary_curiosity,
    "replace_text_value_kcal": config_prepare_data.replace_text_value_kcal,
    "replace_text_value_carbs": config_prepare_data.replace_text_value_carbs,
    "replace_text_value_protein": config_prepare_data.replace_text_value_protein,
    "replace_text_value_fats": config_prepare_data.replace_text_value_fats,
    "replace_text_href_youtube": config_prepare_data.replace_text_href_youtube,
    "replace_text_img_src_youtube_icon": config_prepare_data.replace_text_img_src_youtube_icon,
    "replace_text_wp_img_src_ingredient_icon": config_prepare_data.replace_text_wp_img_src_ingredient_icon,
    "yt_icon_url": config_prepare_data.yt_icon_url,
    "extract_recipe_start_delimiter": config_prepare_data.extract_recipe_start_delimiter, 
    "extract_recipe_end_delimiter": config_prepare_data.extract_recipe_end_delimiter,
    "extract_3_hash": config_prepare_data.extract_3_hash
}

class WordpressPost:
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id

    def prepare_wordpress_post(self):
        try:
            recipe_id = self.recipe_id
            param = [recipe_id]      
            handler = WordpressDataHandler(recipe_id, param, config)

            # Load datatables from excel
            handler.load_data(config['table_recipies'], 'recipies')
            handler.load_data(config['table_recipe_ingredients'], 'recipe_ingredients')
            handler.load_data(config['table_ingredients'], 'ingredients')
            handler.load_data(config['table_recipe_category'], 'recipe_category')

            # Get _TEXT_DIETARY_CURIOSITY (single)
            result_str = handler.process_query("SELECT [{col_dietary_curiosity_id}] FROM [{table_recipies}] WHERE [{filtered_col}] = ?",
                    {"col_dietary_curiosity_id": config['col_dietary_curiosity_id'], "table_recipies": config['table_recipies'], "filtered_col": config['filtered_col']})
            full_file_name = config["path_folder_dietary_curiosity"] + config["file_name_beginning_dietary_curiosity"] + result_str + config["file_extension_md"]
            oryginal_recipe = FileTextManager(full_file_name).read_data()
            extract_recipe = TextExtractor(config_prepare_data.extract_dietary_curiosity_start_delimiter).extract_text(oryginal_recipe)
            handler.modify_text(config["path_file_output"], config["replace_text_dietary_curiosity"], extract_recipe)

            # Get _INSERT_INGREDIENTS_LIST
            FileTextManager(config["path_file_wp_output_ingredients_list"]).clear_data()
            result_str = handler.process_query("SELECT COUNT({filtered_col}) FROM {table_recipe_ingredients} WHERE {filtered_col} = ?",
                {"filtered_col": config['filtered_col'], "table_recipe_ingredients": config['table_recipe_ingredients']})
            result_int = int(result_str)

            for i in range(result_int):
                # Copy wordpress-code template with ingredients list
                copied_template = FileTextManager(config["path_file_wp_template_ingredients_list"]).read_data()

                # Paste wordpress-code template with ingredients list
                FileTextManager(config["path_file_wp_output_ingredients_list"], copied_template).append_to_file()

                # Get list of ingredients name form table with ingredients
                result_str = handler.process_query("SELECT {col_ingredient_id} FROM {table_recipe_ingredients} WHERE {filtered_col} = ? LIMIT 1 OFFSET {i}",
                    {"col_ingredient_id": config['col_ingredient_id'], "table_recipe_ingredients": config['table_recipe_ingredients'], "filtered_col": config['filtered_col'], "i": i})
                ReplaceStringsInTextFile(config["path_file_wp_output_ingredients_list"], config["replace_text_ingredient_x"], result_str).replace_text()

                # Get list of INGREDIENT PORTIONS form table with ingredients
                result_str = handler.process_query("SELECT {col_wp_portion} FROM {table_recipe_ingredients} WHERE {filtered_col} = ? LIMIT 1 OFFSET {i}",
                    {"col_wp_portion": config['col_wp_portion'], "table_recipe_ingredients": config['table_recipe_ingredients'], "filtered_col": config['filtered_col'], "i": i})
                ReplaceStringsInTextFile(config["path_file_wp_output_ingredients_list"], config["replace_text_amount_x"], result_str).replace_text()
                
                # Get ICONS URLS from table with ingredients
                result_str = handler.process_query("""SELECT {table_ingredients}.{col_ingredient_wp_url} FROM {table_ingredients} LEFT JOIN {table_recipe_ingredients} 
                                                        ON {table_recipe_ingredients}.{col_ingredient_id} = {table_ingredients}.{col_ingredient_name}
                                                        WHERE {table_recipe_ingredients}.{filtered_col} = ? LIMIT 1 OFFSET {i}""",
                    {"table_ingredients": config['table_ingredients'], "table_recipe_ingredients": config['table_recipe_ingredients'], 
                     "col_ingredient_wp_url": config['col_ingredient_wp_url'], "col_ingredient_id": config['col_ingredient_id'], "col_ingredient_name": config['col_ingredient_name'],
                     "filtered_col": config['filtered_col'], "i": i})
                ReplaceStringsInTextFile(config["path_file_wp_output_ingredients_list"], config["replace_text_wp_img_src_ingredient_icon"], result_str).replace_text()
                ReplaceStringsInTextFile(config["path_file_wp_output_ingredients_list"], config["replace_text_wp_img_src_ingredient_icon"], result_str).replace_text() # because it appears twice in the template

            output_data = FileTextManager(config["path_file_wp_output_ingredients_list"]).read_data()
            ReplaceStringsInTextFile(config["path_file_output"], config["replace_text_insert_ingredients_lists"], output_data).replace_text()

            # Get _INSERT_RECIPE_STEPS
            full_file_name = config["path_folder_recipies"] + config["file_name_beginning_recipe"] + recipe_id + config["file_extension_md"]
            oryginal_recipe = FileTextManager(full_file_name).read_data()
            extract_recipe = TextExtractor(config["extract_recipe_start_delimiter"], config["extract_recipe_end_delimiter"]).extract_text(oryginal_recipe)

                # Create code with recipe from the input text with recipe 
            CreateMultilinesList(extract_recipe, config["path_file_wp_template_recipe_steps"], config["path_file_wp_temp_file"], config["replace_text_recipe_step_x"]).convert_to_list()
            temp_data = FileTextManager(config["path_file_wp_temp_template_recipe_steps"]).read_data()
            FileTextManager(config["path_file_wp_output_recipe_steps"], temp_data).write_data()
            copied_data = FileTextManager(config["path_file_wp_temp_file"]).read_data()
            ReplaceStringsInTextFile(config["path_file_wp_output_recipe_steps"], config["replace_text_insert_recipe_steps"], copied_data).replace_text()

                # Write full preapred recipe code to the main output file
            copied_data = FileTextManager(config["path_file_wp_output_recipe_steps"]).read_data()
            ReplaceStringsInTextFile(config["path_file_output"], config["replace_text_insert_output_recipe_steps"], copied_data).replace_text()
 
            # Get _INSERT_TIP_STEPS - use variable 'oryginal_recipe' from get _INSERT_RECIPE_STEPS
            if config["extract_recipe_end_delimiter"] in oryginal_recipe: 
                extract_recipe = TextExtractor(config["extract_recipe_end_delimiter"]).extract_text(oryginal_recipe)
                CreateMultilinesList(extract_recipe, config["path_file_wp_template_recipe_tips"], config["path_file_wp_output_recipe_tips"], config["replace_text_tip_x"]).convert_to_list()
                copied_data = FileTextManager(config["path_file_wp_output_recipe_tips"]).read_data()
                ReplaceStringsInTextFile(config["path_file_output"], config["replace_text_insert_tip_steps"], copied_data).replace_text()
            else:
                return False

            # Get _VALUE_KCAL (single)
            result_str = handler.process_query("SELECT CAST(SUM([{col_kcal}]) AS INTEGER) FROM [{table_recipe_ingredients}] WHERE [{filtered_col}] = ?",
                    {"col_kcal": config['col_kcal'], "table_recipe_ingredients": config['table_recipe_ingredients'], "filtered_col": config['filtered_col']})
            handler.modify_text(config["path_file_output"], config["replace_text_value_kcal"], result_str)

            # Get _VALUE_CARBS (single)
            result_str = handler.process_query("SELECT CAST(SUM([{col_carbs}]) AS Integer) FROM [{table_recipe_ingredients}] WHERE [{filtered_col}] = ?",
                    {"col_carbs": config['col_carbs'], "table_recipe_ingredients": config['table_recipe_ingredients'], "filtered_col": config['filtered_col']})
            handler.modify_text(config["path_file_output"], config["replace_text_value_carbs"], result_str)

            # Get _VALUE_PROTEIN (single)
            result_str = handler.process_query("SELECT CAST(SUM([{col_protein}]) AS Integer) FROM [{table_recipe_ingredients}] WHERE [{filtered_col}] = ?",
                    {"col_protein": config['col_protein'], "table_recipe_ingredients": config['table_recipe_ingredients'], "filtered_col": config['filtered_col']})
            handler.modify_text(config["path_file_output"], config["replace_text_value_protein"], result_str)

            # Get _VALUE_FATS (single)
            result_str = handler.process_query("SELECT CAST(SUM([{col_fat}]) AS Integer) FROM [{table_recipe_ingredients}] WHERE [{filtered_col}] = ?",
                    {"col_fat": config['col_fat'], "table_recipe_ingredients": config['table_recipe_ingredients'], "filtered_col": config['filtered_col']})
            handler.modify_text(config["path_file_output"], config["replace_text_value_fats"], result_str)

            # If something is empty in template then replace example text with empty space to avoid any code issues
            handler.modify_text(config["path_file_output"], config["replace_text_food_photo"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_dietary_curiosity"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_insert_ingredients_lists"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_insert_recipe_steps"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_insert_tip_steps"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_value_kcal"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_value_fats"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_value_protein"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_value_carbs"], '')
            handler.modify_text(config["path_file_output"], config["replace_text_href_youtube"], '.')
            handler.modify_text(config["path_file_output"], config["replace_text_img_src_youtube_icon"], config['yt_icon_url']) # include _HREF_YOUTUBE (single)
            
            output_data = FileTextManager(config["path_file_output"]).read_data()

            return output_data
        
        except Exception as e:
            error_message = f"Error preparing Wordpress post parts of post description: {str(e)}"
            trace = traceback.format_exc()
            print(error_message)
            print("Traceback details:")
            print(trace)
            return None