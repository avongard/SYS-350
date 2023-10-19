import getpass
import pdb

passw= getpass.getpass()

from pyVim.connect import SmartConnect
from pyVmomi import vim

import ssl

hostname = "vcenter.michael.local"
username = "michael-adm"

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si=SmartConnect(host=hostname, user=username, pwd=passw, sslContext=s)
content=si.RetrieveContent()

datacenter = si.content.rootFolder.childEntity[0] # Root folder of server and all inventory attached
vms = datacenter.vmFolder.childEntity # Folder in particular to look at
vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
machine = vm_view.view
vm_info = {}

for vm in machine:
    if vm.summary.guest is not None:
        ip_address = vm.summary.guest.ipAddress
        power_state = vm.summary.runtime.powerState
        cpu = vm.summary.config.numCpu
        memory_mb = vm.summary.config.memorySizeMB
        memory_gb = memory_mb * .001
        vm_info[vm.name] = ip_address
        print("Name: " + vm.name)
        print("IP: " + str(ip_address))
        print("Power State: " + str(power_state))
        print("CPUs: " + str(cpu))
        print("Memory: " + str(memory_gb) + " GB")
        print("")