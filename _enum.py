import enum

class Day(enum.Enum):
    sunday=0
    monday=1


for i in Day:
    print i.name
    print i.value