#### Getting started with micropython

1. Download micropython from the official website preferably `esp8266-20170108-v1.8.7.bin`
2. Copy it into the homeAutomation/nodemcu folder
3. Rename the exampleConfig.py to config.py
4. Run 
```shell
make start-mqtt
```
To start mqtt server as a docker container and also start ngrok which exposes the mqtt services
5. Get the url from ngrok. It should look something like this

6. From the ngrok url go to config.py replace the MQTT_HOST to be '2.tcp.ngrok.io'
Replace also the MQTT_PORT to be 14262 add an MQTT_TOPIC.
7. Add your wifi password and essid to the config file
8. The config file you be looking like this at the end
```
MQTT_HOST = '2.tcp.ngrok.io'
MQTT_PORT = 14262
MQTT_TOPIC = 'Lights'
WIFI_ESSID = 'qwerty'
WIFI_PASSWORD = 'qwertyuio8'
```
9. Flash the micropython binary file and upload your code with the following command
```shell=
make all
```
10. Go to putty select connection type to be serial and speed to be 115200. The serial line should be the port your nodemcu is connected. For my case it was at /dev/ttyUSB0
It should look like this

11. Run the following code to start the program

You should see your led blinking. Make sure your wifi is okay and you have started the mqtt server
