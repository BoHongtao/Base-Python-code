# 计算 a2 + b2 + c2 + ……
# 第一种写法
# def calc(number):
#     sum =0
#     for n in number:
#         sum = n*n+sum
#     return sum
#
# res = calc([1,2,3])
# 第二种
# def calc(number):
# #     sum =0
# #     for n in number:
# #         sum = n*n+sum
# #     return sum
# # res = calc([1,2,3])
# 第三种
def calc(*number):
    sum =0
    for n in number:
        sum = n*n+sum
    return sum
nums = [1,2,3]
res = calc(*nums)
print(res)