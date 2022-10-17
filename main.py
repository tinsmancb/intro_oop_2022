from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, p):
        pass

    def abs(self):
        pass


class Rectangle:
    pass


def main():
    p1 = Point(3.0, 4.0)
    print(f"The point ({p1.x}, {p1.y}) is at a distance of {p1.abs()} from the origin.")

    p2 = Point(-1.0, 6.5)
    print(f"It is a distance {p1.dist_do(p2):.5} away from the point ({p2.x}, {p2.y}).")


if __name__ == "__main__":
    main()