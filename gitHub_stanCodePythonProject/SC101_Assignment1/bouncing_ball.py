"""
File: bounce_ball.py
Name: Linda Zhao
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
run = 0
start = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)

    onmouseclicked(ball_full)


def ball_full(mouse):
    global run, start
    vy = 0  # vertical initial speed
    start = False
    if not start and run < 3:   # make sure mouse click would only effect when ball is at start point.
        start = True
        while ball.x < window.width:
            ball.move(dx=VX, dy=vy)
            vy += GRAVITY
            if ball.y >= window.height - ball.height:
                vy = -vy * REDUCE
            pause(DELAY)
        run += 1
        start = False
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
