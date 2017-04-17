class user():
    """docstring for user"""
    def __init__(self, first_name, last_name, age, gender):
        #super(user, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts=0

    def describe_user(self):
        ''' '''
        print(" The name of user is " + self.first_name.title() + ' ' + self.last_name.title())
        print(" user age is " + self.age.title())

    def greet_user(self):
        ''''''
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + "!")
        pass
    def read_login_attemps(self):
        '''read '''
        print(self.login_attempts)
        
    def increment_login_attempts(self):
        ''' '''
        self.login_attempts+=1
        pass

    def reset_login_attempts(self):
        '''类的方法是不能缺少self的'''
        self.login_attempts=0
        pass

my_user=user('weilian', 'x','6','y')
print ("my user's first_name is " + my_user.first_name.title())
print ("my user's last_name is " + my_user.last_name.title())
my_user.describe_user()
my_user.greet_user()

my_user1=user('wangzi', 'x','6','y')
my_user1.describe_user()
my_user1.greet_user()

my_user1.increment_login_attempts()
my_user1.increment_login_attempts()
my_user1.read_login_attemps()
my_user1.reset_login_attempts()
my_user1.read_login_attemps()
