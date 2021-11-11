from optparse import OptionParser
import os.path
import os
import sys
import re
import subprocess
import glob

import time

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# print sys.argv[1]


#################################################### RCDB ENVIRONMENT ####################################################
os.environ["RCDB_HOME"] = "/group/halld/www/halldweb/html/rcdb_home"
sys.path.append("/group/halld/www/halldweb/html/rcdb_home/python")
import rcdb
db = rcdb.RCDBProvider("mysql://rcdb@hallddb/rcdb")

run_number=float(sys.argv[1])


cdc_gas_pressure = db.get_condition(run_number, "cdc_gas_pressure").value

run = db.get_run(run_number)
#print run.number
#print run.start_time
#print run.end_time
#print run.conditions

#print "asdasdasdasd\n" 

print run.start_time, "   ",  cdc_gas_pressure

