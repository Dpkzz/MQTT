# MQTT Communication (Publisher & Subscriber)

This project demonstrates MQTT communication using the `paho-mqtt` library on Raspberry Pi.  
It consists of:  

- **Subscriber (`mqtt_subscriber.py`)**: Listens for messages on the `rpi/broadcast` topic.  
- **Publisher (`mqtt_publisher.py`)**: Sends messages to the `rpi/broadcast` topic.  

## **Setup & Installation**  

1. Install `paho-mqtt`:  
   ```bash
   pip install paho-mqtt
   
## Running the Scripts
1) Start the MQTT broker (e.g., Mosquitto):
sudo systemctl start mosquitto.service

3) Start the Subscriber:
python mqtt_subscriber.py

4) Start the Publisher:
python mqtt_publisher.py

## Expected Output
Received message: 'DEEPAK RAJ' on topic 'rpi/broadcast' with QoS 0
