class Document():
    def __init__(self, connector=None):
        self.connector = connector

    @staticmethod
    def generate_document_from_response(data, connector=None):
        return Document(**data, connector=connector)

class DocumentList():
    def __init__(self):
        self.__id = 0
        self.__documents = []

    def __iter(self):
        self.__id = 0
        return self

    def __next__(self):
        if self.__id < len(self.__documents):
            document = self.__documents[self.__id]
            self.__id += 1
            return document
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.__documents[key]

    def add(self, document):
        self.__documents.append(document)

    def remove_at(self, index):
        self.__documents.pop(index)

    def size(self):
        return len(self.__documents)
