import pyshark
import json_converter as jc
def capture_packet(pkt):
    jc.capture_pack(pkt)

capture = pyshark.LiveCapture(interface='wifi')
capture.apply_on_packets(capture_packet)
capture.sniff()
capture.close()