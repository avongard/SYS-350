import getpass

passw= getpass.getpass()

from pyVim.connect import SmartConnect

import ssl

hostname = "vcenter.michael.local"
username = "michael-adm"

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si=SmartConnect(host=hostname, user=username, pwd=passw, sslContext=s)
content=si.RetrieveContent()

datacenter = si.content.rootFolder.childEntity[0] # Root folder of server and all inventory attached
vms = datacenter.vmFolder.childEntity # Folder in particular to look at
choice = input("What VM would you like to search for?:")
machine = []

for i in vms: # Loop through list of VM's
    machine.append(i.name)
    
if choice in machine:
    print(choice + " exists")
elif choice == "":
    print(machine)
else:
    print(choice + " does not exist.")
