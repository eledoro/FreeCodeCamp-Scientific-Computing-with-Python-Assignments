# ======  class Rectangle ======
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def set_height(self, height):
        self.height = height

    def set_width(self, w):
        self.width = w

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                picture += '*' * self.width + '\n'
            return picture

    def __str__(self):
        rectangle_as_str = f'Rectangle(width={self.width}, height={self.height})'
        return rectangle_as_str

    def get_amount_inside(self, rectangle):
        n_in_width = self.width // rectangle.width
        n_in_height = self.height // rectangle.height
        if n_in_width >= 1 and n_in_height >= 1:
            return n_in_width * n_in_height
        else:
            return 0


# =======  class Square  =========

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        square_as_str = f'Square(side={self.width})'
        return square_as_str

    def set_side(self, side):
        self.width = side
        self.height = side
