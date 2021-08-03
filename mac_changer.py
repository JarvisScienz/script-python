import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parse.error("[-] Please specify an interface. Use --help for more info.")
	elif not options.newMac:
		parse.error("[-] Please specify a MAC address. Use --help for more info.")
	return options


def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "wh", "ehter", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] Could not read MAC address")

options = get_arguments()

current_mac = get_current_mac(options.interface)

#change_mac(options.interface, options.newMac)

current_mac = get_current_mac(options.interface)

if current_mac == options.newMac:
	print("[+] MAC address is correctly changed.")
else:
	print("[-] MAC address is not correctly changed.")
