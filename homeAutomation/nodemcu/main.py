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
