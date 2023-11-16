import cv2 as cv
import numpy as np
import mediapipe as mp
import math

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

# Initialize MediaPipe Pose and Drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose()

white_color = (255, 255, 255)
blue_color = (255, 0, 0)

def thresholding(frame):
    height, width, _ = frame.shape

    # Process the frame with MediaPipe Pose
    results = pose.process(frame)


    if results.pose_landmarks is not None:
        landmarks = results.pose_landmarks.landmark

        point1 = (int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width),
                      int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height))
        point2 = (int(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width),
                      int(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].y * height))
        point3 = (int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].x * width),
                      int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y * height))

        arm = [point1, point2, point3]

        #angles = []

        # draw lines
        prev_point = None
        for point in arm:
            # draw point
            cv.circle(frame, point, 6, blue_color, -1)

            # draw line
            if prev_point:
                cv.line(frame, prev_point, point, white_color, 3)

                """
                # inclination
                inclination = (point[1] - prev_point[1]) / (point[0] - prev_point[0])
                angles.append(inclination)
                #median = ((point[0] + prev_point[0]) // 2, (point[1] + prev_point[1]) // 2)

                # font
                font = cv.FONT_HERSHEY_SIMPLEX


                cv.putText(frame, str(inclination), point, font, 0.5, (0, 0, 255), 1, cv.LINE_AA)
                """

            prev_point = point

        fp = arm[0]
        arm.insert(0, (fp[0], 0))

        for i in range(1, len(arm)-1):
            v1 = arm[i-1][0] - arm[i][0], arm[i-1][1] - arm[i][1]
            v2 = arm[i+1][0] - arm[i][0], arm[i+1][1] - arm[i][1]

            a = angle(v1, v2)
            a = a * 180 / math.pi
            
            cv.putText(frame, str(a), arm[i], cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv.LINE_AA)

    return frame


if __name__ == '__main__':
    cam = cv.VideoCapture(0)
    while True:
        # OpenCV related
        ret_val, img = cam.read()
        if ret_val:
            new_img = thresholding(img)
            cv.imshow('Brazo', new_img)
            if cv.waitKey(1) == 27:
                break  # esc to quit

    cv.waitKey(0)
    cv.destroyAllWindows()
