import getpass

passw= getpass.getpass()

from pyVim.connect import SmartConnect

import ssl

hostname = "vcenter.michael.local"
username = "michael-adm"

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
connect=SmartConnect(host=hostname, user=username, pwd=passw, sslContext=s)

datacenter = connect.content.rootFolder.childEntity[0]
vms = datacenter.vmFolder.childEntity
for i in vms:
    print(i.name)