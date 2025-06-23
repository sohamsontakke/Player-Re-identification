# Player Re-Identification in a Single Feed

## Overview
This project performs player tracking and re-identification in a 15-second sports clip, ensuring each player retains a consistent ID even after leaving and re-entering the frame.

## Setup

1. Clone this repo.
2. Download model and video:
   - YOLO model: [Download](https://drive.google.com/file/d/1-5fOSHO_SB9UXYP_enOoZNAM_ScrePVcMD/view)
   - Video: 15sec_input_720p.mp4
3. Install dependencies:

```bash
pip install -r requirements.txt

path should be 
player_reid_single_feed/
├── models/
│   └── yolo_reid_model.pt         
├── videos/
│   └── 15sec_input_720p.mp4    
├── src/
│   ├── detector.py
│   ├── reid.py
│   └── main.py
├── requirements.txt
├── README.md
├── report.md
