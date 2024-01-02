import time
import sys
import pymodbus

from pymodbus.client import ModbusTcpClient as ModbusClient


client = ModbusClient("10.0.0.128", port=502)
client.connect()

while True:
	client.write_coil(address=0, value=True, unit=1)
	print("sensor off")
    
