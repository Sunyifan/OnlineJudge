"""
1017. 二哥养兔子
Description
二哥培养出了一种繁殖能力很强的兔子。

这种兔子在出生后的第一个月，能够生出a对兔子；第二个月，能够生出b对兔子；第三个月以及以后的每个月，都可以生出c对兔子。

二哥对此很感兴趣，若他有一对刚出生的兔子，按照最理想的模式繁殖，并假设兔子不死，二哥想知道最少需要几个月这些兔子可以遍布地球的每个角落。

为了回答这个问题，二哥想要知道这种兔子在第N个月时的对数。

Input Format
输入只有一行，四个数，分别为a,b,c,N ( 0≤a≤b≤c≤100,N≤1000 )，其含义为题目所述。

Output Format
输出只有一个数，为第N个月兔子的对数。

Sample Input
0 1 1 11
Sample Output
144

"""


import sys


a, b, c, N = [int(item) for item in sys.stdin.readline().split()]
a1, a2, a3 = 1, 0, 0


for i in range(N):
    a1, a2, a3 = a * a1 + b * a2 + c * a3, a1, a2 + a3

print(a1 + a2 + a3)
