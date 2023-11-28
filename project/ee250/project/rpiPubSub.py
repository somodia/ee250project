  GNU nano 3.2                          rpiPubSub.py                                     

"""EE 250L Lab 04 Starter Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""
""" Team: Alexandra Somodi, Victoria Nunez
GitHub Link: https://github.com/somodia/ee250project
"""
import paho.mqtt.client as mqtt
import time
import sys
sys.path.append('../../Software/Python/')
sys.path.append('../../Software/Python/grove_rgb_lcd')
import grovepi

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("asomodi/sound")
    client.subscribe("asomodi/ultrasonic")
    client.subscribe("asomodi/buzzer")
    client.subscribe("asomodi/led")
    client.subscribe("asomodi/baby_mood")
    client.subscribe("asomodi/baby_location")
    client.message_callback_add("asomodi/led",custom_callback)
    #client.message_callback_add("asomodi/lcd",custom_callback_lcd)
    client.message_callback_add("asomodi/buzzer", custom_callback_buzz)

    #modifications
    client.message_callback_add("asomodi/buzzer_command", buzzer_command_callback)

#modifications
# Define a callback for the buzzer command
def buzzer_command_callback(client, userdata, message):
    if message.payload.decode() == "BUZZER_ON":
        # Code to turn on the buzzer
        grovepi.digitalWrite(buzzer, 1)

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py  
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect 
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60) #connect to broker
    client.loop_start()

    #set pins and stuff!
    buzzer = 8 #D8
    led = 3 #D3
    sound = 0 # A0
    ultrasonicPort = 4 #D4

    grovepi.pinMode(buzzer, "OUTPUT")
    grovepi.pinMode(led, "OUTPUT")
    grovepi.pinMode(sound, "INPUT")
    
 while True:
        time.sleep(1) # poll and publish every half second
        range_value = grovepi.ultrasonicRead(ultrasonicPort)
        sound_value = grovepi.analogRead(sound)
        client.publish("asomodi/sound",str(sound_value).encode())
        client.publish("asomodi/ultrasonic", str(range_value).encode())


