"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    this is a game, target to vanish all the brick on the window.
    the program would get the ball velocity from 'breakoutgraphics', and there are three lives to win the game.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    brick_count = graphics.brick_count
    vx = graphics.get_dx()
    vy = graphics.get_dy()
    # Add the animation loop here!
    while True:
        if graphics.start and lives > 0 and brick_count > 0:
            graphics.ball.move(vx, vy)
            pause(FRAME_RATE)
            # check ball touch which side of the window, if touch bottom side, game reset or game over.
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                lives -= 1
                graphics.window.remove(graphics.ball)
                graphics.reset_ball()
                vx = graphics.get_dx()
                vy = graphics.get_dy()

            # check if ball touch the paddle
            ball_top_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            ball_top_right = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
            ball_bottom_right = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y +
                                                              graphics.ball.height)
            ball_bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
            if ball_top_left is not None:
                if ball_top_left is not graphics.paddle:
                    graphics.window.remove(ball_top_left)
                    vy = -vy
                    brick_count -= 1
                if ball_top_left is graphics.paddle and vy > 0:
                    vy = -vy
            elif ball_top_right is not None:
                if ball_top_right is not graphics.paddle:
                    graphics.window.remove(ball_top_right)
                    vy = -vy
                    brick_count -= 1
                if ball_top_right is graphics.paddle and vy > 0:
                    vy = -vy
            elif ball_bottom_left is not None:
                if ball_bottom_left is not graphics.paddle:
                    graphics.window.remove(ball_bottom_left)
                    vy = -vy
                    brick_count -= 1
                if ball_bottom_left is graphics.paddle and vy > 0:
                    vy = -vy
            elif ball_bottom_right is not None:
                if ball_bottom_right is not graphics.paddle:
                    graphics.window.remove(ball_bottom_right)
                    vy = -vy
                    brick_count -= 1
                if ball_bottom_right is graphics.paddle and vy > 0:
                    vy = -vy
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
