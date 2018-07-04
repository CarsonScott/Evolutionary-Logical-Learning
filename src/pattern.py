from tree import *

def nonempty(x):
	return x != None
def istrue(x):
	return x == True

class Pattern(Tree):
	def __init__(self, data):
		super().__init__(data)
		self.fitness = None
		self.operator = None
		self.contraints = []
		self.requirements = [True]
		self.phrase_types = [type]
		for i in range(1, len(self)):
			self.phrase_types.append(None)
			self.requirements.append(False)

	def get_required(self):
		required = []
		for i in range(len(self.requirements)):
			if self.requirements[i]:
				required.append(i)
		return required
	def get_score(self):
		score = sum(map(nonempty, self))
		total = sum(self.requirements)
		if total != 0: score /= total
		return score

	def update(self):
		self.fitness = self.get_score()
		return self.fitness
	def translate(self, data):
		output = []
		for i in range(len(self)):
			value = self[i]
			if isinstance(data, dict):
				if isinstance(value, str):
					if value in list(data.keys()):
						value = data[value]
			if isinstance(data, list): 
				if isinstance(value, int):
					if value < len(data):
						value = data[value]
			output.append(value)
		return output[0], output[1:]
	def compute(self, data):
		function, inputs = self.translate(data)
		for i in range(len(inputs)):
			if isinstance(inputs[i], Tree):
				inputs[i] = inputs[i].compute(data)
		return function(inputs)

memory = Dict({'sum':sum, 'a':1, 'b':2, 'c':4, 'd':3, 'e':1})
tree = Pattern(['sum', 'a', Pattern(['sum', 'b', 'c'])])

output = tree.compute(memory)
tree.display()

print(output)




# from template import addition, create, generate, express, ExpressionTree
# from Generator import *
# from Matrix import *
# from goodata import Dict
# from random import randrange as rr
# from lib.relations import *
# from math import tanh

# class Proposition:
# 	def __init__(self, data):
# 		self.data = data
# 		self.create()
# 	def create(self):
# 		data = self.data
# 		self.expression = None
# 		self.function = None
# 		if isinstance(data, str):
# 			self.expression = data
# 			self.function = generate(data)
# 		elif isinstance(data, Proposition):
# 			self.expression = express(data)
# 			self.function = data
# 		self.template = ExpressionTree(self.expression)
# 	def __call__(self, input):
# 		self.create()
# 		return self.function(input)

# class Pattern(list):
# 	def __init__(self, propositions=[]):
# 		for p in propositions:
# 			self.append(p)
# 	def __call__(self, X):
# 		Y = []
# 		for f in self:
# 			Y.append(f(X))
# 		return Y
# 	def size(self):
# 		return len(self)

# class System:
# 	def __init__(self):
# 		self.patterns = Dict()
# 		self.database = Dict()
# 		self.history = list()
# 		self.counter = 0
# 		symbols = ['matrix', 'size', 'union', 'intersection', 'compliment', 'equivalent', 'containment', 'disjoint']
# 		functions = [Matrix, len, union, intersection, compliment, equivalent, containment, disjoint]
# 		inputs = ['list', 'list', 'list', 'list', 'list', 'list', 'list', 'list']
# 		outputs = ['list', 'int', 'list', 'list', 'list', 'bool', 'bool', 'bool']
# 		for i in range(len(functions)):
# 			self.patterns[symbols[i]] = functions[i]
# 			self.database[symbols[i]] = Dict()
# 			self.database[symbols[i]]['types'] = [inputs[i], outputs[i]]
# 		self.relations = symbols

# 	def type(self, i):
# 		return get_name(self.patterns[i])

# 	def size(self):
# 		return len(self.patterns)

# 	def add(self, pattern, key=None):
# 		if key == None:
# 			index = self.counter
# 			self.counter += 1
# 		else:
# 			index = key
# 		self.patterns[index] = pattern
# 		self.database[index] = Dict()

# 	def compute(self, relation, inputs):
# 		i,j = None,None
# 		if len(inputs) >= 1:
# 			i = inputs[0]
# 		if len(inputs) >= 2:
# 			j = inputs[1]

# 		f = self.patterns[relation]
# 		xi,xj = None,None
# 		if i != None:xi = self.patterns[i]
# 		if j != None:xj = self.patterns[j]

# 		xtypes = self.database[relation]['types'][0]
# 		if xi != None:
# 			if (xtypes != None and get_name(xi) == xtypes) or xtypes == None:
# 				if xj != None:
# 					if (xtypes != None and get_name(xj) == xtypes) or xtypes == None:
# 						return f(xi, xj)
# 				return f(xi)
# 		return f()

# 	def store(self, x):
# 		self.history.insert(0, x)

# 	def __call__(self, statement):
# 		relation = statement[0]
# 		inputs = statement[1:len(statement)]
# 		output = self.compute(relation, inputs)
# 		data = Dict(['function', 'input', 'output'])
# 		data['function'] = relation
# 		data['input'] = [self.patterns[inputs[i]] for i in range(len(inputs))]
# 		data['output'] = output
# 		self.store(data)
# 		return output

# def random_subset(X, s):
# 	Y = []
# 	V = []
# 	for x in X:
# 		V.append(x)

# 	for i in range(s):
# 		j = rr(len(V))
# 		Y.append(V[j])
# 		del V[i]
# 	return Y

# def transpose(X):
# 	if all_equal(to_all(X, get_name)) and get_name(X[0]) == 'dict':
# 		output = Dict(X[0].keys())
# 		for i in range(len(X)):
# 			x = X[i]
# 			for j in x.keys():
# 				if output[j] == None:
# 					output[j] = []
# 				output[j].append(x[j])
# 		return output

# sys = System()
# sys.add(Matrix([5]), 'A')
# sys.add(Matrix([5], 1), 'B')
# sys.add([5], 's')

# y = sys(['union', 'A', 'B'])
# y = sys(['intersection', 'A', 'B'])
# y = sys(['compliment', 'A', 'B'])

# d = sys.history
# print(transpose(d))
# print(y)
