from ConcreteGroupSE import ConcreteGroup
from DB.DB import name
from Decorator import Adminka
from ShowContacts import Contacts

if __name__ == "__main__":
    publisher = ConcreteGroup()
    AddAgain = Adminka.MakeAdmin()
    contacts = Contacts.Contacts()
    start = input('to Add the Avengers to that chat for Assemble press "Enter"...')
    getContact = input('to get your contacts of Heroes enter "Contacts": ')


    def logic(getContact):
        if getContact == "Contacts":
            for i in range(0, 6):
                contacts.showContacts(name[i])
            number_of = int(input('Now input number of participants who will be in that chat: '))
            members = []
            for i in range(0, number_of):
                imya = input('Write the name of the Hero: ')
                members.append(imya)
            adminName = input('Do you wanna give Admin rights to someone?(input yes or no): ')
            if adminName == "yes":
                def addAdminFunction(members):
                    askForAdminName = input('Type a name of Hero who you want to make admin: ')
                    for i in range(len(members)):
                        if members[i] == askForAdminName:
                            members[i] = askForAdminName + ' is admin'
                    print(members)

                addAdminFunction(members)
