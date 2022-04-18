"""
A simple converter for length, square and temperature units.
"""
# input of data
print(
    "What do you like to convert?\nType \"l\" for length(metric system), \"s\" for square(metric system), "
    "\"t\" for temperature")
a = str(input())

if a == "l":
    print("Please, enter a value")
    l_value = int(input())
    print("Type a unit you would like to convert from: mm cm dm m km")
    unit_in = str(input())

    print("Type a unit you would like to convert to: mm cm dm m km")
    unit_out = str(input())


    def convert_length(l_value, unit_in, unit_out):
        length = {'mm': 0.001, 'cm': 0.01, 'dm': 0.1, 'm': 1.0, 'km': 1000}
        print(f"{l_value}{unit_in} is {l_value * length[unit_in] / length[unit_out]}{unit_out}")


    convert_length(l_value, unit_in, unit_out)

elif a == "s":
    print("Please, enter a value")
    s_value = int(input())
    print("Type a unit you would like to convert from: mm^2 cm^2 dm^2 m^2 a ha km^2")
    unit_in = str(input())
    print("Type a unit you would like to convert to: mm^2 cm^2 dm^2 m^2 a ha km^2")
    unit_out = str(input())


    def convert_length(s_value, unit_in, unit_out):
        square = {'mm^2': 0.000001, 'cm^2': 0.0001, 'dm^2': 0.01, 'm^2': 1.0, 'a': 100, 'ha': 10000, 'km^2': 1000000}
        print(f"{s_value}{unit_in} is {s_value * square[unit_in] / square[unit_out]}{unit_out}")


    convert_length(s_value, unit_in, unit_out)

elif a == "t":
    print("Please, enter a value")
    t_value = int(input())
    print("Type a unit you would like to convert from: C K F")
    unit_in = str(input())

    def convert_temperature(t_value, unit_in):
        if unit_in == 'C':
            print(f"{t_value}°{unit_in} is {t_value+273.15}K and {t_value*9/5+32}°F")
        elif unit_in == 'K':
            print(f"{t_value}{unit_in} is {t_value-273.15}°C and {(t_value-273.15)*9/5+32}°F")
        elif unit_in == 'F':
            print(f"{t_value}°{unit_in} is {(t_value-32)*5/9}°C and {(t_value-32)*5/9+273.15}K")

    convert_temperature(t_value, unit_in)

else:
    print("Sorry, we can convert only length, square and temperature units")
