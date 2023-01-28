# Task 3
import math
# from degree to radian
def deg_to_rad(angle):
	return angle*math.pi/180.0
# printing
for i in range(0,91):
	star_pos = int(math.sin(deg_to_rad(i)) * 79.0)
	print (" " * star_pos + "*")
