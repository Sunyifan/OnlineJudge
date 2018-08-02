"""
1015. 高精度乘法
Description
输入2个整数a和b，输出a*b。

Input Format
输入有两行，第一行a，第二行b。

0≤a,b≤2^1000。

Output Format
输出只有一行，a*b。

Sample Input
44
3
Sample Output
132
提交此题

"""


def bigint_add(a, b):
    c = []
    flag = 0

    for i in range(max(len(a), len(b))):
        try:
            a_i = a[i]
        except:
            a_i = 0

        try:
            b_i = b[i]
        except:
            b_i = 0

        this_bit = int(a_i) + int(b_i) + flag
        c.append(str(this_bit % 10))
        flag = 1 if this_bit >= 10 else 0

    if flag:
        c.append("1")

    return c


def bigint_multiply(a, b):
    init = '0'

    for i in range(len(a)):
        flag = 0
        c = []

        for j in range(len(b)):
            exact_value = int(a[i]) * int(b[j]) + flag
            cur_value = exact_value % 10
            flag = int(exact_value / 10)
            c.append(str(cur_value))

        if flag:
            c.append(str(flag))

        v = '0' * i + ''.join(c)
        init = bigint_add(init, v)

    return ''.join(init[::-1])


import sys

a, b = sys.stdin.readline().rstrip()[::-1], sys.stdin.readline().rstrip()[::-1]

print(bigint_multiply(a, b))
