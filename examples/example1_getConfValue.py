from confparser import *

LIBVIRT_CONFIG_FILE = "./libvirtd.conf"

value = getConfValue(LIBVIRT_CONFIG_FILE, "unix_sock_group")

if value == "confCommented":
    print "unix_sock_group is commented"

value = getConfValue(LIBVIRT_CONFIG_FILE, "host_uuid")
print "host_uuid value is %s" % value
