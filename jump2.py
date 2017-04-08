#   根据合理的数学推导可得青蛙跳跃的不同方法和台阶数的数学关系
# 形如： f(n)=f(n-2)+f(n-1)+......+f(1)+f(0)
# 此处是第二题的算法
def jump2(n):
    s = 1
    for i in range(1, n, 1):
        s = s * 2
    return s


stairs = int(input("Please input the stairs:"))
print("There are %d different ways!" % jump2(stairs))
