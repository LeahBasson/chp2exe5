radius = input("Enter radius:")

#Diameter
diameter = 2*float(radius)
d_message = "Diameter of sphere:"

print(d_message, diameter)

#Circumference
import math
circumference = 2*math.pi*float(radius)
c_message = "Circumference of sphere:"

print(c_message, circumference)

#Surface Area
area = 4*math.pi*(float(radius)**2)
a_message = "Surface area of sphere:"

print(a_message, area)

#Volume of sphere
volume = 4/3*math.pi*(float(radius)**3)
v_message = "Volume of sphere:"

print(v_message, volume)
