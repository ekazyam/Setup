# 関数の内部に関数があって、内部の_counter関数からはnonlocalで指定した変数
# つまり、ローカルでない最も近い変count = 0で定義した値が取得できる。

def counter():
	count = 0
	def _counter():
		nonlocal count
		count += 1
		return count
	return _counter

if __name__ == '__main__':
	func = counter()

	print(func())
	print(func())
