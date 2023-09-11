from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    ranks = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # __init__はクラスの新しいインスタンスが作成される際に自動で呼び出し初期化している
    # rubyでゆうところのinitializeになると思う
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __int__(self):
        rank = self.ranks[self.rank]
        if rank == "J" or rank == "Q" or rank == "K":
            rank = 10
        elif rank == "A":
            rank = 1
        return int(rank)

    def __str__(self):
        v = self.ranks[self.rank] + " の " + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        shuffle(self.cards)

    # cardsの配列が0の場合はreturnで終了し、0じゃない場合はpopで配列の最後の要素を取り出す
    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
