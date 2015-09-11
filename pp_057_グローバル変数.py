# グローバル変数という概念はpythonにはない
# 最大スコープはモジュール単位である。
# globalを指定すると、モジュール無いの変数に直接アクセスできるようになる。

def globaltest():
	global hogehoge
	hogehoge = 'hogehoge'
	return True

globaltest()
print(hogehoge)
