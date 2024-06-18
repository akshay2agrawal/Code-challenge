# Code Challenge - Computer Vision

## Task

- Write a Python script that reads an image from a file as grayscale.
- Find the four non-overlapping 5x5 patches with highest average brightness.
- Take the patch centers as corners of a quadrilateral, calculate its area in pixels, and draw the quadrilateral in red into the image.
- Save it in PNG format.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Testing](#testing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/akshay2agrawal/Code-challenge.git
   cd Code-challenge
   ```

2. **Install dependencies:**

   Make sure you have [Python 3](https://www.python.org/) installed. Then install the required libraries using pip:

   ```sh
   pip install opencv-python numpy scipy
   ```

## Usage

1. **Place your input image:**

   Ensure your input image (e.g., `test_image.jpg`) is in the same directory as the script.

2. **Run the script:**

   Execute the main script to process the image and generate the output:

   ```sh
   python main.py
   ```

## Functions

### `dissect_image_into_patches(image, patch_size=(5, 5))`

Dissects the input image into non-overlapping patches of the given size and calculates the average brightness and center of each patch.

### `get_top_patches(patches, brightnesses, centers, top_n=4)`

Identifies the top N patches with the highest average brightness and returns these patches along with their centers.

### `calculate_quadrilateral_area(points)`

Calculates the area of the quadrilateral formed by the given points using the Convex Hull algorithm.

### `draw_quadrilateral(image, points)`

Draws a quadrilateral on the given image using the provided points and colors it red.

## Testing

Unit tests are provided to ensure the functionality of the main components. The tests are written using the `unittest` framework.

### Run Tests

To run the tests, execute the following command:

```sh
python -m unittest test_asaphus.py
```
