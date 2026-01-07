# ⚙️ Industrial IoT Monitoring System (Backend)

> Backend core for a **multi-sensor Industrial IoT system**, built to monitor devices and sensors in **real time**.

---

## 📌 Overview

This is the backend core of my multi-sensor project, designed for the real-time monitoring of industrial devices and sensors. Its primary objective is to collect data from edge devices and transmit it to the frontend through secure APIs.

---

## 🧠 Key Technical Features

###  Django Framework  
The entire backend logic is built on the Django framework, chosen for its scalability and security.

###  IoT Data Models  
Specialized models have been created for **Devices**, **Sensors**, **Data (Value/Timestamp)**, and **Alerts**.

###  Real-time Data Handling  
Optimized database fields are utilized to efficiently handle float data (e.g., temperature, power usage) received from sensors.

###  Automated Alerts  
The system includes a mechanism to set thresholds and automatically generate alerts when critical conditions are detected.

###  Secure Authentication  
Token-based security has been implemented for user login and dashboard access.

###  Debug & Logs  
A DebugLog model has been integrated to perform system health checks and facilitate easier troubleshooting.

---

## 🧰 Tech Stack

| Component | Technology |
|---------|------------|
|  Language | Python |
|  Backend | Django / Django REST Framework |
|  Database | MySQL (or database of choice) |
|  Protocol | MQTT (for sensor data ingestion) |

---
## 🛢 Databse Relationships

**Format: One -> Many:**

    Device -> Sensors  
    Sensor -> Data  
    Sensor -> Alerts  
    Device -> Debug Logs  

**Relationships are based on:**

> One Device has many Sensors.  
> One Sensor has many Data points.  
> One Sensor generates many Alerts.  
> Debugs track overall system.

---

✨ *Built with scalability, security, and real-time performance in mind.*
