from itertools import product
from tabulate import tabulate
from store import Store

def union(X, Y):
	result = []
	for x in X:
		result.append(x)
	for y in Y:
		result.append(y)
	return result

variables = ['K','S','C','T']
formulas = []

def f1(store):
	K,S = store['K', 'S']
	return not K or S
f1.name = 'K->S'
formulas.append(f1)

def f2(store):
	K,C,T = store['K', 'C', 'T']
	return K == (C and T)
f2.name = 'K<->C^T'
formulas.append(f2)

def p(s):
	result = ' ^ '.join( [f'{k} ' if v else f'¬{k}' for k,v in s.values.items()] )

	return result

good_ones = [s for s in Store.generateValues(variables) if all(f(s) for f in formulas)]
for s in good_ones:
	print( p(s) )