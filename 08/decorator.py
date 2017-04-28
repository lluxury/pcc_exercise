def deco(func):
    print("before yann_func() called. ")

    func()

    print(" after yann_func() called.")
    return func

@deco
def yann_func():
    print("yann_func() called.")

#yann_func = deco(yann_func)

yann_func()
yann_func()

#语法糖
#语法糖在前面,赋值在后面

# before yann_func() called. 
# yann_func() called.
#  after yann_func() called.
# yann_func() called.
# yann_func() called.