def test():
	"""これはドックストリングです。"""

	print("ドックストリングのテスト")
	return True

def test2():
	"""
	これはドックストリングの
	複数行テストです。
	こういう感じに記載するっぽいです
	関数の引数とかリターン値とかはここに記載しますです。
	"""

	print("ドックストリングのテスト2です。")
	return True

if __name__ == "__main__":
	test()
	test2()
	# 以下の方法で関数使い方を表示できるっぽいです。(ただし、書いていれば)

	print(test.__doc__)

	print(test2.__doc__)

print(aaa)