import turtle

def triangler(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)

def trianglel(edge=100):
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)

def reverseUp(edge=100):
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)

def reverseDown(edge = 100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.fd(edge)
    turtle.right(120)
    turtle.fd(edge)

triangler()
turtle.left(120)
trianglel()
turtle.left(60)
reverseUp()
reverseDown()
turtle.left(120)
triangler()
turtle.left(120)
reverseUp()

