class TextExtractor:
    def __init__(self, start_delimiter, end_delimiter=None, prefix=None):
        self.start_delimiter = start_delimiter
        self.end_delimiter = end_delimiter
        self.prefix = prefix

    def extract_text(self, input_text):
        start_index = input_text.find(self.start_delimiter)
        if start_index == -1:
            return "Start delimiter not found" 
        start_index += len(self.start_delimiter)
        
        if self.end_delimiter is None:
            return input_text[start_index:]
        else:
            end_index = input_text.find(self.end_delimiter, start_index)
            if end_index == -1:
                return "End delimiter not found"
            return input_text[start_index:end_index]
        
    def extract_text_from_text(self, text):
        """
        Gets and returns the text following the prefix on a given lines.
        If the prefix is ​​not found, returns None.
        """
        lines = text.splitlines()
        for line in lines:
            extracted_text = self.extract_text_from_line(line)
            if extracted_text is not None:
                return extracted_text
        return None
    
    def extract_text_from_line(self, line):
        """
        Gets and returns the text following the prefix on a given line of text.
        If the prefix is ​​not found, returns None.
        """
        if self.prefix in line:
            start_index = line.find(self.prefix) + len(self.prefix)
            return line[start_index:].strip()
        return None
