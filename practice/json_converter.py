import pyshark
import json
from flask import Flask, jsonify
fp = open('packetData.json', 'w')
main_body = {}
it = 0
packets = []
def capture_pack(pkt):
    packets.append(pkt)

    layers = pkt.layers
    layers_as_dict = {}
    for i in range(len(layers)):
        layer_attr = dir(layers[i])
        layer_i_as_dict = {}
        for attr in layer_attr:
            if attr != '':
                if str(eval(f"layers[{i}].{attr}"))[0]!='<':
                    layer_i_as_dict[attr]=eval(f"layers[{i}].{attr}")
        layers_as_dict[str(i)]=layer_i_as_dict

    global main_body,it
    main_body[str(it)]=layers_as_dict
    it+=1

    

    if len(packets) == 2 :
        json.dump(main_body, fp)
        fp.close()
        exit(0)
capture = pyshark.LiveCapture(interface='wifi')
capture.apply_on_packets(capture_pack)
capture.sniff(timeout=1)
capture.close()