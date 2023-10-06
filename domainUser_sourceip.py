import getpass
import socket

passw= getpass.getpass()

from pyVim.connect import SmartConnect

import ssl

host = "vcenter"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
domain = ".michael.local"
username = "michael-adm"
host_domain = host + domain
user = getpass.getuser()

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si=SmartConnect(host=host_domain, user=username, pwd=passw, sslContext=s)

IP = socket.gethostbyname(hostname)

print("Domain/Username = " + domain + "/" + user)
print("Source IP = " + IPAddr)