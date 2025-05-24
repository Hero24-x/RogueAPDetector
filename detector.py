from .beacon_capture import capture_beacons
from .features import extract_features
from .model import MLModel
from .alerts import send_alert
import threading

class RogueAPDetector:
    def __init__(self):
        self.model = MLModel.load_model("model/rogue_ap_model.pkl")  # Model file path
        self.running = False

    def start_detection(self):
        self.running = True
        print("[*] Rogue AP Detection started... Press Ctrl+C to stop.")
        try:
            for packet in capture_beacons():
                if not self.running:
                    break
                features = extract_features(packet)
                prediction = self.model.predict(features)
                if prediction == "rogue":
                    ap_info = self.get_ap_info(packet)
                    send_alert(f"⚠️ Rogue AP detected: {ap_info}")
                    print(f"[!] Rogue AP detected: {ap_info}")
        except KeyboardInterrupt:
            self.stop_detection()

    def stop_detection(self):
        self.running = False
        print("[*] Rogue AP Detection stopped.")

    def get_ap_info(self, packet):
        ssid = packet.info.decode(errors='ignore') if packet.info else "Unknown SSID"
        mac = packet.addr2 if hasattr(packet, 'addr2') else "Unknown MAC"
        signal = getattr(packet, 'dBm_AntSignal', 'N/A')
        return f"SSID: {ssid}, MAC: {mac}, Signal: {signal}dBm"
