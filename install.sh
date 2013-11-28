#! /bin/bash

sudo apt-get install python2.7
sudo easy_install pip
sudo pip install BeautifulSoup4
sudo pip install lxml
sudo apt-get install python-qt4
sudo chmod +x remove.sh commentary.py script.sh error.sh stop.sh
sudo mkdir /opt/desktop-commentary
sudo cp remove.sh commentary.py gui.py script.sh error.sh stop.sh /opt/desktop-commentary
sudo ln -s /opt/desktop-commentary/commentary.py /usr/bin/commentary
sudo ln -s /opt/desktop-commentary/remove.sh /usr/bin/commentary-uninstall
sudo ln -s /opt/desktop-commentary/stop.sh /usr/bin/stopcommentary
