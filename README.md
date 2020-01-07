# SkyLake-II
Little python scripts for using SkyLake-II high-performance clusters easilier and more coveniently.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

qsub.py is written for avoiding repeating to type the '-N', '-n', '-p', and '-J' parameters for the job to be submitted.

Use 'qsub.py' or 'qsub.py xxx' to submit the job.

If job script name 'xxx' is absent, it will search for a 'vasp.sub' script in the current directory.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

qpeek.py is written for quickly and coveniently check the executing state and process of the executing jobs.

Use 'qpeek' to check the newest submitted job.

Use 'qpeek xxx' to check all specified jobs that contain 'xxx' in their job ids.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

qdel.py is written for quickly and coveniently cancel the executing jobs in queue with part of the full id of jobs input.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
