'''
括号匹配
Description
给定一串由左小括号，即“（”，和右小括号“）”组成的串，判断其是否匹配。

判断其合法的标准为即为数学等式中括号匹配的标准。

Input Format
第1行：N, 0<N≤50；

第2至N + 1行，一个括号串，保证串的长度不超过100。

Output Format
共N行，若第i个串匹配，为“YES”，否则为“NO”。

Sample Input
3
(())
(()
)(
Sample Output
YES
NO
NO
'''

import sys

N = int(sys.stdin.readline())


def is_legal_exp(bracket_text):
    if not len(bracket_text):
        return 'NO'

    stack = []

    for _char in bracket_text:
        if _char == '(':
            stack.append(_char)
        else:
            if len(stack):
                stack.pop()
            else:
                return 'NO'

    return 'YES' if not len(stack) else 'NO'


for i in range(N):
    bracket_text = sys.stdin.readline().rstrip()
    print(is_legal_exp(bracket_text))
