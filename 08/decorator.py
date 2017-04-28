def deco(func):
    def _deco(*args, **kwargs):
        '''参数用(*args, **kwargs)，自动适应变参和命名参数'''
        print("before %s called. " % func.__name__)
    
        ret = func(*args, **kwargs)
    
        #print(" after yann_func() called. result: %s" % (func.__name__, ret))
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco
def yann_func(a, b):
    #print("yann_func() called." %(a, b))
    print("yann_func(%s, %s) called." % (a, b))
    return a + b

@deco
def yann_func2(a, b, c):
    print("myfunc2(%s,%s,%s) called." % (a, b, c))
    return a + b + c

yann_func(1, 2)
print("\n")
yann_func(3, 4)

yann_func2(1, 3, 4)
print("\n")
yann_func2(3, 4, 5)


#还是粗心啊, 代码还是对比比较快
#参数是在内层么?
#再一次粗心,一个位置与2个参数
#http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html