
# automating-home-lights
A demonstration of using nodemcu connected to a solid state relay to switch on and off lights using google assistant

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/0x6f736f646f/automating-home-lights)
![Python package](https://github.com/0x6f736f646f/automating-home-lights/workflows/Python%20package/badge.svg?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/354b85bbab1b5c60ee52/maintainability)](https://codeclimate.com/github/0x6f736f646f/backend-blog-application/maintainability)
[![CodeFactor](https://www.codefactor.io/repository/github/0x6f736f646f/automating-home-lights/badge)](https://www.codefactor.io/repository/github/0x6f736f646f/automating-home-lights)
[![Build Status](https://travis-ci.com/0x6f736f646f/automating-home-lights.svg?branch=master)](https://travis-ci.com/0x6f736f646f/automating-home-lights)
[![Coverage Status](https://coveralls.io/repos/github/0x6f736f646f/automating-home-lights/badge.svg?branch=master)](https://coveralls.io/github/0x6f736f646f/automating-home-lights?branch=master)

## Prerequistes

#### Software
* [Docker](https://www.docker.com/)
* [Ngrok](https://ngrok.com/)
* [LocalXpose](https://localxpose.io/)
* [Make](https://www.gnu.org/software/make/)
* [Python3](https://www.python.org/)
* [Putty](https://putty.org/)
* [esptool](https://github.com/espressif/esptool)
* [ampy](https://github.com/scientifichackers/ampy)

#### Hardware
* [Nodemcu](https://store.nerokas.co.ke/index.php?route=product/product&product_id=1764&search=nodemcu&description=true)
* [Jumper wires](https://store.nerokas.co.ke/index.php?route=product/product&product_id=120&search=jumper+wires&description=true)
* [Solid state relay](https://store.nerokas.co.ke/index.php?route=product/product&product_id=1679&search=relay&description=true)
* [Power strip](https://www.amazon.com/GE-Outlet-Protector-Extension-14092/dp/B00DOMYL24/ref=sxin_9_ac_d_rm?ac_md=1-1-c3VyZ2UgcHJvdGVjdG9yIHBvd2VyIHN0cmlw-ac_d_rm&cv_ct_cx=extension+cable&dchild=1&keywords=extension+cable&pd_rd_i=B00DOMYL24&pd_rd_r=13edf795-4726-4731-b57b-f7a50b5aa0ee&pd_rd_w=clOKK&pd_rd_wg=I8lmf&pf_rd_p=7140382f-2020-43a7-a2a8-20d62e199d2c&pf_rd_r=9V2S23H0ZJX2B5C3QJ3Y&psc=1&qid=1593528577&sr=1-2-12d4272d-8adb-4121-8624-135149aa9081)
* [Lamp](https://www.amazon.com/Limelights-LT2024-GRY-Brushed-Charging-Outlet/dp/B075Z643G4/ref=sxin_9_ac_d_rm?ac_md=0-0-bGFtcA%3D%3D-ac_d_rm&cv_ct_cx=lamp&dchild=1&keywords=lamp&pd_rd_i=B075Z643G4&pd_rd_r=7f4912db-809b-48fc-abbd-8a21e0827c56&pd_rd_w=zc3Lo&pd_rd_wg=mTBoM&pf_rd_p=dc697a3c-c4bf-4bf1-bf88-86b22dd0aad3&pf_rd_r=4AQD4QVQE9VAX33T1Z0F&psc=1&qid=1593528538&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081)

## Getting started
To get this project up and running on your machine, follow the following instructions.

#### Dialogflow
Check out the [wiki](https://github.com/0x6f736f646f/automating-home-lights/wiki) to get yourself up and running with the dialogflow agent

#### Hardware
Check out the [wiki](https://github.com/0x6f736f646f/automating-home-lights/wiki) to setup the hardware

#### Micropython
Check out the [wiki](https://github.com/0x6f736f646f/automating-home-lights/wiki) to setup micropython

#### Programming
This instructions will be different for windows users.

```shell
mkdir projectHomeAutomation
cd projectHomeAutomation
virtualenv --no-site-packages --python=python3 venv
source venv/bin/activate
git clone https://github.com/0x6f736f646f/automating-home-lights
cd automating-home-lights
pip3 install -r requirements.txt
```

## Contributing
Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/0x6f736f646f/automating-home-lights/blob/master/LICENSE) file for details

## Acknowledgments
- [PythonKe](https://www.meetup.com/Python-Nairobi/)
- [AI Saturday Kenya](https://www.meetup.com/AI-Saturdays-Nairobi/)
