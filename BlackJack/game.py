from card import Card, Deck
from player import Player
import sys


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("あなた")
        self.dealer = Player("ディーラー")

    def draw_message(self, name, card):
        dealer = "{} の引いたカードは {} です"
        print(dealer.format(name, card))

    def score_message(self, name, score):
        total = "{} の合計スコア {}"
        print(total.format(name, score))

    def hit_or_stand(self):
        while True:
            hit = input("もう一枚引きますか？(y/n):")
            if hit == "y":
                return True
            elif hit == "n":
                return False
            else:
                print("yかnを入力してください")

    def game_continue(self):
        while True:
            yn = input("ゲームを続けますか？(y/n):")
            if yn == "y":
                self.player.score = 0
                self.dealer.score = 0
                self.play_game()
            elif yn == "n":
                print("ゲームを終了します")
                sys.exit(-1)
            else:
                print("yかnを入力してください")

    def play_game(self):
        pc1 = self.deck.draw()
        dc1 = self.deck.draw()
        pc2 = self.deck.draw()
        dc2 = self.deck.draw()
        self.player.score += int(pc1) + int(pc2)
        self.dealer.score += int(dc1) + int(dc2)

        self.draw_message(self.player.name, str(pc1))
        self.draw_message(self.dealer.name, str(pc2))
        self.draw_message(self.player.name, str(dc1))
        self.draw_message(self.dealer.name, "(伏せ札)")

        hs = self.hit_or_stand()

        while hs:
            pc = self.deck.draw()
            self.player.score += int(pc)
            self.draw_message(self.player.name, str(pc))
            if self.player.check():
                self.game_continue()
            hs = self.hit_or_stand()

        self.score_message(self.player.name, self.player.score)
        o = "{} の(伏せ札)は {}"
        print(o.format(self.dealer.name, str(dc2)))

        while self.dealer.score < 17:
            dc = self.deck.draw()
            self.dealer.score += int(dc)
            self.draw_message(self.dealer.name, str(dc))
            if self.dealer.check():
                self.game_continue()

        self.score_message(self.dealer.name, self.dealer.score)

        if self.dealer.score < self.player.score:
            print("{}の勝ち".format(self.player.name))
        elif self.dealer.score > self.player.score:
            print("{}の負け".format(self.player.name))
        else:
            print("引き分け")

        self.game_continue()


if __name__ == "__main__":
    game = Game()
    game.play_game()
