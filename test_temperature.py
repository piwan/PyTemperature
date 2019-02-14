from temperature import Temperature, AbsoluteZeroError

t1 = Temperature(0)
print(t1.celsius)
print(t1.fahrenheit)

t1.fahrenheit = 59
print(t1.celsius)
print(t1.fahrenheit)

try:
    t1.celsius = -274
except AbsoluteZeroError as error:
    print(error)

t1 = Temperature(0)
print(t1 == Temperature(0))
print(t1 != Temperature(100))
print(t1 < Temperature(100))
print(t1 > Temperature(-100))
print(t1 >= Temperature(0))
