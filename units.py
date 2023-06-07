Length = {
    "Nanometer": 1,
    "Micrometer": 1000,
    "Millimeter": 1000000,
    "Centimeter": 10**7,
    "Meter": 10**9,
    "Kilometer": 10**12,
    "Inch": 2.54 * (10**7),
    "Foot": 3.048 * (10**8),
    "Yard": 9.144 * (10**8),
    "Mile": 1.609 * (10**12),
    "Nautical Mile": 1.852 * (10**12)
}
Mass = {
    "Microgram": 1,
    "Milligram": 1000,
    "Gram": 10**6,
    "Kilogram": 10**9,
    "Metric Ton": 10**12,
    "Ounce": 2.835 * (10**7),
    "Pound": 4.536 * (10**8),
    "Stone": 6.35 * (10**9),
    "US Ton": 9.072 * (10**11),
    "Imperial Ton": 1.016 * (10**12)
}
Speed = {
    "Kilometer per hour": 1,
    "Meter per second": 3.6,
    "Foot per second": 1.09728,
    "Miles per hour": 1.60934,
    "Knot": 1.852
}
Time = {
    "Nanosecond": 1,
    "Microsecond": 1000,
    "Millisecond": 10**6,
    "Second": 10**9,
    "Minute": 6 * (10**10),
    "Hour": 3.6 * (10**12),
    "Day": 8.64 * (10**13),
    "Week": 6.048 * (10**14),
    "Month": 2.628 * (10**15),
    "Year": 3.154 * (10**16),
    "Decade": 3.154 * (10**17),
    "Century": 3.154 * (10**18)
}
Temperature = {"Kelvin": 0, "Celsius": 0, "Fahrenheit": 0}

Frequency = {
    "Hertz": 1,
    "KiloHertz": 1000,
    "MegaHertz": 10**6,
    "Gigahertz": 10**9
}
Fuel_Economy = {
    "Miles per gallon(Imperial)": 1,
    "Miles per gallon": 1.20095,
    "Kilometer per liter": 2.82481,
    "Liter per 100 kilometers": 282.481
}
Plane_Angle = {
    "Second of arc": 1,
    "Degree": 3600,
    "Gradian": 3240,
    "Milliradian": 206.265,
    "Minute of arc": 60,
    "Radian": 206265
}
Pressure = {
    "Pascal": 1,
    "Atmosphere": 101325,
    "Bar": 100000,
    "Pound-force per square inch": 6894.76,
    "Torr": 133.322
}
Energy = {
    "Electronvolt": 1,
    "Joule": 6.242 * (10**18),
    "Kilojoule": 6.242 * (10**21),
    "Gram calorie": 2.611 * (10**19),
    "Kilocalorie": 2.611 * (10**22),
    "Watt hour": 2.247 * (10**22),
    "Kilowatt hour": 2.247 * (10**25),
    "British thermal unit": 6.585 * (10**21),
    "US therm": 6.584 * (10**26),
    "Foot-pound": 8.462 * (10**18)
}
Area = {
    "Square inch": 1,
    "Acre": 6.273 * (10**6),
    "Hectare": 1.55 * (10**7),
    "Square foot": 144,
    "Square yard": 1296,
    "Square mile": 4.014 * (10**9),
    "Square meter": 1550,
    "Square kilometer": 1.55 * (10**9)
}
Data_Transfer_Rate = {
    "Bit per second": 1,
    "Kilobit per second": 1000,
    "Kilobyte per second": 8000,
    "Kibibit per second": 1024,
    "Megabit per second": 10**6,
    "Megabyte per second": 8 * (10**6),
    "Mebibit per second": 1.049 * (10**6),
    "Gigabit per second": 10**9,
    "Gigabyte per second": 8 * (10**9),
    "Gibibit per second": 1.074 * (10**9),
    "Terabit per second": 10**12,
    "Terabyte per second": 8 * (10**12),
    "Tebibit per second": 1.1 * (10**12)
}
Volume = {
    "Milliliter": 1,
    "Liter": 1000,
    "Cubic meter": 10**6,
    "Cubic Inch": 16.3871,
    "Cubic foot": 28316.8,
    "Imperial teaspoon": 5.91939,
    "Imperial tablespoon": 17.7582,
    "Imperial fluid ounce": 28.4131,
    "Imperial cup": 284.131,
    "Imperial pint": 568.261,
    "Imperial quart": 1136.52,
    "Imperial gallon": 4546.09,
    "US teaspoon": 4.92892,
    "US tablespoon": 14.7868,
    "US fluid ounce": 29.5735,
    "US legal cup": 240,
    "US liquid pint": 473.176,
    "US liquid quart": 946.353,
    "US liquid gallon": 3785.41
}
Digital_Storage = {
    "Bit": 1,
    "Kilobit": 1000,
    "Kibibit": 1024,
    "Megabit": 10**6,
    "Mebibit": 1.049 * (10**6),
    "Gigabit": 10**9,
    "Gibibit": 1.074 * (10**9),
    "Terabit": 10 * 12,
    "Tebibit": 1.1 * (10 * 12),
    "Petabit": 10**15,
    "Pebibit": 1.126 * (10**15),
    "Byte": 8,
    "Kilobyte": 8000,
    "Kibibyte": 8192,
    "Megabyte": 8 * (10**6),
    "Mebibyte": 8.389 * (10**6),
    "Gigabyte": 8 * (10**9),
    "Gigibyte": 8.59 * (10**9),
    "Terabyte": 8 * (10**12),
    "Tebibyte": 8.796 * (10**12),
    "Petabyte": 8 * (10**15),
    "Pebibyte": 9.007 * (10**15)
}


def units(the_dictionary, value_before, before, after):
    if before == "Liter per 100 kilometers":
        formula = f"{282.481/the_dictionary[after]}/x"
        value_after = the_dictionary[before] / the_dictionary[
            after] / value_before
        conversion = {"formula": formula, "value_after": value_after}
    elif after == "Liter per 100 kilometers":
        formula = f"{282.481/the_dictionary[before]}/x"
        value_after = the_dictionary[after] / the_dictionary[
            before] / value_before
        conversion = {"formula": formula, "value_after": value_after}
    else:
        formula = the_dictionary[before] / the_dictionary[after]
        value_after = formula * value_before
        conversion = {"formula": formula, "value_after": value_after}
    return conversion


def temperature(value_before, before, after):
    if before == "Celsius":
        if after == "Kelvin":
            formula = "x + 273.15"
            value_after = value_before + 273.15
        else:
            formula = "x*(1.8) + 32"
            value_after = value_before * (1.8) + 32
    elif before == "Kelvin":
        if after == "Celsius":
            formula = "x - 273.15"
            value_after = value_before - 273.15
        else:
            formula = "(x-273.15) * (1.8) + 32"
            value_after = (value_before - 273.15) * (1.8) + 32
    elif before == "Fahrenheit":
        if after == "Celsius":
            formula = "(x-32) * 5/9 "
            value_after = (value_before - 32) * 5 / 9
        else:
            formula = "(x-32) * 5/9 + 273.15"
            value_after = (value_before - 32) * 5 / 9 + 273.15
    conversion = {"formula": formula, "value_after": value_after}
    return conversion


unit_kind = {
    "Area": Area,
    "Digital_Storage": Digital_Storage,
    "Fuel_Economy": Fuel_Economy,
    "Length": Length,
    "Mass": Mass,
    "Time": Time,
    "Speed": Speed,
    "Volume": Volume,
    "Data_Transfer_Rate": Data_Transfer_Rate,
    "Energy": Energy,
    "Pressure": Pressure,
    "Plane_Angle": Plane_Angle,
    "Temperature": Temperature
}

# unit_kind = [Area, Digial_Storage, Fuel_Economy, Length, Mass, Time, Speed, Volume, Data_Transfer_Rate, Energy, Pressure, Plane_Angle]
# units(Fuel_Economy, 4, "Liter per 100 kilometers", "Kilometer per liter")
# temperature(-40, "Celsius", "Fahrenheit")


def check_unit(a, b, c, d):
    if a == "" or b == "" or c == "" or d == "":
        return False
    else:
        return True