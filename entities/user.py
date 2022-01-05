class User():
    def __init__(self,username,role):
        self.username = username
        self.role = role

    def get_username(self):
        return self.username


    def set_username(self,value):
        self.__username=value

    def get_roles(self):
        return self.role

    def set_roles(self,roles):
        self.roles=roles