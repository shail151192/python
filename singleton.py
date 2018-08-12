#metaclass-- control creation of object
class Mymeta(type):
    def __new__(cls, classname, bases, attrs):
        if not attrs.get('gender'):
            attrs['gender'] = 'male'

        # if attrs['gender'] == 'female':
        #     raise Exception('You can not create object for female')
        #     return

        return super(Mymeta, cls).__new__(cls, classname, bases, attrs)


class Person(object):

    instance=None
    instance_count = 0
    __metaclass__ = Mymeta

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Person, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.name = 'shailendra'
        self.age = 22

    def __getname(self):
        return 'shailendra'

    # def __setattr__(self, key, value):
    #     print key, value
    #     print "error.. immutable class"
    #
    # def __getattr__(self, item):
    #     print "error"

    def __getattr__(self, item):
        pass

    def __getitem__(self, x):
        print "jjii"


n = Person()
n1 = Person()
print n1.name


class Mylist(list):

    def __init__(self, l):
        self._list = [None]*l

    def __setitem__(self, key, value):
        self._list[key] = value

    def __getitem__(self, item):
        return self._list[item]

    def __repr__(self):
        return str(self._list)

    # def __len__(self):
    #     return len(self._list)

    def __deleteitem__(self, key):
        print "delete method called"


    __delitem__= __len__=NotImplementedError

l = Mylist(4)
print type(list)
print type(Mylist)
l[0]=1
l[1] = 2
l[3] = 3
print len(l)



