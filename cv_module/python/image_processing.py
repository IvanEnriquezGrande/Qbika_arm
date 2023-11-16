import cv2 as cv
import numpy as np
import mediapipe as mp

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

        x1 = int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)
        y1 = int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)
        x2 = int(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width)
        y2 = int(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].y * height)
        x3 = int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].x * width)
        y3 = int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

        cv.line(frame, (x1, y1), (x2, y2), white_color, 3)
        cv.line(frame, (x2, y2), (x3, y3), white_color, 3)
        cv.circle(frame, (x1, y1), 6, blue_color, -1)
        cv.circle(frame, (x2, y2), 6, blue_color, -1)
        cv.circle(frame, (x3, y3), 6, blue_color, -1)
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
