from pygame import *

init()

window = display.set_mode((700, 500))
display.set_caption("ping pong")

background = transform.scale(image.load("background.jpg"), (700, 500))
ball = transform.scale(image.load("ball.jpg"), (100, 100))

clock = time.Clock()
FPS = 60

game = True
finish = False

ball_x = 700 // 2 - 50
ball_y = 500 // 2 - 50

left_rect = Rect(10, 200, 20, 100)
right_rect = Rect(670, 200, 20, 100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        window.blit(ball, (ball_x, ball_y))

        draw.rect(window, (255, 255, 255), left_rect)
        draw.rect(window, (255, 255, 255), right_rect)

    display.update()
    clock.tick(FPS)

