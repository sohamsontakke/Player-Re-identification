# src/detector.py

from ultralytics import YOLO
import cv2
import numpy as np

PLAYER_CLASS_ID = 2  # Change to actual player class index (e.g., 1)

class PlayerDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_players(self, frame):
        results = self.model(frame, verbose=False)[0]
        detections = []
        for box in results.boxes:
            cls = int(box.cls[0])
            if cls != PLAYER_CLASS_ID:
                continue
            x1, y1, x2, y2 = box.xyxy[0]
            conf = float(box.conf[0])
            w = int(x2 - x1)
            h = int(y2 - y1)
            bbox = [int(x1), int(y1), w, h]
            detections.append((bbox, conf))
        return detections

# Make sure this is included below the class — it's the missing function
def extract_histogram(frame, bbox):
    x, y, w, h = bbox
    patch = frame[y:y+h, x:x+w]
    if patch.size == 0 or w == 0 or h == 0:
        return None
    patch = cv2.resize(patch, (64, 128))
    hist = cv2.calcHist([patch], [0, 1, 2], None, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()
