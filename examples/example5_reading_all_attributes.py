from confparser import *

mydict = {}
mydict = confToDict("./libvirtd.conf")

# loop into the dict variable to read all members
for item in sorted(set(mydict)):
    print "{0}, {1}".format(item, mydict[item])
