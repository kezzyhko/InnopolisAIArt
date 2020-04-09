import random
import string



POPULATION_SIZE = 10

def fitness(member):
	return abs(10-len(member))

i = 0
def random_member():
	global i
	return ['adasfgsdfgsdfgsdfg', 'bsdfgggggasdasdasd', 'cs', 'dsdfgsdfgsdfgsdfg', 'e', 'f', 'gsdfgsdfgsdfgsdfg', 'h', 'i', 'j', 'k'][i]
	i+=1

def mutated(member):
	if (random.randint(1, 2) == 1):
		return member[:-1]
	else:
		return member + random.choice(string.ascii_lowercase)



# Random initial population
population = []
for i in range(POPULATION_SIZE):
	member = random_member()
	population += [(fitness(member), member)]
population.sort()


# Generate new population
i = 0
while (population[0][0] > 0 and i <= 1000):
	new_population = []

	for i in range(POPULATION_SIZE // 2):
		# Copy the best half
		new_population += [population[i]]

		# Add mutated copies
		new_member = mutated(population[i][1])
		new_population += [(fitness(new_member), new_member)]

	population = new_population
	population.sort()

	i+=1

print(population[0][1])