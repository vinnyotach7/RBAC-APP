from cmd import Cmd
from BaseUser.createBaseUser import createBaseUser
from entities.user import User 
from PyInquirer import prompt
from examples import custom_style_2
from prompt_toolkit.validation import Validator, ValidationError
from constants import questions,viewQuestions,deleteQuestions,loginQuestions,introAdmin,introDeveloper

class MyPrompt(Cmd):
    __currentUser = []
    __currentRole = []
    prompt = '>>> '
    intro = """Press 1 to login as admin
         Press 2 to login as developer"""
 
    def do_exit(self, inp):
        print("Bye")
        return True



    def begin(self):
        #user = self.__currentUser[0]
        userRole = self.__currentRole[0]
        print(userRole)
        if userRole != 'admin':
            print(introDeveloper)
        else:
            print(introAdmin)



    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')



    #add a user
    def do_add(self, inp):
        userRole = self.__currentRole[0]
        print("current role is",userRole)
        if userRole != 'admin':
            print("action not allowed")
        else:
            answers = prompt(questions, style=custom_style_2)
            createUser = createBaseUser()
            user = User(answers.get("userName"),answers.get("roles"))
            createUser.addUser(user)
            print("user {} added".format(answers.get("userName")))
        return self.begin()



    #view a user
    def do_view(self, inp):
        answers = prompt(viewQuestions, style=custom_style_2)
        try:
            userRole = createBaseUser.userData[answers.get('userName')]
        except KeyError:
            print("Invalid username")
            return self.begin()
        print("user roles are '{}'".format(userRole))



    #delete a user
    def do_delete(self, inp):
        #userRole = createBaseUser.userData[self.__currentUser[0]]
        createUser = createBaseUser()
        if self.__currentRole[0]!='admin':
            print("action not allowed")
            return self.begin()
        answers = prompt(deleteQuestions, style=custom_style_2)
        if(answers.get('continue') is True):
            resp = self.check_user_delete(answers.get('userName'))
            if(resp == False):
                print("cannot delete user")
            
            else:
                print("existing users are '{}'".format(createUser.userData))
                del createBaseUser.userData[answers.get('userName')]
                print("Users after deletion '{}'".format(createUser.userData))

        return self.begin()    

            
        

    def do_login(self,inp):
        answers = prompt(loginQuestions, style=custom_style_2)
        checkUser = self.check_user_exists(answers.get('userName'),answers.get('role'))
        if(checkUser == True):
            print("You are now logged in as {} with role {}".format(answers.get('userName'),answers.get('role')))
            self.__currentUser.clear()
            self.__currentRole.clear()
            self.__currentUser.append(answers.get('username'))
            self.__currentRole.append(answers.get('role'))
        return self.begin()

 
    def help_add(self):
        
        print("Add a new entry to the system.")
    
    def check_user_delete(self,username):
        #user = createBaseUser.userData[username]
        if username in ["user1","user2"]:
            return False
        return True



    def check_user_exists(self,username,role):
        try:
            userRole = createBaseUser.userData[username]
        except KeyError:
            print("Invalid username")
            return self.begin()
        if role not in userRole:
            print("User with role {} does not exist".format(role))
            return self.begin()
        return True




    def default(self, inp):
        if inp == '1':
            self.__currentUser.append("user1")
            self.__currentRole.append('admin')
            print(introAdmin)
        elif inp == '2':
            self.__currentUser.append("user2")
            self.__currentRole.append('user')
            print(self.__currentUser)
            print(introDeveloper)
            
        elif inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        else:
            print("sorry,I did not get that")
            return self.begin()
 
        #print("Default: {}".format(inp))
 
    do_EOF = do_exit
    help_EOF = help_exit

    


 
if __name__ == '__main__':
    createBaseUser.create()
    MyPrompt().cmdloop()