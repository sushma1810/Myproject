class sushma:
	something=123
	def __init__(self):
		print("this is class sanjay")
	def set(self,anything):
		sanjay.something=anything
	def get(self):
		print("something=:",sushma.something)
class manaswini(sushma):
	def __init__(self):
		print("manaswini")
	def get(self):
		print("anything of manaswini:",sushma.something)
s2=manaswini()
s2.set(234)
s1=sushma()
s1.get()
s2.get()




	
	
