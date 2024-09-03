import sys
import os
import shutil

class FileMover:
    def __init__(self, source_path, destination_folder, file_name):
        self.source_path = source_path
        self.destination_folder = destination_folder
        self.file_name = file_name

    def move_file(self):
        full_source_path = os.path.join(self.source_path, self.file_name)

        if not os.path.isfile(full_source_path):
            return f"Error: File '{full_source_path}' does not exist."
        
        full_destination_path = os.path.join(self.destination_folder, self.file_name)

        try:
            shutil.move(full_source_path, full_destination_path)
            return f"File '{self.file_name}' was moved to '{self.destination_path}'"
        except Exception as e:
            return f"Error: {str(e)}"
        