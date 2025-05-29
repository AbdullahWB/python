# # # # # import pygame

# # # # # print("Pygame version:", pygame.version.ver)

# # # # # import pygame

# # # # # # Initialize Pygame
# # # # # pygame.init()

# # # # # # Set up the display
# # # # # screen = pygame.display.set_mode((800, 600))
# # # # # pygame.display.set_caption("Pygame Example")

# # # # # # Main loop
# # # # # running = True
# # # # # while running:
# # # # #     for event in pygame.event.get():
# # # # #         if event.type == pygame.QUIT:
# # # # #             running = False

# # # # #     # Fill the screen with white
# # # # #     screen.fill((255, 255, 255))

# # # # #     # Draw a red rectangle
# # # # #     pygame.draw.rect(screen, (255, 0, 0), (300, 200, 200, 100))

# # # # #     # Update the display
# # # # #     pygame.display.flip()

# # # # # # Quit Pygame
# # # # # pygame.quit()


# # # # import pygame
# # # # import time
# # # # import random

# # # # pygame.init()

# # # # # Colors
# # # # white = (255, 255, 255)
# # # # yellow = (255, 255, 102)
# # # # black = (0, 0, 0)
# # # # red = (213, 50, 80)
# # # # green = (0, 255, 0)
# # # # blue = (50, 153, 213)

# # # # # Display
# # # # width = 600
# # # # height = 400
# # # # screen = pygame.display.set_mode((width, height))
# # # # pygame.display.set_caption("Snake Game")

# # # # clock = pygame.time.Clock()
# # # # snake_block = 10
# # # # snake_speed = 15

# # # # font_style = pygame.font.SysFont(None, 50)
# # # # score_font = pygame.font.SysFont(None, 35)

# # # # def our_snake(snake_block, snake_list):
# # # #     for x in snake_list:
# # # #         pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# # # # def message(msg, color):
# # # #     mesg = font_style.render(msg, True, color)
# # # #     screen.blit(mesg, [width / 6, height / 3])

# # # # def gameLoop():
# # # #     game_over = False
# # # #     game_close = False

# # # #     x1 = width / 2
# # # #     y1 = height / 2

# # # #     x1_change = 0
# # # #     y1_change = 0

# # # #     snake_List = []
# # # #     Length_of_snake = 1

# # # #     foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
# # # #     foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# # # #     while not game_over:

# # # #         while game_close == True:
# # # #             screen.fill(blue)
# # # #             message("You Lost! Press Q-Quit or C-Play Again", red)
# # # #             pygame.display.update()

# # # #             for event in pygame.event.get():
# # # #                 if event.type == pygame.KEYDOWN:
# # # #                     if event.key == pygame.K_q:
# # # #                         game_over = True
# # # #                         game_close = False
# # # #                     if event.key == pygame.K_c:
# # # #                         gameLoop()

# # # #         for event in pygame.event.get():
# # # #             if event.type == pygame.QUIT:
# # # #                 game_over = True
# # # #             if event.type == pygame.KEYDOWN:
# # # #                 if event.key == pygame.K_LEFT:
# # # #                     x1_change = -snake_block
# # # #                     y1_change = 0
# # # #                 elif event.key == pygame.K_RIGHT:
# # # #                     x1_change = snake_block
# # # #                     y1_change = 0
# # # #                 elif event.key == pygame.K_UP:
# # # #                     y1_change = -snake_block
# # # #                     x1_change = 0
# # # #                 elif event.key == pygame.K_DOWN:
# # # #                     y1_change = snake_block
# # # #                     x1_change = 0

# # # #         if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
# # # #             game_close = True
# # # #         x1 += x1_change
# # # #         y1 += y1_change
# # # #         screen.fill(black)
# # # #         pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
# # # #         snake_Head = []
# # # #         snake_Head.append(x1)
# # # #         snake_Head.append(y1)
# # # #         snake_List.append(snake_Head)
# # # #         if len(snake_List) > Length_of_snake:
# # # #             del snake_List[0]

# # # #         for x in snake_List[:-1]:
# # # #             if x == snake_Head:
# # # #                 game_close = True

# # # #         our_snake(snake_block, snake_List)
# # # #         pygame.display.update()

# # # #         if x1 == foodx and y1 == foody:
# # # #             foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
# # # #             foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
# # # #             Length_of_snake += 1

# # # #         clock.tick(snake_speed)

# # # #     pygame.quit()
# # # #     quit()

# # # # gameLoop()



# # # import pygame

# # # pygame.init()

# # # # Screen setup
# # # width, height = 800, 600
# # # screen = pygame.display.set_mode((width, height))
# # # pygame.display.set_caption("Bouncing Ball")

# # # # Colors
# # # white = (255, 255, 255)
# # # red = (255, 0, 0)

# # # # Ball properties
# # # ball_radius = 20
# # # ball_x = width // 2
# # # ball_y = height // 2
# # # ball_dx = 5
# # # ball_dy = 5

# # # clock = pygame.time.Clock()

# # # running = True
# # # while running:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # #     # Move the ball
# # #     ball_x += ball_dx
# # #     ball_y += ball_dy

# # #     # Bounce off the edges
# # #     if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
# # #         ball_dx *= -1
# # #     if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
# # #         ball_dy *= -1

# # #     # Draw everything
# # #     screen.fill(white)
# # #     pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
# # #     pygame.display.flip()

# # #     clock.tick(60)

# # # pygame.quit()





# # import pygame

# # pygame.init()

# # # Screen setup
# # screen = pygame.display.set_mode((400, 300))
# # pygame.display.set_caption("Music Player")

# # # Load and play music
# # pygame.mixer.music.load("background_music.mp3")  # Replace with your music file
# # pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     pygame.display.flip()

# # pygame.quit()




# import pygame
# import random

# pygame.init()

# # Screen setup
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Math Quiz")

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Fonts
# font = pygame.font.SysFont(None, 55)

# def generate_question():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     operator = random.choice(["+", "-", "*"])
#     question = f"{num1} {operator} {num2} = ?"
#     answer = eval(f"{num1} {operator} {num2}")
#     return question, answer

# def display_text(text, x, y):
#     text_surface = font.render(text, True, black)
#     screen.blit(text_surface, (x, y))

# running = True
# question, answer = generate_question()
# user_input = ""

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 try:
#                     if int(user_input) == answer:
#                         question, answer = generate_question()
#                         user_input = ""
#                 except ValueError:
#                     pass
#             elif event.key == pygame.K_BACKSPACE:
#                 user_input = user_input[:-1]
#             else:
#                 user_input += event.unicode

#     screen.fill(white)
#     display_text(question, 50, 50)
#     display_text(f"Your Answer: {user_input}", 50, 150)
#     pygame.display.flip()

# pygame.quit()


