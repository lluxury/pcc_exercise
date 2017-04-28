def deco(func):
    def _deco(a, b):
        print("before yann_func() called. ")
    
        ret = func(a, b)
    
        print(" after yann_func() called. result: %s" %ret)
        return ret
    return _deco

@deco
def yann_func(a, b):
    #print("yann_func() called." %(a, b))
    print("yann_func(%s, %s) called." %(a, b))
    return a + b

yann_func(1, 2)
print("\n")
yann_func(3, 4)

#还是粗心啊, 代码还是对比比较快
#参数是在内层么?
