import pygame
import random

#setup
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('mouse moving and snake catching along ')
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
last_mouse_boost = last_snake_boost = start_time
message_end =messages_end_S = 0

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

#game_variables
#mouse
mouse_pos = [width//2,height//2]
mouse_size = 20
mouse_speed = 10

#snake
snakes = [[0,0]]
snake_speed = 5
snake_size =35

#main game loop
seconds = 0
running =True
while running:
    screen.fill(black)

    #check for events (for closing the window)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    #movment logic
    key = pygame.key.get_pressed()
    #player
    if key[pygame.K_LEFT] and mouse_pos[0]>0:
        mouse_pos[0] -= mouse_speed
    if key[pygame.K_RIGHT] and mouse_pos[0]<width:
        mouse_pos[0] += mouse_speed
    if key[pygame.K_UP] and mouse_pos[1]>0:
        mouse_pos[1] -= mouse_speed
    if key[pygame.K_DOWN] and mouse_pos[1]<height:
        mouse_pos[1] += mouse_speed

    # draw_mouse
    mouse_shape = pygame.Rect(mouse_pos[0], mouse_pos[1], mouse_size, mouse_size)
    pygame.draw.rect(screen, yellow, mouse_shape)


    #snake
    for s in snakes:
        if s[0] < mouse_pos[0]:
            s[0] += snake_speed
        if s[0] > mouse_pos[0]:
            s[0] -= snake_speed
        if s[1] < mouse_pos[1]:
            s[1] += snake_speed
        if s[1] > mouse_pos[1]:
            s[1] -= snake_speed
        snake_shape = pygame.Rect(s[0], s[1], 20, 20)
        pygame.draw.rect(screen, red, snake_shape)
        # checking for collison
        if mouse_shape.colliderect(snake_shape):
            print("snake survived")
            running = False

    current_time = pygame.time.get_ticks()

    #mouse speed increase
    if current_time - last_mouse_boost > 5000:
        mouse_speed += 5.0
        last_mouse_boost = current_time
        message_end=current_time + 4000

    #snake multiply at random
    if current_time - last_snake_boost > 4000:
        new_clone=[]
        for s in snakes:
            random_x = random.randint(0,width//2)
            random_y = random.randint(0,height//2)
            new_clone.append([random_x,random_y])
        snakes.extend(new_clone)
        last_snake_boost = current_time
        messages_end_S = current_time+3000


    #UI Text
    font = pygame.font.SysFont("Aerial",18)
      # font.render(text, antialias, color)
      # to turn the text into an image
    label = font.render("dont let red catch you", True, white)
    screen.blit(label,(10,10)) #screen.blit(image,(x,y)) where x and y are coordinates




    seconds = (current_time - start_time)//1000

    if current_time < message_end:
        msg_surface = font.render("speed increased",True, white)
        screen.blit(msg_surface,(300,550))

    if current_time < messages_end_S:
        msg_surface = font.render("snake multiplied",True, white)
        screen.blit(msg_surface,(400,550))

    timer_text = font.render(f"time: {seconds} seconds", True, white)
    screen.blit(timer_text, (400,20))


    #update display
    pygame.display.flip()

    #cap the frame rate at 60 fps
    clock.tick(60)


pygame.quit()
print(f"you survived for {seconds}seconds")
