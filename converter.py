"""
A simple converter.
"""
# choosing units
print(
    """
What do you like to convert?
Type:
\"l\" for length(metric system)
\"s\" for square(metric system)
\"tem\" for temperature
\"t\" for time
\"m\" for mass
\"d\" for data
\"v\" for volume
\"sp\" for speed
    """)

a = str(input())

# length

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
    
# square

elif a == "s":
    print("Please, enter a value")
    s_value = int(input())
    print("Type a unit you would like to convert from: mm2 cm2 dm2 m2 a ha km2")
    unit_in = str(input())
    print("Type a unit you would like to convert to: mm2 cm2 dm2 m2 a ha km2")
    unit_out = str(input())


    def convert_square(s_value, unit_in, unit_out):
        square = {'mm2': 0.000001, 'cm2': 0.0001, 'dm2': 0.01, 'm2': 1.0, 'a': 100, 'ha': 10000, 'km2': 1000000}
        print(f"{s_value}{unit_in} is {s_value * square[unit_in] / square[unit_out]}{unit_out}")


    convert_square(s_value, unit_in, unit_out)
    
# temperature

elif a == "tem":
    print("Please, enter a value")
    tem_value = int(input())
    print("Type a unit you would like to convert from: C K F")
    unit_in = str(input())


    def convert_temperature(tem_value, unit_in):
        if unit_in == 'C' or unit_in == 'c':
            print(f"{tem_value}°{unit_in} is {tem_value + 273.15}K and {tem_value * 9 / 5 + 32}°F")
        elif unit_in == 'K' or unit_in == 'k':
            print(f"{tem_value}{unit_in} is {tem_value - 273.15}°C and {(tem_value - 273.15) * 9 / 5 + 32}°F")
        elif unit_in == 'F' or unit_in == 'f':
            print(f"{tem_value}°{unit_in} is {(tem_value - 32) * 5 / 9}°C and {(tem_value - 32) * 5 / 9 + 273.15}K")


    convert_temperature(tem_value, unit_in)
    
# time

elif a == "t":
    print("Please, enter a value")
    t_value = int(input())
    print("Type a unit you would like to convert from: ms s min h d")
    unit_in = str(input())
    print("Type a unit you would like to convert to: ms s min h d")
    unit_out = str(input())


    def convert_time(t_value, unit_in, unit_out):
        time = {'ms': 0.001, 's': 1, 'min': 60, 'h': 3600, 'd': 86400}
        print(f"{t_value} {unit_in} is {t_value * time[unit_in] / time[unit_out]} {unit_out}")


    convert_time(t_value, unit_in, unit_out)

# mass

elif a == "m":
    print("Please, enter a value")
    m_value = int(input())
    print("Type a unit you would like to convert from: mg g oz lb kg t")
    unit_in = str(input())
    print("Type a unit you would like to convert to: mg g oz lb kg t")
    unit_out = str(input())


    def convert_mass(m_value, unit_in, unit_out):
        mass = {'mg': 0.001, 'g': 1, 'oz': 28.35, 'lb': 453.59, 'kg': 1000, 't': 1000000}
        print(f"{m_value} {unit_in} is {m_value * mass[unit_in] / mass[unit_out]} {unit_out}")


    convert_mass(m_value, unit_in, unit_out)

# data

elif a == "d":
    print("Please, enter a value")
    d_value = int(input())
    print("Type a unit you would like to convert from: b B KB MB GB ")
    unit_in = str(input())
    print("Type a unit you would like to convert to: b B KB MB GB ")
    unit_out = str(input())


    def convert_data(d_value, unit_in, unit_out):
        data = {'b': 1 / 8, 'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
        print(f"{d_value} {unit_in} is {d_value * data[unit_in] / data[unit_out]} {unit_out}")


    convert_data(d_value, unit_in, unit_out)

# volume

elif a == "v":
    print("Please, enter a value")
    v_value = int(input())
    print("Type a unit you would like to convert from: mm3 cm3 l m3 ")
    unit_in = str(input())
    print("Type a unit you would like to convert to: mm3 cm3 l m3 ")
    unit_out = str(input())


    def convert_volume(v_value, unit_in, unit_out):
        volume = {'mm3': 0.001, 'cm3': 1, 'l': 1000, 'm3': 1000000}
        print(f"{v_value} {unit_in} is {v_value * volume[unit_in] / volume[unit_out]} {unit_out}")


    convert_volume(v_value, unit_in, unit_out)

# speed

elif a == "sp":
    print("Please, enter a value")
    sp_value = int(input())
    print("Type a unit you would like to convert from: m/s km/h kn ")
    unit_in = str(input())
    print("Type a unit you would like to convert to: m/s km/h kn ")
    unit_out = str(input())


    def convert_speed(sp_value, unit_in, unit_out):
        speed = {'m/s': 1, 'km/h': 3.6, 'kn': 1.944}
        print(f"{sp_value} {unit_in} is {sp_value * speed[unit_in] / speed[unit_out]} {unit_out}")


    convert_speed(sp_value, unit_in, unit_out)
    
else:
    print("Wrong unit")
