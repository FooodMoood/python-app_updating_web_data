import os

# COMMON DATA ***************************************************************************************
# filter_criteria = 'avocado_chocolate_mousse' # ONLY FOR TEST
filtered_col = 'id_readable_dish_name'

# MAIN PATHS ***************************************************************************************
## Path for all needed files with folders
parent_dir = os.path.dirname(os.path.dirname(__file__))
## Dirs in main file file
path_folder_prepare_data = parent_dir + r'\prepare_data'
path_folder_templates = path_folder_prepare_data + r'\templates'
path_folder_wp_recipe_post = path_folder_templates + r'\wordpress'
path_folder_ai_prompts = path_folder_templates + r'\chatgpt_prompts'
path_folder_output_data = path_folder_prepare_data + '\output'
## Dirs with data
path_folder_data_food = parent_dir + '\data'
path_folder_dietary_curiosity = path_folder_data_food + '\dietary_curiosity'
path_folder_recipies = path_folder_data_food + r'\recipies'

## FULL PATHS: Files with wordpress templates for recipe
### Main files
path_file_excel = path_folder_data_food + '\data-food.xlsx'
path_file_output = path_folder_output_data + '\output.txt'

### Individual records are stored in the main text file
### Records where you have to list something are in separated files and later it is pasted to the main file
path_file_wp_main_template_recipe_post = path_folder_wp_recipe_post + '\wp_post_main_template.txt'
path_file_wp_template_ingredients_list = path_folder_wp_recipe_post + '\wp_post_template_ingredients_list.txt'
path_file_wp_template_recipe_steps = path_folder_wp_recipe_post + '\wp_post_template_recipe_steps.txt'
path_file_wp_temp_template_recipe_steps = path_folder_wp_recipe_post + '\wp_post_temp_template_recipe_steps.txt'
path_file_wp_template_recipe_tips = path_folder_wp_recipe_post + '\wp_post_template_recipe_tips.txt'

path_file_wp_output_ingredients_list = path_folder_wp_recipe_post + '\wp_post_output_ingredients_list.txt'
path_file_wp_output_recipe_steps = path_folder_wp_recipe_post + '\wp_post_output_recipe_steps.txt'
path_file_wp_output_recipe_tips = path_folder_wp_recipe_post + '\wp_post_output_recipe_tips.txt'

path_file_wp_temp_file = path_folder_wp_recipe_post + r'\temp_file.txt'

## FULL PATHS: Prompts files
path_file_prompt_yt_description = path_folder_ai_prompts + '\PROMPT_CHATGPT-DESCRIPTION_FOR_YOUTUBE.txt'
path_file_prompt_instagram_description = path_folder_ai_prompts + '\PROMPT_CHATGPT-DESCRIPTION_FOR_INSTAGRAM.txt'
path_file_prompt_pinterest_description = path_folder_ai_prompts + '\PROMPT_CHATGPT-DESCRIPTION_FOR_PINTEREST.txt'

# DATA TO REPLACE ***************************************************************************************
## Inner data to replace in prompt and wordpress template
### Variables in main file
replace_text_food_photo = '_IMG_SRC_FOOD_PHOTO'
replace_text_dietary_curiosity = '_TEXT_DIETARY_CURIOSITY'

replace_text_insert_ingredients_lists = '_INSERT_INGREDIENTS_LIST'
replace_text_insert_recipe_steps = '_INSERT_RECIPE_STEPS'
replace_text_insert_output_recipe_steps = '_INSERT_OUTPUT_RECIPE_STEPS'
replace_text_insert_tip_steps = '_INSERT_TIP_STEPS'

replace_text_value_kcal = '_VALUE_KCAL'
replace_text_value_fats = '_VALUE_FATS'
replace_text_value_protein = '_VALUE_PROTEIN'
replace_text_value_carbs = '_VALUE_CARBS'

replace_text_href_youtube = '_HREF_YOUTUBE'
replace_text_img_src_youtube_icon = '_IMG_SRC_YOUTUBE_ICON'

replace_text_recipe_title = '_TEXT_TITLE'
# replace_text_title_for_3hash= '_TILTE_FOR_3HASH'
replace_text_recipe_number = '_TEXT_RECIPE_NO'
replace_text_ingredients = '_TEXT_INGREDIENTS'
replace_text_recipe = '_TEXT_RECIPE'

### Variables in subfiles with lists
replace_text_wp_img_src_ingredient_icon = '_IMG_SRC_INGREDIENT_ICON_X'
replace_text_ingredient_x = '_TEXT_INGREDIENT_X'
replace_text_amount_x = '_TEXT_AMOUNT_X'
replace_text_recipe_step_x = '_TEXT_RECIPE_STEP_X'
replace_text_tip_x = '_TEXT_TIP_X'

### Other variables for simple-single prompt (prepare data to recipie) 
replace_text_food_icon = "_TEXT_FOOD_ICON"
replace_text_dietary_curiosity_ingredient ="_TEXT_DIETARY_CURIOSITY_INGREDIENT"

# FOOD DATA IN TABLES (RECIPES DETAILS) ***************************************************************************************
## Data in main table - store basic-single information about the recipe like title, portions, tags etc.
table_recipies = 'recipies'
col_dish_name = 'dish_name'
col_general_dish_type = 'general_dish_type'
col_dish_no_id = 'dish_no_id'
col_dietary_curiosity_id = 'dietary_curiosity_id'

## Data in table with ingredients - store information about ingredients, nutrition values etc.
table_recipe_ingredients = 'recipe_ingredients'
col_wp_portion = "wp_portion"
col_ingredient_id = 'ingredient_id'
col_kcal = 'kcal'
col_protein = 'protein'
col_fat = 'fat'
col_carbs = 'carbs'
col_grams = 'grams'
col_portion_for_recipe = 'portion_for_recipe'

## Data with ingredients details
table_ingredients = 'ingredients'
col_ingredient_name = 'ingredient_name'
col_ingredient_icon_name = 'ingredient_icon_name'
col_ingredient_wp_url = "ingredient_wp_url"

## Data with recipe categories (categories from wordpress)
table_recipe_category = 'recipe_category'
col_wp_category_id = 'wp_category_id'

# OTHER SMALL INPUT DATA ***************************************************************************************
## File extensions
file_extension_md = ".md"

## Constants in filenames
file_name_beginning_recipe = r"\recipe-"
file_name_beginning_dietary_curiosity = "\dietary_curiosity-"

## Extractors for RECIPIES
extract_recipe_start_delimiter = "## Recipe"
extract_recipe_end_delimiter = "## Tips"
extract_dietary_curiosity_start_delimiter = "## Dietary Curiosity"
yt_icon_url = "YOUR_YOUTUBE_ICON_URL_IN_WORDPRESS"

