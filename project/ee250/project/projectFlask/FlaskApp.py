from flask import Flask, render_template
import threading
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Global variable to store the baby's status
baby_status = "Loading..."

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("asomodi/baby_status")

def on_message(client, userdata, msg):
    global baby_status
    baby_status = msg.payload.decode()

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
    return render_template('ee250finalprojv1.html', status=baby_status)

@app.route('/activate_buzzer')
def activate_buzzer():
    # Publish message to the MQTT topic to turn on the buzzer
    client.publish("asomodi/buzzer_command", "BUZZER_ON")
    return render_template('ee250finalprojv1.html', status=baby_status)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
