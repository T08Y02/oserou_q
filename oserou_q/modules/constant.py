EMPTY = 0
BLACK = 1
WHITE = 2
SIZE = 4

WINNER_SCORE = 1000.0   # 勝利時の褒章スコア
LOSER_SCORE = -1000.0
DEFAULT_ALPHA = 0.1  # 学習レート（スコア変動）は 1 割
DEFAULT_GAMMA = 0.9  # 続行時のスコア変動レート
DEFAULT_EPSILON = 0.20 # ランダムで置き場所を決定する確率