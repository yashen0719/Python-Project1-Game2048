import pygame
import sys
from game_logic import initialize_game, move_left, move_right, move_up, move_down, add_new_tile, check_game_over

# Constants
WINDOW_SIZE = 400
GRID_SIZE = 4
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
CELL_PADDING = 10
FONT_SIZE = 50

# Colors
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_CELL_COLOR = (205, 193, 180)
CELL_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
FONT_COLOR = (119, 110, 101)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("2048")
font = pygame.font.Font(None, FONT_SIZE)

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = board[i][j]
            color = CELL_COLORS.get(value, EMPTY_CELL_COLOR)
            rect = pygame.Rect(j * CELL_SIZE + CELL_PADDING, i * CELL_SIZE + CELL_PADDING,
                               CELL_SIZE - CELL_PADDING * 2, CELL_SIZE - CELL_PADDING * 2)
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                text = font.render(str(value), True, FONT_COLOR)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)
    pygame.display.flip()

def main():
    board = initialize_game()
    draw_board(board)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_a:
                        board = move_left(board)
                    elif event.key == pygame.K_d:
                        board = move_right(board)
                    elif event.key == pygame.K_w:
                        board = move_up(board)
                    elif event.key == pygame.K_s:
                        board = move_down(board)
                    else:
                        continue

                    if check_game_over(board):
                        print("Game Over!")
                        pygame.quit()
                        sys.exit()

                    board = add_new_tile(board)
                    draw_board(board)
                except Exception as e:
                    print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
