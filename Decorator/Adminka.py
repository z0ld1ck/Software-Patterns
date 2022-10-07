import SEInterface
import DB


class MakeAdmin(SEInterface):

    def attach(self, observer):
        print(f'\n{observer.name} become an Admin')
        self._observers.append(observer)

    def detach(self, observer):
        print(f'\n{observer.name} removed from SE-2118\n')
        self._observers.remove(observer)

    def notify(self):
        for observer in self._ObserverList:
            observer.update()
