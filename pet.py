class Pet: 
    def __init__(self, name, energy_level): 
        self.name = name 
        self.energy_level = energy_level 
 
    def feed_pet(self): 
        self.energy_level += 10 
        print(f"{self.name} has been fed! Energy level: {self.energy_level}") 
 
    def pull_pet(self): 
        self.energy_level -= 5 
        print(f"{self.name} has been pulled! Energy level: {self.energy_level}") 
