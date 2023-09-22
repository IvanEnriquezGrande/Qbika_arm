import cv2 as cv
import numpy as np

def thresholding(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, th = cv.threshold(gray, 80, 255, cv.THRESH_BINARY)
    return th


if __name__ == '__main__':
    img_path = '../../img/example.jpg'
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    new_img = thresholding(img)
    cv.imshow('caja', new_img)

    cv.waitKey(0)
    cv.destroyAllWindows()