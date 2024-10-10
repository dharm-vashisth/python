from dataclasses import dataclass


@dataclass
class Rectangle:
    length: float
    breadth: float

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

@dataclass(frozen=True) # parameters values become immutable
class Square:
    side: float

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4*self.side

def main():
    rectangle = Rectangle(10,20)
    print(f"Area of Rectangle is {rectangle.area()} and perimeter is {rectangle.perimeter()}")
    rectangle.length = 20 # allowed
    rectangle.breadth = 40 # allowed
    print(f"Area of Rectangle is {rectangle.area()} and perimeter is {rectangle.perimeter()}")
    square = Square(10)
    print(f"Area of Square is {square.area()} and perimeter is {square.perimeter()}")
    # square.side=20 # it will throw exception as reassignment is not possible.
    # print(f"Area of Square is {square.area()} and perimeter is {square.perimeter()}")


if __name__ == "__main__":
    main()