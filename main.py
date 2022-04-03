import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture('1.mp4 - Медиапроигрыватель VLC')

cascadeHits = cv.CascadeClassifier('cascade/cascade.xml')

visionHits = Vision(None)
loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # do object detection
    rectangles = cascadeHits.detectMultiScale(screenshot)

    processed_image = visionHits.draw_rectangles(screenshot, rectangles)
    # display the images
    cv.imshow('Unprocessed', processed_image)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image,
    # press 'd' to save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('p'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('n'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')