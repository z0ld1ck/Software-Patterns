from Admin import AdminAbilities
import DB


class Send(AdminAbilities):

    def DeleteUser(self, observer):
        print(f'\n{observer.name} were removed by Admin\n')
        self._ObserverList.remove(observer)

    def AddUser(self, observer):
        print(f'\n{observer.name} was added by Admin\n')
        self._ObserverList.append(observer)

    def SendPic(self, observer):
        print(f'\n{observer.name} ### ### ### ### ### ###\n ### ### ### ### ### ###\n ### ### ### ### ### ###\n')
        self._observers_list.append(observer)
