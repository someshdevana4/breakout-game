import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game 🎮")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2,
                     SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_RADIUS = 8
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                   BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [4, -4]

# Bricks
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
bricks = []
for row in range(6):
    for col in range(10):
        brick = pygame.Rect(col * (BRICK_WIDTH + 5) + 35,
                            row * (BRICK_HEIGHT + 5) + 50,
                            BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Clock
clock = pygame.time.Clock()


def draw():
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, BLUE, paddle)
    pygame.draw.ellipse(SCREEN, RED, ball)
    for brick in bricks:
        pygame.draw.rect(SCREEN, GREEN, brick)
    score_text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))
    pygame.display.flip()


# Game loop
running = True
while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.move_ip(6, 0)

    # Ball movement
    ball.move_ip(ball_speed)

    # Collisions with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= SCREEN_HEIGHT:
        print("Game Over! Final Score:", score)
        running = False

    # Collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Collision with bricks
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed[1] = -ball_speed[1]
        score += 10

    draw()

pygame.quit()
sys.exit()
