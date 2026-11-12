

class WriterDocument:

    def __init__(self, filename:str):
        self.filename = filename

    def create(self, text:str):
        with open(self.filename, 'w') as fl:
            fl.write(text)

    @classmethod
    def new_from_markdown(cls, filename:str, markdown_text:str=''):
        instance = cls(filename)
        instance.create(markdown_text)
        return instance