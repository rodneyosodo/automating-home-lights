ESP = esptool.py
EFLAG = --port /dev/ttyUSB0
AFLAG = $(EFLAG) --baud 115200 put
erase:
	$(ESP) $(EFLAG) erase_flash

flash: esp8266-20170108-v1.8.7.bin
	$(ESP) $(EFLAG) --baud 460800 write_flash --flash_size=detect 0 $<

upload: main.py config.py
	sleep 5
	ampy $(AFLAG) config.py
	ampy $(AFLAG) main.py

start-docker:
	docker run --rm --name=mqtt -d -p 1883:1883 -p 9001:9001 eclipse-mosquitto

stop-docker:
	docker stop mqtt

start-ngrok:
	sleep 5
	ngrok tcp 1883

all: erase flash upload
start-mqtt: start-docker start-ngrok