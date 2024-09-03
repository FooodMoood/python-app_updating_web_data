from backup.backup_runner import RunBackups
from prepare_data.description_handler import PreparePromptTemplate, DescriptionHandler
import ctk_components.get_config as get_config_ctk

class WebsiteHandler:
    def __init__(self, recipe_id, website_type):
        self.recipe_id = recipe_id
        self.website_type = website_type

    def perform_action(self):
        try:
            run_backup = RunBackups()
            run_backup.run_backups()

            prompt_template = PreparePromptTemplate(self.website_type)
            prompt_template.prepare_prompt_template()

            if self.website_type == get_config_ctk.PLATFORM_WORDPRESS:
                handler = DescriptionHandler(self.recipe_id)
                output_data = handler.prepare_wordpress_description()
            else:
                handler = DescriptionHandler(self.recipe_id)
                output_data = handler.prepare_social_media_description()
            
            return output_data
        
        except Exception as e:
            error_message = f"An error occurred in WebsiteHandler: {str(e)}"
            # Log the error or handle it as needed
            print(error_message)
            raise Exception(error_message)