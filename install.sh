#! /bin/bash

sudo chmod +x remove.sh commentary.py script.sh error.sh stop.sh wickets.jpg
sudo mkdir /opt/desktop-commentary
sudo cp remove.sh commentary.py gui.py script.sh error.sh stop.sh wickets.jpg /opt/desktop-commentary
sudo ln -s /opt/desktop-commentary/commentary.py /usr/bin/commentary
sudo ln -s /opt/desktop-commentary/remove.sh /usr/bin/commentary-uninstall
sudo ln -s /opt/desktop-commentary/stop.sh /usr/bin/stopcommentary
