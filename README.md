# Description
A simple little tool that track your internet speed at regular intervals and store it in a `.txt` file. If your ISP is not giving you what they are promising, show them a written record ;)

# Prerequisite
- `python3`

# Dependency
- `speedtest-cli`

## Install dependency
```sh
pip3 install speedtest-cli
```

# Run Program
```sh
python3 speedtest_record.py
```

## Run in the background
*This part of the section is for linux users only*

You can run this program in the background with `nohup`
```sh
nohup python3 speedtest_record.py &
```
To kill the process find the `PID` with command below:
```sh
ps ax | grep speedtest_record.py
```
Then kill the process with command below:
```sh
kill `PID`
```

# Options
### Servers
Leave this empty for your nearest server. You can also populate this list with your favorite server id's. To get a server list run `speedtest --list`
```python
servers = []
```

### Threads
If you want to use single thread set it to 1
```python
threads = None
```

### Interval
Add your preferred interval time in minutes. 
```python
interval = 30
```

# Instructions for Windows users
Replace `python3` and `pip3` command with `python` and `pip` respectively.