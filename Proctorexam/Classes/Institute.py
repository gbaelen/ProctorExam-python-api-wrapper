class Institute():
    def __init__(self, connector=None):
        self.connector = connector

    @staticmethod
    def generate_institute_from_response(data, connector=None):
        return Institute(**data, connector=connector)

class InstituteList():
    def __init__(self):
        self.__id = 0
        self.__institutes = []

    def __iter(self):
        self.__id = 0
        return self

    def __next__(self):
        if self.__id < len(self.__institutes):
            institute = self.__institutes[self.__id]
            self.__id += 1
            return institute
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.__institutes[key]

    def add(self, institute):
        self.__institutes.append(institute)

    def remove_at(self, index):
        self.__institutes.pop(index)

    def size(self):
        return len(self.__institutes)
