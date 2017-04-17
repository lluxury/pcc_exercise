from user import user
from user import privileges
from user import Admin

my_user1=user('wangzi', 'x','6','y')
my_user1.describe_user()
my_user1.greet_user()

my_user1.increment_login_attempts()
my_user1.increment_login_attempts()
my_user1.read_login_attemps()
my_user1.reset_login_attempts()
my_user1.read_login_attemps()

my_user2=Admin('admin','x','u','xx')
my_user2.privileges.show_privileges()