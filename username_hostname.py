import getpass

passw= getpass.getpass()

from pyVim.connect import SmartConnect

import ssl

hostname = "vcenter.michael.local"
username = "michael-adm"

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si=SmartConnect(host=hostname, user=username, pwd=passw, sslContext=s)

print("Hostname = " + hostname)
print("Username = " + username)


