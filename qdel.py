#!/usr/bin/env python
#-- coding:utf-8 --
# Author: Hongyang Huang
# This script is written for cutting a specified job.
# type 'qdel.py xxx' to cut a specified job with 'xxx' as part of its job_id.
import os
import re
import sys
from qpeek import refCode
from qpeek import refCode_no

# Main entry.
if __name__ == '__main__':
    res = os.popen('squeue -u hhuang').read().splitlines()
    if len(res) < 2:
        print("There are no executing jobs in the queue.")
        sys.exit(1)
    if len(sys.argv) > 1:
        code_num = refCode(sys.argv[1], res)
    else:
        code_num = refCode_no(res)
    try:
        os.system("scancel %s" % code_num)
    except:
        print("[__main__]: Job is missing!")
sys.exit(0)
