import psutil
import signal_strength as ss
def get_process_network_connections():
    connections = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name']:
                pid = proc.info['pid']
                name = proc.info['name']
                connections.extend(psutil.net_connections(kind='inet'))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return connections

# Example usage
network_connections = get_process_network_connections()
for conn in network_connections:
    print(f"Process ID: {conn.pid}, Process Name: {psutil.Process(conn.pid).name()}, Local Address: {conn.laddr}, Remote Address: {conn.raddr}, Status: {conn.status}, Signal Strength: {ss.get_signal_strength(psutil.Process(conn.pid).name())}")
