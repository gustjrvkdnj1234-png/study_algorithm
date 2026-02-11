prior = {'+' : 1, '*' : 2, '(': 0}

def infix_to_profix(tokens):
    result = []
    oper_stack = []
    
    for token in tokens:
        if token.isdigit():
            result.append(token)
        
        elif token == '(':
            oper_stack.append(token)
        
        elif token == ')':
            while oper_stack and oper_stack[-1] != '(':
                result.append(oper_stack.pop())
            oper_stack.pop()
        
        else:
            while oper_stack and prior[oper_stack[-1]] >= prior[token] :
                result.append(oper_stack.pop())

            oper_stack.append(token)
        
    while oper_stack:
        result.append(oper_stack.pop())

    return result
# -----------------------------------------------------
def get_result(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            
            if token == '+':
                stack.append(num1 + num2)
            elif token == '*':
                stack.append(num1*num2)

    return stack[0]
# ------------------------------------------------------        
for tc in range(1, 11):
    n = int(input())
    row = input()
    profix = infix_to_profix(row)
    result = get_result(profix)

    print(f'#{tc} {result}')