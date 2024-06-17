# Code Challenge
This is my result from the following coding challenge:<br>
Write a Python script that reads an image from a file as grayscale,<br>
and finds the four non-overlapping 5x5 patches with highest average brightness.<br>
Take the patch centers as corners of a quadrilateral,<br>
calculate its area in pixels, and draw the quadrilateral in red into the image<br>
and save it in PNG format.<br>
Use the opencv-python package for image handling. Write test cases.<br>

### Thoughts and approach to the task
To get the brightness of each 5x5 patch in the image, mean filtering with a 5x5 mask was the most obvious idea for me.
Each pixel value reflects the average brightness of the 5x5 patch around that pixel.
Since we are talking about the five brightest areas within the image, I ignored the border treatment for filtering and set the two outer rows of the image to zero, since they do not reflect a 5x5 area within the image.
This is followed by a search for the four largest gray values in the filtered image.
To prevent an overlapping of the 5x5 areas, each time a gray value is found, the area around it is set to zero.
Then a quadrilateral is drawn using the four found points. 
To connect the four random points in the right order, I form a convex hull with them. 
To draw a red quadrilateral into the image, I convert the grayscale image into a BGR image.

### With the test cases I wanted to cover the following cases
- The image is read in as a grayscale image
- The four brightest 5x5 patches are found
- The four 5x5 patches do not overlap
- The correct size of the quadrilateral is calculated 
