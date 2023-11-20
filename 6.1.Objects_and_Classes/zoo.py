class Zoo:
    __animals = 0
    mammals = []
    fishes = []
    birds = []

    def __init__(self, zoo_name):

        self.zoo_name = zoo_name

    def add_animal(self, animal_species, animal_kind):   #ZASHTO TOVA RABOTI BEZ SELF??
        # self.animal_species = animal_species
        # self.animal_kind = animal_kind

        if animal_species == "mammal":
            self.mammals.append(animal_kind)
        if animal_species == "fish":
            self.fishes.append(animal_kind)
        if animal_species == "bird":
            self.birds.append(animal_kind)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        self.species = species

        if self.species == "mammal":
            result = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif self.species == "fish":
            result = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif self.species == "bird":
            result = f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"

        return result


zoo_name_input = Zoo(input())
n = int(input())

for _ in range(n):
    animal_info = input().split()

    species_current = animal_info[0]
    name_current = animal_info[1]

    zoo_name_input.add_animal(species_current, name_current)

species_input = input()

print(zoo_name_input.get_info(species_input))
