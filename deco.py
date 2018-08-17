def calculateTime(fun):
    def oracle:dba
wrapper(*args, **kwargs):
        print "starting function call......."
        fun(*args, **kwargs)
        print "end function call.........."

    return wrapper


@calculateTime
def printNumber(a):
    print 'Hi', 
    print "hello world"
<<<<<<< HEAD
    print "this is master"
    print "no "    
=======
    print "this is dev branch"
    print "no "
    print "cherry pic changes"
>>>>>>> ff98883... cherry pic changes
printNumber(100)
