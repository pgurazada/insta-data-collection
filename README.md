# Collecting data from Instagram

This document outlines a broad set of guidelines to execute a large-scale data collection project on Instagram

## Code
 - Use Python 3.6+; never ever revert to Python 2 just because ready-code is available
 - Minimize dependencies (e.g., if a task can be executed with the builtin `requests` module, don’t use a bespoke module from third-party sources)
 - The project git repo shall contain as a rule:
     - A bash script that identifies and installs all the requirements for the project on a new machine (`$ bash install-requirements.sh`)
     - A bash script (`runscraper.sh`) that provides the machinery to run on a new machine - a specific script, write data to storage and shut the machine down post task execution 

## Compute - master and workers

- All primary code development should be done only on the master machine (default - 16 GB RAM, 100 GB storage)(avoid local compute)
- Only master machines shall amend the code in the git repo (1000 git push origin’s in master are better than 1 minor edit in worker)
- Parallelizable processes shall be shared among worker machines 
- Default worker for data collection - 0.6 GB RAM, 10 GB storage
- Workers shall NEVER amend git repos. Use vim -R as default on workers
- Workers shall communicate with git repo code only via bash scripts
- Workers CPU load shall be monitored before full deployment. At no time shall workers run below 80% utilization. If space capacity exists, run more code (`screen -ls` shall always return more than one socket)
- Parallelization shall be driven by:
    - Logical separation and independence of the code base
    - Spare capacity on workers
- Each payload executed on a worker shall be a bash script that ends with a shutdown command. Ensure:
    - Idle workers shall never be left running
    - Workers shall always write data to storage before shutdown
- Delete all workers post execution of the project

## Storage
- Buckets are a good idea, do more of those
- Always stream data from stores
                from google.cloud import storage
                data_store = storage.Client()

