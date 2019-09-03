def infix_to_postfix(expression):
    precision = {}
    precision['*'] = 3
    precision['/'] = 3
    precision['+'] = 2
    precision['-'] = 2
    precision['('] = 1

    op_stack = []
    postfix_expression_list = []
    expression_list = expression.split()

    for token in expression_list:
        try:
            int(token)
            postfix_expression_list.append(token)
        except:
            if token == "(":
                op_stack.append(token)
            elif token == ")":
                op_token = op_stack.pop()
                while op_token != "(":
                    postfix_expression_list.append(op_token)
                    op_token = op_stack.pop()
            else:

                while(len(op_stack) != 0) and \
                        (precision[token] <= precision[op_stack[-1]]):
                    top_token = op_stack.pop()
                    postfix_expression_list.append(top_token)
                op_stack.append(token)

    while len(op_stack) != 0:
        postfix_expression_list.append(op_stack.pop())

    return postfix_expression_list


def evaluating_postfix_expression(postfix_expression_list):
    operand_stack = []
    for token in postfix_expression_list:
        try:
            operand_stack.append(int(token))
        except:

            operand2 = operand_stack.pop()
            try:
                operand1 = operand_stack.pop()
            except:
                operand1 = 0

            if token == "*":
                res = operand2 * operand1
                operand_stack.append(res)
            elif token == "/":
                res = operand1 / operand2
                operand_stack.append(res)
            elif token == "+":
                res = operand2 + operand1
                operand_stack.append(res)
            elif token == "-":
                res = operand1 - operand2
                operand_stack.append(res)
            else:
                raise("unsupported operation")

    return operand_stack.pop()


def main():
    postfix_expression_list = infix_to_postfix(input())
    print(evaluating_postfix_expression(postfix_expression_list))
