import pygame
import time
import random

# Initialize the pygame library
pygame.init()

# Define the screen dimensions
width = 600
height = 400

# Colors
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define the snake properties
snake_block = 10
snake_speed = 15

# Create the clock object to control the snake's speed
clock = pygame.time.Clock()

# Define the font for text
font_style = pygame.font.SysFont("bahnschrift", 25)

# Function to display messages
def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Boundary conditions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Draw food
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Add snake's new position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Remove the last segment if the snake hasn't grown
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_block, snake_list)

        # Update the display
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Control the speed of the game
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
