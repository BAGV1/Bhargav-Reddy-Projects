# Network Anomaly Detector

## Project Purpose
The purpose of this project was to create a simple network anomaly detector utilizing Python. The Scapy library was used to let Python listen to network traffic, NumPy was used to calculate Z-Scores in order to distinguish abnormal traffic from regular traffic, and Pandas was used to properly display the data in a DataFrame in order to properly export the anomaly-generated sheets into a .csv format.

## Statistical Logic & Scalability
By utilizing Z-Scores, we are able to scale the project to to suit the needs of the person using it, small or large, so that we don't get caught up in the mindset of the large amount of packet movement being flagged as a Direct Denial-of-Service (DDoS) attack. We take the absolute value of the Z-Score and check for numbers larger than 2.50, as that is considered an extreme threshold for Z-Scores.

## Data Flow & Architecture
<img width="900" height="1100" alt="Network-Anomaly-Detector-DFD drawio (1)" src="https://github.com/user-attachments/assets/e2e00871-075d-4714-878d-4c0a21f02b9e" />

## Prerequisites & Installation
Ensure you have Python 3 installed on your system. Run the following command in your terminal to install all the required packages:

```bash
pip install scapy
pip install pandas
pip install numpy
pip install scipy
