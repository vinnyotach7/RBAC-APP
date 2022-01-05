class Roles:
    def __init__(self,type,role):
        self.__validRole = ['User','Admin','Viewer']

    @username.setter
    def username(self,type):
        if type not in self.__validRole:
            raise Exception('User type not allowed')
        #self.role=