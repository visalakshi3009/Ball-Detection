# Ball-Detection

Developed a Python Program using the OpenCV package to detect the ball in the video.

## Highlights
* Used the HSV values for the colour of the ball (green in this case) to detect the ball using a mask.
* The contours of the ball are then detected using the mask and an enclosing circle is then made for the ball in the frame.
* This process is repeated for every frame in the video to detect the ball throughout the video.
