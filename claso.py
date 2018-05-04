
#!/usr/bin/python3
class A():
	def bag(self):
		print("hello")
class B(A):
	def bag(self):
		pass

class C(B,A):
	pass


print(isinstance(A,B))
