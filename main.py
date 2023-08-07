import pygame
import time
import random

# pygame setup
pygame.init()
pygame.display.set_caption("Snake AI")
window_x = 500
window_y = 500
game_window = pygame.display.set_mode((window_x,window_y))
fps = pygame.time.Clock()

# Initial entity spawning
snake_pos = [250,250]
snake_body = [[250,250]]

apple_pos = [random.randrange(1,window_x//10)*10,
             random.randrange(1,window_y//10)*10]
apple_spawn = True

direction = "right"
change_to = direction

score = 0
print(score)

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Snake movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "up"
            if event.key == pygame.K_DOWN:
                change_to = "down"
            if event.key == pygame.K_LEFT:
                change_to = "left"
            if event.key == pygame.K_RIGHT:
                change_to = "right"
    
    # Validate direction changing
    if change_to == "up" and direction != "down":
        direction = "up"
    elif change_to == "down" and direction != "up":
        direction = "down"
    elif change_to == "left" and direction != "right":
        direction = "left"
    elif change_to == "right" and direction != "left":
        direction = "right"
    
    # Change snake position 
    if direction == "up":
        snake_pos[1] -= 10
    if direction == "down":
        snake_pos[1] += 10
    if direction == "left":
        snake_pos[0] -= 10
    if direction == "right":
        snake_pos[0] += 10
    
    snake_body.insert(0, list(snake_pos)) # Add new snake body part at beginning
    # Snake eat apple
    if snake_pos == apple_pos: 
        score += 1
        print(score)
        apple_spawn = False
    else:
        # Remove snake tail for movement
        snake_body.pop()
    
    # Random apple spawning
    if not apple_spawn:
        apple_pos = [random.randrange(1,window_x//10)*10,
                     random.randrange(1,window_y//10)*10]
        apple_spawn = True
    
    game_window.fill(pygame.Color(0,0,0))
    
    # Draw each snake body part
    for pos in snake_body:
        pygame.draw.rect(game_window, pygame.Color(0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw apple
    pygame.draw.rect(game_window, pygame.Color(255,0,0), pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))
    
    # Check if snake is within bounds of window
    if not (0 < snake_pos[0] < window_x-10):
        running = False
    if not (0 < snake_pos[1] < window_y-10):
        running = False
    
    # Check if snake hits self
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False
        
    pygame.display.update()
    
    fps.tick(15)

pygame.quit()
