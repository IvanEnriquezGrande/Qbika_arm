import cv2 as cv
import numpy as np


def thresholding(frame):
    # grayscale color
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cimg = cv.medianBlur(cimg, 7)
    #    cimg = cv2.bilateralFilter(cimg,11,25,25)
    edges = cv.Canny(cimg, 125, 150)
    #return edges
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 60, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
    # Para obtener caracteríscticas obtendremos los ángulos
    return frame


if __name__ == '__main__':
    img_path = '../../img/caja2.jpg'
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    new_img = thresholding(img)
    cv.imshow('caja', new_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
