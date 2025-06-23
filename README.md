# 🧠 Player Re-Identification in a Single Camera Feed

This project implements a real-time **player re-identification system** for sports video analysis. It ensures that players retain consistent identities (IDs) even when they temporarily leave the frame and re-enter later. The system simulates real-world sports tracking challenges using computer vision and appearance-based matching.

---

## 🎯 Objectives

- Detect and identify all **players** from a single 15-second video clip.
- Maintain consistent **player IDs** even across occlusions or re-entries.
- Ignore irrelevant objects such as the **ball**.
- Demonstrate appearance-based **ReID (Re-Identification)** using color histograms.

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/player-reid-single-feed.git
   cd player-reid-single-feed
