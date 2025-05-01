import math
from fractions import Fraction
a=int(input("Enter your Angle  "))
radian=math.radians(a)
c=input("Enter your Trignometric Function ")
if c.lower() in["sin","sine"] or c.capitalize() in ["SIN","SINE"]:
    print(f"Sin{a} is equal to : {math.sin(radian)}",f" or {Fraction(math.sin(radian)).limit_denominator()}")
elif c.lower() in["cos","cose"] or c.capitalize() in ["COS","COSE"]:
    print(f"Cos{a} is equal to : {math.cos(radian)}",f" or {Fraction(math.cos(radian)).limit_denominator()}")
elif c.lower() in["tan","tangent"] or c.capitalize() in ["TAN","TANGENT"]:
    print(f"Tan{a} is equal to : {math.tan(radian)}",f" or {Fraction(math.tan(radian)).limit_denominator()}")    
else :
    print("Invalid Argument")