'''
1022. Fib数列
Description
定义Fib数列：1,1,2,3,5,8,13,…
求第N项除以2010的余数

Input Format
输入仅一行，为一个整数N
Output Format
输出仅一行，为第N项除以2010的余数

Sample Input
3
Sample Output
2
Limits:
对于70%的数据 N≤1,000,000
对于100%的数据 N≤210,000,000,000

'''


def fib(n):
    if n < 3:
        return 1
    else:
        this, last = 1, 1

        for i in range(n - 2):
            last, this = this, this + last

        return this


import sys

n = int(sys.stdin.readline())
print(fib(n % 2040) % 2010)
