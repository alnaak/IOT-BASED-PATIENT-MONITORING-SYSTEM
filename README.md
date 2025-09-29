# IoT-Based Patient Monitoring System

## Project Overview
This project is a **comprehensive patient monitoring system** that combines multiple sensing modalities to track a patient’s vital signs and immediate physical reactions:

1. **ECG Monitoring** – Captures heart activity using an ECG sensor.  
2. **Temperature Monitoring** – Measures body/object temperature using an MLX90614 infrared sensor.  
3. **Facial Expression Detection** – Detects gasping or abnormal mouth opening in real-time via a webcam and OpenCV.

The system integrates **Arduino** for sensor readings and **Python** for facial monitoring, providing a versatile platform for healthcare monitoring.

---

## Components

### Hardware
- Arduino UNO / ESP32  
- ECG Sensor (analog output)  
- Adafruit MLX90614 Temperature Sensor  
- USB Camera / Webcam  
- Jumper wires  
- Power supply  

### Software & Libraries
- Arduino IDE  
  - Wire.h  
  - Adafruit_MLX90614.h  
  - WiFi.h (if sending data online)  
- Python 3.x  
  - OpenCV (`cv2`)  
  - NumPy (`numpy`)  

---

## Features
- Real-time **ECG monitoring** via serial output.  
- Real-time **temperature monitoring** with object/body temperature readings.  
- **Gasping detection** via webcam using facial landmarks approximation.  
- Potential integration with **WiFi** for cloud or remote monitoring.  
- Visual feedback on the screen for facial expressions.  

---

## Circuit Connections

### ECG + Temperature Sensor (Arduino)
- ECG sensor → Analog pin `A0`  
- MLX90614 → I2C pins (SDA, SCL)  
- Power → 5V and GND  

### Webcam (Python)
- Connect a standard USB webcam to the PC running the Python script  
