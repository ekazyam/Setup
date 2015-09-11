spam = "test"
print(spam)
del spam
try:
	print(spam)
except:
	print('変数が未定義です')
	