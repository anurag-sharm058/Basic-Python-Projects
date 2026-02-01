# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image2.jpg', 30 )
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171),
              (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.shape("arrow")
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(200)
tim.setheading(0)

# <================================= MY CODE ======================================>
# def draw_dot():
#     for _ in range(10):
#         dot_color = random.choice(color_list)
#         tim.dot(20,dot_color)
#         tim.forward(50)
# for i in range(10):
#     draw_dot()
#     tim.setheading(90)
#     tim.forward(50)
#     tim.setheading(180)
#     tim.forward(500)
#     tim.setheading(0)


# <================================= MY TUTOR CODE ======================================>

num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.getcanvas()
screen.exitonclick()
