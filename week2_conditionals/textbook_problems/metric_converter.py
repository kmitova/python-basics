number = float(input())
initial_unit = input(). lower()
converted_unit = input(). lower()

if initial_unit == "m":
    if converted_unit == "mm":
        number = number * 1000
        print(number)
    elif converted_unit == "cm":
        number = number * 100
        print(number)
    elif converted_unit == "km":
        number = number / 1000
        print(number)
    elif converted_unit == "mi":
        number = number * 0.000621371192
        print(number)
    elif converted_unit == "in":
        number = number * 39.3700787
        print(number)
    elif converted_unit == "ft":
        number = number * 3.2808399
        print(number)
    else:  # yd
        number = number * 1.0936133
        print(number)


if initial_unit == "mm":
    if converted_unit == "m":
        number = number / 1000
        print(number)
    elif converted_unit == "cm":
        number = number / 10
        print(number)
    elif converted_unit == "km":
        number = number * 0.000001
        print(number)
    elif converted_unit == "mi":
        number = number * 6.2137119223733E-7
        print(number)
    elif converted_unit == "in":
        number = number * 0.0393701
        print(number)
    elif converted_unit == "ft":
        number = number * 0.00328084
        print(number)
    else:  # yd
        number = number * 0.00109361
        print(number)


if initial_unit == "cm":
    if converted_unit == "m":
        number = number * 0.01
        print(number)
    elif converted_unit == "mm":
        number = number * 10
        print(number)
    elif converted_unit == "km":
        number = number / 100000
        print(number)
    elif converted_unit == "mi":
        number = number * 6.21371e-6
        print(number)
    elif converted_unit == "in":
        number = number * 0.393701
        print(number)
    elif converted_unit == "ft":
        number = number * 0.0328084
        print(number)
    else:  # yd
        number = number * 0.0109361
        print(number)

if initial_unit == "km":
    if converted_unit == "m":
        number = number / 1000
        print(number)
    elif converted_unit == "mm":
        number = number / 1000000
        print(number)
    elif converted_unit == "cm":
        number = number / 100000
        print(number)
    elif converted_unit == "mi":
        number = number * 0.621371
        print(number)
    elif converted_unit == "in":
        number = number * 39370.07874
        print(number)
    elif converted_unit == "ft":
        number = number * 3280.84
        print(number)
    else:  # yd
        number = number * 1093.61
        print(number)


if initial_unit == "in":
    pass  # code is similar to the above
if initial_unit == "ft":
    pass  # code is similar to the above
if initial_unit == "yd":
    pass  # code is similar to the above
if initial_unit == "mi":
    pass  # code is similar to the above
