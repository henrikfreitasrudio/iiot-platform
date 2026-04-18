import time, json, random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mosquitto", 1883)

while True:
    data = {
        "device": "esp32_01",
        "temperature": random.uniform(20,30),
        "pressure": random.uniform(1, 2)
    }
    client.publish("sensors/data", json.dumps(data))
    print(data)
    time.sleep(2)
