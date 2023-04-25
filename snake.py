import pygame
import random

# Define constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 10

VAR = ''
TEST = '123'
if VAR == TEST:
    print("Hi")
    assert VAR==TEST, "Does this work?"
    
# Playing with assert
assert VAR+"123",VAR+TEST
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.segments = [(10, 10), (9, 10), (8, 10)]
        self.direction = "right"
    
    def move(self):
        # Get the head of the snake
        x, y = self.segments[0]
        
        # Move the head in the current direction
        if self.direction == "up":
            y -= 1
        elif self.direction == "down":
            y += 1
        elif self.direction == "left":
            x -= 1
        elif self.direction == "right":
            x += 1
        
        # Add the new head to the front of the snake
        self.segments.insert(0, (x, y))
        
        # Remove the tail segment
        self.segments.pop()
    
    def grow(self):
        # Get the last segment of the snake
        x, y = self.segments[-1]
        
        # Add a new segment to the end of the snake
        self.segments.append((x, y))
    
    def draw(self):
        for segment in self.segments:
            x, y = segment
            pygame.draw.rect(screen, GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Define the Apple class
class Apple:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1)
        self.y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1)
    
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Create the Snake and Apple objects
snake = Snake()
apple = Apple()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
    
    # Move the Snake
    snake.move()
    
    # Check for collision with the Apple
    if snake.segments[0] == (apple.x, apple.y):
        snake.grow()
        apple = Apple()
    
    # Check for collision with the walls or with itself
    if snake.segments[0][1] < 0 or snake.segments[0][1] >= SCREEN_HEIGHT // BLOCK_SIZE:
        running = False

    for segment in snake.segments[1:]:
        if snake.segments[0] == segment:
            running = False

    # Clear the screen
    screen.fill(BLACK)      

    # Draw the Snake and Apple
    snake.draw()
    apple.draw()

    # Update the screen
    pygame.display.update()

    # Delay the game to control the frame rate
    clock.tick(FPS)
