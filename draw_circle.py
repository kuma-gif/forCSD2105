import matplotlib.pyplot as plt

def draw_circle(radius):
    x = 0
    y = radius
    
    d = 1-radius

    points = [(x, y)]

    while x <= y:
        x += 1
        if d < 0:
            
            d = d + 2 * x  + 1
        else:
          
            d = d + 2 * (x - y) + 1
            y -= 1

        points.extend([(x, y), (x, -y), (-x, y), (-x, -y),
                       (y, x), (-y, x), (y, -x), (-y, -x)])

    return points

def plot_circle(points):
    fig, ax = plt.subplots()
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    ax.scatter(x_values, y_values, marker='.')
    ax.axis('equal')

    plt.show()

# Input radius
radius = int(input("Enter the radius of the circle: "))
circle_points = draw_circle(radius)
plot_circle(circle_points)