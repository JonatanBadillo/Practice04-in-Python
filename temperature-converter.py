'''
Write a program that asks for degrees centigrade to convert, and prints the equivalence in Kelvin and Farenheit
K = 273 + C
F = 1,8*C + 32
'''

centigrades = int(input("Give me the °C to convert: "))
K = 273 + centigrades
F = 1.8 * centigrades + 32

print("f{centigrades}°C are equivalent to: " )
print(f"{K}K and {F}°F")