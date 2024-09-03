class TextManager():
    def __init__(self, text):
        self.text = text

    def remove_section(self, section_text):
        """Removes the specified section of text from the text attribute."""
        self.text = self.text.replace(section_text, '')
        return self.text