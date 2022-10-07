import ObserverInterface


class Sultan(ObserverInterface):
    name = 'Sultan'

    def update(self):
        print('Sultan report now\n')

