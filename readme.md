I have made 2 apps inside my BlogApplication i.e. userStuff - To handle the login, logout and registeration functionalities related to a user
and blog - just for maintaining the contents and attachments of a post. This is done just to keep the project clean.

I have made a common templates and static file folders for both the apps so that the code can be reused and avoid redundant code.

TEMPLATES
'DIRS': [os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')],

STATICFILES
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
]

Since the navbar is common for all the pages, I have kept navbar in base.html

Added custom validation for captha in forms.py of UserCreateForm(UserCreationForm)

Made use of authentication() and login() methods for user login

The user is restricted from directly entering /profile or /home on url 
by using @login_required decorator
Thus accordingly configured settings.py file as: 
LOGIN_URL = 'index'
i.e. the user will be automatically navigated to landing page for logging in


made use of {{ value | truncatechars:25 }} to restrict the no. of characters on homepage description


on clicking on the post, the detail post would open up taking url parameters