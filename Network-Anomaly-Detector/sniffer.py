"""
Scapy lets Python listen to traffic
flowing through the network card
"""
from scapy.all import sniff
from analyzer import calculate_anomalies
from reporter import create_report

size_data = []

def process_packet(packet):
    packet_size = len(packet)
    size_data.append(packet_size)

sniff(prn=process_packet, count=200)


calculated_scores = calculate_anomalies(size_data)
final_report = create_report(size_data, calculated_scores)

# We only want reports on anomalies as they are noteworthy
if not final_report.empty:
    print("!! ALERT: Anomaly Detected!\n", final_report)
    final_report.to_csv('Network_Anomaly.csv')

else:
    print("The traffic is normal.")
