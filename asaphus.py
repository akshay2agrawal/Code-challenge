import cv2
import numpy as np
from scipy.spatial import ConvexHull

def dissect_image_into_patches(image, patch_size=(5, 5)):
    # Get the dimensions of the image
    height, width = image.shape
    
    # Calculate the number of patches along each dimension
    num_patches_y = height // patch_size[0]
    num_patches_x = width // patch_size[1]
    
    patches = []
    brightnesses = []
    centers = []
    
    # Extract patches and calculate their average brightness and centers
    for i in range(num_patches_y):
        for j in range(num_patches_x):
            start_y = i * patch_size[0]
            start_x = j * patch_size[1]
            patch = image[start_y:start_y + patch_size[0], start_x:start_x + patch_size[1]]
            average_brightness = np.mean(patch)
            patches.append(patch)
            brightnesses.append(average_brightness)
            centers.append((start_x + patch_size[1] // 2, start_y + patch_size[0] // 2))
    
    return patches, brightnesses, centers

def get_top_patches(patches, brightnesses, centers, top_n=4):
    # Sort patches by brightness and get the indices of the top N patches
    top_indices = np.argsort(brightnesses)[-top_n:][::-1]
    top_patches = [patches[idx] for idx in top_indices]
    top_centers = [centers[idx] for idx in top_indices]
    return top_patches, top_centers

def calculate_quadrilateral_area(points):
    hull = ConvexHull(points)
    return hull.volume

def draw_quadrilateral(image, points):
    points = np.array(points, dtype=np.int32)
    cv2.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=2)
    return image

# Usage
image_path = 'lena.jpg'

# Read the color image
color_image = cv2.imread(image_path)
if color_image is None:
    raise ValueError(f"Image at path {image_path} could not be loaded.")

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Dissect the grayscale image into patches
patches, brightnesses, centers = dissect_image_into_patches(gray_image)

# Get the top patches by brightness
top_patches, top_centers = get_top_patches(patches, brightnesses, centers)

# Calculate the area of the quadrilateral
area = calculate_quadrilateral_area(top_centers)
print(f"The area of the quadrilateral is {area} pixels.")

# Draw the quadrilateral on the original color image
output_image = draw_quadrilateral(color_image, top_centers)

# Save the image
output_image_path = 'test.png'
cv2.imwrite(output_image_path, output_image)

# Optionally, display the image
cv2.imshow('Image with Quadrilateral', output_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
