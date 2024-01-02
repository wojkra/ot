import time
import sys
import pymodbus

from pymodbus.client import ModbusTcpClient as ModbusClient


client = ModbusClient("10.0.0.128", port=502)
client.connect()

while True:
    print("Coils:    ", client.read_coils(0,8, unit=1).bits)
    print("Discrete: ", client.read_discrete_inputs(0,8, unit=1).bits)
    print("Holding:  ", client.read_holding_registers(0, 8, unit=1).registers)
    print("Input:    ", client.read_input_registers(0,8, unit=1).registers)
    time.sleep(1)
