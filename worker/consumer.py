import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT", reason_code)
    client.subscribe("sensors/data")
    
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received: ", data, flush=True)
    
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("mosquitto", 1883)
client.loop_forever()
