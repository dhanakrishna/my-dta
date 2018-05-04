
#!/usr/bin/python3
class A:
	def __init__(self,name,place,age):
		self.name = name
		self.place = place
		self.age = age
	def  display(self):
		return "name:{}\nplace:{}\nage:{}\n".format(self.name,self.place,self.age)
	
	@classmethod
	def detail (cls,string):
		name,place,age = map(str,string.split('-'))
		x = cls(name,place,age)
		return x


p,q = A.detail('name-kakinada-24')
print(q.display())
