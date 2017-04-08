#  根据合理的数学推导可得青蛙跳跃的不同方法和台阶数的数学关系
# 此处是第一题的算法
def jump1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return jump1(n - 1) + jump1(n - 2)


stairs = int(input("Please input the number of stairs:"))
print("There are %d different ways!" % jump1(stairs))
