# src/main.py

import cv2
from detector import PlayerDetector, extract_histogram  
from reid import ReIDManager 

def main():
    cap = cv2.VideoCapture("videos/15sec_input_720p.mp4")
    detector = PlayerDetector("models/yolo_reid_model.pt")
    reid = ReIDManager(threshold=0.35)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect_players(frame)
        for bbox, conf in detections:
            hist = extract_histogram(frame, bbox)
            pid = reid.match_or_assign(hist)
            if pid == -1:
                continue
            x, y, w, h = bbox
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {pid}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Player Re-ID", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
