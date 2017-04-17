class user():
    """docstring for user"""
    def __init__(self, first_name, last_name, age, gender):
        #super(user, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        '''模拟小狗被命令时蹲下'''
        print(" The name of user is " + self.first_name.title() + ' ' + self.last_name.title())
        print(" user age is " + self.age.title())

    def greet_user(self):
        '''模拟小狗被命令打滚'''
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + "!")
        pass
        

my_user=user('weilian', 'x','6','y')
print ("my user's first_name is " + my_user.first_name.title())
print ("my user's last_name is " + my_user.last_name.title())
my_user.describe_user()
my_user.greet_user()

my_user1=user('wangzi', 'x','6','y')
my_user1.describe_user()
my_user1.greet_user()