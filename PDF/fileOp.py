class FileOp:
    @staticmethod
    def savefile(filename, note):
        f = open(filename, mode='a', encoding='utf-8')
        f.write(note)

    def __init__(self, filename, note):
        self.Filename = filename

