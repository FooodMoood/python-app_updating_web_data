class FileTextManager:
    def __init__(self, file_path, data=None, string_to_remove=None):
        self.file_path = file_path
        self.data = data
        self.string_to_remove = string_to_remove

    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()
        
    def write_data(self):
        if self.data is None:
            raise ValueError("No data provided for writing.")
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(self.data)
    
    def clear_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.truncate()

    def append_to_file(self):
        with open(self.file_path, 'a') as file:
            file.write(self.data)

    def remove_section(self, section_text):
        """Removes the specified section of text from the data attribute."""
        self.data = self.data.replace(section_text, '')
        return self.data