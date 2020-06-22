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

all: erase flash upload