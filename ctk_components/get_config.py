import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config as config
import prepare_data.config as config_prepare_data

PLATFORM_YOUTUBE = config.PLATFORM_YOUTUBE
PLATFORM_INSTAGRAM = config.PLATFORM_INSTAGRAM
PLATFORM_PINTEREST = config.PLATFORM_PINTEREST
PLATFORM_WORDPRESS = config.PLATFORM_WORDPRESS

path_github_repo = config.path_github_repo

path_file_output = config_prepare_data.path_file_output
