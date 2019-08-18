#!/usr/bin/env python
#-- coding:utf-8 --
# Copyright: Hongyang Huang
# This script is written to avoid repeating to enter the '-N', '-n', '-p', and '-J' parameters.
# The order of the parameters '-N', '-n', and '-J' must be aligned as '...-N...-n...-J...'
# type 'qsub' to submit a job with a job script named 'vasp.sub' in current directory.
# type 'qsub xxx' to submit a job with specified job script named 'xxx' in current directory.
import os
import re
import sys


try:
    file_name = sys.argv[1]
except:
    file_name = 'vasp.sub'
    print "No file name specified, searching for vasp.sub...\n"
try:
    subfile_fh = open(file_name, 'r')
except IOError:
    print "ERROR Couldn't find a file named %s!\n" % file_name
    sys.exit(1)
subfile_fh.seek(0)
while True:
    line = subfile_fh.readline()
    if not line:
        break
    if "yhrun" in line:
        p = re.search(r'^\s*yhrun.*-N (\d+).*-n (\d+).*-J ([^\s]*).*', line)
        node_nums = int(p.group(1))
        core_nums = int(p.group(2))
        job_name = p.group(3)
        #print "Nodes: %04i, Cores: %04i, Job_name: %s\n" % (node_nums, core_nums, job_name)
        QSUB = "yhbatch -p gsc -N %d -n %d -J %s %s" % (node_nums, core_nums, job_name, file_name)
        #print QSUB
        os.system(QSUB)
        print "mission successfully submitted...\n"
if not 'p' in locals().keys():
    print "ERROR Relative mission parameters not found in %s!\nMission not submitted...\n" % file_name
subfile_fh.close()
