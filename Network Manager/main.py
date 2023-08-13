import collections

import matplotlib.pyplot as plt
import numpy as np
import pyshark

# cap1 = pyshark.FileCapture('second_data.pcap')
# cap2 = pyshark.FileCapture('third.pcap')
# cap3 = pyshark.FileCapture('fourth.pcap')
cap4 = pyshark.FileCapture('first_data.pcap')
cap = []
# cap.extend(cap1)
# cap.extend(cap2)
# cap.extend(cap3)
cap.extend(cap4)

protocol_list = []
for packet in cap:
    line = str(packet)
    formattedLine = line.split(" ")
    protocol_list.append(formattedLine[4])
counter = collections.Counter(protocol_list)

plt.style.use('ggplot')
y_pos = np.arange(len(list(counter.keys())))
plt.bar(y_pos, list(counter.values()), align='center', alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])
plt.xticks(y_pos, list(counter.keys()))
plt.show()

