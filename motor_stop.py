
#!/bin/python3
import snap7
from snap7.util import *
import struct

#S7AreaPE = 0x81 S7AreaPA = 0x82 S7AreaMK = 0x83 S7AreaDB = 0x84 S7AreaCT = 0x1C S7AreaTM = 0x1D



plc = snap7.client.Client()
plc.connect("192.168.77.1",0,1)
area = 0x83    # area for Q memory
start = 0      # location we are going to start the read
length = 1     # length in bytes of the read
bit = 0        # which bit in the Q memory byte we are reading

data=bytearray(b'\x00')

plc.write_area(snap7.types.Areas.MK,1,0,data)
print("Lampka czerwona")
#plc.as_write_area(area,0,start,length,data, )
#data=plc.ab_write(area,data)
#print(type(data))
#data_read=plc.ab_read(area,length)
#print(data_read)
plc.disconnect()

