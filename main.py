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

snake_pos = [window_x // 2, window_y // 2]
snake_body = [snake_pos]

fruit_pos = [random.randrange(1,window_x//10)*10,
             random.randrange(1,window_y//10)*10]
fruit_spawn = True

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "up"
            if event.key == pygame.K_DOWN:
                change_to = "down"
            if event.key == pygame.K_LEFT:
                change_to = "left"
            if event.key == pygame.K_RIGHT:
                change_to = "right"
        
    if change_to == "up" and direction != "down":
        direction = "up"
    elif change_to == "down" and direction != "up":
        direction = "down"
    elif change_to == "left" and direction != "right":
        direction = "left"
    elif change_to == "right" and direction != "left":
        direction = "right"
    
    if direction == "up":
        snake_pos[1] -= 10
    if direction == "down":
        snake_pos[1] += 10
    if direction == "left":
        snake_pos[0] -= 10
    if direction == "right":
        snake_pos[0] += 10
    
    snake_body.insert(0, snake_pos)
    if snake_pos == fruit_pos:
        score += 1
        print(score)
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_pos = [random.randrange(1,window_x//10)*10,
                     random.randrange(1,window_y//10)*10]
    
    fruit_spawn = True
    
    game_window.fill(pygame.Color(0,0,0))
    for pos in snake_body:
        pygame.draw.rect(game_window, pygame.Color(0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(game_window, pygame.Color(255,0,0), pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))
    
    if not (0 < snake_pos[0] < window_x-10):
        running = False
    if not (0 < snake_pos[1] < window_y-10):
        running = False
        
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False
    
    pygame.display.update()
    
    fps.tick(15)

pygame.quit()
