#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(intf):
    print(f"Sniffing on interface {intf}")
    scapy.sniff(iface=intf, store=False, prn=process)

def process(packet):
    print(packet.content)
    #if packet.haslayer(http.HTTPRequest):
     #   url = packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
      #  print(f"[+] HTTP Request URL: {url}")
        
       # if packet.haslayer(scapy.Raw):
        #    load = packet[scapy.Raw].load.decode(errors="ignore")
         #   print(f"[+] Request Payload:\n{load}\n")
    
    #if packet.haslayer(http.HTTPResponse):
     #   print(f"[+] HTTP Response")
      #  if packet.haslayer(scapy.Raw):
       #     load = packet[scapy.Raw].load.decode(errors="ignore")
        #    print(f"[+] Response Payload:\n{load}\n")

sniff("eth0")
