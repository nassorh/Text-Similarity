class File():
    def __init__(self,fileName,file_directory):
        self.file_directory = file_directory
        self.name = fileName

    def get_name(self):
        return self.name

    def get_text(self):
        text = ""
        with open(self.file_directory) as file:
            text += file.read()
        return text

