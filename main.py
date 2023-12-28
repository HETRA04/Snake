import pygame,random,sys
pygame.init()
clock = pygame.time.Clock()
# screen section
screen_width = 700
screen_height = 630
cell_size = 35
green = (107, 235, 52)
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill("green")
def drawGrid(): 
    for x in range(0, screen_width, cell_size):
        for y in range(0, screen_height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, "black", rect, 1)
# Snake initialisation and functions and colisions
class snake:
    def __init__(self):
        self.x,self.y = cell_size,cell_size
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x,self.y,cell_size,cell_size)
        self.body = [pygame.Rect(self.x-cell_size,self.y,cell_size,cell_size)]
        self.dead = False    
    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x,self.body[i].y = self.body[i+1].x,self.body[i+1].y
            
        self.head.x += self.xdir * cell_size
        self.head.y += self.ydir * cell_size
        self.body.remove(self.head)

    

    
        

    
        

# Fruit 
red = (235, 52, 52)
def draw_fruit():
    
    
    randx = random.randrange(0,screen_width,cell_size)
    randy = random.randrange(0,screen_height,cell_size)
    square = pygame.Rect(randx,randy,cell_size,cell_size)
    
    pygame.draw.rect(screen,red,square,0)
    
                    


    
    


# Main loop
Snake = snake()
drawGrid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,"brown", Snake.head)
    for square in Snake.body:
        pygame.draw.rect(screen,"brown",square)
    Snake.update()
    
    clock.tick(10)
    pygame.display.update()
    
sys,exit()
pygame.quit()


