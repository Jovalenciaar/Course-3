set_a = {'Col', 'Arg', 'Chi'}
set_b = {'Bol', 'Pe',}

#  Suma de conjuntos usamos el simbolo |, O usamos  .union() set_c = set_a + set_b
set_c = set_a.union(set_b)
set_c = set_a | set_b
print(set_c)

#  Para la interseccion usamos el simbolo & o el comando .intersection()
set_c = set_a.intersection(set_b)
set_c = set_a & set_b
print(set_c)

#  Diferencia, para esta usamos el comando .difference() o el simobolo -
set_c = set_a - set_b
set_c = set_a.difference(set_b)
print(set_c)