# 计算斐波那契数列
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# f = fib(6);
# print(f);
# 杨辉三角
def tri(max):
    L = [1]
    n = 1
    while n < max:
        yield L
        n = n+1
        L = [L[l] + L[l - 1] for l in range(len(L))]
        L[0]=1
        L.append(1)
    return 'done'
for i in tri(20):
    print(i)