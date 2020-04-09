import random
import string
import math
from PIL import Image, ImageChops, ImageDraw
from functools import reduce
import operator



# Problem definition

W = 512
H = 512

POPULATION_SIZE = 10

input_image = Image.open("./input.png")
def fitness(member):
	h = ImageChops.difference(member, input_image).histogram()
	return math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(member.size[0]) * member.size[1]))

i = 0
def random_member():
	global i
	return ['adasfgsdfgsdfgsdfg', 'bsdfgggggasdasdasd', 'cs', 'dsdfgsdfgsdfgsdfg', 'e', 'f', 'gsdfgsdfgsdfgsdfg', 'h', 'i', 'j', 'k'][i]
	i+=1

def mutated(member):
	new_member = member.copy()
	draw = ImageDraw.Draw(new_member)
	draw.text((random.randint(1, W), random.randint(1, H)), "Sample Text" ,(255,255,255))
	return new_member



# Initial population

population = []
initial_fitness = fitness(Image.new('RGB', (W, H)))
for i in range(POPULATION_SIZE):
	member = Image.new('RGB', (W, H))
	population += [(initial_fitness, member)]
population.sort()



# Generate new population

c = 0
while (population[0][0] > 0 and c <= 1000):
	new_population = []

	for i in range(POPULATION_SIZE // 2):
		# Copy the best half
		new_population += [population[i]]

		# Add mutated copies
		new_member = mutated(population[i][1])
		new_population += [(fitness(new_member), new_member)]

	population = new_population
	population.sort(key=lambda x: x[0])

	print(c)
	c+=1

print(population[0][1])
population[0][1].save('output.png', 'PNG')