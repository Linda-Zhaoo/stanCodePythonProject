"""
File: draw_line.py
Name: Linda Zhao
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 20

window = GWindow()
click = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    when user click mouse,
    program would judge if it need a circle or connect to previous circle to become a line
    """
    onmouseclicked(point_line)


def point_line(mouse):
    global click
    click += 1
    if click % 2 == 1:
        # if times of mouse click is odd make a circle
        xc = mouse.x - SIZE / 2
        yc = mouse.y - SIZE / 2
        window.add(circle, x=xc, y=yc)
    else:
        # if times of mouse click is even draw a line at last circle's center and remove the last circle
        line = GLine(x0=circle.x+SIZE/2, y0=circle.y+SIZE/2, x1=mouse.x, y1=mouse.y)
        window.add(line)
        window.remove(circle)


if __name__ == "__main__":
    main()
