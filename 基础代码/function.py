# def power(x,n):
# 	s=1;
# 	while n>0:
# 		n=n-1;
# 		s=s*x;
# 	return s;
# print(power(5,2));
def fib(max):
	n,a,b = 0,0,1;
	while n < max:
		print(b);
		a,b=b,a+b
		n=n+1;
	return 'done';
fib(5);