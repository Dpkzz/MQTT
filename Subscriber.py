import paho.mqtt.client as mqtt
#enable mosquitto command - sudo systemctl status mosquitto.service

# Callback function for when a message is received from the server
def on_message(client, userdata, msg):
    print(f"Received message: '{msg.payload.decode()}' on topic '{msg.topic}' with QoS {msg.qos}")

# Create an MQTT client instance
client = mqtt.Client("rpi_client_subscriber")  # This name should be unique

# Assign the on_message callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect('127.0.0.1', 1883)

# Start the network loop
client.loop_start()

# Subscribe to the topic 'rpi/broadcast'
client.subscribe('rpi/broadcast')

print("Subscriber is running and waiting for messages...")

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Subscriber interrupted and stopped.")
finally:
    client.loop_stop()
    client.disconnect()
