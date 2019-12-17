# Returns the maximum amount of elements in a list for a given object

class MaxSizeList(object):
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.list = []

	def push(self, element):
		if(len(self.list) >= self.maxSize):
			self.list.pop(0)
		self.list.append(element)


	def get_list(self):
		return self.list

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")


b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
