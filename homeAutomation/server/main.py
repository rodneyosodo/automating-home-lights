from flask import Flask, request
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="broker.env")

broker_url = os.getenv("MQTT_HOST")
broker_port = int(os.getenv("MQTT_PORT"))
mqtt_topic = os.getenv("MQTT_TOPIC")

client = mqtt.Client()
client.connect(broker_url, broker_port)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def publish():
    if request.method == "GET":
        return "Hello world"
    elif request.method == "POST":
        global client
        command = request.get_json()['queryResult']['queryText']
        if command.__contains__("on"):
            client.publish(topic=mqtt_topic, payload="ON", qos=0, retain=True)
            return {
                "payload": {
                    "google": {
                        "expectUserResponse": True,
                        "richResponse": {
                            "items": [
                                {
                                    "simpleResponse": {
                                        "textToSpeech": "The lights are on"
                                        }
                                }
                            ]
                        }
                    }
                }
            }
        else:
            client.publish(topic=mqtt_topic, payload="OFF", qos=0, retain=True)
            return {
                "payload": {
                    "google": {
                        "expectUserResponse": True,
                        "richResponse": {
                            "items": [
                                {
                                    "simpleResponse": {
                                        "textToSpeech": "The lights are off"
                                        }
                                }
                            ]
                        }
                    }
                }
            }


if __name__ == "__main__":
    app.run()
