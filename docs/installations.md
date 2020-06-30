# Installation

The NodeMCU is a development board featuring the popular ESP8266 WiFi chip. As it turns out, you can program the ESP8266 just like any other microcontroller. Its obvious advantage over the Arduino or PIC is that it can readily connect to the Internet via WiFi.

MicroPython is a re-implementation of Python 3 targeted for microcontrollers and embedded systems. MicroPython is very similar with regular Python. So, if you already know how to program in Python, you also know how to program in MicroPython.

PuTTY  is a free and open-source terminal emulator, serial console and network file transfer application. It can also connect to a serial port.

## Steps

1. Install Python On windows 10

    Visit https://www.python.org/ and download the latest version of python install it on your machine.

    **Do not forget to check the add to path while installing on you machine**

2. Install ESPTool

    Use your terminal to complete this step and using the command below.

    ```shell
    pip3 install esptool
    ```

3. Download ESP8266 firmware

    Visit https://micropython.org/download  and download the latest version of ESP8266 bin file for windows and install it on your machine.


4. Plug in Device

    Now plug in your NodeMCU 8266 device using a USB wire in to your machine and go to the next step after confirming that its properly plugged.

    **Remember the port number mentioned**

5. Erase Flash

    Use the command below to erase flash in your powershell.

    ```shell
    esptool.py --port /dev/ttyUSB0 erase_flash
    ```

6. Execute upload command

    Use the command below to upload bin file in your powershell.

    ```shell
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
    ```

7. Test with Putty
Go to [https://www.putty.org/](https://www.putty.org/) and download the windows version and install it.


    Now install it and open the program and follow these steps.

    Click on Open button or press Enter and you will be given access to MicroPython Terminal.

![](https://i.imgur.com/L1MEf0l.png)


Voila, you are set and ready to go and explore the MicroPython World.

![](https://i.imgur.com/xhqKobv.png)

