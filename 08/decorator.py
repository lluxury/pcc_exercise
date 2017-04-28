def deco(func):
    def _deco():
        print("before yann_func() called. ")
    
        func()
    
        print(" after yann_func() called.")
        #return func
    return _deco

@deco
def yann_func():
    print("yann_func() called.")
    return 'ok'

yann_func()
yann_func()

#先读出3个函数,调用,执行内层函数,
'''
使用内嵌包装函数来确保每次新函数都被调用
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
'''
#理解,不用内嵌的时候,只有第一次路过时候,装饰,使用后,每次调用都装饰

# before yann_func() called. 
# yann_func() called.
#  after yann_func() called.
# before yann_func() called. 
# yann_func() called.
#  after yann_func() called.