# # Manera clasica
countries = ['Colombia', "Mexico", "Venezuela", 'Peru', 'Ecuador']
population = ['45000', '40000', '35000', '42000', '43000']

for countries, population in zip(countries, population):
    if population >= str(40000):
        print(countries, str(population))



# Diccionary comprehension con condicional
countries = ['Colombia', "Mexico", "Venezuela", 'Peru', 'Ecuador']
population = ['45000', '40000', '35000', '42000', '43000']

result = {countries: population for (countries, population) in zip(countries, population) 
            if population >= str(40000)}
print(result)

# text = "Hola como estas, espero que muy bien"

# unique = {c: str(c+c) for c in text if c in "aeiou"}
# print(unique)