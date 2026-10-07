import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Aim Trainer - Pygame Version")

# Colors
DARK_GRAY = (35, 35, 40)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)


def main():
    running = True

    while running:
        SCREEN.fill(DARK_GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            engine.handle_event(event)

        if engine.should_exit:
            running = False

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
