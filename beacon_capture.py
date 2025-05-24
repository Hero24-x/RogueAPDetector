from scapy.all import sniff, Dot11Beacon

def capture_beacons(interface="wlan0mon"):
    """
    Generator function to capture Wi-Fi beacon frames.
    Requires Wi-Fi adapter in monitor mode (default interface wlan0mon).
    """
    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            yield pkt

    # Using sniff with a filter to capture beacons only
    return sniff(iface=interface, prn=lambda x: x if x.haslayer(Dot11Beacon) else None, store=0)
  
