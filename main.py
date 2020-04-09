import random
import math
from PIL import Image, ImageChops, ImageDraw



INPUT_FILE = "./input.png"
OUTPUT_FILE = "./output.png"

POPULATION_SIZE = 10
MAX_ITERATIONS = 20000



def fitness(member, input_image):
	h = ImageChops.difference(member, input_image).histogram()
	return math.sqrt(sum(map(lambda h, i: h*(i**2), h, range(256))) / (float(member.size[0]) * member.size[1]))



def mutated(member):
	new_member = member.copy()
	draw = ImageDraw.Draw(new_member)
	draw.text(
		(random.randint(1, member.width), random.randint(1, member.height)), # random place
		"Sample Text", # random character
		(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)) # random color
	)
	return new_member



def population_selection(population, input_image):
	new_population = []
	for i in range(len(population) // 2):
		# Copy the best half
		new_population += [population[i]]

		# Add mutated copies
		new_member = mutated(population[i][1])
		new_population += [(fitness(new_member, input_image), new_member)]
	return sorted(new_population, key = lambda x: x[0])



def produce_art(input_image):

	# Initial population
	population = []
	initial_fitness = fitness(Image.new(input_image.mode, input_image.size, (0, 0, 0)), input_image)
	for i in range(POPULATION_SIZE):
		member = Image.new(input_image.mode, input_image.size, (0, 0, 0))
		population += [(initial_fitness, member)]
	population.sort()

	# Make EA iterations
	for i in range(MAX_ITERATIONS + 1):
		population = population_selection(population, input_image)

		# Show progress
		if (i % (MAX_ITERATIONS//100) == 0):
			print("%d%%" % (i*100//MAX_ITERATIONS))

	# Return best member of population
	return population[0][1];



if __name__ == "__main__":
	produce_art(Image.open(INPUT_FILE)).save(OUTPUT_FILE)