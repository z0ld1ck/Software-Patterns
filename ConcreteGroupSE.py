import SEInterface
import DB


class ConcreteGroup(SEInterface.Group):

    def attach(self, observer):
        print(f'\n{observer.name} added to SE-2118')
        self._observers.append(observer)

    def detach(self, observer):
        print(f'f\n{observer.name} removed from SE-2118\n')
        self._observers.remove(observer)

    def notify(self):
        print('\n\nSE-2118 assemble,we need defence patterns!!\n\n')
        for observer in self.Observer_list:
            observer.update()
