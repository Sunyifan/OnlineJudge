'''
1006. 求和游戏
Description
石柱上有一排石头键盘，每个键上有一个整数。请你在键盘上选择两个键，使这两个键及其之间的键上的数字和最大。如果这个最大的和不为正，则输出“Game Over"。

Input Format
第1行：键的个数n。

第2..n+1行：键上的数字整数 ai。

−100≤ai≤100
对于70%的数据，2≤n≤1,000
对于100%的数据，2≤n≤1,000,000
Output Format
一行，最大和或者”Game Over"。

Sample Input
5
3
-5
7
-2
8
Sample Output
13
Sample Input
3
-6
-9
-10
Sample Output
Game Over
Hints
数据得到了增强！

'''


import sys


GAME_OVER = 'Game Over'

line_no = int(sys.stdin.readline())
curr_sum = max_sum = in_progress = 0


if line_no > 2:
    for i in range(line_no):
        this_value = int(sys.stdin.readline())

        if i == line_no - 2:
            last_second_value = this_value

        if curr_sum + this_value >= 0:
            curr_sum += this_value
            in_progress += 1
        else:
            curr_sum = in_progress = 0

        if curr_sum > max_sum and in_progress > 1:
            max_sum = curr_sum
        elif i == line_no - 1 and this_value + last_second_value > max_sum:
            max_sum = this_value + last_second_value
else:
    max_sum = sum([int(sys.stdin.readline()) for i in range(line_no)])


if max_sum <= 0:
    print(GAME_OVER)
else:
    print(max_sum)
