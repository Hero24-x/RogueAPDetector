def extract_features(packet):
    """
    Extract features from a beacon frame for ML prediction.
    Example features: SSID length, MAC vendor prefix, signal strength.
    """
    ssid = packet.info.decode(errors='ignore') if packet.info else ""
    ssid_length = len(ssid)

    mac = packet.addr2 if hasattr(packet, 'addr2') else ""
    mac_prefix = mac[:8].replace(":", "") if mac else ""

    signal = getattr(packet, 'dBm_AntSignal', -100)  # Default to very weak

    features = {
        "ssid_length": ssid_length,
        "mac_prefix": mac_prefix,
        "signal": signal,
    }

    # Convert features dict to list/array depending on ML model requirements
    # For example, return as list:
    return [features["ssid_length"], features["signal"]]
