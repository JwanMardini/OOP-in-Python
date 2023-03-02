from player import Player


class Intelligence(Player):
    def __init__(self, mode, score, currentScore) -> None:
        super().__init__(None, score, currentScore)
        self._mode = mode

    def easy(self):
        pass

    def set_score(self, new_score):
        self._score = new_score

    def get_score(self):
        return self._score

    def set_tempScore(self, score):
        self._currentScore = score

    def get_tempScore(self):
        return self._currentScore
