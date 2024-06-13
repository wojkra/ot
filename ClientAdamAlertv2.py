#!/bin/python3

from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host="192.168.77.2", port=502)

if client.open():
    print("Połączenie nawiązane")
else:
    print("Nie udało się nawiązać połączenia")
    exit(1)

try:
    while True:
        success = client.write_single_register(10, 1800)
        if success:
            print("Zapisano wartość 1800 do rejestru 10")
        else:
            print("Błąd zapisu do rejestru")
        sleep(4)
finally:
    client.close()
    print("Połączenie zamknięte")
