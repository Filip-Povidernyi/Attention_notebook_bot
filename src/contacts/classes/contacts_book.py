from collections import UserDict


class ContactsBook(UserDict):

    def add_contact(self, contact):
        self.data[contact.name.value] = contact

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):

        if name in self.data:
            del self.data[name]
