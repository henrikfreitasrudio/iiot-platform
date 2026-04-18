import time, json, random
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("mosquitto", 1883)

while True:
    data = {
        "device": "sim_esp32",
        "temperature": 25 + (time.time() % 5),
        "pressure": 60 + (time.time() % 10),
        "timestamp": time.time()
    }
    client.publish("sensors/data", json.dumps(data))
    print("Sent: ", data, flush=True)
    time.sleep(2)
