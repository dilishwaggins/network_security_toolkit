from scapy.all import sniff
import logging
from datetime import datetime

# Configure logging
log_filename = "traffic_analyzer.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def packet_callback(packet):
    """Callback function to process each captured packet."""
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        src_ip = packet["IP"].src if packet.haslayer("IP") else "Unknown"
        dst_ip = packet["IP"].dst if packet.haslayer("IP") else "Unknown"
        protocol = packet["IP"].proto if packet.haslayer("IP") else "Unknown"
        
        log_entry = f"{timestamp} - Src: {src_ip}, Dst: {dst_ip}, Protocol: {protocol}"
        logging.info(log_entry)
        
        print(log_entry)  # Optional: Display in real-time
    except Exception as e:
        logging.error(f"Error processing packet: {e}")


def start_sniffing(interface="eth0", packet_count=0):
    """Start capturing network traffic."""
    print("Starting traffic analysis...")
    sniff(iface=interface, prn=packet_callback, store=False, count=packet_count)
    

if __name__ == "__main__":
    try:
        start_sniffing()
    except KeyboardInterrupt:
        print("Traffic analysis stopped.")
