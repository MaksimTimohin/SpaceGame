from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent

class Stats():
    """"Отслеживание статистики"""

    def __init__(self):
        """"Инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        self.high_score = self.get_high_score()

    def get_high_score(self):
        value = 0
        try:
            with open(BASE_DIR / 'highscore.txt', 'r') as f:
                value = int(f.readline())
        except (FileExistsError, TypeError, ValueError) as e:
            value = 0

        return value

    def reset_stats(self):
        """"Статистика изменяющаяся во время игры"""
        self.guns_left = 2
        self.score = 0
