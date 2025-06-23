# src/reid.py

from scipy.spatial.distance import cosine

class ReIDManager:
    def __init__(self, threshold=0.4):
        self.known_players = {}  # Dictionary: {id: histogram}
        self.next_id = 1
        self.threshold = threshold

    def match_or_assign(self, hist):
        if hist is None:
            return -1  # No ID assigned if histogram is invalid

        for pid, known_hist in self.known_players.items():
            similarity = 1 - cosine(hist, known_hist)
            if similarity > (1 - self.threshold):  # High similarity = match
                return pid

        # No match found, assign new ID
        new_id = self.next_id
        self.known_players[new_id] = hist
        self.next_id += 1
        return new_id
