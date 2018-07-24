'''
1202. bigint
Description
本题做一些简化，题目要求改为输入两个正整数，输出两个正整数的和。

Input Format
输入文件包括两行。

第一行包括一个正整数，保证位数不超过1000000。

第一行包括一个正整数，保证位数不超过1000000。

Output Format
输出文件包括一行。

第一行包括一个正整数。

Sample Input
10558
22
Sample Output
10580
Limits
1.请使用链表答题，否则代码分给0分。

2.请存储下来两个正整数的和，否则代码分给0分。

提交此题
'''



import sys

a, b = sys.stdin.readline().rstrip()[::-1], sys.stdin.readline().rstrip()[::-1]
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


print(''.join(c[::-1]))
