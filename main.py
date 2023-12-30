import pygame,random,sys
pygame.init()
clock = pygame.time.Clock()
# screen section
score = 0
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
        self.size = 1
        self.length = cell_size
        self.x,self.y = cell_size,cell_size
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x,self.y,cell_size,cell_size)
        self.body = [pygame.Rect(self.x-cell_size,self.y,self.length,self.length)] 
        self.dead = False    
    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x,self.body[i].y = self.body[i+1].x,self.body[i+1].y
            
        self.head.x += self.xdir * cell_size
        self.head.y += self.ydir * cell_size
        self.body.remove(self.head)


    

    
        

    
        

# Fruit 
class fruit:
    def __init__(self): 
        self.x,self.y = random.randrange(0,screen_width,cell_size) , random.randrange(0,screen_height,cell_size)
        self.color = (235, 52, 61)
        self.size = pygame.Rect(self.x,self.y,cell_size,cell_size)

    def update(self):
        pygame.draw.rect(screen,"red", self.size)
        
    
    
            
        
            
            


            

        
        
    
         
                    


    
    


# Main loop
Fruit = fruit()
Snake = snake()


drawGrid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Snake.ydir = 1
                Snake.xdir = 0
            elif event.key == pygame.K_UP:
                Snake.ydir = -1
                Snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                Snake.ydir = 0
                Snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                Snake.ydir = 0
                Snake.xdir = -1
        
        
            

    Snake.update()
    

    screen.fill("green")
    drawGrid()

    Fruit.update()
    
    
    pygame.draw.rect(screen,"blue",Snake.head)
    
        
    
        
    
            
    for square in Snake.body:
        pygame.draw.rect(screen,"orange",square)

    if Snake.head.x == Fruit.x and Snake.head.y == Fruit.y:
        Snake.body.append(pygame.Rect(Snake.head.x,Snake.head.y,cell_size,cell_size))
        Fruit = fruit()
    
    pygame.display.update()
    clock.tick(10)

sys.exit()
pygame.quit()

