import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Levels
grid_size = 40
LEVELS = [
    [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
]

def draw_grid(level):
    """Draw the maze grid on the screen."""
    for row_index, row in enumerate(level):
        for col_index, cell in enumerate(row):
            color = BLACK if cell == 1 else WHITE
            pygame.draw.rect(
                screen,
                color,
                (col_index * grid_size, row_index * grid_size, grid_size, grid_size)
            )

def show_start_screen():
    """Display the start screen."""
    screen.fill(WHITE)
    title_text = font.render("Welcome to the Maze Game!", True, BLACK)
    instruction_text = small_font.render("Press SPACE to Start", True, BLACK)
    screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width()) // 2, SCREEN_HEIGHT // 3))
    screen.blit(instruction_text, ((SCREEN_WIDTH - instruction_text.get_width()) // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    # Wait for the player to press SPACE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

def main():
    """Main game loop."""
    # Show the start screen
    show_start_screen()

    # Load the first level
    level = LEVELS[0]

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw the maze
        draw_grid(level)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
