from confparser import *

LIBVIRT_CONFIG_FILE = "./libvirtd.conf"

print "current auth_unix_rw value: %s" \
    % getConfValue(LIBVIRT_CONFIG_FILE, "auth_unix_rw")
print "current mdns_adv value: %s" \
    % getConfValue(LIBVIRT_CONFIG_FILE, "mdns_adv")

ret = setConfValue(LIBVIRT_CONFIG_FILE, "auth_unix_rw", "my-super-new-value", CONFSTRING)
if ret == 0:
        print "\nsuccess auth_unix_rw now contain my-super-new-value"

ret = setConfValue(LIBVIRT_CONFIG_FILE, "mdns_adv", "88888", CONFNUMBER)
if ret == 0:
        print "success mdns_adv contain now 8888"
