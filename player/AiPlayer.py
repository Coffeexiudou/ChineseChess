from player.Player import Player
from engine.algorithm.MinMax import MinMax
from engine.algorithm.ABpruning import ABpruning
from engine.algorithm.IterativeDeepeningABpruning import IterativeDeepeningABpruning


class AiPlayer(Player):

    def next_move(self):
        result = []
        if self.mode == 'easy':
            result = MinMax.search_next_move(self.board, self.color, 0)
        elif self.mode == 'medium':
            result = ABpruning.search_next_move(self.board, self.color, 1)
        elif self.mode == 'hard':
            result = IterativeDeepeningABpruning.search_next_move(self.board,
                                                                  self.color, 2)
        return result


if __name__ == '__main__':
    pass
