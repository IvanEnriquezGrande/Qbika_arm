import cv2 as cv
import numpy as np


def thresholding(frame):
    # grayscale color
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #blur = cv.GaussianBlur(frame, (5, 5), 0)

    ret2, thresh_otsu = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


    kernel = np.ones((5, 5), np.uint8)
    closing = cv.dilate(thresh_otsu, kernel, iterations=50)
    closing = cv.erode(thresh_otsu, kernel, iterations=50)

    # Now, you can use np.where
    nframe = np.where(thresh_otsu, gray, 0)

    return nframe
    """
    cv.imshow(nframe)

    #gray = cv.normalize(gray, norm_type=cv.NORM_MINMAX)


    gray = np.float32(gray)
    dest = cv.cornerHarris(gray, 2, 5, 0.07)
    dest = cv.dilate(dest, None)
    frame[dest > 0.01 * dest.max()] = [0, 0, 255]

    return frame
"""

if __name__ == '__main__':
    img_path = '../../img/example5.jpeg'
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    new_img = thresholding(img)
    cv.imshow('caja', new_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
