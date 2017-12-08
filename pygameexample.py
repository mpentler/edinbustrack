# Edinburgh bus tracker - example of output to a PyGame screen
# (c) Mark Pentler 2017

from edinbustrack import *
import pygame
import os
import datetime

stop_id = "36232626"

# PyGame requires quite a bit of setup, the block below is to setup the surface
pygame.init() # required for setting some variables
os.putenv('DISPLAY', ':0.0') # use framebuffer for output via an envvar
res_info = pygame.display.Info() # find the size of our framebuffer...
screen_width = res_info.current_w
screen_height = res_info.current_h
size = (screen_width, screen_height) # ...and make our screen that big
screen = pygame.display.set_mode(size) # finally, define our PyGame surface

# Define some constants for later use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CELL_BG = (180, 180, 180)
CELL_WIDTH = 156
CELL_HEIGHT = 90
H_SPACING = 200
COL_1_L_EDGE = H_SPACING
COL_2_L_EDGE = COL_1_L_EDGE + CELL_WIDTH + H_SPACING
COL_3_L_EDGE = COL_2_L_EDGE + CELL_WIDTH + H_SPACING + H_SPACING
COL_4_L_EDGE = COL_3_L_EDGE + CELL_WIDTH + H_SPACING
EXTRA = 10

# Font definitions
title_font = pygame.font.Font("/usr/share/fonts/truetype/lato/Lato-Heavy.ttf", 72)
time_font = pygame.font.Font("/usr/share/fonts/truetype/lato/Lato-Heavy.ttf", 40)
col_head_font = pygame.font.Font("/usr/share/fonts/truetype/lato/Lato-Regular.ttf", 40)
cell_font = pygame.font.Font("/usr/share/fonts/truetype/lato/Lato-Heavy.ttf", 60)

# Draw some UI elements. Title first
screen.fill(WHITE)
title = title_font.render("Edinburgh Bus Tracker", 1, (0, 0, 0))
title_rect = title.get_rect(center=(screen_width/2, 35))
screen.blit(title, title_rect)

# And some more labels and lines and things
pygame.draw.lines(screen, BLACK, False, [((screen_width/2), 130), ((screen_width/2), screen_height)], 10)
col_1_label = col_head_font.render("Service", 1, (0, 0, 0))
col_1_label_rect = col_1_label.get_rect(center=(COL_1_L_EDGE + EXTRA + CELL_WIDTH/2, 140))
col_2_label = col_head_font.render("Mins", 1, (0, 0, 0))
col_2_label_rect = col_2_label.get_rect(center=(COL_2_L_EDGE + EXTRA + CELL_WIDTH/2, 140))
col_3_label = col_head_font.render("Service", 1, (0, 0, 0))
col_3_label_rect = col_3_label.get_rect(center=(COL_3_L_EDGE + EXTRA + CELL_WIDTH/2, 140))
col_4_label = col_head_font.render("Mins", 1, (0, 0, 0))
col_4_label_rect = col_4_label.get_rect(center=(COL_4_L_EDGE + EXTRA + CELL_WIDTH/2, 140))
screen.blit(col_1_label, col_1_label_rect)
screen.blit(col_2_label, col_2_label_rect)
screen.blit(col_3_label, col_3_label_rect)
screen.blit(col_4_label, col_4_label_rect)

# And a few function definitions for EZPZ code reading
def draw_cell_bgs(): # Re-blank our cells for new data display
	Y_POS = 200
	for i in range (6):
		pygame.draw.rect(screen, CELL_BG, (COL_1_L_EDGE, Y_POS, 180, CELL_HEIGHT), 0)
		pygame.draw.rect(screen, CELL_BG, (COL_2_L_EDGE, Y_POS, 180, CELL_HEIGHT), 0)
		pygame.draw.rect(screen, CELL_BG, (COL_3_L_EDGE, Y_POS, 180, CELL_HEIGHT), 0)
		pygame.draw.rect(screen, CELL_BG, (COL_4_L_EDGE, Y_POS, 180, CELL_HEIGHT), 0)
		Y_POS = Y_POS + 130
	return

def update_times(): # get new timing data and redraw the screen
	services = get_bus_times(stop_id)
	Y_POS = 240
	for id, service, mins in services: # iterate through the list
		if id < 6: # which column are we writing to?
			label1 = cell_font.render(service, 1, (0, 0, 0))
			label1_rect = label1.get_rect(center=(COL_1_L_EDGE + EXTRA + CELL_WIDTH/2, Y_POS))
			screen.blit(label1, label1_rect)
			label2 = cell_font.render(mins, 1, (0, 0, 0))
			label2_rect = label2.get_rect(center=(COL_2_L_EDGE + EXTRA + CELL_WIDTH/2, Y_POS))
			screen.blit(label2, label2_rect)
			Y_POS = Y_POS + 130
		elif id == 6: # move to column 2
			Y_POS = Y_POS - (130*6) # move the cursor up
			label3 = cell_font.render(service, 1, (0, 0, 0))
			label3_rect = label3.get_rect(center=(COL_3_L_EDGE + EXTRA + CELL_WIDTH/2, Y_POS))
			screen.blit(label3, label3_rect)
			label4 = cell_font.render(mins, 1, (0, 0, 0))
			label4_rect = label4.get_rect(center=(COL_4_L_EDGE + EXTRA + CELL_WIDTH/2, Y_POS))
			screen.blit(label4, label4_rect)
			Y_POS = Y_POS + 130
		else:
			label3 = cell_font.render(service, 1, (0, 0, 0))
			label3_rect = label3.get_rect(center=(COL_3_L_EDGE + EXTRA + CELL_WIDTH/2, Y_POS))
			screen.blit(label3, label3_rect)
			label4 = cell_font.render(mins, 1, (0, 0, 0))
			label4_rect = label4.get_rect(center=(COL_4_L_EDGE + EXTRA + CELL_WIDTH/2, Y_POS))
			screen.blit(label4, label4_rect)
			Y_POS = Y_POS + 130
	return

# After all of this setup we want to draw the cells, then grab the data and populate for first run
# Every successive check will be on :30 or :00 seconds
draw_cell_bgs()
update_times()
pygame.display.flip() # draw screen for the first time
clock = pygame.time.Clock() # Setup the PyGame tick clock
quitting = False # running state

# Main Loop
while not quitting:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN: # any key to exit
			quitting = True # change the running state
			break

	current_datetime = datetime.datetime.now()
	time_string = current_datetime.strftime('%H:%M:%S')
	time_display = time_font.render(time_string, 1, (0, 0, 0))
	time_rect = time_display.get_rect(center=(100, 35))
	pygame.draw.rect(screen, WHITE, (0, 0, 250, 100), 0)
	screen.blit(time_display, time_rect)

	if current_datetime.second == 0 or current_datetime.second == 30:
		draw_cell_bgs()
		update_times()
	pygame.display.flip() # update the display
	clock.tick() # tick tock!

pygame.quit() # required to exit cleanly and not mess up the framebuffer

