from abc import ABC, abstractmethod


class Contacts(ABC):
    @abstractmethod
    def show(self, names):
        pass


class Contacts(Contacts):
    def show(self, names):
        print(names)
