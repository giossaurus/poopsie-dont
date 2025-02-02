# (temporary file)
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2
from utils.video_utils import setup_camera

cap = setup_camera()
while True:
    ret, frame = cap.read()
    cv2.imshow('Test Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()