import scapy.all as scapy
import optparse

def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-r","--range",dest="ip_address",help=" Enter ip address")
    (user_input,arguments)=parse_object.parse_args()
    if not user_input.ip_address:
        print("Please enter ip address")
    return user_input


def scan_my_network(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    brodcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether)
    combined_packet=brodcast_packet/arp_request_packet
    # 2 tane isteği birleştirmemiz için gerekli kullanım
    (answered,unanswered)=scapy.srp(combined_packet,timeout=1)
    #  biz srp komutunda hem cevap veren hem vermeyenleri görücez bu yüzden
    #  timeout = bulunamayan iplerde beklemeden devam et
    answered.summary()

user_ip_addres=get_user_input()
scan_my_network(user_ip_addres.ip_address)
