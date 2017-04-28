def salesgirl(method):
    def serve(*args):
        print "Salesgirl: Hello, what do you want?", method.__name__
        return method(*args)
    return serve

@salesgirl
def try_this_shirt(size):
    if size <35:
        print "I: %d inches is to small to me" %(size)
        return False
    else:
        print "I: %d inches is just enough" %(size)
        return True

result = try_this_shirt(38)
print "Mum:dou you want to buy this ", result

#希望获得结果,第4行是返回给最后1行的结果
#先执行装饰器,然后执行调用,然后调用参数传到装饰器内部,然后执行函数