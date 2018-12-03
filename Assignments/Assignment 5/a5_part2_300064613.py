class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:

    def __init__(self, pbottom_left=(0,0), ptop_right=(0,0), color="red"):
        """(Point(number,number), Point(number, number), str)->none
        Initializes the rectangle object with a bottom left point, a top right point, and a color."""
        self.bl = pbottom_left
        self.tr = ptop_right
        self.col = color

    def get_bottom_left(self):
        """(Rectangle)->Point(number, number)
        returns the bottom left Point object of the rectangle."""
        return self.bl

    def get_top_right(self):
        """(Rectangle)-> Point(number, nnumber)
        returns the top right Point object of the rectangle."""
        return self.tr

    def get_color(self):
        """(Rectangle)->str
        returns the color of the Rectangle object as a string."""
        return self.col

    def reset_color(self, col):
        """(Rectangle, str)->none
        Changes the color of the Rectangle to the given String."""
        self.col=col

    def get_perimeter(self):
        """(Rectangle)->number
        returns the perimeter of the Rectangle object"""
        return (self.tr.x-self.bl.x)*2+(self.tr.y-self.bl.y)*2

    def get_area(self):
        """(Rectangle)->number
        returns the area of the Rectangle object"""
        return (self.tr.x-self.bl.x)*(self.tr.y-self.bl.y)

    def move(self, dx, dy):
        """(Rectangle, number, number)->none
        changes the x and y coordinates of the top right and the bottom left points of the rectangle."""
        self.tr.move(dx, dy)
        self.bl.move(dx, dy)

    def intersects(self, other):
        """(Rectangle, Rectangle)->bool
        returns True if two Rectangle objects intersect and False if otherwise."""
        return (self.bl.x<=other.bl.x<=self.tr.x and self.bl.y<=other.bl.y<=self.tr.y) or (self.bl.x<=other.tr.x<=self.tr.x and self.bl.y<=other.tr.y<=self.tr.y)

    def contains(self, x, y):
        """(Rectangle, number, number)->bool
        returns True if the Rectangle object contains a point within its perimeter and false otherwise."""
        return (self.bl.x<=x<=self.tr.x and self.bl.y<=y<=self.tr.y)

    def __repr__(self):
        '''(Rectangle)->str
        retrurns canonical representation of the Rectangle(Point(x, y), Point(x, y), color).
        '''
        return "Rectangle({}, {}, '{}')".format(self.bl, self.tr, self.col)
    def __str__(self):
        '''(Rectnalge)->str
        Returns nice string representation of the Rectangle object.
        _'''
        return "I am a {} rectangle with a bottom left corner at {} and top right corner at {}.".format(self.col, self.bl.get(), self.tr.get())

    def __eq__(self, other):
        """(Rectangle, Rectangle)->bool
        returns True if the two rectangles have the same points and color."""
        return self.tr == other.tr and self.bl == other.bl and self.col == other.col


class Canvas:

    def __init__(self, collection=[]):
        """(Canvas, list)->none
        Initializes the canvas Object with an optional parameter for the collection of objects (list)."""
        self.col=collection

    def add_one_rectangle(self, rect):
        """(Canvas, Rectangle)->none
        Adds given Rectangle object into the list held in the Canvas object."""
        self.col.append(rect)

    def count_same_color(self, color):
        """(Canvas, str)->int
        returns the number of rectangles that are of given color."""
        counter=0
        for rect in self.col:
            if rect.col == color:
                counter+=1
        return counter

    def total_perimeter(self):
        """(Canvas)->number
        returns the total perimeter of all the Rectangle objects in the Canvas"""
        total=0
        for rect in self.col:
            total+=rect.get_perimeter
        return total

    def min_enclosing_rectangle(self):
        """(Canvas)->Rectangle
        returns the Rectangle object as a smallest rectangle able to enclose all rectangles in the Canvas object."""
        minx=self.col[0].bl.x
        miny=self.col[0].bl.x

        maxx=self.col[0].tr.y
        maxy=self.col[0].tr.y

        for rect in self.col:
            if rect.bl.x<minx:
                minx=rect.bl.x
            if rect.bl.y<miny:
                miny=rect.bl.y
            if rect.tr.x>maxx:
                maxx=rect.tr.x
            if rect.tr.y>maxy:
                maxy=rect.tr.y
        return Rectangle(Point(minx, miny), Point(maxx, maxy))

    def common_point(self):
        """(Canvas)->bool
        returns True if all the Rectangles in the Canvas contain a same Point and False if otherwise."""
        tf=""
        for i in range(len(self.col)-1):
            for j in range(i, len(self.col)-1):
                if not self.col[i].intersects(self.col[j]):
                    tf+="f"
        if tf!="":
            return False
        return True

    def __repr__(self):
        """(Canvas)->str
        returns the canonical representation of Canvas(list)"""
        return "Canvas({})".format(self.col)

    def __len__(self):
        """Canvas->int
        returns the number of Rectangle Objects that exist in the Canvas object."""
        return len(self.col)