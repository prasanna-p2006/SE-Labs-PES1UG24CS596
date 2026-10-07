
import pygame
import random
from .target import Target

# Game Engine

WHITE = (255, 255, 255)
RED = (220, 60, 60)


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.margin = 60
        self.hud_height = 60

        self.round_seconds = 30
        self.difficulties = {
            "Easy": {
                "base_radius": 50,
                "min_radius": 18,
                "lifespan_frames": 120
            },
            "Medium": {
                "base_radius": 40,
                "min_radius": 12,
                "lifespan_frames": 90
            },
            "Hard": {
                "base_radius": 30,
                "min_radius": 8,
                "lifespan_frames": 60
            }
        }

        self.difficulty = "Medium"

        self.hits = 0
        self.misses = 0
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 26)

        self.game_over = False
        self.should_exit = False

        self.hit_sound = pygame.mixer.Sound("sounds/hit.wav")
        self.miss_sound = pygame.mixer.Sound("sounds/miss.wav")
        self.timeout_sound = pygame.mixer.Sound("sounds/timeout.wav")
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")

        self._start_new_game()

    def _spawn_target(self):
        x = random.randint(self.margin, self.width - self.margin)
        y = random.randint(
            self.margin + self.hud_height,
            self.height - self.margin
        )

        settings = self.difficulties[self.difficulty]

        return Target(
            x,
            y,
            settings["base_radius"],
            settings["min_radius"],
            settings["lifespan_frames"]
        )

    def _start_new_game(self):
        self.hits = 0
        self.misses = 0
        self.score = 0
        self.time_left_frames = self.round_seconds * 60
        self.game_over = False
        self.target = self._spawn_target()

    def handle_event(self, event):
        if self.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.difficulty = "Easy"
                    self._start_new_game()

                elif event.key == pygame.K_2:
                    self.difficulty = "Medium"
                    self._start_new_game()

                elif event.key == pygame.K_3:
                    self.difficulty = "Hard"
                    self._start_new_game()

                elif event.key == pygame.K_4:
                    self.should_exit = True

            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_click(event.pos)

    def _handle_click(self, pos):
        x, y = pos

        if self.target.contains_point(x, y):
            self.hits += 1
            self.score += 1
            self.hit_sound.play()
            self.target = self._spawn_target()
        else:
            self.misses += 1
            self.miss_sound.play()

    def handle_input(self):
        # Reserved for continuously-held-key input; this game is
        # entirely mouse-driven, so there's nothing to poll here.
        pass

    def update(self):
        if self.game_over:
            return

        self.time_left_frames -= 1

        if self.time_left_frames <= 0:
            self.game_over = True
            self.game_over_sound.play()
            return

        self.target.update()

        if self.target.expired():
            self.misses += 1
            self.timeout_sound.play()
            self.target = self._spawn_target()

    def accuracy(self):
        total = self.hits + self.misses

        if total == 0:
            return 0.0

        return round(100 * self.hits / total, 1)

    def render(self, screen):
        if self.game_over:
            game_over_text = self.font.render(
                "GAME OVER",
                True,
                WHITE
            )

            score_text = self.font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            accuracy_text = self.font.render(
                f"Final Accuracy: {self.accuracy()}%",
                True,
                WHITE
            )

            difficulty_text = self.font.render(
                f"Difficulty: {self.difficulty}",
                True,
                WHITE
            )

            easy_text = self.font.render(
                "1 - Easy",
                True,
                WHITE
            )

            medium_text = self.font.render(
                "2 - Medium",
                True,
                WHITE
            )

            hard_text = self.font.render(
                "3 - Hard",
                True,
                WHITE
            )

            exit_text = self.font.render(
                "4 - Exit",
                True,
                WHITE
            )

            screen.blit(
                game_over_text,
                (
                    self.width // 2 - game_over_text.get_width() // 2,
                    60
                )
            )

            screen.blit(
                score_text,
                (
                    self.width // 2 - score_text.get_width() // 2,
                    110
                )
            )

            screen.blit(
                accuracy_text,
                (
                    self.width // 2 - accuracy_text.get_width() // 2,
                    150
                )
            )

            screen.blit(
                difficulty_text,
                (
                    self.width // 2 - difficulty_text.get_width() // 2,
                    190
                )
            )

            screen.blit(
                easy_text,
                (
                    self.width // 2 - easy_text.get_width() // 2,
                    250
                )
            )

            screen.blit(
                medium_text,
                (
                    self.width // 2 - medium_text.get_width() // 2,
                    290
                )
            )

            screen.blit(
                hard_text,
                (
                    self.width // 2 - hard_text.get_width() // 2,
                    330
                )
            )

            screen.blit(
                exit_text,
                (
                    self.width // 2 - exit_text.get_width() // 2,
                    370
                )
            )

            return

        r = int(self.target.visual_radius())

        pygame.draw.circle(
            screen,
            RED,
            (self.target.x, self.target.y),
            r
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (self.target.x, self.target.y),
            r,
            2
        )

        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            WHITE
        )

        screen.blit(score_text, (10, 10))

        seconds_left = max(
            0,
            self.time_left_frames // 60
        )

        timer_text = self.font.render(
            f"Time: {seconds_left}s",
            True,
            WHITE
        )

        screen.blit(
            timer_text,
            (self.width - 140, 10)
        )

        acc_text = self.font.render(
            f"Accuracy: {self.accuracy()}%",
            True,
            WHITE
        )

        screen.blit(
            acc_text,
            (self.width // 2 - 90, 10)
        )