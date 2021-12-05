def rec_fibo(n):

	if n <= 1:
		return n
	else:
		return rec_fibo(n-1) + rec_fibo(n-2)


#########################
# Driver code
for i in range(30):
	print('Fibonacci number is ', rec_fibo(i))