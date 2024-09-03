import os

# API's VARIABLES
## Wordpress
wp_base_url = "YOUR_URL"
wp_username = 'YOUR_USERNAME'
wp_password = 'YOUR_PASSOWRD'
auth_url = f"{wp_base_url}/wp-json/api/v1/token"
new_post_url = f"{wp_base_url}/wp-json/wp/v2/posts"

wp_post_status = "private"

# MAIN PATHS
## Path for all needed files with folders
script_dir = os.path.dirname(__file__)
path_folder_output_data = os.path.join(script_dir, 'outputs')
path_file_output = os.path.join(path_folder_output_data, 'output.txt')
