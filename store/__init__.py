from itertools import product
values = {False, True}

def cart(X, n):
	l = []
	for i in range(n):
		l.append(X)
	return product(*l)

class Store:
	def __init__(self, variables = []):
		self.variables = variables
		self.values = dict()

	def __repr__(self):
		return f'Store({str(self)})'
		
	def __str__(self):
		return self.values.__str__()

	def _get_single_item(self, k):
		return self.values[k]

	def __getitem__(self, k):
		if type(k) == tuple:
			return (self._get_single_item(_) for _ in k)
		else:
			return self._get_single_item(k)
	
	def __setitem__(self, k, v):
		self.values[k] = v
	
	def symbols(self):
		return self.variables
	
	def populate(self, symbols, values):
		for s,v in zip(symbols, values):
			self[s] = v

	def generateValues(variables):
		result = []
		vals = cart(values, len(variables))
		vals = list(vals)
		for p in vals:
			store = Store(variables)
			store.populate(variables, p)
			result.append(store)
		return result