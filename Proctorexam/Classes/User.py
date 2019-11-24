class User():
    def __init__(self, id=None, email=None, name=None, role=None, logo_image=None, institute_name=None, connector=None):
        self.id=id
        self.email=email
        self.name=name
        self.role=role
        self.logo_image=logo_image
        self.institute_name=institute_name
        self.connector = connector

    @staticmethod
    def generate_user_from_response(data, connector=None):
        return User(**data, connector=connector)

class UserList():
    def __init__(self):
        self.__id = 0
        self.__users = []

    def __iter(self):
        self.__id = 0
        return self

    def __next__(self):
        if self.__id < len(self.__users):
            user = self.__users[self.__id]
            self.__id += 1
            return user
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.__users[key]

    def add(self, user):
        self.__users.append(user)

    def remove_at(self, index):
        self.__users.pop(index)

    def size(self):
        return len(self.__users)
