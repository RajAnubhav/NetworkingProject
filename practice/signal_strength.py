import subprocess
import re

def get_signal_strength(interface):
    command = "netsh wlan show interfaces name=" + interface
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    signal_strength = re.search(r"Signal\s+: (\d+)", output)
    
    if signal_strength:
        return int(signal_strength.group(1))
    else:
        return None

interface = "wifi"  # Replace with the name of your wireless interface
signal_strength = get_signal_strength(interface)

if signal_strength is not None:
    print(f"Signal Strength: {signal_strength}%")
else:
    print("Failed to retrieve signal strength.")
