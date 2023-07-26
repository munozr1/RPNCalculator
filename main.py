import sys


def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

if len(sys.argv) < 2 :
    print_colored_text("Usage: python <file-name> <path>", "32")
    print_colored_text("\t<file-name>: the name of the python script to run", "33")
    print_colored_text("\t<path>: the path of the input file to use", "33")
    sys.exit()

file_path = str(sys.argv[1])

# !!! Added modulo division operator !!!
operators = {'+' , '-' , '/' , '*', '%'}

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
def modulo(a , b):
    return a % b 

operate_funcs = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    # !!! Added modulo division operator !!!
    '%': modulo
}

def operate(op1, op2, op):
    # return new calulated value
    func = operate_funcs.get(op)
    return func(int(op2), int(op1))

try:
    with open(file_path, 'r') as file_object:
        for line in file_object:
            # Process each line here
            tokens = line.split()
            stack = []
            # iterate through the expression
            for token in tokens:
                if token in operators:
                    # if operator found, replace prev 2 operands with the new calculated value
                    op1 = stack.pop()
                    op2 = stack.pop()
                    new_val = operate(op1, op2, token)
                    stack.append(new_val)
                else:
                    # if normal integer, push to stack
                    stack.append(token)
            # left on the stack is the final result
            print(stack.pop())
except FileNotFoundError:
    print_colored_text(f"File '{file_path}' not found.", "31")
except IOError:
    print_colored_text(f"Error reading file '{file_path}'.", "31")
