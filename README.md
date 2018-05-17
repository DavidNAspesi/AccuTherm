# AccuTherm

AccuTherm is a full stack web application that reads temperature from a type-k thermocouple (which is able to withstand temperatures up to 600 degrees Celsius) and feeds that real-time data to a webpage.

## Screenshot

![AccuTherm screencap](./static/accuThermsc.gif)

## Setup

First, assemble the needed hardware.  This app requires a Raspberry Pi 3 B+, GrovePi sensor hat, and the GrovePi High Temperature Sensor.  Once the hardware is set up, clone this repo into a folder somewhere on the Pi's filesystem.  Then, run apt-get install on the following packages:
build-essential
libncurses5-dev
libncursesw5-dev
libreadline6-dev
libbz2-dev
libexpat1-dev
liblzma-dev
zlib1g-dev
libsqlite3-dev
libgdbm-dev
tk8.5-dev
python-dev
libssl-dev openssl

The only remaining command should be `systemctl restart emperor.uwsgi.service.  The app should now be running, and the webpage should be live at the IP address of your Raspberry Pi.

