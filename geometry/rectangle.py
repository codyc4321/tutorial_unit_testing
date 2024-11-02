class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        if area < 0:
            return None
        return area