from turtle import *
speed('fastest')
hideturtle()

# The original challenge was to make a Sierpinski drawer that was iterative
# instead of recursive in order to cope with Python's recursion depth limit,
# but after failing to find a way after considerable effort I conjectured that
# it was impossible to convert the recursion relation into an iterative form.
# So, I tried to write a program that passed every edge of the Sierpinski
# triangle once which is possible since the triangle is an Euler graph and
# to use the min. number of moves doing so. A move is a fd/lt/rt command.
# I think my program minimizes the moves (note: I'm assuming you cannot pick up the pen).


# right is a boolean denoting if the previous turn was a right or left one
def draw_sierpinski_recurse(iters, side, right):
    if iters < 2:
        return

    half_side = side/2
    left = not right

    if right:
        lt(60)
    else:
        rt(60)

    for i in range(3):
        fd(half_side)
        
        draw_sierpinski_recurse(iters-1, half_side, left)

        fd(half_side)
        # this is the last side if the triangle
        if i == 2:
            break
        
        if right:
            lt(120)
        else:
            rt(120)

    if right:
        lt(60)
    else:
        rt(60)


# input:
# iters, the number of recursive iterations to perform
# side, the side length of the biggest triangle
# init_x, init_y, init_angle, these are the optional initial conditions for the turtle
def draw_sierpinski_triangle(iters, side, init_x=0, init_y=0, init_angle=0):
    if iters < 1 or side < 0:
        return

    # the initial setup
    up()
    setpos(init_x, init_y)
    down()
    lt(init_angle)

    # draw the big outer triangle
    half_side = side/2
    fd(half_side)
    draw_sierpinski_recurse(iters, half_side, True)
    fd(half_side)
    lt(120)
    fd(side)
    lt(120)
    fd(side)

def main():
    draw_sierpinski_triangle(6, 256, 0, 0, 180)

if __name__ == '__main__':
    main()
