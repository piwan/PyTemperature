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

print(Temperature(0) + Temperature(10))
print(Temperature(20) - Temperature(10))
print(Temperature(5) * 2)
print(Temperature(5) * Temperature(2))
print(Temperature(20) / 2)
print(Temperature(20) / Temperature(2))
print(abs(Temperature(-10)))
