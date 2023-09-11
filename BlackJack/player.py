class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.burst = False

    def check(self):
        if self.score == 21:
            total = "{} の合計スコア {}"
            print(total.format(self.name, self.score))
            win = "BLACKJACK!! {} の勝ちです"
            print(win.format(self.name))
            return True
        elif self.score > 21:
            total = "{} の合計スコア {}"
            print(total.format(self.name, self.score))
            lose = "{} はバーストしました"
            print(lose.format(self.name))
            return True
        else:
            return False
