import math

class Cylinder:
	def __init__(self,radius,height):
		self.radius=radius
		self.height=height
	def surface_area(self):
		pi=math.pi
		r=self.radius
		h=self.height
		sur_area=2*pi*r*(r+h)
		return "The surface area of the cylinder with radius {} units and height {} units is {}".format(self.radius,self.height,sur_area)
	def volume(self):
		pi=math.pi
		r=self.radius
		h=self.height
		vol=pi*r**2*h
		return "The volume of the cylinder with radius {} units and height {} units is {}".format(self.radius,self.height,vol)



c1=Cylinder(1,1)
print(c1.volume())
print(c1.surface_area())