import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
    print("message published")

client = mqtt.Client("rpi_client2")  # This name should be unique
client.on_publish = on_publish
client.connect('127.0.0.1', 1883)
# Start a new thread
client.loop_start()

while True:
    try:
        msg = "DEEPAK RAJ "  # The data you want to send
        pubMsg = client.publish(
            topic='rpi/broadcast',
            payload=msg.encode('utf-8'),
            qos=0,
        )
        pubMsg.wait_for_publish()
        print(pubMsg.is_published())

    except Exception as e:
        print(e)
        
    time.sleep(2)
