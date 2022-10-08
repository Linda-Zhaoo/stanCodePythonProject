"""
File: 
Name: Linda Zhao
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(width=900, height=600, title='Dive besides whale')


def main():
    """
    Title: Dive besides a whale
    Love free diving. Hope one day I can meet a whale and dive with it.
    """
    # The background
    sky = GRect(900, 250)
    sky.filled = True
    sky.fill_color = 'azure'
    sky.color = 'azure'
    window.add(sky)

    ocean = GRect(900, 450, x=0, y=251)
    ocean.filled = True
    ocean.fill_color = 'cornflowerblue'
    ocean.color = 'cornflowerblue'
    window.add(ocean)

    # whale body and tail
    whale_body = GArc(400, 650, 0, 180, x=150, y=205)
    whale_body.filled = True
    whale_body.fill_color = 'steelblue'
    window.add(whale_body)

    whale_lower_body = GArc(600, 300, 180, 180, x=150, y=300)
    whale_lower_body.filled = True
    whale_lower_body.fill_color = 'steelblue'
    window.add(whale_lower_body)

    tail = GPolygon()
    tail.add_vertex((560, 368))
    tail.add_vertex((750, 368))
    tail.add_vertex((730, 250))
    tail.filled = True
    tail.fill_color = 'steelblue'
    window.add(tail)

    tail_l = GPolygon()
    tail_l.add_vertex((650, 180))
    tail_l.add_vertex((678, 280))
    tail_l.add_vertex((723, 250))
    tail_l.add_vertex((700, 240))
    tail_l.filled = True
    tail_l.fill_color = 'steelblue'
    window.add(tail_l)

    tail_r = GPolygon()
    tail_r.add_vertex((735, 251))
    tail_r.add_vertex((742, 290))
    tail_r.add_vertex((850, 245))
    tail_r.add_vertex((760, 255))
    tail_r.filled = True
    tail_r.fill_color = 'steelblue'
    window.add(tail_r)

    # whale eye
    whale_eye = GOval(20, 20, x=200, y=320)
    whale_eye.filled = True
    whale_eye.fill_color = 'black'
    window.add(whale_eye)

    whale_eye_white = GOval(13, 13, x=201, y=321)
    whale_eye_white.filled = True
    whale_eye_white.fill_color = 'white'
    window.add(whale_eye_white)

    # whale mouth and teeth
    whale_mouth = GArc(800, 300, 180, 100, x=150, y=300)
    whale_mouth.filled = True
    whale_mouth.fill_color = 'lightcyan'
    window.add(whale_mouth)

    teeth_1 = GLine(x0=170, y0=376, x1=174, y1=410)
    window.add(teeth_1)

    teeth_2 = GLine(x0=210, y0=376, x1=215, y1=427)
    window.add(teeth_2)

    teeth_3 = GLine(x0=250, y0=376, x1=257, y1=438)
    window.add(teeth_3)

    teeth_4 = GLine(x0=290, y0=376, x1=298, y1=445)
    window.add(teeth_4)

    teeth_5 = GLine(x0=330, y0=376, x1=338, y1=449)
    window.add(teeth_5)

    teeth_6 = GLine(x0=370, y0=376, x1=380, y1=452)
    window.add(teeth_6)

    # fountain
    fountain_center = GRect(15, 120, x=345, y=120)
    fountain_center.filled = True
    fountain_center.fill_color = 'paleturquoise'
    fountain_center.color = 'paleturquoise'
    window.add(fountain_center)

    fountain_top = GPolygon()
    fountain_top.add_vertex((280, 90))
    fountain_top.add_vertex((350, 120))
    fountain_top.add_vertex((360, 120))
    fountain_top.add_vertex((430, 90))
    fountain_top.add_vertex((380, 95))
    fountain_top.add_vertex((355, 70))
    fountain_top.add_vertex((330, 95))
    fountain_top.filled = True
    fountain_top.fill_color = 'paleturquoise'
    fountain_top.color = 'paleturquoise'
    window.add(fountain_top)

    fountain_l = GPolygon()
    fountain_l.add_vertex((325, 115))
    fountain_l.add_vertex((338, 120))
    fountain_l.add_vertex((348, 140))
    fountain_l.filled = True
    fountain_l.fill_color = 'paleturquoise'
    fountain_l.color = 'paleturquoise'
    window.add(fountain_l)

    fountain_r = GPolygon()
    fountain_r.add_vertex((385, 115))
    fountain_r.add_vertex((372, 120))
    fountain_r.add_vertex((362, 140))
    fountain_r.filled = True
    fountain_r.fill_color = 'paleturquoise'
    fountain_r.color = 'paleturquoise'
    window.add(fountain_r)

    fountain_w1 = GPolygon()
    fountain_w1.add_vertex((280, 75))
    fountain_w1.add_vertex((320, 85))
    fountain_w1.add_vertex((330, 80))
    fountain_w1.add_vertex((300, 65))
    fountain_w1.filled = True
    fountain_w1.fill_color = 'paleturquoise'
    fountain_w1.color = 'paleturquoise'
    window.add(fountain_w1)

    fountain_w2 = GPolygon()
    fountain_w2.add_vertex((440, 70))
    fountain_w2.add_vertex((400, 80))
    fountain_w2.add_vertex((390, 75))
    fountain_w2.add_vertex((435, 65))
    fountain_w2.filled = True
    fountain_w2.fill_color = 'paleturquoise'
    fountain_w2.color = 'paleturquoise'
    window.add(fountain_w2)

    fountain_w3 = GPolygon()
    fountain_w3.add_vertex((332, 40))
    fountain_w3.add_vertex((335, 65))
    fountain_w3.add_vertex((347, 70))
    fountain_w3.add_vertex((350, 50))
    fountain_w3.filled = True
    fountain_w3.fill_color = 'paleturquoise'
    fountain_w3.color = 'paleturquoise'
    window.add(fountain_w3)

    fountain_w4 = GPolygon()
    fountain_w4.add_vertex((375, 40))
    fountain_w4.add_vertex((365, 65))
    fountain_w4.add_vertex((377, 70))
    fountain_w4.add_vertex((390, 50))
    fountain_w4.filled = True
    fountain_w4.fill_color = 'paleturquoise'
    fountain_w4.color = 'paleturquoise'
    window.add(fountain_w4)

    fountain_w5 = GPolygon()
    fountain_w5.add_vertex((200, 80))
    fountain_w5.add_vertex((280, 85))
    fountain_w5.add_vertex((270, 80))
    fountain_w5.add_vertex((210, 75))
    fountain_w5.filled = True
    fountain_w5.fill_color = 'paleturquoise'
    fountain_w5.color = 'paleturquoise'
    window.add(fountain_w5)

    fountain_w6 = GPolygon()
    fountain_w6.add_vertex((530, 85))
    fountain_w6.add_vertex((510, 90))
    fountain_w6.add_vertex((430, 85))
    fountain_w6.add_vertex((430, 80))
    fountain_w6.filled = True
    fountain_w6.fill_color = 'paleturquoise'
    fountain_w6.color = 'paleturquoise'
    window.add(fountain_w6)

    fountain_w7 = GPolygon()
    fountain_w7.add_vertex((270, 40))
    fountain_w7.add_vertex((300, 50))
    fountain_w7.add_vertex((295, 55))
    fountain_w7.add_vertex((260, 45))
    fountain_w7.filled = True
    fountain_w7.fill_color = 'paleturquoise'
    fountain_w7.color = 'paleturquoise'
    window.add(fountain_w7)

    fountain_w8 = GPolygon()
    fountain_w8.add_vertex((410, 52))
    fountain_w8.add_vertex((458, 37))
    fountain_w8.add_vertex((465, 42))
    fountain_w8.add_vertex((420, 57))
    fountain_w8.filled = True
    fountain_w8.fill_color = 'paleturquoise'
    fountain_w8.color = 'paleturquoise'
    window.add(fountain_w8)

    # People
    head = GOval(50, 30, x=400, y=500)
    head.filled = True
    head.fill_color = 'mediumvioletred'
    head.color = 'mediumvioletred'
    window.add(head)

    face = GOval(30, 10, x=405, y=520)
    face.filled = True
    face.fill_color = 'bisque'
    face.color = 'bisque'
    window.add(face)

    neck = GRect(10, 15, x=445, y=510)
    neck.filled = True
    neck.fill_color = 'mediumvioletred'
    neck.color = 'mediumvioletred'
    window.add(neck)

    arm_r = GPolygon()
    arm_r.add_vertex((460, 505))
    arm_r.add_vertex((460, 515))
    arm_r.add_vertex((515, 495))
    arm_r.add_vertex((515, 485))
    arm_r.filled = True
    arm_r.fill_color = 'deeppink'
    arm_r.color = 'deeppink'
    window.add(arm_r)

    hand_r = GOval(10, 10, x=517, y=483)
    hand_r.filled = True
    hand_r.fill_color = 'bisque'
    hand_r.color = 'bisque'
    window.add(hand_r)

    torso = GRect(70, 30, x=450, y=500)
    torso.filled = True
    torso.fill_color = 'mediumvioletred'
    torso.color = 'mediumvioletred'
    window.add(torso)

    leg_u = GPolygon()
    leg_u.add_vertex((510, 500))
    leg_u.add_vertex((515, 510))
    leg_u.add_vertex((565, 502))
    leg_u.add_vertex((565, 492))
    leg_u.filled = True
    leg_u.fill_color = 'mediumvioletred'
    leg_u.color = 'mediumvioletred'
    window.add(leg_u)

    leg_u1 = GPolygon()
    leg_u1.add_vertex((610, 482))
    leg_u1.add_vertex((615, 485))
    leg_u1.add_vertex((565, 502))
    leg_u1.add_vertex((565, 492))
    leg_u1.filled = True
    leg_u1.fill_color = 'mediumvioletred'
    leg_u1.color = 'mediumvioletred'
    window.add(leg_u1)

    fin_u = GArc(100, 20, 45, 160, x=610, y=475)
    fin_u.filled = True
    window.add(fin_u)

    leg_d = GPolygon()
    leg_d.add_vertex((510, 515))
    leg_d.add_vertex((515, 525))
    leg_d.add_vertex((565, 530))
    leg_d.add_vertex((565, 520))
    leg_d.filled = True
    leg_d.fill_color = 'mediumvioletred'
    leg_d.color = 'mediumvioletred'
    window.add(leg_d)

    leg_d1 = GPolygon()
    leg_d1.add_vertex((610, 512))
    leg_d1.add_vertex((615, 515))
    leg_d1.add_vertex((565, 530))
    leg_d1.add_vertex((565, 520))
    leg_d1.filled = True
    leg_d1.fill_color = 'mediumvioletred'
    leg_d1.color = 'mediumvioletred'
    window.add(leg_d1)

    fin_d = GArc(80, 30, 180, 160, x=610, y=508)
    fin_d.filled = True
    window.add(fin_d)

    arm_l = GPolygon()
    arm_l.add_vertex((460, 515))
    arm_l.add_vertex((460, 525))
    arm_l.add_vertex((515, 535))
    arm_l.add_vertex((515, 525))
    arm_l.filled = True
    arm_l.fill_color = 'deeppink'
    arm_l.color = 'deeppink'
    window.add(arm_l)

    hand_l = GOval(10, 10, x=517, y=525)
    hand_l.filled = True
    hand_l.fill_color = 'bisque'
    hand_l.color = 'bisque'
    window.add(hand_l)

    # goggle
    goggle1 = GOval(10, 5, x=410, y=527)
    window.add(goggle1)

    goggle2 = GOval(12, 7, x=409, y=520)
    window.add(goggle2)

    goggle3 = GRect(2, 18, x=414, y=502)
    goggle3.filled = True
    window.add(goggle3)

    straw = GRect(2, 35, x=428, y=485)
    straw.filled = True
    straw.fill_color = 'midnightblue'
    straw.color = 'midnightblue'
    window.add(straw)

    straw1 = GArc(3, 15, 180, 270, x=427, y=515)
    straw1.filled = True
    straw1.fill_color = 'midnightblue'
    straw1.color = 'midnightblue'
    window.add(straw1)

    # small fish
    fish_body = GOval(40, 25, x=50, y=500)
    fish_body.filled = True
    fish_body.fill_color = 'moccasin'
    window.add(fish_body)

    fish_tail = GPolygon()
    fish_tail.add_vertex((90, 512))
    fish_tail.add_vertex((110, 525))
    fish_tail.add_vertex((110, 500))
    fish_tail.filled = True
    fish_tail.fill_color = 'moccasin'
    window.add(fish_tail)

    fish2_body = GOval(40, 25, x=150, y=530)
    fish2_body.filled = True
    fish2_body.fill_color = 'salmon'
    window.add(fish2_body)

    fish2_tail = GPolygon()
    fish2_tail.add_vertex((190, 542))
    fish2_tail.add_vertex((210, 555))
    fish2_tail.add_vertex((210, 530))
    fish2_tail.filled = True
    fish2_tail.fill_color = 'salmon'
    window.add(fish2_tail)

    jellyfish = GArc(60, 40, 40, 180, x=800, y=350)
    jellyfish.filled = True
    jellyfish.fill_color = 'lightcyan'
    window.add(jellyfish)

    jellyfish_hand1 = GArc(120, 80, 180, 90, x=815, y=360)
    window.add(jellyfish_hand1)

    jellyfish_hand2 = GArc(120, 80, 180, 90, x=825, y=355)
    window.add(jellyfish_hand2)

    jellyfish_hand3 = GArc(120, 80, 180, 90, x=840, y=350)
    window.add(jellyfish_hand3)

    jellyfish_hand4 = GArc(120, 80, 180, 90, x=850, y=340)
    window.add(jellyfish_hand4)


if __name__ == '__main__':
    main()
