import paho.mqtt.client as mqtt
import time
from pynput import keyboard

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here AKA everything i/o haha
    client.subscribe("asomodi/sound")
    client.subscribe("asomodi/buzzer")
    client.subscribe("asomodi/ultrasonic")
    client.subscribe("asomodi/led")

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':

    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.message_callback_add
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()

    while True:

        time.sleep(1)
