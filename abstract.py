from abc import abstractmethod, ABCMeta
class Area(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print "initializing abstract method"

    @abstractmethod
    def getname(self):
        pass


class Rectangle(Area):

    def getname(self):
        pass


r=Rectangle()