# Copyright (C) 2012
#
# Douglas Schilling Landgraf <dougsland@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import unittest
from confparser import *

LIBVIRT_CONFIG_FILE = "./libvirtd.conf"

class confParseTests(unittest.TestCase):

    def test_getConf(self):
        print "\n-----------------------------"
        print "Testing getConfValue"
        print "-----------------------------"
        if getConfValue(LIBVIRT_CONFIG_FILE,
                "unix_sock_group") != "confCommented":
            assert()

        print "Testing getConfValue - confCommented [OK]"

        if getConfValue(LIBVIRT_CONFIG_FILE,
                "keepalive_count") != "5":
            assert()

        print "Testing getConfValue - confValue [OK]"

        if getConfValue(LIBVIRT_CONFIG_FILE,
                "not_existing_conf_value") != "confNotFound":
            assert()

        print "Testing getConfValue - confNotFound [OK]"

    def test_setConf(self):

        mydict = {}
        mydict = confToDict(LIBVIRT_CONFIG_FILE)

        print "\n-----------------------------"
        print "Testing setConfValue"
        print "-----------------------------"

        # Setting Value as String
        ret = setConfValue(LIBVIRT_CONFIG_FILE, "auth_unix_rw",
            "my-super-new-value", CONFSTRING)

        if ret != 0:
            assert()

        # Reading the new value
        if getConfValue(LIBVIRT_CONFIG_FILE,
                "auth_unix_rw") != "my-super-new-value":
            assert()

        # re read the conf
        mydict = confToDict(LIBVIRT_CONFIG_FILE)

        # Is it string?
        if mydict['auth_unix_rw_type'] != "string":
            assert() 

        print "Testing setConfValue - Setting string [OK]"
        ##########################################################

        # Setting Value as CONF_NOT_STRING
        ret = setConfValue(LIBVIRT_CONFIG_FILE, "auth_unix_rw",
                "8888", CONF_NOT_STRING)
        if ret != 0:
            assert()

        if getConfValue(LIBVIRT_CONFIG_FILE,
                "auth_unix_rw") != "8888":
            assert()
        
        # re read the conf
        mydict = confToDict(LIBVIRT_CONFIG_FILE)
        if mydict['auth_unix_rw_type'] != "no string":
            assert() 

        print "Testing setConfValue - Setting not string [OK]"
        ##########################################################
        # Setting Value as CONFNUMBER
        ret = setConfValue(LIBVIRT_CONFIG_FILE, "auth_unix_rw",
                "8888", CONFNUMBER)
        if ret != 0:
            assert()

        if getConfValue(LIBVIRT_CONFIG_FILE,
                "auth_unix_rw") != "8888":
            assert()
        
        # re read the conf
        mydict = confToDict(LIBVIRT_CONFIG_FILE)
        if mydict['auth_unix_rw_type'] != "no string":
            assert() 

        print "Testing setConfValue - Setting notnumber [OK]"
        ##########################################################

    def test_confToDict(self):
        mydict = {}
        mydict = confToDict(LIBVIRT_CONFIG_FILE)

        if (not mydict['tls_port']) or (not mydict['tls_port_status']) or \
                (not mydict['tls_port_type']):
            assert()

        print "-----------------------------"
        print "Testing confToDict "
        print "-----------------------------"

        print "dict - created [OK]"
        print "tls_ports %s [OK]" % mydict['tls_port']
        print "tls_port_status %s [OK]" % mydict['tls_port_status']
        print "tls_port_type %s [OK]" % mydict['tls_port_type']
        print "tls_port_key %s [OK]" % mydict['tls_port_key']

        if getNumberOfElementsInDict(mydict) != 40:
            assert()
        
        print "getNumberOfElementsInDict [OK]"

    def test_getParserVersion(self):
        if not getConfparserVersion():
            assert()

        print "\n-----------------------------"
        print "getConfparserVersion() [OK]"
        print "-----------------------------"

    def test_confToDictChangeValue(self):

        mydict = {}
        mydict = confToDict(LIBVIRT_CONFIG_FILE)

        mydict['tls_port'] = "7777"

        writeDictToFile(LIBVIRT_CONFIG_FILE, mydict)

        # re-read file
        mydict = confToDict(LIBVIRT_CONFIG_FILE)
        if mydict['tls_port'] != "7777":
            assert()

        print "\n-----------------------------"
        print "changing dict value [OK]"
        print "-----------------------------"

if __name__ == '__main__':

	# Test - search all URLs
	suite = unittest.TestLoader().loadTestsFromTestCase(confParseTests)
	unittest.TextTestRunner(verbosity=0).run(suite)

