
#!/bin/python3

from pyModbusTCP.client import ModbusClient
from time import sleep
client = ModbusClient(host="192.168.77.2", port=502)
client.open()
while (True):
    #client = ModbusClient(host="192.168.5.100", port=502)      
    #client.open()
    a = client.read_holding_registers(0)
    print(a)
    client.write_single_register(10, 300)
    sleep(2)
    client.write_single_register(10, 10)
    sleep(2)
client.close()
print("Zamykamy")
''' Jesli chdozi o adam to aby zminic stan na wyjsciach analogowych nalzy uzyc 10 lub 11 i komende write_single_register( rejestr, wartos)'''
'''single_write_coil odnosi sie do wyjsc cyfrowych ( rejestr 16 i 17) aby odczytac wartosc na wyjsciach cyfrowych nalezy uzyc komendy read_discret_input'''







