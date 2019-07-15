class PetStore:
	
	def __init__ (self, pets):
		self.pets = pets
    
    def how_many (self):
    	return "I have {} pets".format(len(self.pets))

class Employees:
	base_salary = 1000
	def __init__ (self,name,age,years_experience)
		self.name = name
		self.age = age
		self.years_experience = years_experience
		self.salary = self.generate_salary()

	def generate.salary (self):
		return self.base_salary+1.5*(self.years_experience)
	def update_years_experience (self, years_of_experience):
		self.years_experience = years_of_experience


phillo = Dog ("Phillo",5)
mikey = Dog ("Mikey",6)
lulu = Dog ("Lulu",3)
jim = Bulldog ("Jim", 12)
my_pets = [phillo,mikey,lulu,jim]
animals = PetStore(my_pets)

print (animals.how_many())

jack = Employees("Jack",34,5)
print (jack.salary)
jack.update_years_experience = 10
print (jack.salary)