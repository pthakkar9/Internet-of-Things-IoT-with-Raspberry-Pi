sudo apt-get update
sudo apt-get install python-dev // so that you can write and execute pythong scripts
sudo apt-get install python-rpi.gpio // so that your python scripts can work with gpio
sudo apt-get install xrdp // read first raspberry pi .md for more info
nano ____.py // write your python script now 
sudo python ____.py //execute your python stuff

//sudo apt-get install python3-pip 
sudo apt-get install python-pip // so that you can use pip (python package manager .. just like npm/rubygems
//sudo pip-3.3 install twilio
sudo pip install twilio // so that you can use twilio

//copy file from local to remote over ssh - use it from local command prompt
scp /path/to/file username@a:/path/to/destination
//copy file from remote to local over ssh - use it from local command prompt
scp username@b:/path/to/file /path/to/destination

