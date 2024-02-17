psw = 'a123456'
x = int(3) #剩餘機會
while x > 0:
	x -= 1
	user = input('please enter the password:')
	if user == psw: #只需要寫存進去的代號
		print('login successful')
		break #離開迴圈
	else:
		print('Incorrect password')
		if x > 0:
			print('you have', x , 'chance')
		else:
			print('Too many attempts, please try again later.')




	
