from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

# Draw leaves
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

# Draw flower center
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

# Define points to draw letters
def point(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(4), end_fill()

# Function to draw 'T'
def draw_T(x, y):
    positions_t = [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30), (x+24, y+30),
                   (x+12, y+30), (x+12, y+24), (x+12, y+18), (x+12, y+12), (x+12, y+6), (x+12, y)]

    for pos in positions_t:
        point(*pos)

# 
# x0y30   x6y30   x12/y30   x18y30   x24y30
#                 x12y24
#                 x12y18
#                 x12y12  
#                 x12y6
#                 x12y0  
#   

# Function to draw 'Ú'
def draw_U(x, y):
    positions_u = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6),
                   (x+3, y+3), (x+6, y), (x+12, y-1), (x+18, y), (x+21, y+3),
                   (x+24, y+6), (x+24, y+12), (x+24, y+18), (x+24, y+24), (x+24, y+30),
                   (x+12, y+36), (x+16, y+40)]

    for pos in positions_u:
        point(*pos)

#
#               x16y40
#           x12y36
# x0y30                 x24y30
# x0y24                 x24y24
# x0y18                 x24y18
# x0y12                 x24y12
# x0y6                  x24y6
#     x3y3           x21y3
#        x6y0   x18y0 
#           x12y-1
#

# Function to draw 'I'
def draw_I(x, y):
    positions_i = [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30), (x+24, y+30),
                   (x+12, y+30), (x+12, y+24), (x+12, y+18), (x+12, y+12), (x+12, y+6), (x+12, y+0),
                   (x+0, y+0), (x+6, y+0), (x+12, y+0), (x+18, y+0), (x+24, y+0)]

    for pos in positions_i:
        point(*pos)

#
#   x0y30   x6y30   x12y30   x18y30   x24y30
#                   x12y24
#                   x12y18
#                   x12y12
#                   x12y6
#   x0y0    x6y0    x12y0    x18y0    x24y0
#

# Draw 'TÚ'
    #draw_T(-27, -20)
    #draw_U(7, -20)
# Draw 'I'
draw_I(-9, -20)

hideturtle()
done()