print("数当てゲームを始めます")
print("答えの数の範囲は0~100です")

answer = 10
guess = int(input("あなたが予想する数字:"))
tries = 1

while guess != answer:
	if guess > answer:
		print("大きすぎます")
	else:
		print("小さすぎます")

	tries += 1
	guess = int(input("あなたが予想する数字:"))

print("正解です答えは{}でした".format(answer))
print("あなたが答えを当てるまでに{}回かかりました".format(tries))