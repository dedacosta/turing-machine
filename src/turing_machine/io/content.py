
class Content:
    def __int__(self, filename: str):
        self.__filename = filename

    def read(self):
        contents = []
        with open(self.__filename) as f:
            contents = f.readlines()
        return "".join(map(lambda a: a.rstrip(), contents))



