#!/usr/bin/python3


### 1 - Instance - object relationship - self
class Joe(object):
	greeting = "hello, Joe"
	def callme(self):
		print('Calling "callme" method with insance: ', self)


thisjoe = Joe()

print(thisjoe.greeting)
thisjoe.callme()

print(thisjoe)


### 2 - Instance attributes/data
import random

class MyClass(object):
	def dothis(self):
		self.rand_value = random.randint(1,10)

myinst = MyClass()
myinst.dothis()
print(myinst.rand_value)

##$ 3 - Encapsulation

class MyInteger(object):
	def set_val(self, val):
		try:
			self.value = int(val)
		except ValueError:
			print("Error!")
			return

	def get_val(self):
		return self.value

	def increment_val(self):
		self.value += 1


myobj = MyInteger()

myobj.set_val(100)
myobj.increment_val()
print(myobj.get_val())

#this gives error
myobj2 = MyInteger()
myobj2.set_val("Hi")
print(myobj2.get_val())

### 4 - Init Constructor

class MyInt(object):
	def __init__(self, value):
		try:
			value = int(value)
		except ValueError:
			print("Error - setting it to default value 0")
			value = 0
		self.value = value

	def increment(self):
		self.value += 1

	def get_val(self):
		return self.value

myint = MyInt(5)
myint.increment()

print(myint.get_val())
print(dir(myint))


### 5 - Class Attributes

# Looks for the attribute in the instance then in the class

class InstanceCounter(object):
	count = 0

	def __init__(self, value):
		try:
			value = int(value)
		except ValueError:
			print("Error - setting it to default value 0")
			value = 0
		self.value = value
		InstanceCounter.count += 1

	def set_val(self, newval):
		self.value = newval

	def get_val(self):
		return self.value

	def get_count(self):
		return InstanceCounter.count

myobj4 = InstanceCounter(5)
myobj5 = InstanceCounter(10)
for obj in (myobj4, myobj5):
	print("Object value: {} - object count {}".format(obj.value, obj.get_count()))


print;print;