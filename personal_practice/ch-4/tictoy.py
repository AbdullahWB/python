import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
BUTTON_COLOR = (52, 152, 219)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Fonts
font = pygame.font.SysFont("comicsans", 40)
small_font = pygame.font.SysFont("comicsans", 30)

# Board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Scores
scores = {"X": 0, "O": 0}

# Draw grid lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw X or O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, LINE_WIDTH)
            elif board[row][col] == "X":
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Check for a win
def check_win(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if all([cell == player for cell in board[row]]):
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)]):
        return True
    return False

# Check for a draw
def check_draw():
    return all([cell is not None for row in board for cell in row])

# Draw the replay button
def draw_replay_button():
    pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT - 80, BUTTON_WIDTH, BUTTON_HEIGHT))
    text = small_font.render("Replay", True, BUTTON_TEXT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 70))

# Draw the score
def draw_score():
    x_score_text = font.render(f"X: {scores['X']}", True, TEXT_COLOR)
    o_score_text = font.render(f"O: {scores['O']}", True, TEXT_COLOR)
    screen.blit(x_score_text, (20, HEIGHT - 50))
    screen.blit(o_score_text, (WIDTH - o_score_text.get_width() - 20, HEIGHT - 50))

# Restart the game
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None

# Main game loop
def main():
    draw_lines()
    player = "X"
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if not game_over:
                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE

                    if clicked_row < BOARD_ROWS and clicked_col < BOARD_COLS and board[clicked_row][clicked_col] is None:
                        board[clicked_row][clicked_col] = player
                        if check_win(player):
                            scores[player] += 1
                            print(f"Player {player} wins!")
                            game_over = True
                        elif check_draw():
                            print("It's a draw!")
                            game_over = True
                        player = "O" if player == "X" else "X"
                        draw_figures()
                else:
                    # Check if replay button is clicked
                    if WIDTH // 2 - BUTTON_WIDTH // 2 <= mouseX <= WIDTH // 2 + BUTTON_WIDTH // 2 and HEIGHT - 80 <= mouseY <= HEIGHT - 30:
                        restart()
                        game_over = False
                        player = "X"

        # Draw UI elements
        draw_score()
        if game_over:
            draw_replay_button()

        pygame.display.update()

if __name__ == "__main__":
    main()