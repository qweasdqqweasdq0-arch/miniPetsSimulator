from pet import Pet 
 
my_pet = Pet("Buddy", 80) 
print(f"Pet Name: {my_pet.name}") 
print(f"Initial Energy: {my_pet.energy_level}") 
 
my_pet.feed_pet() 
my_pet.pull_pet() 
 
print(f"Final Energy: {my_pet.energy_level}") 
