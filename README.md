# invdb
Inventory API Consumer CLI.
 
## Audience.
consumers of Inventory data API.

## Description.
This tool consumes Inventory API and display results.

## How to Install.

- Clone this repo
- cd to the cloned project
- Create Virtual env and install this package.

```
pip install wheel
pip install setuptools
pip install virtualenv

virtualenv venv
source venv/bin/activate
python setup.py install 
python setup.py develop (if you want to work and extend.)
```

## How to use.

```
invdb group-resources --help
Usage: invdb [OPTIONS] {group-resources|group-overlap}

Options:
  --limit, --l INTEGER            Limit to top-k results defaults to 10
  --groups, --g TEXT              comma separated values of N number of groups
  --sort, --s [total_cpus|total_memory|total_disk]
                                  How to sort the result CPU, MEMORY, DISK,
                                  defaults to CPU
  --help                          Show this message and exit.

```

Example.

```
To find  total CPU, memory, and disk space of each group sort by memory limit to top 5.

# invdb group-resources --limit 5 --sort total_memory

To find  total CPU, memory, and disk space of each group sort by cpu.

# invdb group-resources --sort total_cpus

To find N number groups which have nodes across them.

# invdb group-overlap --groups presto-master,hbase-regionserver
# invdb group-overlap --groups all,all,presto-master

```

### Important docs.
- [Link to Challenger Answers file](./challenge_answer.md)
- [Link to Unit Tests](./tests)

### Known Issues
```
- invdb group-overlap --groups all,all,presto-master --limit 5
(Limits are not handled in group over laps)
- Unit test does not cover all (Time constraint)

```
