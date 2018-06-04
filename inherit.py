class sanjay:
	something=123
	def __init__(self):
		print("this is class sanjay")
	def set(self,anything):
		sanjay.something=anything
	def get(self):
		print("something=:",sanjay.something)
class manaswini(sanjay):
	def __init__(self):
		print("manaswini")
	def get(self):
		print("anything of manaswini:",sanjay.something)
s2=manaswini()
s2.set(234)
s1=sanjay()
s1.get()
s2.get()




	
	
