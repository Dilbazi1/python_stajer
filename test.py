import unittest
import square
class SquareTest(unittest.TestCase):
    def test_area_circle(self):
        circle = square.Circle(5)
        result = circle.square()
        self.assertEqual(result, 78.53981633974483)

    def test_area_triangle(self):
        triangle = square.Triangle(3, 4, 5)
        result = triangle.square()
        self.assertEqual(result, 6)

    def test_area_calculation(self):
            test_data = {
                (4,): 50.26548245743669,
                (4, 5, 3,): 6,
            }
            for numbers, result in test_data.items():
                self.assertEqual(square.calculate_area(*numbers), result)

    def test_is_triangle(self):
        with self.assertRaises(ValueError):
            square.Triangle(1, 2, 3, )

    def test_is_right_triangle(self):
        test_data = {
            (3, 4, 5,): True,
            (80, 110, 90,): False,
        }
        for numbers, result in test_data.items():
            self.assertEqual(
              square.Triangle(*numbers).is_right_triangle(), result
            )
