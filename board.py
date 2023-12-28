import pygame,main,fruit,snake


    screen_width = 700
    screen_height = 630
    cell_size = 35

    green = ()


    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill("green")

# draw grid + colouur function

#def draw_grid():
#    for x in range(0,screen_width):
 #       for y in range(0,screen_height):
 #           if x % 10 == 0:
  #              if y % 10 == 10:
   #                 pygame.draw.rect(screen,green2,cell_size,1)