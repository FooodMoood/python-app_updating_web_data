from tkinter import messagebox

from prepare_data.scripts_wordpress.get_all_data_for_wp_api import *
from apis.api_publishing_posts_on_wordpress import *

class PostConfirmation:
    def __init__(self, root, recipe_id):
        self.root = root
        self.recipe_id = recipe_id
        self.ask_confirmation()

    def ask_confirmation(self):
        response = messagebox.askquestion("Confirm Post", "Are you sure you want to post this?")
        if response == 'yes':
            wp_post_code, wp_post_title, wp_post_slug, wp_post_categories_list = GetAllDataForWordpressApi(self.recipe_id).all_wp_data_for_api()
            PublishPostOnWordpress(wp_post_code, wp_post_title, wp_post_slug, wp_post_categories_list).create_wp_post()
            print("Post was created successfully!")
        else:
            print("Post creation cancelled")

