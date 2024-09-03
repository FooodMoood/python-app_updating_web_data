import os
import requests

import apis.config as config_apis

# Set CONST 
wp_base_url = config_apis.wp_base_url
wp_username = config_apis.wp_username
wp_password = config_apis.wp_password
wp_post_status = config_apis.wp_post_status

# # [TEST] Example VARIABLES for post
# wp_post_title = "Strawberries in Chocolate [Recipe #29]"
# wp_post_content = ""
# wp_post_slug = "recipe-29"
# wp_post_categories = [27, 35, 61, 29]

# URL for JWT autorization API
auth_url = config_apis.auth_url

class PublishPostOnWordpress:
    def __init__(self, wp_post_code, wp_post_title, wp_post_slug, wp_post_categories_list):
        self.wp_post_code = wp_post_code
        self.wp_post_title = wp_post_title
        self.wp_post_slug = wp_post_slug
        self.wp_post_categories_list = wp_post_categories_list

    def create_wp_post(self):    
        # Data for publication
        auth_data = {
            "username": wp_username,
            "password": wp_password
        }

        # Do POST request
        auth_response = requests.post(auth_url, json=auth_data)
        auth_response_data = auth_response.json()

        print("Server request:", auth_response_data)

        if 'jwt_token' in auth_response_data:
            token = auth_response_data['jwt_token']
            print("Get token JWT", token)
        else:
            print("Failed to obtain JWT. Check the server data and response.")
            exit()

        # Data to create new post
        new_post_url = config_apis.new_post_url
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        post_data = {
            'title': self.wp_post_title,
            'content': self.wp_post_code,
            'status': wp_post_status,
            'slug': self.wp_post_slug,
            'categories': self.wp_post_categories_list
        }

        # Create post
        response = requests.post(new_post_url, headers=headers, json=post_data)

        # Check response
        if response.status_code == 201:
            response_message = ("Post was created successfully. URL post: ", response.json()['link'])
            print(response_message)
        else:
            response_message = ("Post wasn't created. State: ", response.status_code, " Answer: ", response.json())
            print(response_message)