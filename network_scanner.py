import scapy.all as scapy
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="IP address/mask")
	(options, arguments) = parser.parse_args()
	if not options.target:
		parse.error("[-] Please specify a target. Use --help for more info.")
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

	clients_list = []
	for element in answered_list:
		client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(client_dict)
		return clients_list
	#print(answered.summary())
	#print(arp_request_broadcast.summary())
	#arp_request_broadcast.show()

def print_result(results_list):
	print("IP\t\t\tMAC Address\t\t\t\n----------------------------------")
	for client in results_list:
		print(client["ip"] + "\t\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target) #"192.168.1.1/24"
print_result(scan_result)
