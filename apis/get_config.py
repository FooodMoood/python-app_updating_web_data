import os
import sys
import apis.config as config_apis

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

replace_text_food_photo = config_apis.replace_text_food_photo
replace_text_dietary_curiosity = config_apis.replace_text_dietary_curiosity
