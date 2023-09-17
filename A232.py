import turtle

# Function to draw a node in the decision tree
def draw_node(turtle, label, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.color('black')
    turtle.write(label, align='center', font=('Arial', 12, 'bold'))

# Function to draw an arrow
def draw_arrow(turtle, x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.color('black')
    turtle.width(2)
    turtle.goto(x2, y2)

# Recursive function to draw the decision tree
def draw_decision_tree(tree, x, y):
    if isinstance(tree, dict):
        label = next(iter(tree))
        draw_node(turtle, label, x, y)
        children = tree[label]
        width = len(children) * 100
        next_x = x - width / 2
        next_y = y - 100
        for child in children:
            draw_arrow(turtle, x, y-30, next_x, next_y+30)
            draw_decision_tree(child, next_x, next_y)
            next_x += 100
    else:
        draw_node(turtle, tree, x, y)

# Example decision tree
decision_tree = {
    'Outlook': {
        'Sunny': 'No',
        'Overcast': 'Yes',
        'Rainy': {
            'Wind': {
                'Weak': 'Yes',
                'Strong': 'No'
            }
        }
    }
}

# Initialize Turtle
turtle.setup(800, 600)
screen = turtle.Screen()
turtle.speed(0)

# Draw the decision tree
draw_decision_tree(decision_tree, 0, 200)

# Hide Turtle cursor after drawing
turtle.hideturtle()

# Close the Turtle graphics window
turtle.done()
