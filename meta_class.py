
# class create_class:
#     def __new__(cls, classname, bases, attrs):
#
#
# class Person(object):
#     __metaclass__ = 'create_class'
#
#     def __init__(self):
#         pass
#

class Person:
    def __new__(cls, *args, **kwargs):
        print "creating new object"
        return super(Person, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print "initilized.........."

print Person.__bases__
print Person
print type(Person)
p=Person()


