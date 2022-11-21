# Manera Clasica diccionary
countries= {'Colombia': 45000,
            'Venezuela': 35000,
           'Argentina': 30000,}

for key, value in countries.items():
    print(key , str(value))


# # Diccionary comprehension 
countries= {'Colombia': 45000,'Venezuela': 35000,'Argentina': 30000}

general = {key: value *1000 for(key, value) in countries.items()}
print(general)


# # # Manera clasica de Diccionary comprehension,
# # # En este caso tenemos que identificar el valor de cada llave(Key) como i
dict = {}
for i in range (1,6):
    dict[i] = i *2

print (dict)

# # # # Diccionary comprehension
dict_2 = {i : i * 2 for i in range (1,6)}
print(dict_2)


# # # Zip nos sirve para unir dos listas y combertirlas en una, para que nos arroge una lista
# # debemos color -- lits(zip())
countries = ['Colombia', "Mexico", "Venezuela"]
population = ["45000", '40000', '35000']

print(list(zip(countries, population)))


# # # Diccionary comprehension con dos listas
pais = ['Colombia', 'Venezuela', 'Peru']
poblacion = [45000, 30000, 40000]

total = {pais: poblacion for (pais, poblacion) in zip(pais, poblacion)}
print(total)

