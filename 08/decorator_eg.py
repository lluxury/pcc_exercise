def salesgirl(method):
    def serve(*args):
        print "Salesgirl: Hello, what do you want?", method.__name__
        result = method(*args)
        if result:
            print "salesgirl: This shirt is 50$."
        else:
            print "Salesgirl: Well, how about trying another style?"
        return result
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

#需求改变,函数不改变,结果加判断,输出附加信息