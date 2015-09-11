def main():
	x = "ほげ"
	y = 123
	concat(x, y)

def concat(a, b):
	try:
		return a + b
	except:
		return a(str) + b(str)

if __name__ == '__main__':
	main()
