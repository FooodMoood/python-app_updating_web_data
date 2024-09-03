from prepare_data.file_text_manager import *

class ReplaceStringsInTextFile:
    def __init__(self, input_file_path, strings_to_replace, text_to_paste):
        self.input_file_path = input_file_path
        self.strings_to_replace = strings_to_replace
        self.text_to_paste = text_to_paste

    def replace_text(self):
        try:
            data = FileTextManager(self.input_file_path).read_data()

            if self.strings_to_replace in data:
                data = data.replace(self.strings_to_replace, self.text_to_paste, 1)
            
            FileTextManager(self.input_file_path, data).write_data()

        except FileNotFoundError:
            print(f"File '{self.input_file_path}' not found.")
        except Exception as e:
            print(f"An error occured: {e}")
