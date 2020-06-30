# Harware

## INTRODUCTION

We all want our home appliances to be controlled automatically based on some conditions. So when we want to control AC powered devices like a lamp or fans we use relay module since our micro controllers only operate at 5V. You can use the relay module to control teh AC mains and the micro controller to control the relay.

## BACKGROUND INFO

We will walk through how to setup the one channel relay module to switch on a lamp or other device.

### How Do Relays Work?

A relay is an electromagnetic switch operated by a relatively small current that can control much larger current.

Initially the first circuit is switched off and no current flows through it until something \(either a sensor or switch closing\) turns it on. The second circuit is also switched off.

When a small current flows through the first circuit, it activates the electromagnet, which generates a magnetic field all around it.

The energized electromagnet attracts a contact in the second circuit toward it, closing the switch and allowing a much bigger current to flow through the second circuit.

When the current stops flowing, the contact goes back up to its original position, switching the second circuit off again.

### Relay Basics

Typically the relay has 5 pins, three of them are high voltage terminals \(NC, COM, and NO\) that connect to the device you want to control.

The mains electricity enters the relay at the common \(COM\) terminal. While use of NC & NO terminals depends upon whether you want to turn the device ON or OFF.

When current flows through the coil, the electromagnet becomes charged and moves the internal contacts of the switch. At that time the normally open \(NO\) terminal connects to the common \(COM\), and the normally closed \(NC\) terminal becomes disconnected.

When current stops flowing through the coil, the internal contact returns to its initial state i.e. the normally closed \(NC\) terminal connects to the common \(COM\), and the normally open \(NO\) terminal reopens.

* **COM \(Common\)**: This is the pin you should connect to the signal \(mains electricity in our case\) you are planning to switch.
* **NC \(Normally Closed\)**: A normally closed configuration is used when you want to turn off the relay by default. In this configuration the relay is always closed and remains closed until you send a signal from the eris dev kit to the relay module to open the circuit.
* **NO \(Normally Open\)**: A normally open configuration works the other way in which the relay is always open until you send a signal from the eris dev kit to the relay module to close the circuit.
* **Control** transmit data
* **GND** is the ground connection.
* **VCC** pin supplies power to the module.

### Pinout

Generic relay

![](https://i.imgur.com/8NuMAID.png)

How it looks like

![](https://i.imgur.com/XrJftak.jpg)

**Warning: This board interacts with HIGH AC voltage. Incorrect or improper use could result in serious injury or death. So, it is intended for people experienced around, and knowledgeable about HIGH AC voltage.**

## PROCEDURE

### How to setup relay

Start by connecting VCC pin on the module to 5V on the eris-dev-kit and GND pin to ground. Connect the pin PA6 to the signal pin for controlling the relay.

You’ll also need to place the relay module in line with the AC powered device \(lamp in our case\) you’re attempting to control. You’ll have to cut your live AC line and connect one end of the cut wire \(coming from the wall\) to COM and the other to NC or NO depending on what you want your device’s resting state to be.

If your AC device is going to be off for most of the time, and you occasionally want to turn it on, you should connect the other to NO. Connect to NC if the device will be on for most of the time.

![](https://i.imgur.com/Rbzywjb.jpg)


### Programming

```python
from machine import Pin
from time import sleep

# declaring the pin to which input pin of relay module is connected and Set RelayPin as an output pin
relayPin = Pin(5, Pin.OUT) 

while True:
    # Turns on and off the relaypin at intervals of 3 seconds
    relayPin.value(not relayPin.value())
    sleep(3000)
```

![](https://i.imgur.com/ExQyuu5.jpg)

```python=
import network
import config
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient


class HomeAutomation:

    def __init__(self, ledpin: int, lightpin: int, ssid: str,
                 password: str, host: str, port: int, topic: str):
        """

        :param ledpin:
        :param lightpin:
        :param ssid:
        :param password:
        :param host:
        :param port:
        :param topic:
        """
        self.ledpin = Pin(ledpin, Pin.OUT)
        self.lightpin = Pin(lightpin, Pin.OUT)
        self.ssid = ssid
        self.password = password
        self.host = host
        self.port = port
        self.topic = topic

    def boardTest(self):
        """
        Testing the board by blinking LED
        :return:
        """
        print("INFO: Blinking LED")
        for i in range(0, 5, 1):
            self.ledpin.value(not self.ledpin.value())
            sleep(1)
            i = i + 1
        print("INFO: Board is fine")

    def turn_on(self):
        """
        Turns on the lights
        :return:
        """
        self.lightpin.value(1)
        print("INFO: Turning on lights")

    def turn_off(self):
        """
        Turns off the lights
        :return:
        """
        self.lightpin.value(0)
        print("INFO: Turning off lights")

    def wifiConnect(self):
        """
        Connects to the config wifi
        :return:
        """
        print("INFO: Connecting to wifi")
        station = network.WLAN(network.STA_IF)  # create station interface
        station.active(True)  # activate the interface
        if station.isconnected():
            print("INFO: Connected to wifi initially")
        else:
            while True:
                try:
                    scanned_wifi = station.scan()  # scan for access points
                    for i in scanned_wifi:
                        if i[0].decode('utf-8') == self.ssid:
                            # Connect to wifi
                            station.connect(self.ssid, self.password)
                            print("INFO: Connected to wifi")
                            break
                        else:
                            print("INFO: Wifi Not found")
                            self.wifiConnect()
                    break
                except OSError as e:
                    print("Error: ", e)

    def on_message(self, topic, msg):
        """
        This callback is used to process messages
        that are published to a subscribed topic.
        :param topic:
        :param msg:
        :return:
        """
        message = msg.decode("utf-8")
        if message == "ON":
            self.turn_on()
        elif message == "OFF":
            self.turn_off()

    def main(self):
        """
        Main function runs the board test, connects to wifi and mqtt server
        and finally waits for oncoming messages
        :return:
        """
        self.boardTest()
        self.wifiConnect()
        print("INFO: Connecting to MQTT")
        client = MQTTClient("umqtt_client", self.host, self.port)
        client.set_callback(self.on_message)
        client.connect()
        print("INFO: Connected to MQTT")
        client.subscribe(self.topic)
        while True:
            client.wait_msg()


def run():
    homeautomation = HomeAutomation(ledpin=2, lightpin=5,
                                    ssid=config.WIFI_ESSID,
                                    password=config.WIFI_PASSWORD,
                                    host=config.MQTT_HOST,
                                    port=config.MQTT_PORT,
                                    topic=config.MQTT_TOPIC)
    homeautomation.main()


if __name__ == "__main__":
    run()

```
## APPLICATIONS

* home automation
* farm or garden monitoring systems.

