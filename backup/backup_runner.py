from backup.create_backups import DataBackup

import backup.get_config as config

class RunBackups:
    def __init__(self):
        pass

    def run_backups(self):
        # Backup for data-food.xlsx
        food_data_backup = DataBackup(config.path_file_excel, config.path_folder_backup_with_data_files)
        food_data_backup.make_file_backup()

        # Backup for config files with all variables
        main_config_code_backup = DataBackup(config.parent_dir + "\config.py", config.path_folder_backup_with_code_files, "main")
        main_config_code_backup.make_file_backup()

        preapre_data_config_code_backup = DataBackup(config.path_folder_prepare_data + "\config.py", config.path_folder_backup_with_code_files, "prepare_data")
        preapre_data_config_code_backup.make_file_backup()

        # Make dirs backups
        templated_dir_data_backup = DataBackup(config.path_folder_templates, config.path_folder_backup_with_data_files)
        templated_dir_data_backup.make_directory_backup()