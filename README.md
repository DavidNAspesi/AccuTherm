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

The only remaining command should be `systemctl restart emperor.uwsgi.service`.  The app should now be running, and the webpage should be live at the IP address of your Raspberry Pi.

## License

Copyright 2018 David Aspesi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
