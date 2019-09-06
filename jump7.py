# game for jump 7
# _7 7_ 7* will be ignored

for num in range(101):
	if num%7 != 0 and num%10 != 7 and num//10 != 7:
		print(num)
