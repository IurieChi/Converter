#Distance converter 

print("""Select type of conversion:
'1' From Km to Miles
'2' From Miles to Km 
'3' From Foot to Meter
'4' From Inch to Centimeter""")
conver = int(input())

# while conver !=1 or conver !=2:
#     print('Select 1 or 2 ')

if conver == 1:
        kilometers = float(input("Type Km = "))
        kilometers_to_miles = kilometers * 0.621
        print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles\n")
        #break
elif conver == 2:
        miles = float(input("Type Miles = "))
        miles_to_kilometers = miles * 1.609
        print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers\n")
        #break
elif conver == 3:
        foot = float(input("Type Foot = "))
        foot_to_meter = foot * 0.3048
        print(foot, "foot is", round(foot_to_meter, 2), "meters\n")
elif conver == 4:
        inch = float(input("Type Inch = "))
        inch_to_centimeter = inch * 2.54
        print(inch, "inch is", round(inch_to_centimeter, 2), "centimeters\n")