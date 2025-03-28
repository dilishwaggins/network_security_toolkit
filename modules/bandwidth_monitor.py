import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename='bandwidth_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def monitor_bandwidth(interval=1):
    """Monitors network bandwidth usage."""
    old_stats = psutil.net_io_counters()
    
    while True:
        time.sleep(interval)
        new_stats = psutil.net_io_counters()
        
        bytes_sent = new_stats.bytes_sent - old_stats.bytes_sent
        bytes_recv = new_stats.bytes_recv - old_stats.bytes_recv
        
        log_message = f"Sent: {bytes_sent / 1024:.2f} KB/s, Received: {bytes_recv / 1024:.2f} KB/s"
        print(log_message)
        logging.info(log_message)
        
        old_stats = new_stats  # Update stats

if __name__ == "__main__":
    try:
        print("Starting bandwidth monitor...")
        monitor_bandwidth()
    except KeyboardInterrupt:
        print("Monitoring stopped.")
