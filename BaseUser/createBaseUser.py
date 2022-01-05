from entities.user import User
class createBaseUser:
    """def createBaseUser(self):
        user = {}
        user['User1']='Admin'
        return user"""
    superAdminActions = ['read','write','delete']
    adminActions = ['read','write']
    devActions = ['read']
    userData = dict()
    #suserData = dict()

    @staticmethod
    def create():
        roleAdmin = []
        roleAdmin.append('admin')
        user1 = User("user1",roleAdmin)

        roleDev = []
        roleDev.append('user')
        user2 = User("user2",roleDev)
        
        createBaseUser.userData[user1.get_username()]=user1.get_roles()
        createBaseUser.userData[user2.get_username()]=user2.get_roles()
        print(createBaseUser.userData)


    def addUser(self,user):
        if user.get_username() in createBaseUser.userData.keys():
            print("user already exists")
        else:
            createBaseUser.userData[user.get_username()]=user.get_roles()


