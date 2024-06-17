import unittest
import code_challenge
import numpy as np


class TestAsaphus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.img_1 = code_challenge.load_image('lena.jpg')
        cls.img_2 = np.zeros([50, 50], np.uint8)
        cls.img_2[0:5, 0:5] = 255
        cls.img_2[10:15, 10:15] = 255
        cls.img_2[0:5, 10:15] = 255
        cls.img_2[10:15, 0:5] = 255
        cls.img_3 = np.ones([15, 15], np.uint8)*255

        cls.patch_centers_1 = code_challenge.find_patches(cls.img_1)
        cls.patch_centers_2 = code_challenge.find_patches(cls.img_2)
        cls.patch_centers_3 = code_challenge.find_patches(cls.img_3)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_image(self):
        # Test if image is a grayscale image
        self.assertLessEqual(len(self.img_1.shape), 3)

    def test_find_patches(self):
        # Test if four patches where found
        self.assertTrue(np.all(self.patch_centers_1))
        # Test if center of the 4 highest brightness patches are correct
        self.assertTrue((self.patch_centers_2 == [2, 2]).all(1).any())
        self.assertTrue((self.patch_centers_2 == [12, 2]).all(1).any())
        self.assertTrue((self.patch_centers_2 == [2, 12]).all(1).any())
        self.assertTrue((self.patch_centers_2 == [12, 12]).all(1).any())
        # Test if the 5x5 patches are overlapping each other
        self.assertGreaterEqual(np.linalg.norm(
            self.patch_centers_3[0] - self.patch_centers_3[1]), 5)
        self.assertGreaterEqual(np.linalg.norm(
            self.patch_centers_3[0] - self.patch_centers_3[2]), 5)
        self.assertGreaterEqual(np.linalg.norm(
            self.patch_centers_3[0] - self.patch_centers_3[3]), 5)
        self.assertGreaterEqual(np.linalg.norm(
            self.patch_centers_3[1] - self.patch_centers_3[2]), 5)
        self.assertGreaterEqual(np.linalg.norm(
            self.patch_centers_3[1] - self.patch_centers_3[3]), 5)
        self.assertGreaterEqual(np.linalg.norm(
            self.patch_centers_3[2] - self.patch_centers_3[3]), 5)

    def test_draw_quadrilateral(self):
        # Test if the size is calculated correctly
        quadrilateral_area = code_challenge.draw_quadrilateral(
            self.img_2, self.patch_centers_2)
        self.assertEqual(quadrilateral_area, 121)


if __name__ == '__main__':
    unittest.main()
