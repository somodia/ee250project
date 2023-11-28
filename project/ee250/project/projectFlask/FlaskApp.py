from flask import Flask, render_template, request, redirect, url_for
import threading
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Global variable to store the baby's status
baby_mood = "Loading..."
baby_location = "Loading..."

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("asomodi/baby_mood")
    client.subscribe("asomodi/baby_location")

def on_message(client, userdata, msg):
    global baby_location, baby_mood
    if msg.topic == "asomodi/baby_mood":
        baby_mood = msg.payload.decode()
    elif msg.topic == "asomodi/baby_location":
        baby_location = msg.payload.decode()

# MQTT Client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

# Start the MQTT client in a separate thread
mqtt_thread = threading.Thread(target=client.loop_forever)
mqtt_thread.start()

@app.route('/')
def index():
    return render_template('ee250finalproj.html', mood_status=baby_mood, location_status = baby_location)

@app.route('/set_baby_emotion', methods=['POST'])
def set_baby_emotion():
    global baby_status
    status = request.form['status']
    if status == 'calm':
        baby_status = 'Baby is Calm'
    elif status == 'crying':
        baby_status = 'Baby is Crying'
    # Publish the new status to MQTT, handle as needed
    # client.publish("your_topic_here", baby_status)
    return redirect(url_for('index'))

@app.route('/set_baby_proximity', methods=['POST'])
def set_baby_proximity():
    global baby_status
    status = request.form['status']
    if status == 'ran_away':
        baby_status = 'Baby Ran Away'
    elif status == 'close':
        baby_status = 'Baby is Close'
    # Publish the new status to MQTT, handle as needed
    # client.publish("your_topic_here", baby_status)
    return redirect(url_for('index'))

@app.route('/activate_buzzer', methods=['POST'])
def activate_buzzer():
    # Publish message to the MQTT topic to turn on the buzzer
    client.publish("asomodi/buzzer_command", "BUZZER_ON")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
