#!/usr/bin/env python3

import os
import re

path_to_token = input("Path to token: ")
with open('{token}'.format(token=input('Path to token: ')), 'r') as f:
    token = f.read().rsplit()[0]
#print(token)
#token = path_to_token

scheme       = 'https'
authority = 'api.digitalocean.com'
path = '/v2/droplets'
endpoint     = '{scheme}://{authority}{path}'.format(
                    scheme=scheme, authority=authority, 
                    path=path
                )



data = 'sata'
#token = 'smoken'

# FIXME - Format the following string
create_droplet_command = "curl -X POST -d \'{data}\'                            \
                            -H \"Authentication: Bearer {token}\"               \
                            -H \"Content-Type: application/json\"               \
                            \"{endpoint}\"".format(data=data,                   \
                                token=token,                                    \
                                endpoint=re.sub(' +' , ' ', endpoint))

create_droplet_command = re.sub(' +', ' ', create_droplet_command)

print(create_droplet_command)
#print(create_droplet_command)

# Then, we need to wait for the droplet to be created
# os.system()
# Then, we need to get the IP address of the droplet that we created
# os.system()
# Finally, we need to get the IP address of the droplet that we created (host).
#host = 
#os.system('ssh -o "StrictHostKeyChecking no" root@{host}                        \
#            \'bash -s\' < dotfiles/run.sh'.format(host=host)')
#os.system()
