#Distance converter 

print("""Select type of conversion:
'1' From kilometer to miles
'2' From miles to Km 
'3' From mile to yard
'4' From mile to foot 
'5' From foot to meter
'6' From feet and inches to meter
'7' From meter to foot
'8' From yard to foot
'9' From inch to centimeter
'10' From inch to millimetre
'11' Pounds to Kg""")
conver = int(input())


if conver == 1:
        kilometers = float(input("Type Km = "))
        kilometers_to_miles = kilometers * 0.621
        print(kilometers, "kilometer is", round(kilometers_to_miles, 2), "mile\n")
elif conver == 2:
        miles = float(input("Type Mile = "))
        miles_to_kilometers = miles * 1.609
        print(miles, "mile is", round(miles_to_kilometers, 2), "kilometer\n")
elif conver == 3:
        miles = float(input("Type Mile = "))
        miles_to_yard = miles * 1760
        print(miles, "mile is", round(miles_to_yard, 2), "yard\n")
elif conver == 4:
        miles = float(input("Type Mile = "))
        miles_to_foot = miles * 5280
        print(miles, "mile is", round(miles_to_foot, 2), "foot\n")
elif conver == 5:
        foot = float(input("Type Foot = "))
        foot_to_meter = foot * 0.3048
        print(foot, "foot is", round(foot_to_meter, 2), "meter\n")
elif conver ==6:
        ft=float(input("Type Foot = "))
        inch =float(input("Type inch = "))
        print(f'{ft} foot and {inch} inch is, {round(ft * 0.3048 + inch * 0.0254, 2)}, meter\n')
elif conver == 7:
        meter = float(input("Type Meter = "))
        meter_to_foot = meter * 3.28084 
        print(meter, "meter is", round(meter_to_foot, 2), "foot\n")
elif conver == 8:
        yard = float(input("Type Yard = "))
        yard_to_foot = yard * 3
        print(yard, "yard is", round(yard_to_foot, 2), "foot\n")
elif conver == 9:
        inch = float(input("Type Inch = "))
        inch_to_centimeter = inch * 2.54
        print(inch, "inch is", round(inch_to_centimeter, 2), "centimeters\n")
elif conver == 10:
        inch = float(input("Type Inch = "))
        inch_to_millimetre = inch * 25.4
        print(inch, "inch is", round(inch_to_millimetre, 2), "millimetre\n")
elif conver == 11:
        pound = float(input("Type pound = "))
        print(pound, "pounds is", round(pound * 0.45359237, 2), "kg\n")