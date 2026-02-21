import pygame

#setup
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('mouse moving')
clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

#game_variables
mouse_pos = [width//2,height//2]
mouse_size = 20
mouse_speed = 10

#main game loop
running =True
while running:
    screen.fill(black)

    #check for events (for closing the window)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    #movment logic
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and mouse_pos[0]>0:
        mouse_pos[0] -= mouse_speed
    if key[pygame.K_RIGHT] and mouse_pos[0]<width:
        mouse_pos[0] += mouse_speed
    if key[pygame.K_UP] and mouse_pos[1]>0:
        mouse_pos[1] -= mouse_speed
    if key[pygame.K_DOWN] and mouse_pos[1]<height:
        mouse_pos[1] += mouse_speed

    #draw_mouse
    mouse_shape = pygame.Rect(mouse_pos[0], mouse_pos[1], mouse_size, mouse_size)
    pygame.draw.rect(screen, yellow, mouse_shape)
    pygame.display.flip()

    #UI Text
    font = pygame.font.SysFont("Aerial",18)
      # font.render(text, antialias, color)
      # to turn the text into an image
    label = font.render("version 1", True, white)
    screen.blit(label,(10,10)) #screen.blit(image,(x,y)) where x and y are coordinates

    #update display
    pygame.display.flip()

    #cap the frame rate at 60 fps
    clock.tick(45)




pygame.quit()
