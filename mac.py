import subprocess

addresses = subprocess.check_output(['arp', '-a'])

#print(str(addresses))

addressess= addresses.decode('utf-8')

print(addressess)
print("List of MAC Addresses on the Network : -")
i = 1
for mac in addressess.split():
    if mac.count('-') == 5:
        print(str(i) + ". ", end= " ")
        print(mac)
        i = i + 1
