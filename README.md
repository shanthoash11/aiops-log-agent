\# AIOps Log Monitoring Agent



\## Project Overview

This project works to demonstrate a simple AI-driven AIOps agent that monitors system logs, detects abnormal behavior, and triggers automated responses.



The system simulates how AI can help IT operations teams by identifying certain issues early and taking automated actions.



\# How the System Works



The agent follows a basic pipeline:



Observe -> Detect -> Decide -> Act



1\. Observe

&nbsp;  - The agent reads logs from `runs/app.log`.



2\. Detect

&nbsp;  - An anomaly detection method monitors spikes in errors and warnings.



3\. Decide

&nbsp;  - A policy module determines the appropriate action.



4\. Act

&nbsp;  - The executor simulates automated actions to help and improve the situation.



\# File Descriptions



1. generate\_logs.py

Simulates system logs by generating normal activity along with warning and error spikes to simlate system incidents.



2\. agent.py 

Main controller that reads logs, runs anomaly detection, applies decision logic, and executes automated actions.



3\. detector.py 

Implements a statistical anomaly detection method using a rolling window approach.



4\. policy.py

Contains decision rules that determine what action should be taken based on detected anomalies.



5\. executor.py 

Simulates automated actions such as restarting services or scaling system resources.





