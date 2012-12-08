from confparser import *

mydict = {}

mydict = confToDict("./libvirtd.conf")

print "reading tls_port"
print "tls_port value: %s" % mydict['tls_port']
print "tls_port type: %s" % mydict['tls_port_type']
print "tls_port status: %s" % mydict['tls_port_status']

print "\nreading keepalive"
print "keepalive_count value: %s" % mydict['keepalive_count']
print "keepalive_count type: %s" % mydict['keepalive_count_type']
print "keepalive_count status: %s" % mydict['keepalive_count_status']
