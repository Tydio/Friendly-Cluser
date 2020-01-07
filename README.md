# SkyLake-II
Little python scripts for using SkyLake-II high-performance clusters easilier and more coveniently.
*********************************************************************************
> qsub.py
- qsub.py is written for avoiding repeating to type the '-N', '-n', '-p', and '-J' parameters for the job to be submitted.
- Use 'qsub.py' or 'qsub.py xxx' to submit the job.
- If job script name 'xxx' is absent, it will search for a 'vasp.sub' script in the current directory.
*********************************************************************************
> qpeek.py
- qpeek.py is written for quickly and coveniently check the executing state and process of the executing jobs.
- Use 'qpeek.py [-f]' to display the screen file of the newest submitted job.
- Use 'qpeek.py [-f] xxx' to display the screen file of a specified job that end with 'xxx' in it job_id.
- [-f] means to display the screen file continuously.
*********************************************************************************
> qdel.py
- qdel.py is written for quickly and coveniently cancel the executing jobs in queue with part of the full id of jobs input.
- Use 'qdel.py xxx' to kill a job, in which 'xxx' is the last several characters of a job.
- And it should be put togeter with 'qpeek.py' in a same directory, since it refers some functions inside 'qpeek.py'.
*********************************************************************************
