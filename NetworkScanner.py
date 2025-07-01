import scapy.all as scapy
import optparse

# Kullanıcıdan IP adresi girişi almak için fonksiyon
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address",
                            help="Enter IP Address (e.g. 192.168.1.1/24)")  # Örnek aralık verildi

    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("[-] Please enter an IP address using -i or --ipaddress")
        exit()  # IP girilmediyse programı sonlandır

    return user_input

# Ağda ARP taraması yapan fonksiyon
def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)  # Hedef IP'ye ARP isteği
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast: tüm ağdaki cihazlara gönder
    combined_packet = broadcast_packet / arp_request_packet  # İki paketi birleştir

    # Cevap veren ve vermeyen cihazları listele (verbose=False ile sessiz çalışır)
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1, verbose=False)

    print("\nIP\t\t\tMAC Address\n" + "-"*40)
    for answer in answered_list:
        print(answer[1].psrc + "\t\t" + answer[1].hwsrc)  # IP ve MAC adresini yazdır

# Program akışı başlatılır
user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)
