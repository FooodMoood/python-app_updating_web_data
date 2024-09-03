from prepare_data.file_text_manager import *
from prepare_data.replace_strings_in_text_file import *

class CreateMultilinesList:
    def __init__(self, input_text, input_file_path, output_file_path, text_to_replace):
        self.input_text = input_text
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.text_to_replace = text_to_replace

    def convert_to_list(self):
        lines = self.input_text.split('\n')
        result = ""
        FileTextManager(self.output_file_path).clear_data()
        
        for line in lines:
            if line.strip():
                text = line.split('.', 1)[1].strip() if '.' in line else line.strip()

                copied_data = FileTextManager(self.input_file_path).read_data()
                FileTextManager(self.output_file_path, copied_data).append_to_file()
                ReplaceStringsInTextFile(self.output_file_path, self.text_to_replace, text).replace_text()
