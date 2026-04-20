import json
from datetime import datetime
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision

# Conexão Influx
client_influx = InfluxDBClient(
    url="http://influxdb:8086",
    token="token123",
    org="iiot"
)

write_api = client_influx.write_api()

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT", reason_code)
    client.subscribe("sensors/data")
    
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received: ", data, flush=True)
    
    device = data.get("device_id" or data.get("device") or "unknown")
    point = (
        Point("sensor_data")
        .tag("device", data["device"])
        .field("temperature", float(data["temperature"]))
        .field("pressure", float(data["pressure"]))
        # .time(datetime.utcnow(), WritePrecision.NS)
    )
    
    write_api.write(bucket="iiot", org="iiot", record=point)
    
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("mosquitto", 1883)
client.loop_forever()
