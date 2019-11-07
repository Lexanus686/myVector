import math

class Point:
    """ Create a 2-dimensional Point """

    def __init__(self, *args):
        assert len(args) != 1 and len(args) <= 2, "You need to write 1 tuple or 2 args."
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        for i in range(len(self.values)):
            yield self.values[i]

    def __getitem__(self, item):
        return self.values[item]

    def __eq__(self, other):
        return self.values == other.values

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.values[0] + other.values[0], self.values[1] + other.values[1])
        else:
            return Point(self.values[0] + other, self.values[1] + other)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.values[0] - other.values[0], self.values[1] - other.values[1])
        else:
            return Point(self.values[0] - other, self.values[1] - other)

    def __mul__(self, number):
        return Point(self.values[0] * number, self.values[1] * number)

    def __truediv__(self, number):
        return Point(self.values[0] / number, self.values[1] / number)

    def __str__(self):
        return "(" + str(self.values[0]) + "," + str(self.values[1]) + ")"

class Vector:

    def __init__(self, *args):
        """ Create a vector, example: v = Vector((1,2)) """
        assert len(args) == 1 or len(args) == 2, "You need 1 or 2 arguments"

        assert len(args[0]) == 2 and isinstance(args[0], tuple) or isinstance(
            args[0], Point), "If you write 1 argument, make it 2-length tuple or standard Point (1)"

        if len(args) == 2:
            assert not (isinstance(args[0], int) or isinstance(
                args[1], int)), "You need 2 arguments to be tuple or Point (0)"
            assert len(args[1]) == 2 and isinstance(args[1], tuple) or isinstance(
                args[1], Point), "If you write 1 argument, make it 2-length tuple or standard Point (2)"

        if len(args) == 1:
            self.values = (Point(0, 0), args[0])
        else:
            self.values = args

    def __str__(self):
        out = '('
        for number in range(len(self.values)):
            out += str(self.values[number]) + ','
        out = out[0:-1] + ')'
        return out

    def norm(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum((second-first)**2 for first, second in zip(self.values[0], self.values[1])))

    def projection_x(self):
        """ Returns the projection on axis x"""
        return self.values[1][0] - self.values[0][0]


    def projection_y(self):
        """ Returns the projection on axis y"""
        return self.values[1][1] - self.values[0][1]

    def angle(self):
        """ Returns the argument of the vector, the angle clockwise in direction of +x in [0,180]."""
        arg_in_rad = math.asin(self.projection_x()/self.norm())
        arg_in_deg = math.degrees(arg_in_rad)

        if self.projection_x() < 0:
            return 180 + arg_in_deg
        else:
            return arg_in_deg

    """ Description: function takes Vector as an input and
            returns in output vector which norm function is equal to 1.
    
        Returns: Vector(x, y) -- new vector
    """
    def normalize(self):
        normedBeg = (self.values[0][0]/self.norm(),
                     self.values[1][0]/self.norm())
        normedEnd = (self.values[0][1]/self.norm(),
                     self.values[1][1]/self.norm())
        return Vector(normedBeg, normedEnd)

    def rotate2D(self, theta):
        """Rotate vector2D by theta in degrees"""
        theta = math.radians(theta)
        dc, ds = math.cos(theta), math.sin(theta)
        first, second = self.values[0][0], self.values[0][1]
        x, y = self.values[1][0], self.values[1][1]
        x, y = dc*x - ds*y, dc*x + dc*y
        return Vector((first, second), (x, y))

    def fRead(self, fileName):
        file = open(fileName, 'r')
        line = file.read()
        tmp0 = Point(tuple(line.split(';')[0])[1], tuple(line.split(';')[0])[3])
        tmp1 = Point(tuple(line.split(';')[1])[1], tuple(line.split(';')[1])[3])
        return Vector(tmp0, tmp1) 

    def fWrite(self, fileName):
        file = open(fileName, 'w') 
        line = str(self.values[0]) + ';' + str(self.values[1])
        file.write(line)
        pass

    def reverseDirection(self): 
        return Vector(self.values[1], self.values[0])

    def reverseByXAxis(self):
        return Vector(Point(self.values[0][0], -self.values[0][1]), Point(self.values[1][0], -self.values[1][1]))

    def reverseByYAxis(self): 
        return Vector(Point(-self.values[0][0], self.values[0][1]), Point(-self.values[1][0], self.values[1][1]))

class VectorError(ValueError):
    pass

if __name__ == "__main__":
    a1 = Point(2, -2)
    # print((a1+3) == Point(5, 1))
    v = Vector(a1, (4, -4))
    v = v.reverseByXAxis()
    print(v)
    # v1 = v.fRead('my.txt')
    # print(v1)
    # print(v.norm())
    # print(v.angle())
    # print(v.normalize())
    # print(v.rotate2D(15))