                                                                    

import snap7
from time import sleep
from snap7.util import *
import struct
#S7AreaPE = 0x81 S7AreaPA = 0x82 S7AreaMK = 0x83 S7AreaDB = 0x84 S7AreaCT = 0x1C S7AreaTM = 0x1D

plc = snap7.client.Client()
plc.connect("192.168.77.1",0,1)
area = 0x83    # area for Q memory
start = 0      # location we are going to start the read
length = 1     # length in bytes of the read
bit = 0        # which bit in the Q memory byte we are reading


mbyte = plc.read_area(snap7.types.Areas.MK,0,start,length)
print(mbyte)
print ("M0.0:",get_bool(mbyte,0,bit))

plc.disconnect()
















