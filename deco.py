def calculateTime(fun):
    def oracle:dba
wrapper(*args, **kwargs):
        print "starting function call......."
        fun(*args, **kwargs)
        print "end function call.........."

    return wrapper


@calculateTime
def printNumber(a):
    print 'Hi', a
    print "hello world"
    print "no "    
printNumber(100)
