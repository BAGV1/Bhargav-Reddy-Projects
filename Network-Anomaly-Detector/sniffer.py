"""
Scapy lets Python listen to traffic
flowing through the network card
"""
from scapy.all import sniff
from analyzer import calculate_anomalies
from reporter import create_report
from database import save_anomaly


size_data = []
time_data = []

def process_packet(packet):
    packet_size = len(packet)
    size_data.append(packet_size)
    time_data.append(packet.time)

sniff(prn=process_packet, count=200)


size_scores, time_scores = calculate_anomalies(size_data, time_data)
final_report = create_report(size_data[1:], size_scores, time_scores)

# We only want reports on anomalies as they are noteworthy
if not final_report.empty:
    print("!! ALERT: Anomaly Detected!\n", final_report)
    final_report.to_excel('Network_Anomaly.xlsx', index=False)
    save_anomaly(final_report)

else:
    print("The traffic is normal.")
