import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config as main_config
import prepare_data.config as config 

## MAIN CONFIG
parent_dir = main_config.parent_dir

path_folder_backup_with_data_files = main_config.path_folder_backup_with_data_files
path_folder_backup_with_code_files = main_config.path_folder_backup_with_code_files

## CONFIG
path_file_excel = config.path_file_excel
path_folder_prepare_data = config.path_folder_prepare_data
path_folder_templates = config.path_folder_templates

