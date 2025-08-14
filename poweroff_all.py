import paramiko
import os
import time
from passwordfile import password

print("Beginning poweroff seqence")

alpineIP = "10.0.0.10"
raspIP = "10.0.0.11"
LaptopIP = "10.0.0.18"

client1 = paramiko.SSHClient()
client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client3 = paramiko.SSHClient()
client3.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connecting to RaspBerryPI
try:
    print("Connecting to RaspberryPI")
    client1.connect(hostname=raspIP,port=22,username="martin",password=str(password))
    print("Issueing poweroff command")
    client1.exec_command("sudo poweroff")
    client1.close()
    print("RaspberryPI poweroff sucsessful")
    time.sleep(10)

except Exception as e:
    print(f"RaspberryPI connection failed: {e}")  

#Connecting to Alpine Server
try:
    print("Connecting to Alpine Linux")
    client2.connect(hostname=alpineIP,port=22,username="martin",password=str(password))
    print("Issueing poweroff command")
    client2.exec_command("sudo poweroff")
    client2.close()
    print("Alpine Linux poweroff sucsessful")

except Exception as e:
    print(f"Alpine Linux connection failed: {e}")  

#Connecting to Laptop
try:
    print("Connecting to Laptop")
    client3.connect(hostname=LaptopIP,port=22,username="martin",password=str(password))
    print("Issueing poweroff command")
    client3.exec_command("sudo poweroff")
    client3.close()
    print("Laptop poweroff sucsessful")

except Exception as e:
    print(f"Laptop connection failed: {e}")  

#Powering down Desktop
print("Powering down Desktop")
time.sleep(1)
os.system("shutdown -P")
