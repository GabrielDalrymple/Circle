import math
class Circle:
	#Constructors
	def __init__(self, x = 0, y = 0, radius = 1):
		self.x = x
		self.y = y
		self.radius = radius
	#Getters
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getRadius(self):
		return self.radius
	#Setters
	def setX(self, x):
		self.x = x
	def setY(self, y):
		self.y = y
	def setRadius(self, radius):
		self.radius = radius
	#Methods
	def getArea(self):
		return math.pi * self.radius * self.radius
	def getPerimeter(self):
		return 2 * math.pi * self.radius
	def isPointWithinCircle(self, x, y):
		#check if the distance from the center of the circle and the point is less than the radius 
		return ( (x - self.x) * (x - self.x) + (y - self.y) * (y - self.y) ) < (self.radius * self.radius)