set_countries = {'Col', 'Mex', 'Bol'}

# .lem() sirve para conocer el numero de elementos
size = len(set_countries)
print(size)

print('Col' in set_countries)

# .add() sierve para agregar un solo elemento el conjutno
set_countries.add('Per')
print(set_countries)

# update() sirve apara agragar mas de 1 elemento en una sola linea, En este caso usamos
    # los corchetes por que estamos usando un conjunto
set_countries.update({'Arg', 'Chi', 'Ven'})
print(set_countries)

# remove() sirve para remover elementos del conjunto
set_countries.remove("Col")
print(set_countries)

# clear() sirve para elmiminar todo del conjunto
set_countries.clear()
print(set_countries)