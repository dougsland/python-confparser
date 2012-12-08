from confparser import *

LIBVIRT_CONFIG_FILE = "./libvirtd.conf"

mydict = {}
mydict = confToDict(LIBVIRT_CONFIG_FILE)

print "reading tls_port"
print "tls_port value: %s" % mydict['tls_port']
print "tls_port type: %s" % mydict['tls_port_type']
print "tls_port status: %s" % mydict['tls_port_status']

print "\nchanging tls_port value to my-new-value"
mydict['tls_port'] = "my-new-value"
mydict['tls_port_status'] = "activated"
ret = writeDictToFile(LIBVIRT_CONFIG_FILE, mydict)
if ret != 0:
    print "cannot save file!"

print "\ncurrent value tls_port"
print "tls_port value: %s" % mydict['tls_port']
print "tls_port type: %s" % mydict['tls_port_type']
print "tls_port status: %s" % mydict['tls_port_status']
