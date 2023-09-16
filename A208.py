import math

operators = ['+', '-', '*', '/', '^', 'sin', 'cos', 'tan', 'pi']

def rpn_calculator(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                result = a + b
                stack.append(result)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                result = a - b
                stack.append(result)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                result = a * b
                stack.append(result)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                result = a / b
                stack.append(result)
            elif token == '^':
                b = stack.pop()
                a = stack.pop()
                result = a ** b
                stack.append(result)
            elif token == 'sin':
                a = stack.pop()
                result = math.sin(a)
                stack.append(result)
            elif token == 'cos':
                a = stack.pop()
                result = math.cos(a)
                stack.append(result)
            elif token == 'tan':
                a = stack.pop()
                result = math.tan(a)
                stack.append(result)
            elif token == 'pi':
                stack.append(math.pi)
        else:
            stack.append(float(token))
    
    return stack.pop()

# Example usage
expression = "5 2 + 3 *"
result = rpn_calculator(expression)
print(result)  # Output: 21.0
