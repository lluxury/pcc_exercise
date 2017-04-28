def salesgirl(method):
    def serve(*args):
        print "Salesgirl: Hello, what do you want?", method.__name__
        method(*args)
    return serve

@salesgirl
def try_this_shirt(size):
    if size <35:
        print "I: %d inches is to small to me" %(size)
    else:
        print "I: %d inches is just enough" %(size)

try_this_shirt(38)


#三个函数, serve(*args)的父是salesgirl
#执行装饰器,执行调用  ,method.__name__
