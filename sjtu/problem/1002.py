'''
1002. 二哥种花生
Description
二哥在自己的后花园里种了一些花生，也快到了收获的时候了。这片花生地是一个长度为L、宽度为W的矩形，每个单位面积上花生产量都是独立的。他想知道，对于某个指定的区域大小，在这么大的矩形区域内，花生的产量最大会是多少。

Input Format
第1行有2个整数，长度L和宽度W。

第2行至第L+1行，每行有W个整数，分别表示对应的单位面积上的花生产量A（ 0≤A<10 ）。

第L+2行有2个整数，分别是指定的区域大小的长度a和宽度b。

Output Format
输出一个整数m，表示在指定大小的区域内，花生最大产量为m。

Sample Input
4 5
1 2 3 4 5
6 7 8 0 0
0 9 2 2 3
3 0 0 0 1
3 3

Sample Output
38
样例解释
左上角：38 = (1+2+3) + (6+7+8) + (0+9+2)

数据范围
对于30%的数据： 1≤L,W≤100；

对于100%的数据： 1≤L,W≤1000。

全部区域大小满足：1≤a≤L，1≤b≤W 。
'''


import sys

l, w = [int(item) for item in sys.stdin.readline().split()]
matrix = [[int(item) for item in sys.stdin.readline().split()] for i in range(l)]
obj_l, obj_w = [int(item) for item in sys.stdin.readline().split()]


row_sum_matrix = []

for i in range(l):
    row = []

    for j in range(w - obj_w + 1):
        if j == 0:
            row.append(sum(matrix[i][:obj_w]))
        else:
            row.append(row[-1] + matrix[i][j + obj_w - 1] - matrix[i][j - 1])

    row_sum_matrix.append(row)


max_peanuts = 0


for j in range(w - obj_w + 1):
    for i in range(l - obj_l + 1):
        if i == 0:
            curr_peanuts = sum([row_sum_matrix[k][j] for k in range(obj_l)])
        else:
            curr_peanuts = curr_peanuts + row_sum_matrix[i + obj_l - 1][j] - row_sum_matrix[i - 1][j]

        max_peanuts = curr_peanuts if curr_peanuts >= max_peanuts else max_peanuts

print(max_peanuts)
