import traceback
import prepare_data.config as config_prepare_data
import prepare_data.get_config as get_config_prepare_data
from prepare_data.scripts_social_media.prepare_social_media_prompts import *
from prepare_data.scripts_wordpress.wp_recipe_data_handler import *
from prepare_data.scripts_wordpress.prepare_wordpress_post_code import *

# Set MAIN VARIABLES
PLATFORM_YOUTUBE = get_config_prepare_data.PLATFORM_YOUTUBE
PLATFORM_INSTAGRAM = get_config_prepare_data.PLATFORM_INSTAGRAM
PLATFORM_PINTEREST = get_config_prepare_data.PLATFORM_PINTEREST
PLATFORM_WORDPRESS = get_config_prepare_data.PLATFORM_WORDPRESS

path_yt_description = config_prepare_data.path_file_prompt_yt_description
path_instagram_description = config_prepare_data.path_file_prompt_instagram_description
path_pinterest_description = config_prepare_data.path_file_prompt_pinterest_description
path_wp_main_temp = config_prepare_data.path_file_wp_main_template_recipe_post
path_file_output = config_prepare_data.path_file_output

class PreparePromptTemplate:
        def __init__(self, website_type):
            self.website_type = website_type

        def prepare_prompt_template(self):
            website_type = self.website_type

            if website_type == PLATFORM_YOUTUBE:
                prompt_path = path_yt_description
            elif website_type == PLATFORM_INSTAGRAM:
                prompt_path = path_instagram_description
            elif website_type == PLATFORM_PINTEREST:
                prompt_path = path_pinterest_description
            elif website_type == PLATFORM_WORDPRESS:
                prompt_path = path_wp_main_temp
            else:
                raise ValueError("Unsupported website typ")  

            copied_data = FileTextManager(prompt_path).read_data()
            FileTextManager(path_file_output, copied_data).write_data()

class DescriptionHandler:
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id

    def prepare_social_media_description(self):
        try:
            output_data = SocialMediaPrompts(self.recipe_id).prepare_social_media_prompts()
            return output_data
        
        except Exception as e:
            error_message = f"Error preparing social media description: {str(e)}"
            trace = traceback.format_exc()
            print(error_message)
            print("Traceback details:")
            print(trace)
            return None
    
    def prepare_wordpress_description(self):
        try:
            output_data = WordpressPost(self.recipe_id).prepare_wordpress_post()
            return output_data
        
        except Exception as e:
            error_message = f"Error preparing Wordpress description handler: {str(e)}"
            trace = traceback.format_exc()
            print(error_message)
            print("Traceback details:")
            print(trace)
            return None
