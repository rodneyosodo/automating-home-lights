# automating-home-lights
A demonstration of using nodemcu connected to a solid state relay to switch on and off lights using google assistant

## Dependencies

- Git flow:

    - https://github.com/petervanderdoes/gitflow-avh
    - https://github.com/bobthecow/git-flow-completion
    - https://github.com/pytest-dev/pytest-cov

- legit: https://github.com/kennethreitz/legit
- SemVer: http://semver.org/
- pytest: https://github.com/pytest-dev/pytest
- tox: https://tox.readthedocs.io/en/latest/
- sphinx: http://www.sphinx-doc.org/en/stable/

Todo
----

- [x] Test todo list
- [ ] Test todo list


















# MQTT MAM

This project seeks to demonstrate the use of MQTT protocol and IOTA-MAM to store temperature sensor on the blockchain.

A view of the temperature and humidity data on the iota tangle.

<p  align="center">
  <img src="assets/mam_explorer.png" width="900" />
</p>

## Hardware setup

### Nodemcu & Current sensor

Circuit design

<p  align="center">
  <img src="assets/nodemcu_dht11_schem.png" width="600" />
</p>

Board design 

<p align="center">
  <img src="assets/nodemcu_dht11_bb.png" width="600" />
</p>

Final look

<p align="center">
  <img src="assets/final.JPG" width="600" />
</p>

## Installation

### Esp

Installing in a NodeMCU involves pushing the python files into the device whether it's via a usb to ttl or just a usb cable. This can be done using the command

```bash
sudo ampy --port /dev/ttyUSB0 --baud 115200 put main.py
sudo ampy --port /dev/ttyUSB0 --baud 115200 put config.py
sudo ampy --port /dev/ttyUSB0 --baud 115200 put connectWifi.py
```

You need to create a config.py file with the following information for each and every esp folder (current-sensor, dht-sensor, motion-sensor, relay-bulb, relay-fan)

```python
MQTT_CONFIG = {
    'SENSOR_ID': '',
    'MQTT_HOST': '',
    'PORT': '',
    'PUB_TOPIC': ''
}

WIFI_CONFIG = {
    'WIFI_ESSID': '',
    'WIFI_PASSWORD': ''
}
```

### Raspberry Pi

To install npm packages used for the Raspberry Pi, you run.

```bash
npm install @iota/mam mqtt
```

You also need to create a config folder and have the file config/config.js with the following configuration

```js
module.exports = {
    brokerUrl: "",
    port: "",
    topic: "",
    provider, ""
};
```
# Usage

## Raspberry Pi

To run the code for Raspberry Pi just cd into the folder and run

```bash
node app.js
```

To ensure that the Raspberry Pi runs the code whenever it boots, edit the rc.local file

```
sudo nano /etc/rc.local
```

and add

```
node app.js &
```

# Contributing

To contribute code to this repository please read the [CONTRIBUTING](https://github.com/peterokwara/mqtt-mam/blob/master/CONTRIBUTING.md) guidelines.

# License

[MIT](https://github.com/peterokwara/mqtt-mam/blob/master/LICENSE)










The Super Easy Micropython ESP8266 Windows Guide. No Guesswork Required!
By esper2142 in CircuitsMicrocontrollers34,88519113Featured
licenseDownloadFavorite
Introduction: The Super Easy Micropython ESP8266 Windows Guide. No Guesswork Required!
The Super Easy Micropython ESP8266 Windows Guide. No Guesswork Required!
esper2142By esper2142Faraday RobotechFollow
More by the author:
Custom Anvil Stand - No Welding RequiredWood USB W/Custom PyrographyPiE-Ink Name Badge
About: It's dark. You are likely to be eaten by a grue. More About esper2142 »
So you want to check out Micropython, but aren't sure where to begin? Confused by the many guides, boards, and instructions out there that seemingly only work for everyone but you? Want a guide to take ALL of the guesswork out of the equation for you, and show you step by step where to start?

Great - because you found one! BOOM!

MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments. The differences between Micropython and the regular Python 3 are so small and meaningless, that it's not really worth getting into. With that out of the way, what are we gearing up for?

With Micropython & this tutorial, we'll be able to:

Use Python on freggin' microcontrollers (arduino devices, etc)!
Use a python interpreter in a web browser or from a program to change code ON THE FLY with your creations, no compiling necessary!
Connect to your device WIRELESSLY via a broadcasted SSID! WHAT!? CRAZY!
Let's get started!

Add TipAsk QuestionCommentDownload
Teacher Notes
Teachers! Did you use this instructable in your classroom?
Add a Teacher Note to share how you incorporated it into your lesson.

Add Teacher Note
Step 1: Materials Needed
Materials Needed
To take the guesswork out of which guide to use or what instructions to use, we're going to work with a single board - the NodeMCU 12-E. We'll be referencing this board and it's instructions for the entirety of this particular instructable. If you're using a different board, I will list some other tutorials you may want to follow at the end of this guide.

Things we'll need:

A NodeMCU 12E (Version 2) ESP8266 Board
A Micro USB to USB cable
Add TipAsk QuestionCommentDownload
Step 2: Install + Configure Python 2.7
Install + Configure Python 2.7
Install + Configure Python 2.7
Install + Configure Python 2.7
Unfortunately, the tool we need to flash the appropriate binary on the NodeMCU 12E ESP8266 board for Micropython only works with Python 2.7.x (not the latest Python 3.x). So, we'll need to install it and make sure it works.

Download python 2.7 here and begin the installation
Install python somewhere easy to find. I choose root C. We'll need to access the folder to place some files and scripts later. (check screenshot)
On the next screen, be sure to add python.exe to PATH. This will be required for later. (check screenshot)
Once you've installed it successfully, check that it's working right by going to a command prompt (Run --> CMD, or Windows Key + R --> CMD) and typing 'python'. It should return the version installed (screenshot).
Great! Now we'll need to install the thing that will actually do the flashing - esptool.

Add TipAsk QuestionCommentDownload
Step 3: Install Esptool
Install Esptool
From a command prompt, we'll need to go into our installed python 2.7 directory.

We'll need to type:

cd /
cd Python27 (or whatever directory you installed it to)
cd Scripts
pip install esptool

Check the screenshot for a visual of the commands and the output of the install.

esptool is a Python-based, open source, platform independent, utility to communicate with the ROM bootloader in Espressif ESP8266.
Add TipAsk QuestionCommentDownload
Step 4: Connect to Board + Install Micropython
Connect to Board + Install Micropython
Connect to Board + Install Micropython
Connect to Board + Install Micropython
Connect to Board + Install Micropython
The moment of truth has arrived!

Now we'll hook up the board and flash it with the binary to run Micropython! :-)

Plug your USB cable into the NodeMCU board, and then into your computer.
Go into device manager and confirm what port your device is on. We'll need this information later. I'm on COM port 3 (screenshot).
Download the micropython ESP8266 code I've conveniently hosted for you on my github, and place it in your python/Scripts directory from earlier (screenshot).
Place the NodeMCU board into bootloader mode by holding the flash button, pressing the RST button, then releasing the flash button. You'll see the blue light briefly flash once when you've done this (screenshot).
Open a command prompt, and return to the scripts directory.
Run the following command, keeping in mind to substitute COM3 with YOUR particular COM port:
esptool.py --port COM3 --baud 460800 write_flash --flash_size=detect 0 esp8266-20161110-v1.8.6.bin

Congratulations! You've successfully flashed Micropython onto a microcontroller! AWWW YESS!!!

Now it's time to access it, and enable easy web access!

Add TipAsk QuestionCommentDownload
Step 5: Connect Using PuTTY + WebREPL
Connect Using PuTTY + WebREPL
Connect Using PuTTY + WebREPL
Connect Using PuTTY + WebREPL
Unplug and plug your NodeMCU board back into USB. This should let the code compile and work properly after flashing.
Open up PuTTY. Use a serial connection to your COM port, with a baud rate of 115200. You may want to save this for quick access later on. (check screenshot)
Once we've got our command prompt, we should be at the interpreter. AWESOME! Now we can run and do all kinds of crazy cool python stuff right from the command line!
Let's give ourselves the capability to control it via the web! type import webrepl_setup in order to start the WebREPL daemon on startup. type E to enable on boot, then type y to change the default password. Use something you'll remember, but strong enough to keep others from guessing. Reference the screenshot for help.
Unplug and plug your NodeMCU board back in again.
We can now see a new SSID being broadcast. It's our Micropython-enabled NodeMCU board! WHOA! Connecting to this right now will cause us to lose connectivity, so just make note of it. The default password is: micropythoN (capital N at the end)
To save space on the board, the required files to connect to our web interface must be downloaded on your local machine. Go here to download the webREPL files. Extract them somewhere you can find them, then open up webrepl.html
Go ahead and connect to the Micropython SSID with the micropythoN password. Be careful, you'll lose internet connectivity at this point! Make sure you have these instructions loaded and ready to go in another window.
Go to your webrepl browser window you opened up previously. You should see the ws://192.168.4.1:8266/ address by default in the connect window. Click connect, and enter the password you set earlier. You now have access to your Micropython-enabled ESP8266 board via wireless! BLACK MAGIC! (screenshot)
Add TipAsk QuestionCommentDownload
Step 6: AWESOME IT WORKS....Now What?
AWESOME IT WORKS....Now What?
AWESOME IT WORKS....Now What?
AWESOME IT WORKS....Now What?
AWESOME IT WORKS....Now What?
You have access to an amazing microcontroller and all it's powerful sensors + actions in REAL TIME! You can access it over the web from your couch in another room.

Want to dynamically draw on LED displays? How about control a servo motor? Why not some kind of funky watch? It's all possible!

I highly recommend you check out the Micropython guides over at Adafruit. You will learn the intricacies of Micropython, as well as discover some easy projects to get you started. Most of these projects are headed by the fabulous Tony DiCola, a fantastic and prolific Micropython communicator and expert. Stop reading this - get going! :)

Getting Started with MicroPython on ESP32 and ESP8266
Learn how to get started with MicroPython firmware on the ESP32 and ESP8266. We’ll introduce you to MicroPython, show you the differences between MicroPython and regular Python, and how to program your ESP based boards with MicroPython using uPyCraft IDE. After completing this guide, you’ll have your first LED blinking using MicroPython.



What is MicroPython?
MicroPython is a re-implementation of Python 3 targeted for microcontrollers and embedded systems. MicroPython is very similar with regular Python. So, if you already know how to program in Python, you also know how to program in MicroPython.



Python vs MicroPython
Apart from a few exceptions, the language features of Python are also available in MicroPython. The biggest difference between Python and MicroPython is that MicroPython was designed to work under constrained conditions.



Because of that, MicroPython does not come with the full standard library. It only includes a small subset of the Python standard library. However, it does include modules to access low-level hardware – this means that there are libraries to easily access and interact with the GPIOs.

Additionally, devices with Wi-Fi capabilities like the ESP8266 and ESP32 include modules to support network connections.

Why MicroPython?
Python is one of the most widely used, simple and easy-to-learn programming languages around. So, the emergence of MicroPython makes it extremely easy and simple to program digital electronics. If you’ve never programmed digital electronics before, MicroPython is a good starting point.

MicroPython’s goal is to make programming digital electronics as simple as possible, so it can be used by anyone. Currently, MicroPython is used by hobbyists, researchers, teachers, educators, and even in commercial products. The code for blinking an LED on a ESP32 or ESP8266 is as simple as follows:

# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)
View raw code

One great feature of MicroPython is that it comes with an interactive REPL (Read-Evaluate-Print Loop). The REPL allows you to connect to a board and execute code quickly without the need to compile or upload code.

MicroPython – Boards support
MicroPython runs on many different devices and boards, such as:



ESP32
ESP8266
PyBoard
Micro:Bit
Teensy 3.X
WiPy – Pycom
Adafruit Circuit Playground Express
Other ESP32/ESP8266 based boards
For more information about other boards that support MicroPython, take a look at the following links:

Boards running MicroPython – MicroPython Forum
Boards summary – MicroPython Github
In our projects, we’ll use MicroPython with the ESP32 and ESP8266 boards.

ESP32 is the successor of the ESP8266. So, at the moment, not all features are available in MicroPython to take the most out of the ESP32 – it’s still an ongoing project. However, it’s very usable and you can make a lot of projects with it.

ESP32 and ESP8266 boards are similar, and you won’t feel almost any difference programming them using MicroPython. This means that anything you write for the ESP8266 should also run with no changes or minimal changes on the ESP32 (mainly changing the pin assignment).

Installing uPyCraft IDE
Before continuing with this tutorial, you should install uPyCraft IDE in your computer. Follow one of the next tutorials to install uPyCraft IDE:

Install uPyCraft IDE – Windows PC
Install uPyCraft IDE – Mac OS X
Install uPyCraft IDE – Linux Ubuntu
Note: if you’re having trouble installing or using uPyCraft IDE, we’ve also created an alternative guide on how to program the ESP32/ESP8266 using Thonny IDE.

Flashing MicroPython Firmware to ESP32/ESP8266
Unlike other boards, MicroPython isn’t flashed onto the ESP32 or ESP8266 by default. That’s the first thing you need to do to start programming your boards with MicroPython: flash/upload the firmware. Follow the next tutorial to flash MicroPython firmware on your board:

Flash/Upload MicroPython Firmware to ESP32 and ESP8266


Getting Started with uPyCraft IDE
In this section we’ll give you an overview of the uPyCraft IDE software, so that you can start programming the ESP32/ESP8266 with MicroPython.

The IDE is a software that contains tools to make the process of development, debugging and upload code easier. There are many ways to program your ESP board with MicroPython. We’ve chosen uPyCraft IDE because it is simple and intuitive to use and works great with the ESP boards.

At this point, we assumed that you have:

uPyCraft IDE installed on your computer
ESP32/ESP8266 flashed with MicroPython firmware
uPyCraft IDE Overview
Open uPyCraft IDE, a new window opens as follows:



Let’s take a closer look at each section of uPyCraft IDE:



Folder and files
Editor
MicroPython Shell/Terminal
Tools
1. Folder and files
This section shows several folders and files. The device folder shows the files that are currently stored on your ESP board. If you have your ESP32 or ESP8266 connected via serial to uPyCraft IDE, when you expand the device folder, all files stored should load. By default, you should only have a boot.py file. To run your main code, it is recommended to create a main.py file.

boot.py: runs when the device starts and sets up several configuration options;
main.py: this is the main script that contains your code. It is executed immediately after the boot.py.
The sd folder is meant to access files stored on SD cards – this is only works with boards like the PyBoard that come with an SD card slot.

The uPy_lib shows the built-in IDE library files.

Finally, the workspace is a directory to save your files. These files are saved in your computer in a directory defined by you. This is a specially useful to keep all your files organized at hand.

When using uPycraft for the first time, to select your working directory, click the workspace folder. A new window pops up for you to chose your workspace path. Create a new folder or select an existing folder to be your working directory.

Then, go to File > Reflush Directory to update the directory.



Note: to change your user directory, simply go to Tools >InitConfig and click the workspace directory folder to chose a different path.



2. Editor
The Editor section is where you write your code and edit your .py files. You can open more than one file, and the Editor will open a new tab for each file.

3. MicroPython Shell/terminal
On the MicroPython Shell you can type commands to be executed immediately by your ESP board without the need to upload new files. The terminal also provides information about the state of an executing program, shows errors related with upload, syntax errors, prints messages, etc…

4. Tools
The icons placed at the rightmost side allow you to quickly perform tasks. Each button is labeled in the figure below:



New file: creates a new file on the Editor;
Open file: open a file from your computer;
Save file: saves a file;
Download and run: upload the code to your board and execute the code;
Stop: stop the execution of the code – it’s the same as entering CRTL+C on the Shell to stop all scripts from running;
Connect/Disconnect: connect or disconnect to your board via Serial. You must select the serial port first in Tools > Serial;
Undo: undo last change in the code Editor;
Redo: redo last change in the code Editor;
Syntax check: checks the syntax of your code;
Clear: clear the Shell/terminal window messages.
Running Your First Script
To get you familiar with the process of writing a file and executing code on your ESP32/ESP8266 boards, we’ll upload a new script that simply blinks the on-board LED of your ESP32 or ESP8266.

Establishing a communication with the board
After having the MicroPython firmware installed on your board and having the board connected to your computer through an USB cable, follow the next steps:

1. Go to Tools > Board and select the board you’re using.

2. Go to Tools > Port and select the com port your ESP is connected to.

3. Press the Connect button to establish a serial communication with your board.



4. The >>> should appear in the Shell window after a successful connection with your board. You can type the print command to test if it’s working:

>>> print('Hello')
Hello
>>>
It should print the “Hello” message. Only if you see that message, you can continue with this tutorial. Otherwise, make sure you have established a serial communication with your board or that you’ve flashed successfully the MicroPython firmware on your board.



Creating the main.py file on your board
1. Press the “New file” button to create a new file.



2. Press the “Save file” button to save the file in your computer.

3. A new window opens, name your file main.py and save it in your computer:



4. After that, you should see the following in your uPyCraft IDE (the boot.py file in your device and a new tab with the main.py file):



5. Click the “Download and run” button to upload the file to your ESP board:



6. The device directory should now load the main.py file. Your ESP has the file main.py stored.



Uploading the blink LED script
1. Copy the following code to the Editor on the main.py file:

# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)
View raw code

2. Press the “Stop” button to stop any script from running in your board:



3. Click the “Download and Run button” to upload the script to the ESP32 or ESP8266:



4. You should see a message saying “download ok” in the Shell window.



Testing the script
To run the script that was just uploaded to your board, you need to follow these steps:

1. Press the “Stop” button



2. Press the on-board ESP32/ESP8266 EN (ENABLE) or RST (RESET) button to restart your board and run the script from the start:



If you’re using an ESP32, your Terminal messages should look something as shown in the following figure after a EN/RST button press:



Your ESP32 or ESP8266 on-board LED should be blinking every 500 milliseconds. Here’s where the ESP32’s on-board LED is located:



Here’s the ESP8266 on-board LED:

