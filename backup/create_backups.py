import os
import shutil

class DataBackup:
    def __init__(self, source_path, backup_directory, name_suffix=""):
        self.source_path = source_path
        self.backup_directory = backup_directory
        self.name_suffix = name_suffix

        # Ensure the backup directory exist
        os.makedirs(self.backup_directory, exist_ok=True)
    
    def make_file_backup(self):
        try:
            base_name = os.path.basename(self.source_path)
            name, ext = os.path.splitext(base_name)
            
            if self.name_suffix:
                new_file_name = f"{name}_{self.name_suffix}{ext}"
            else:
                new_file_name = base_name

            backup_file_path = os.path.join(self.backup_directory, new_file_name)

            shutil.copy2(self.source_path, backup_file_path)
            print(f"File backup created at {backup_file_path}")

        except FileNotFoundError:
            print(f"Source file '{self.source_path}' not found.")
        except Exception as e:
            print(f"An error occurred while making a backup: {e}")

    def make_directory_backup(self):
        try:
            base_name = os.path.basename(self.source_path.rstrip('/'))

            if self.name_suffix:
                new_dir_name = f"{base_name}_{self.name_suffix}"
            else:
                new_dir_name = base_name

            backup_dir_path = os.path.join(self.backup_directory, new_dir_name)

            if os.path.exists(backup_dir_path):
                shutil.rmtree(backup_dir_path)

            shutil.copytree(self.source_path, backup_dir_path)
            print(f"Directory backup created at {backup_dir_path}")
        
        except FileNotFoundError:
            print(f"Source directory '{self.source_path}' not found.")
        except Exception as e:
            print(f"An error occurred while maikng a directory backup: {e}")


