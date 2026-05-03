from pygame import *

init()

WIDTH, HEIGHT = 700, 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping Pong")

background = transform.scale(image.load("background.jpg"), (WIDTH, HEIGHT))

clock = time.Clock()
FPS = 60

font.init()
lose_font = font.SysFont("Arial", 50)
score_font = font.SysFont("Arial", 30)


class Racket:
    def __init__(self, x, y, w, h, speed):
        self.rect = Rect(x, y, w, h)
        self.speed = speed

    def move_racket1(self, keys):
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

    def move_racket2(self, ball):
        if self.rect.centery < ball.rect.centery and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        elif self.rect.centery > ball.rect.centery and self.rect.top > 0:
            self.rect.y -= self.speed

    def draw(self, color):
        draw.rect(window, color, self.rect)


class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.radius = radius
        self.rect = Rect(x, y, radius * 2, radius * 2)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self, left_racket, right_racket):
        hit_left = False
        hit_right = False

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

        if self.rect.colliderect(left_racket.rect):
            self.speed_x *= -1
            hit_left = True

        if self.rect.colliderect(right_racket.rect):
            self.speed_x *= -1
            hit_right = True

        return hit_left, hit_right

    def draw(self):
        draw.circle(
            window,
            (255, 255, 255),
            (self.rect.centerx, self.rect.centery),
            self.radius
        )


left_racket = Racket(10, 200, 20, 100, 10)
right_racket = Racket(670, 200, 20, 100, 10)
ball = Ball(WIDTH // 2, HEIGHT // 2, 25, 10, 10)

left_score = 0
right_score = 0

game = True
result_text = None

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()

    left_racket.move_racket1(keys)
    right_racket.move_racket2(ball)

    ball.move()
    hit_left, hit_right = ball.bounce(left_racket, right_racket)

    if hit_left:
        left_score += 1
    if hit_right:
        right_score += 1

    if ball.rect.left <= 0:
        result_text = lose_font.render("LOSE", True, (255, 0, 0))
        game = False

    if ball.rect.right >= WIDTH:
        result_text = lose_font.render("WIN!", True, (255, 255, 0))
        game = False

    window.blit(background, (0, 0))

    left_racket.draw((84, 0, 120))
    right_racket.draw((2, 207, 230))
    ball.draw()

    score_text = score_font.render(f"{left_score} : {right_score}", True, (255, 255, 255))
    window.blit(score_text, (WIDTH // 2 - 40, 20))

    display.update()
    clock.tick(FPS)


window.blit(background, (0, 0))

if result_text:
    window.blit(result_text, (285, 200))

display.update()
time.delay(3000)
quit()