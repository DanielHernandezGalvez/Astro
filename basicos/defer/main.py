class Padre:
	def hablar(self):
		print("Hola")
		
class Madre:
	def reir(self):
		print("jajaja")
		
class Hijo(Padre, Madre):
	pass

mi_hijo = Hijo.hablar()
	
