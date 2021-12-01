# 1. Modify the class Rational of Lab No2 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.
from math import gcd

def reduced_form(method):
	def reduce(self, *args, **kwargs):
		method(self, *args, **kwargs)
		if self.denominator < 0:
			self.denominator = -self.denominator
			self.numerator = -self.numerator
		k = gcd(self.numerator, self.denominator)
		self.numerator//=k
		self.denominator//=k
		return None
	return reduce

def reduced_formi(method):
	def reduce(self, *args, **kwargs):
		method(self, *args, **kwargs)
		if self.denominator < 0:
			self.denominator = -self.denominator
			self.numerator = -self.numerator
		k = gcd(self.numerator, self.denominator)
		self.numerator//=k
		self.denominator//=k
		return self
	return reduce

class Rational:
	@reduced_form
	def __init__(self, numerator, denominator):
		self.numerator, self.denominator = numerator, denominator
		# self.__reduced_form()

	def __str__(self):
		return f'{self.__numerator}/{self.__denominator}' 

	@property
	def numerator(self):
		return self.__numerator

	@numerator.setter
	def numerator(self, value):
		if not (isinstance(value, int)):
			raise TypeError("Wrong value type")
		self.__numerator = value

	@property
	def denominator(self):
		return self.__denominator

	@denominator.setter
	def denominator(self, value):
		if not (isinstance(value, int)):
			raise TypeError("Wrong value type")
		if not value:
			raise ZeroDivisionError("Denominator cant be Zero")
		self.__denominator = value

	@property
	def floated(self):
		return self.numerator/self.denominator

	def __add__(self, other):
		return Rational(self.numerator * other.denominator + other.numerator * self.denominator, 
						self.denominator *  other.denominator)

	def __sub__(self, other):
		return Rational(self.numerator * other.denominator - other.numerator * self.denominator, 
						self.denominator * other.denominator)

	def __mul__(self, other):
		return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
	
	def __truediv__(self, other):
		return Rational(self.numerator *other.denominator, self.denominator *  other.numerator)

	def __eq__(self, other) -> bool:
		return self.floated == other.floated

	def __ne__(self, other) -> bool:
		return self.floated != other.floated

	def __lt__(self, other) -> bool:
		return self.floated < other.floated

	def __gt__(self, other) -> bool:
		return self.floated > other.floated

	def __le__(self, other) -> bool:
		return self.floated <= other.floated

	def __ge__(self, other) -> bool:
		return self.floated >= other.floated

	# def __reduced_form(self):
	# 	k = gcd(self.numerator, self.denominator)
	# 	self.numerator//=k
	# 	self.denominator//=k

	@reduced_formi
	def __iadd__(self, other):
		self.numerator =  self.numerator * other.denominator + other.numerator * self.denominator 
		self.denominator = self.denominator * other.denominator
		return self

	@reduced_formi
	def __isub__(self, other):
		self.numerator =  self.numerator * other.denominator - other.numerator * self.denominator 
		self.denominator = self.denominator *  other.denominator
		return self

	@reduced_formi
	def __imul__(self, other):
		self.numerator =  self.numerator * other.numerator 
		self.denominator = self.denominator *  other.denominator
		return self
	

	@reduced_formi
	def __itruediv__(self, other):
		self.numerator =  self.numerator * other.denominator
		self.denominator = self.denominator *  other.numerator
		return self

	

if __name__ == "__main__":
	x = Rational(2, -6)
	y = Rational(-1, 3)

	print("Z:")
	z = x + y
	print (z)

	z = x - y
	print (z)

	z = x * y
	print (z)

	z = x / y
	print (z)

	print("X:")
	print(x)

	x+=y
	print (x)

	x-=y
	print (x)

	x*=y
	print (x)

	x/=y
	print (x)

	print("СРАВНЕНИЯ")
	print (x == y)
	print (x < y)
	print (x > y)
	print (x <= y)
	print (x >= y)















