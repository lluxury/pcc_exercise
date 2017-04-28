def deco(func):
    print("before yann_func() called. ")

    func()

    print(" after yann_func() called.")
    return func

def yann_func():
    print("yann_func() called.")

yann_func = deco(yann_func)

yann_func()
yann_func()

#装饰函数的参数是被装饰的函数对象，返回原函数对象
#先执行装饰器,前,到func参数时,调用yann_func,后,完成,最后手动调用2次函数

# before yann_func() called. 
# yann_func() called.
#  after yann_func() called.
# yann_func() called.
# yann_func() called.