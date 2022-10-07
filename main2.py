from abc import ABC, abstractmethod


class AvengersTeam(ABC):
    """
    Interface AvengersTeam represents publisher
    """

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteAvengersTeam(AvengersTeam):
    """
    ConcreteAvengersTeam implements interface AvengersTeam
    """

    _observers_list = list()

    def attach(self, observer):
        print(f'\n{observer.name} added to Avengers team!')
        self._observers_list.append(observer)

    def detach(self, observer):
        print(f'\n{observer.name} removed from Avengers team!\n')
        self._observers_list.remove(observer)

    def notify(self):
        print('\n\nAvengers assemble!!!\n\n')
        for observer in self._observers_list:
            observer.update()


class Observer(ABC):
    """
    Interface Observer represnts subscribers
    """

    @abstractmethod
    def update(self, subject):
        pass


class IronMan(Observer):
    name = "Iron Man"

    def update(self):
        print('Iron Man report now\n')


class CaptainAmerica(Observer):
    name = "Captain America\n"

    def update(self):
        print('Captain America report now\n')


class Thor(Observer):
    name = "Thor"

    def update(self):
        print('Thor report now\n')


class BlackWidow(Observer):
    name = "Black Widow"

    def update(self):
        print('Black Widow report now\n')


class Hulk(Observer):
    name = "Hulk"

    def update(self):
        print('Hulk report now\n')


class SpiderMan(Observer):
    name = "Spider Man"

    def update(self):
        print('Spider Man report now\n')


class MakeAdmin(AvengersTeam):
    # Decorator
    _observers_list = list()

    def attach(self, observer):
        print(f'\n{observer.name} added to Avengers team and become an Admin!')
        self._observers_list.append(observer)

    def detach(self, observer):
        print(f'\n{observer.name} removed from Avengers team!\n')
        self._observers_list.remove(observer)

    def notify(self):
        # print('\n\nAvengers assemble!!!\n\n')
        for observer in self._observers_list:
            observer.update()


class AdminAbilities(ABC):
    def DeleteUser(self):
        pass

    def AddUser(self):
        pass

    def SendPic(self):
        pass


class Pravo(AdminAbilities):
    ObserverList = list()

    def DeleteUser(self, observer):
        print(f'\n{Observer.name} were removed by Admin\n')
        self._ObserverList.remove(observer)

    def AddUser(self,observer):
        print(f'\n{Observer.name} were added by Admin\n')
        self._ObserverList.append(observer)

    def SendPic(self,observer):
        print(f'\n{Observer.name} ### ### ### ### ### ###\n ### ### ### ### ### ###\n ### ### ### ### ### ###\n')
        self._ObserverList.append(observer)


class contactContainer(ABC):
    @abstractmethod
    def showContacts(self, names):
        pass


class Contacts(contactContainer):

    def showContacts(self, names):
        print(names)


if __name__ == "__main__":

    publisher = ConcreteAvengersTeam()
    addAgain = MakeAdmin()
    contacts = Contacts()
    start = input('to Add the Avengers to that chat for Assemble press "Enter"...')
    getContact = input('to get your contacts of Heroes enter "Contacts": ')


    def logic(getContact):
        name = ["1. IronMan", "2. Cap", "3. Thor", "4. Black_widow", "5. Hulk", "6. Spider_man"]
        if getContact == "Contacts":
            for i in range(0, 6):
                contacts.showContacts(name[i])
            number_of = int(input('Now input number of participants who will be in that chat: '))
            data = []
            for i in range(0, number_of):
                name = input('Write the name of the Hero: ')
                data.append(name)
            adminName = input('Do you wanna give Admin rights to someone?(input yes or no): ')
            if adminName == 'yes':
                def addAdminFunction(data):
                    # numberOfAdmins = int(input('input number of Admins you want to add'))
                    askForAdminName = input('Type a name of Hero who you want to make admin: ')
                    # for i in range(0, numberOfAdmins):
                    for i in range(len(data)):
                        if data[i] == askForAdminName:
                            data[i] = askForAdminName + ' is admin'
                    print(data)

                addAdminFunction(data)

                def printAvengersRes(data):
                    for i in data:
                        if i == "IronMan is admin":
                            iron_man = IronMan()
                            addAgain.attach(iron_man)
                        elif i == "IronMan":
                            iron_man = IronMan()
                            publisher.attach(iron_man)

                        if i == "Cap is admin":
                            captain_america = CaptainAmerica()
                            addAgain.attach(captain_america)
                        elif i == "Cap":
                            captain_america = CaptainAmerica()
                            publisher.attach(captain_america)

                        if i == 'Thor is admin':
                            thor = Thor()
                            addAgain.attach(thor)
                        elif i == 'Thor':
                            thor = Thor()
                            publisher.attach(thor)

                        if i == 'Black_widow is admin':
                            black_widow = BlackWidow()
                            addAgain.attach(black_widow)
                        elif i == 'Black_widow':
                            black_widow = BlackWidow()
                            publisher.attach(black_widow)

                        if i == 'Hulk is admin':
                            hulk = Hulk()
                            addAgain.attach(hulk)
                        elif i == 'Hulk':
                            hulk = Hulk()
                            publisher.attach(hulk)
                        if i == 'Spider_man is admin':
                            # spider_man = SpiderMan()
                            # publisher.attach(spider_man)
                            # publisher.detach(spider_man)
                            print('\nSpider Man is too young to be an Admin!\n')
                            reset = input('Do you want to add an Admin again?(yes or no): ')
                            if reset == 'yes':
                                for j in range(len(data)):
                                    if data[j] == 'Spider_man is admin':
                                        data[j] = 'Spider_man'
                                        return (addAdminFunction(data),
                                                printAvengersRes(data))
                            else:
                                spider_man = SpiderMan()
                                publisher.attach(spider_man)
                                print('\nSpider Man: Why the Admin is not me?! \n')
                        elif i == 'Spider_man':
                            spider_man = SpiderMan()
                            publisher.attach(spider_man)
                            print('\nSpider Man: Why the Admin is not me?! \n')

                    publisher.notify()

                printAvengersRes(data)

            elif adminName == 'no':
                def printAvengersRes(data):
                    for i in data:
                        if i == "IronMan":
                            iron_man = IronMan()
                            publisher.attach(iron_man)
                        if i == "Cap":
                            captain_america = CaptainAmerica()
                            publisher.attach(captain_america)
                        if i == 'Thor':
                            thor = Thor()
                            publisher.attach(thor)
                        if i == 'Black_widow':
                            black_widow = BlackWidow()
                            publisher.attach(black_widow)
                        if i == 'Hulk':
                            hulk = Hulk()
                            publisher.attach(hulk)
                        if i == 'Spider_man':
                            spider_man = SpiderMan()
                            publisher.attach(spider_man)
                            publisher.detach(spider_man)
                            print('\nSpider Man: Why do you guys always do this to me!\n')
                    publisher.notify()

                printAvengersRes(data)

        else:
            return print("Please try again")


    logic(getContact)
