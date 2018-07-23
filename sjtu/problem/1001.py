'''
1001. 二哥摘苹果
题目描述
二哥平日喜欢自己种一些东西，并以此为写程序和看电影之外的最大爱好。最近，二哥种的一棵苹果树到了采摘的时候，但是由于二哥身高的限制，有些苹果太高摘不到。于是二哥借来了一个凳子，踩在上面可以摘到更多的苹果。

二哥是一个懒于行动的人，他想在摘苹果之前知道自己能摘到多少苹果，如果实在太少（苹果树很茂盛，主要是由于身高原因），他宁可坐在树下等苹果自己掉下来砸到头上。

输入格式
输入共有两行。

第1行有3个整数，分别表示二哥的身高、凳子的高度和苹果的个数n。

第2行有n个整数，分别表示每个苹果的高度。

输出格式
输出一个整数m，表示二哥最多能摘到的苹果的个数为m。

说明
对于全部数据：高度为1000以下的正整数，苹果的个数1≤n≤1000。

Sample Input
177 40 10
180 151 152 193 168 255 278 303 211 217
Sample Output
7
'''

import sys


man_height, chair_height, apple_num = [int(item) for item in sys.stdin.readline().split()]
print(len([item for item in sys.stdin.readline().split() if int(item) <= man_height + chair_height]))
