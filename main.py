import pygame
import sys
import time
import random

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1100,650))


# Receive a cell and count all the live (black) neighbor cells
def check_neighbor(square_list,z): # receives the list and the index
	neighbors = []			
	try:
		if square_list[z-61].icon == sq_black:
			neighbors.append(z-61) 
	except IndexError:
		print('indexError{}'.format(z))
	try:	
		if square_list[z-60].icon == sq_black:
			neighbors.append(z-60)
	except IndexError:
		print('indexError{}'.format(z))	
	try:	
		if square_list[z-59].icon == sq_black:
			neighbors.append(z-59) 
	except IndexError:
		print('indexError{}'.format(z))
	try:	
		if square_list[z-1].icon == sq_black:
			neighbors.append(z-1) 
	except IndexError:
		print('indexError{}'.format(z))
	try:	
		if square_list[z+1].icon == sq_black:
			neighbors.append(z+1) 
	except IndexError:
		print('indexError{}'.format(z))
	try:	
		if square_list[z+59].icon == sq_black:
			neighbors.append(z+59) 
	except IndexError:
		print('indexError{}'.format(z))
	try:	
		if square_list[z+60].icon == sq_black:
			neighbors.append(z+60) 
	except IndexError:
		print('indexError{}'.format(z))
	try:	
		if square_list[z+61].icon == sq_black:
			neighbors.append(z+61) 
	except IndexError:
		print('indexError{}'.format(z))
	return len(neighbors)


class square():
	def __init__(self,state,icon, x, y, change): #state is bool, icon is pygame.image.load('image file')
		self.state = state #bool
		self.icon = icon #refers to pygame.image.load('file.png')
		self.x = x # x position 
		self.y = y # y position
		self.change = change # remember if it must change color

square_list = []
sq_white = pygame.image.load('square_white.png') # white color is dead cell
sq_black = pygame.image.load('square_black.png') # black color is live cell
x = 10
y = 10

# Creates a list of squares instances, the start parameters is shown below

for i in range(100):
	for z in range (60):
		square_list.append(square(True,sq_white,x+10*i,y+10*z,False))
		'''
		start values:
		square_list[].state = True
		square_list[].icon = sq_white
		square_list[].x = x coordinate position in the matrix
		square_list[].y = y coordinate position in the matrix
		square_list[].change = False #so that the square does not change color
		'''

#### GAME LOOP ####
continue_life = False
run_life = 0
running = True
while running:

	# Draw all squares	
	for i in range(6000):
		screen.blit(square_list[i].icon, (square_list[i].x,square_list[i].y))
	
	# Check for input commands of the user	
	for event in pygame.event.get():
		# Exit if exit button is pressed on window
		if event.type == pygame.QUIT:	
			running = False
		# Change the square to black if user clicks in the square
		if event.type == pygame.MOUSEBUTTONDOWN:	
			mx, my = pygame.mouse.get_pos()
	
			for i in range(6000):
				# Distance between the click and the square
				distance = ((mx-square_list[i].x)**2+(my-square_list[i].y)**2)**0.5		
				if distance <=10:
					#print('Square[{}]'.format(i))
					# Turn the square nearest to black and draw it
					square_list[i].icon = sq_black
					screen.blit(square_list[i].icon, (square_list[i].x,square_list[i].y))
					run_life += 1
					
	# Droping seeds
	#### To do: must add an option to the user to choose between random input or chosen input				
	if not(continue_life):				
		for i in range (1000):
			
			square_list[random.randint(0,5999)].icon = sq_black				
										
		continue_life = True

	if run_life > 60 or continue_life:
		# Runs throught the entire grid checking for the cells being born or dying
		# Set square_list[i].change to True if stays alive (black) or be born (black)
		# Set square_list[i].change to False if it must die (white)
		for i in range(6000):
			if check_neighbor(square_list,i) == 2 and square_list[i].icon == sq_black: # when 2 neighbors, keep in black
				square_list[i].change = True
			elif check_neighbor(square_list,i) == 3: #when 3 neighbors, born
				square_list[i].change = True
			else:
				square_list[i].change = False
		
		# Change the colors accordingly to the square_list[i].change value		
		for i in range(6000):
			if square_list[i].change: #change color to sq_black if there is 3 neighbors or has 2 neighbors and is white
				square_list[i].icon = sq_black
				square_list[i].change = False
			else: # change color to sq_white if number of neighbors == 0 or >=4
				square_list[i].icon = sq_white		
			
			#time.sleep(0.001)
	
	pygame.display.update()

pygame.quit()
quit()	
