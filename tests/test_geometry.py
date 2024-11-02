import unittest

from geometry.rectangle import Rectangle


class TestInitAndAttributeSetters(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual(3, rectangle.width)
        self.assertEqual(5, rectangle.height)

    def test_set_width(self):
        rectangle = Rectangle(6, 7)
        rectangle.set_width(4)
        self.assertEqual(4, rectangle.width)

    def test_set_height(self):
        rectangle = Rectangle(1, 2)
        rectangle.set_height(9)
        self.assertEqual(9, rectangle.height)



class TestGetAreaRectangle(unittest.TestCase):

    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
    def test_negative_case(self): 
        rectangle = Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), None, "incorrect negative area output")
