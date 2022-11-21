# Manera clasica de utilizar un ciclo FOR
numbers = []
for element in range (1, 11):
    numbers.append(element *2)

print(numbers)

# List Comprehension
numbers_2 = [element * 2 for element in range (1, 11)]
print(numbers_2)

# Manera clasica pero con una condicion
numbers_3 = []
for element in range (1, 51) :
    if element % 2 == 0:
        numbers_3.append(element)

print(numbers_3)

# Lis comprehension con condicion
number_4 =[element for element in range (1,51) if element % 2 == 0]
print(number_4)