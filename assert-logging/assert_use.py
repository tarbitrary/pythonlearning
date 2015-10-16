def test(n):
	#assert断言n != 0 如果等于0则抛出n is zero的提示信息，可以用python -O *.py来禁用assert,加上-O后assert语句相当于pass
	assert n != 0, "n is zero!"
	return 10/n

print(test(1))
test(0)
print(test(2))
