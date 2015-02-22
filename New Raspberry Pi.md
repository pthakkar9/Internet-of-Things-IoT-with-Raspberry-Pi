A few things for new R Pi so that I don't have to go thru' my bookmarks again

Whenever I get new Raspberry Pis this is what I have to do. Start to headless..  
===============================================================================

1. Download NOOBS zip from http://www.raspberrypi.org/downloads/ (700 MB+ file, takes a long time.. so do this first)
2. Extract
3. Format new microSD card 
4. Copy content of extracted folder to microSD
5. Plug microSD in Raspberry Pi & connect to Display and network
6. Install Raspbian (takes a few minutes).. and it gets restarted
7. File systems are already expanded. But change setting so that GUI gets loaded every time.. it will restart
8. Either connect ethernet cable or wifi router & connect to wifi
9. Go to network admin page (for AT&T uverse it's at http://192.168.1.254) and either assign static IP or static static IP.
or Go to LX terminal and type `sudo ifconfig` to find IP address and look up at admin page
10. 'sudo apt-get install xrdp' (Xrdp is a daemon, a computer process that runs in the background that can support Microsoft Remote Desktop Client on both Mac and PC.)
11. if haven't done wifi yet, do it.. go to wifi config, scan, double click, enter password and done
