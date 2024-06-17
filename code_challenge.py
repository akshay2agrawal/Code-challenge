"""
Write a Python script that reads an image from a file as grayscale,
and finds the four non-overlapping 5x5 patches with highest average brightness.
Take the patch centers as corners of a quadrilateral,
calculate its area in pixels, and draw the quadrilateral in red into the image
and save it in PNG format.
Use the opencv-python package for image handling. Write test cases.
"""

import numpy as np
import cv2


def load_image(image_name):
    """Read the image as grayscale"""
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    return img


def find_patches(img):
    """Find the patches with the highest average brightness"""
    kernel_size_x = 5
    kernel_size_y = 5
    kernel_halfsize_x = np.int0(kernel_size_x/2)
    kernel_halfsize_y = np.int0(kernel_size_y/2)

    number_highest_patches = 4
    patch_centers = np.zeros((number_highest_patches, 2))
    patch_values = np.zeros((number_highest_patches))

    # Defining the kernel of size 5x5
    kernel = (np.ones((kernel_size_y, kernel_size_x))
              / (kernel_size_y*kernel_size_x))
    # Filtering the Image
    res_img = cv2.filter2D(img, -1, kernel)
    # Cut away unwanted information (no use of padding)
    res_img_crop = res_img[
        kernel_halfsize_y:-kernel_halfsize_y,
        kernel_halfsize_x:-kernel_halfsize_x
        ]
    # Creates border with zeros so that same image size is restored
    res_img_crop = cv2.copyMakeBorder(
        res_img_crop,
        kernel_halfsize_y, kernel_halfsize_y,
        kernel_halfsize_x, kernel_halfsize_x,
        cv2.BORDER_CONSTANT, None, 0
        )

    for i in np.arange(0, number_highest_patches):
        # Searches for largest gray value and determines index and value
        _, max_val, _, max_indx = cv2.minMaxLoc(res_img_crop)
        patch_centers[i, :] = np.asarray(max_indx)
        patch_values[i] = max_val
        # Sets values around the determined gray value to 0
        # so that no overlap to the next patch can occur
        left = (np.int0(patch_centers[i, 0])
                - (kernel_size_x - 1))
        right = (np.int0(patch_centers[i, 0])
                 + kernel_size_x)
        top = (np.int0(patch_centers[i, 1])
               - (kernel_size_y - 1))
        bottom = (np.int0(patch_centers[i, 1])
                  + kernel_size_y)
        if(left < 0):
            left = 0
        if(right > img.shape[0] - 1):
            right = img.shape[0] - 1
        if(top < 0):
            top = 0
        if(bottom > img.shape[1] - 1):
            bottom = img.shape[1] - 1
        res_img_crop[top:bottom, left:right] = 0
    return patch_centers


def draw_quadrilateral(img, patch_centers):
    """Use the patch centers to draw a quadrilatera and calculate its area"""
    # Calculate the convex hull from the center points to get the quadrilateral
    hull = cv2.convexHull(np.int0(patch_centers))
    # Calculate the area of the quadrilateral in pixel
    temp = np.zeros(img.shape, np.uint8)
    cv2.drawContours(temp, [hull], -1, 255, cv2.FILLED)
    quadrilateral_area = cv2.countNonZero(temp)
    # Converts gray scale image to BGR so that a red square can be drawn
    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # Draw the quadrilateral in red into the image
    cv2.drawContours(img_bgr, [hull], -1, (0, 0, 255), cv2.FILLED)
    # Save the image as .png
    cv2.imwrite("image_with_quadrilateral.png", img_bgr)
    return quadrilateral_area

#define the main function
if __name__ == "__main__":
    """Runs the code challenge in its entirety with lena.jpg as the input image"""
    print("Running code challenge with lena.jpg as the input image")
    image_name = 'lena.jpg'
    img = load_image(image_name)
    corners = find_patches(img)
    area = draw_quadrilateral(img, corners)
    print(f"The quadrilateral has a size of {area} pixels")
