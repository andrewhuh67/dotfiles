import json
import os
import sys
import time

import build
from pprint import pprint

from wrappers import digitalocean


def spin_up():
	timestamp_utc = time.time()
	writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
	aws_lightsail = ['awsl', 'aws lightsail']
	digital_ocean = ['do', 'digitalocean']
	iaas_platform = aws_lightsail + digital_ocean
	vendor_choice = 'do'
	if vendor_choice in iaas_platform:
		if vendor_choice in aws_lightsail:
			pass

		elif vendor_choice in digital_ocean:
			os.system('{unix_command} > {writeout_file}'		\
				.format(unix_command=build.create_digital_ocean_vps(),	\
						writeout_file=writeout_file))
			time.sleep(60)
			return harden(writeout_file)

	else:
		pass


def harden(writeout_file):
	response = json.load(open(writeout_file))
	
	payloads = []
	if 'droplets' in response:
		payloads = response['droplets']
	else:
		payloads = [response['droplet']]
	ip_addresses = []
	for payload in payloads:
		ip_addresses.append(build.get_host(payload['id'], writeout_file))

	return ip_addresses
	# y = response['droplet']['id']
	# timestamp_utc = #
	# c = digitalocean.get_ip_addresses(y, timestamp_utc)

if __name__ == '__main__':
	pprint(spin_up())




