 

import sys

def calc_expr(tokens):
    operations = {
            '*': lambda x, y: y * x,
            '/': lambda x, y: y / x,
            '+': lambda x, y: y + x,
            '-': lambda x, y: y - x
            }

    stack = []

    for item in tokens:
        if item not in operations:
            stack.append(int(item))
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(operations[item](x, y))
    return stack[-1]

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    OP = ("*", "/", "+", "-", "(", ")")
    P = {
        "*" : 50,
        "/" : 50,
        "+" : 40,
        "-" : 40,
        "(" : 0
    }
    for _ in range(N):
        split = sys.stdin.readline().strip().split(' ')
        output = []
        stack = []
        for i in range(len(split)):
            
            token = split[i]
            for item in token:
                if item not in OP:
                    output.append(item)
                elif item == "(":
                    stack.append(item)
                elif item == ")":
                    while stack != [] and stack[-1] != "(":
                        output.append(stack.pop())
                    stack.pop()
                else:
                    while stack != [] and P[stack[-1]] >= P[item]:
                        output.append(stack.pop())
                    stack.append(item)
                    

        while stack:
            output.append(stack.pop())
            
        print(calc_expr(output))