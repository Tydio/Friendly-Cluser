#!/usr/bin/env python
#-- coding:utf-8 --
# Author: Hongyang Huang
# This script is written for conveniently check the state of executing jobs.
# type 'qpeek' to check the newest job state.
# type 'qpeek xxx' to check all specified job with 'xxx' as part of its job_id.
import os
import re
import sys


result = os.popen('yhqueue -u xjtu_hhy')
res = result.read()
if len(res) < 2:
    print "There are no executing jobs in the queue."
    sys.exit(1)
try:
    code_num = sys.argv[1]
except:
    if len(res) > 1:
        code_num = re.search(r'\s+(\d+).*',res.splitlines()[-1]).group(1)
    else:
        print "There are no executing jobs in the queue."
        sys.exit(1)
else:
    extend_f = False
    res_lines = res.splitlines()
    for i in res_lines[-1:-len(res_lines):-1]:
        full_code = re.search(r'\s+(\d+).*',i).group(1)
        if str(code_num) in str(full_code):
            code_num = full_code
            extend_f = True
            break
    if not extend_f:
        print "No matched job found."
        sys.exit(1)
file_name = "slurm-%s.out" % (code_num)
result = os.popen("find /THFS/home/xjtu_hhy -name %s" % file_name)
try:
    res = result.read().splitlines()
except:
    print "Job log file is absent!"
else:
    for i in res:
        os.system("cat %s" % i)
