from mylocker import *
 
class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(" myfunc() called.")
 
    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b
 
if __name__=="__main__":
    a = example()
    a.myfunc()
    print(a.myfunc())
    print(a.myfunc2(1, 2))
    print(a.myfunc2(3, 4))

#写法不规范,仅做参考

# before myfunc called.
# mylocker.acquire() called.
#  myfunc() called.
#   mylocker.unlock() called.
# before myfunc called.
# mylocker.acquire() called.
#  myfunc() called.
#   mylocker.unlock() called.
# None

# before __deco called.
# mylocker.acquire() called.
# before myfunc2 called.
# lockerex.acquire() called.
#  myfunc2() called.
#   lockerex.unlock() called.
#   mylocker.unlock() called.
# 3

# before __deco called.
# mylocker.acquire() called.
# before myfunc2 called.
# lockerex.acquire() called.
#  myfunc2() called.
#   lockerex.unlock() called.
#   mylocker.unlock() called.
# 7


#后期 再回顾,不是目前可以掌握的内容 http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html