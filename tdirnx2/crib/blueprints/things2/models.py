from .thing import Thing

ts = [Thing(x,name="thing" + str(x)) for x in range(100)]

THINGS = ts