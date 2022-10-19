from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, p):
        return sqrt((p.x-self.x)**2 + (p.y-self.y)**2)

    def abs(self):
        return self.dist_to(Point(0, 0))

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rectangle:

    def __init__(self, p1, p2):
        self.p_tl = Point(min(p1.x, p2.x), max(p1.y, p2.y))
        self.p_br = Point(max(p1.x, p2.x), min(p1.y, p2.y))

    def area(self):
        return (self.p_br.x-self.p_tl.x)*(self.p_tl.y-self.p_br.y)

    def center(self):
        return Point((self.p_tl.x + self.p_br.x)/2,
                     (self.p_tl.y + self.p_br.y)/2)

def main():
    p1 = Point(3.0, 4.0)
    print(f"The point ({p1.x}, {p1.y}) is at a distance of {p1.abs()} from the origin.")

    p2 = Point(-1.0, 6.5)
    print(f"It is a distance {p1.dist_to(p2):.5} away from the point ({p2.x}, {p2.y}).")

    test_rect = Rectangle(p1, Point(0, 0))
    print(f"My rectangle has an aread of {test_rect.area()}")

    print(f"It's center is at {test_rect.center()}")

if __name__ == "__main__":
    main()