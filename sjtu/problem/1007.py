'''
1007. 二哥领工资
题目描述
二哥当了多年的助教，今天终于要发工资了！二哥正在高兴之际，得知工资是分两部分发放的。第一部分是这学期的工资，另一部分是之前所有学期的工资总和。而领取工资时，出纳员会问二哥，两部分工资加在一起是多少，如果二哥回答错了，就只能领到这个学期的工资之前所有学期的劳动就白费了。

二哥从小道消息得知，出纳员是个对数字敏感的人，不能有一点差错，所以二哥需要一个程序来帮他算出精确的工资总和。

输入格式
输入共两行，每行是一个十进制表示的工资金额（没有正负号，小数点后有两位数字）。

输出格式
输出共一行，即精确的工资总和（没有正负号，小数点后有两位数字）。

说明
工资金额的有效数字位数不超过200位，并保证有小数点。

Sample Input
123.45
543.21
Sample Output
666.66
提交此题
'''


import sys

a, b = sys.stdin.readline().replace('.', '').rstrip()[::-1], sys.stdin.readline().replace('.', '').rstrip()[::-1]
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


print(''.join(c[2:][::-1]) + '.' + ''.join(c[:2][::-1]))
