def main():
	pass

	for i in range(1, 6):
		if i % 2 == 0:
			print("%sは偶数です。" % i)
		else:
			print("%sは奇数です。" % i)

if __name__ == "__main__":
	main()
	print ("実行形式は %s です。" % __name__)