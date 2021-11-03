hotfix for Gateway: 2021-11-03

Issue: 

`current_versions.json` has an incorrect setting for thermocouple firmware version, which 
causes thermocouples to get stuck in an endless OTA FW UPDATE loop.

Fix: 

In `current_versions.json` update `{"thermocouple": {"version":2}}` to `{"thermocouple": {"version":1}}`

How to install / run:

- log in as gateway user (or any user with sudo privileges)
- enter `sudo su` then enter gateway user password
- enter `cd /opt`
- enter `git clone https://github.com/gregcompton/xbeeBasicListener.git`
- enter `cd hotfix_Gateway-2021-11-03`
- run `python fixit.py`  if you get an error here, run `python3 fixit.py`
