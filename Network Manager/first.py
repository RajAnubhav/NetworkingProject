import pyshark


def capture_protocols(pcap_file):
    # Open the pcap file for reading
    capture = pyshark.FileCapture(pcap_file)

    # Initialize an empty list to store the protocols
    protocols = []

    # Iterate over each packet in the capture
    for packet in capture:
        # Check if the packet has a 'Protocol' field
        if 'Protocol' in packet:
            protocol = packet['Protocol'].showname

            # Add the protocol to the list if it's not already present
            if protocol not in protocols:
                protocols.append(protocol)

    # Close the capture file
    capture.close()

    return protocols


# Example usage
pcap_file = 'first_data.pcap'
protocol_list = capture_protocols(pcap_file)

# Print the captured protocols
for protocol in protocol_list:
    print(protocol)
