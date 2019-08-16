def fahrenheit_converter(C):
    fahrenheit = C * 9/5 +32
    print( str(fahrenheit) + "`F")
C2F = fahrenheit_converter(35)

def g_to_kg(g):
    kg = g / 1000
    print ( str(kg) + "kg" )

weight = g_to_kg(300)
weight2 = g_to_kg(10000)

import math
def long_side(s1,s2):
    third_sid = math.sqrt(  s1**2 + s2**2 )
    print("The right triangle third side's length is " + str(third_sid))

long_side(3,4)

def bian(s1,s2):
    third_side = (s1**2 + s2**2 )**0.5
    print("The right triangle third side's length is {}".format(third_side) )

bian(3,4)