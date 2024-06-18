import unittest
import numpy as np
import cv2
from scipy.spatial import ConvexHull

class TestImageProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.image_path = 'lena.jpg'
        cls.color_image = cv2.imread(cls.image_path)
        if cls.color_image is None:
            raise ValueError(f"Image at path {cls.image_path} could not be loaded.")
        cls.gray_image = cv2.cvtColor(cls.color_image, cv2.COLOR_BGR2GRAY)
    
    def test_image_loading(self):
        self.assertIsNotNone(self.color_image, "Color image should be loaded correctly.")
    
    def test_image_conversion_to_grayscale(self):
        self.assertEqual(len(self.gray_image.shape), 2, "Grayscale image should have 2 dimensions.")
    
    def test_dissect_image_into_patches(self):
        patches, brightnesses, centers = dissect_image_into_patches(self.gray_image)
        self.assertEqual(len(patches), (self.gray_image.shape[0] // 5) * (self.gray_image.shape[1] // 5),
                         "Number of patches should be correct.")
        self.assertEqual(len(patches), len(brightnesses), "Each patch should have a corresponding brightness.")
        self.assertEqual(len(patches), len(centers), "Each patch should have a corresponding center.")
    
    def test_get_top_patches(self):
        patches, brightnesses, centers = dissect_image_into_patches(self.gray_image)
        top_patches, top_centers = get_top_patches(patches, brightnesses, centers)
        self.assertEqual(len(top_patches), 4, "Should return top 4 patches.")
        self.assertEqual(len(top_centers), 4, "Should return top 4 centers.")
    
    def test_calculate_quadrilateral_area(self):
        points = [(0, 0), (0, 1), (1, 0), (1, 1)]
        area = calculate_quadrilateral_area(points)
        expected_area = 1.0  # For a unit square
        self.assertAlmostEqual(area, expected_area, places=6, msg="Area of unit square should be 1.")
    
    def test_draw_quadrilateral(self):
        points = [(10, 10), (10, 20), (20, 10), (20, 20)]
        image_with_quadrilateral = draw_quadrilateral(self.color_image.copy(), points)
        self.assertEqual(image_with_quadrilateral.shape, self.color_image.shape,
                         "The shape of the image should not change after drawing.")
        # Check if the red line is drawn
        self.assertTrue(np.any(np.all(image_with_quadrilateral[10:21, 10] == [0, 0, 255], axis=-1)),
                        "Red line should be drawn at the specified points.")

if __name__ == '__main__':
    unittest.main()
