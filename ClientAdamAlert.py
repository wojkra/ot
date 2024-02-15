  GNU nano 2.9.8                 ClientAdamAlert.py                             

#!/bin/python3

from pyModbusTCP.client import ModbusClient
from time import sleep
client = ModbusClient(host="192.168.77.2", port=502)
client.open()
while (True):
    #client = ModbusClient(host="192.168.5.100", port=502)      
    #client.open()
    client.write_single_register(10, 1800)
    sleep(4)
client.close()

print("Zamykamy")
''' Jesli chdozi o adam to aby zminic stan na wyjsciach analogowych nalzy uzyc $
'''single_write_coil odnosi sie do wyjsc cyfrowych ( rejestr 16 i 17) aby odczy$


