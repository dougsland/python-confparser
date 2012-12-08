from confparser import *

mydict = {}
mydict = confToDict("./libvirtd.conf")

print getNumberOfElementsInDict(mydict)
