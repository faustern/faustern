import asyncio
import pygame
import random

# Define constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
GRAY = (30,30,30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Define tetromino shapes
tetrominos = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1], [1, 1]]  # O
]

# Define tetromino colors
tetromino_colors = [CYAN, MAGENTA, ORANGE, BLUE, GREEN, RED, YELLOW]

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Define helper functions
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_tetromino(tetromino, x, y, color):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col]:
                draw_block(x + col, y + row, color)

def new_tetromino():
    tetromino_index = random.randint(0, len(tetrominos) - 1)
    tetromino = tetrominos[tetromino_index]
    color = tetromino_colors[tetromino_index]
    return tetromino, color, 3, 0

def check_collision(grid, tetromino, x, y):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col]:
                if x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT:
                    return True
                if grid[y + row][x + col]:
                    return True
    return False

def merge_tetromino(grid, tetromino, x, y):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col]:
                grid[y + row][x + col] = 1

def remove_complete_lines(grid):
    lines_removed = 0
    y = GRID_HEIGHT - 1
    while y >= 0:
        if all(grid[y]):
            del grid[y]
            grid.insert(0, [0] * GRID_WIDTH)
            lines_removed += 1
        else:
            y -= 1
    return lines_removed

# Main game loop
async def main():
    clock = pygame.time.Clock()
    move_delay = 70  # Movement delay in milliseconds
    last_move_time = pygame.time.get_ticks()
    rotation_delay = 50000  # Rotation delay in milliseconds
    last_rotation_time = pygame.time.get_ticks()
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    tetromino, color, tetromino_x, tetromino_y = new_tetromino()
    game_over = False
    fall_time = 5
    fall_speed = 5
    speedup = False
    score = 0

    while not game_over:
        screen.fill(BLACK)

        # Handle events#
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and current_time - last_move_time > move_delay:
            tetromino_x -= 1
            if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                tetromino_x += 1
            last_move_time = current_time
        if keys[pygame.K_RIGHT] and current_time - last_move_time > move_delay:
            tetromino_x += 1
            if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                tetromino_x -= 1
            last_move_time = current_time
        if keys[pygame.K_DOWN]:
            tetromino_y += 1
            if check_collision(grid, tetromino, tetromino_x, tetromino_y):
               tetromino_y -= 1
        if keys[pygame.K_UP]:
                if not check_collision(grid, rotated_tetromino, tetromino_x, tetromino_y):
                    tetromino = rotated_tetromino
        if keys[pygame.K_SPACE]:
            while not check_collision(grid, tetromino, tetromino_x, tetromino_y + 1):
                tetromino_y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino_x -= 1
                    if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                        tetromino_x += 1
                elif event.key == pygame.K_RIGHT:
                    tetromino_x += 1
                    if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                        tetromino_x -= 1
                elif event.key == pygame.K_DOWN:
                    tetromino_y += 1
                    if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                        tetromino_y -= 1
                elif event.key == pygame.K_UP:
                    rotated_tetromino = [list(row) for row in zip(*tetromino[::-1])]
                    if not check_collision(grid, rotated_tetromino, tetromino_x, tetromino_y):
                        tetromino = rotated_tetromino
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    speedup = False

        # Move tetromino down
        if pygame.time.get_ticks() - fall_time > 1000 * fall_speed:
            tetromino_y += 1
            if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                tetromino_y -= 1
                merge_tetromino(grid, tetromino, tetromino_x, tetromino_y)
                lines_removed = remove_complete_lines(grid)
                score += lines_removed ** 2
                tetromino, color, tetromino_x, tetromino_y = new_tetromino()
                if check_collision(grid, tetromino, tetromino_x, tetromino_y):
                    game_over = True
            fall_time = pygame.time.get_ticks()

        # Handle speedup
        if speedup:
            fall_speed = 1
        else:
            fall_speed = 0.5

        # Handle rotation with delay
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_UP] and current_time - last_rotation_time > rotation_delay:
            rotated_tetromino = [list(row) for row in zip(*tetromino[::-1])]
            if not check_collision(grid, rotated_tetromino, tetromino_x, tetromino_y):
                tetromino = rotated_tetromino
                last_rotation_time = current_time

        # Draw everything
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if grid[row][col]:
                    draw_block(col, row, tetromino_colors[grid[row][col] - 1])
        draw_tetromino(tetromino, tetromino_x, tetromino_y, color)
        draw_grid()

        # Display score
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (20, 20))

        # Update the display
        pygame.display.update()
        clock.tick(30)

    # Game over message
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)
    await asyncio.sleep(0)


if __name__ == "__main__":
    main()

asyncio.run(main())
