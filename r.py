import random
start = input('請輸入起始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)#產生隨機整數
count = 0
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')





