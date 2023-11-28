"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""
""" Team: Alexandra Somodi, Victoria Nunez
"""
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to necessary topics & add custom callbacks
    client.subscribe("asomodi/ultrasonic", 1)
    client.subscribe("asomodi/sound", 1)
    client.subscribe("asomodi/led", 1)
    client.subscribe("asomodi/buzzer", 1)
    client.subscribe("asomodi/baby_mood", 1)
    client.subscribe("asomodi/baby_location", 1)

    client.message_callback_add("asomodi/ultrasonic", custom_callback)
    client.message_callback_add("asomodi/sound", custom_callback_sound)
    
#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg): 
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def custom_callback(client, userdata, message):
    print("VM: " + str(message.payload, "utf-8") + "cm")
    ultrasonicReading = message.payload.decode("utf-8")
    ultrasonicReading = int(ultrasonicReading)

    if (ultrasonicReading < 20): # baby is near, led off
        client.publish("asomodi/led", "LED_OFF")
        client.publish("asomodi/baby_location", "Baby is close")
    if (ultrasonicReading >= 20): # baby is far, led on
        client.publish("asomodi/led", "LED_ON")
        client.publish("asomodi/baby_location", "Baby ran away")
    
def custom_callback_sound(client, userdata, message):
    print("VM: " + str(message.payload, "utf-8") + "sound")
    soundReading = message.payload.decode("utf-8")
    soundReading = int(soundReading)
    if (soundReading < 400):
        client.publish("asomodi/buzzer", "BUZZER_OFF")
        client.publish("asomodi/baby_mood", "Baby is calm")
    if (soundReading >= 400):
        client.publish("asomodi/buzzer", "BUZZER_ON")
        client.publish("asomodi/baby_mood", "Baby is crying")

    
if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client() 
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()

    while True:
        print("", end="")
        time.sleep(1)        
