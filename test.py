from unittest import TestCase, main
from store import *
class TestStore(TestCase):
	def testBindValue(self):
		store = Store()
		store['A'] = 2
		assert 2 == store['A']

	def testGetMultipleValues(self):
		store = Store()
		store['A'] = 2
		store['B'] = 3
		A,B = store['A', 'B']
		assert 2 == A
		assert 3 == B


	def testGetSymbols(self):
		store = Store(['A', 'B'])
		assert store.symbols() == ['A', 'B']

	def testPopulate(self):
		store = Store(['A', 'B'])
		store.populate(['A','B'], [2,3])
		self.assertEqual(store['A'], 2)
		self.assertEqual(store['B'], 3)


	def testGenerateValues(self):
		values = Store.generateValues(['A','B'])
		self.assertEqual(len(values), 4)
		self.assertEqual(type(values[0]['A']), bool)
		self.assertEqual(values[0]['A'] == False, values[0]['B'] == False)
		self.assertEqual(values[1]['A'] == False, values[1]['B'] == True)
		self.assertEqual(values[2]['A'] == True, values[2]['B'] == False)
		self.assertEqual(values[3]['A'] == True, values[3]['B'] == True)

if __name__ == '__main__':
	main()