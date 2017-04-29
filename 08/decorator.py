class locker:
    def __init__(self):
        print("locker.__init__() should not be called")

    @staticmethod
    def acquire():
        print("locker.acquire() called. (staticmethod)")

    @staticmethod
    def release():
        print("  locker.release() called. (no object )")
    
def deco(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def yann_func():
    print(" yann_func() called.")

yann_func()
yann_func()


#让装饰器带类参数? 可以直接使用??

# before yann_func called [<class '__main__.locker'>].
# locker.acquire() called. (staticmethod)
#  yann_func() called.
#   locker.release() called. (no object )

# before yann_func called [<class '__main__.locker'>].
# locker.acquire() called. (staticmethod)
#  yann_func() called.
#   locker.release() called. (no object )
