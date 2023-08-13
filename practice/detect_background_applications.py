import wmi
import pyshark

fp = open('test.txt', 'w')


def packet_sniffer():
    capture = pyshark.LiveCapture(interface='wifi')
    capture.sniff(packet_count=10)  # Capture 10 packets, adjust as needed
    
    for packet in capture:
        # Filter packets based on destination IP address
        fp.write(str(packet))
        if 'ip' in packet and packet.ip.dst == '192.168.0.1':
            print(packet)


def get_running_applications_windows():
    c = wmi.WMI()
    processes = c.Win32_Process()
    running_applications = []
    
    for process in processes:
        fp.write(str(process.Name)+"\n")
        running_applications.append(process.Name)
        packet_sniffer()
    
    return running_applications

running_apps = get_running_applications_windows()
print(running_apps)

print('\n')