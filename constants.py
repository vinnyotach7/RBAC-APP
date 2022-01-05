from PyInquirer import prompt, Separator

questions = [
    {
        'type': "input",
        "name": "userName",
        "message": "Enter a UserName",
    },

    {
        'type': 'checkbox',
        'message': 'Select roles',
        'name': 'roles',
        'choices': [ 
            Separator('= ROLES ='),
            {
                'name': 'admin'
            },
            {
                'name': 'user'
            }
            
        ],
        'validate': lambda answer: 'You must choose at least one role.' \
            if len(answer) == 0 else True
    }


]

viewQuestions = [
    {
        'type': "input",
        "name": "userName",
        "message": "Enter a UserName to view attached roles",
    }
]

deleteQuestions = [
    {
        'type': "input",
        "name": "userName",
        "message": "Enter a UserName to be removed",
    },
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
    }
]

loginQuestions = [
    {
        'type': "input",
        "name": "userName",
        "message": "Enter a UserName ",
    },
    {
        'type': "input",
        "name": "role",
        "message": "Enter a role to be used",
    },
]


introAdmin = """Enter view to view roles
Enter add to add a User
Enter delete to delete a user
Enter login to login as another user"""

introDeveloper = """Enter view to view roles
Enter login to login as another user"""