'''
1000. A+B Problem
Description
作为所有 Online Judge 的传统题目，你只需读两个整数，输出即可，保证输入的数绝对值不超过1000。

Input Format
一行,两个空格隔开的整数A,B。

Output Format
一个数A+B。

Sample Input
3 2
Sample Output
5
'''

import sys


lines = sys.stdin.readline()
print(sum([int(item) for item in lines.split()]))
