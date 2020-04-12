import random
import re
import sys
import inspect
from os import path
from PIL import Image, ImageChops, ImageDraw, ImageStat



# To work with one image (as required in the assignment)
# INPUT_FILE = "./input.png"
# OUTPUT_FILE = "./output.png"
# COLLAGE_FILE = None
# GIF_FRAMES = None

# To work with all images from folder and also create gifs (as was convenient for testing)
INPUT_FILE = "./input/%d.png"
OUTPUT_FILE = "./output/%d.png"
COLLAGE_FILE = "./output/%d.gif"
GIF_FRAMES = 500

POPULATION_SIZE = 10
MAX_ITERATIONS = 200000



def fitness(member, input_image):
	return sum(ImageStat.Stat(ImageChops.difference(member, input_image)).rms)



WORDS = re.findall(r"[\w']+", inspect.getsource(sys.modules[__name__]))
def mutated(member):
	new_member = member.copy()
	draw = ImageDraw.Draw(new_member)
	draw.text(
		(random.randint(-10, member.width), random.randint(-10, member.height)), # random place
		random.choice(WORDS), # random word
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



def produce_art(input_image, create_collage):
	# Initial population
	population = []
	initial_fitness = fitness(Image.new(input_image.mode, input_image.size, (0, 0, 0)), input_image)
	for i in range(POPULATION_SIZE):
		member = Image.new(input_image.mode, input_image.size, (0, 0, 0))
		population += [(initial_fitness, member)]
	population.sort()

	# Initial collage frame
	collage = None
	if (create_collage):
		frame = Image.new(input_image.mode, (input_image.width*2, input_image.height), (0, 0, 0))
		frame.paste(input_image)
		collage = [frame]

	# Make EA iterations
	for i in range(MAX_ITERATIONS + 1):
		population = population_selection(population, input_image)

		# Show progress
		if (i % (MAX_ITERATIONS//100) == 0):
			print("%d%%" % (i*100//MAX_ITERATIONS))

		# Add frame to the collage
		if (create_collage and i % (MAX_ITERATIONS//GIF_FRAMES) == 0):
			frame = Image.new(input_image.mode, (input_image.width*2, input_image.height), (0, 0, 0))
			frame.paste(input_image)
			frame.paste(population[0][1], (input_image.width, 0))
			collage += [frame]

	# Return best member of population
	return (population[0][1], collage);



if __name__ == "__main__":
	create_collage = COLLAGE_FILE != None and GIF_FRAMES != None
	if ("%d" in INPUT_FILE and "%d" in OUTPUT_FILE and (not create_collage or "%d" in COLLAGE_FILE)):
		i = 1
		while (path.isfile(INPUT_FILE % i)):
			art, collage = produce_art(Image.open(INPUT_FILE % i), create_collage)
			art.save(OUTPUT_FILE % i)
			if (create_collage):
				collage[-1].save(COLLAGE_FILE % i, save_all=True, append_images=collage, optimize=True, duration=40, loop=0)
			i += 1
	else:
		art, collage = produce_art(Image.open(INPUT_FILE), create_collage)
		art.save(OUTPUT_FILE)
		if (create_collage):
			collage[-1].save(COLLAGE_FILE, save_all=True, append_images=collage, optimize=True, duration=40, loop=0)
