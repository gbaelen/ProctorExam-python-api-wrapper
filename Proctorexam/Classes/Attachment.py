class Attachment():
    def __init__(self, connector=None):
        self.connector = connector

    @staticmethod
    def generate_attachment_from_response(data, connector=None):
        return Document(**data, connector=connector)

class AttachmentList():
    def __init__(self):
        self.__id = 0
        self.__attachments = []

    def __iter__(self):
        self.__id = 0
        return self

    def __next__(self):
        if self.__id < len(self.__attachments):
            attachment = self.__attachments[self.__id]
            self.__id += 1
            return attachment
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.__attachments[key]

    def add(self, attachment):
        self.__attachments.append(attachment)

    def remove_at(self, index):
        self.__attachments.pop(index)

    def size(self):
        return len(self.__attachments)
