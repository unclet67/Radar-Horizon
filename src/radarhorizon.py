#Radar Horizon

import math
from time import sleep


# Radar_Horizon = Square Root of Lightfish antenna height + square root of target * 1.23

T = int(input("Enter target radar height:")) 
L = math.sqrt(3.6)
result = math.sqrt(T) + L * 1.23
print("Radar Horizon of target is",round(result),"NM")  
sleep(5)

