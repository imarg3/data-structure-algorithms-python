class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def is_empty(self):
        return len(self.arr) == 0


def calc(a, b, op):
    if op == '$':
        return a ** b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '%':
        return a % b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    return 0


def pri(op):
    switch = {
        '$': 10,
        '*': 7,
        '/': 7,
        '%': 7,
        '+': 4,
        '-': 4,
    }
    return switch.get(op, 0)


def infix_to_postfix(infix):
    s = Stack()
    postfix = ''
    # 1. access symbols from infix one by one (left to right)
    for i in range(0, len(infix)):
        sym = infix[i]
        # 2. if symbol is operand, append it to postfix.
        if sym.isdigit():
            postfix = postfix + sym
        # 5. if opening ( is found, push it on stack
        elif sym == '(':
            s.push(sym)
        # 6. if closing ) is found,
        # pop all operators from stack one by one and append to postfix, until opening ( is found on stack.
        elif sym == ')':
            while s.peek() != '(':
                postfix = postfix + s.pop()
            s.pop()  # pop and discard opening ( as well.
        else:  # 3. if symbol is operator, push it on stack.
            # * if priority of topmost operator >= priority of current operator,
            # then pop it and append to posfix.
            while not s.is_empty() and pri(s.peek()) >= pri(sym):
                postfix = postfix + s.pop()
            s.push(sym)
    # 4. if all symbols from infix are over,
    # then pop all operators from stack one by one and append to postfix.
    while not s.is_empty():
        postfix = postfix + s.pop()
    return postfix


def infix_to_prefix(infix):
    s = Stack()
    prefix = ''
    # 1. access symbols from infix one by one (left to right)
    for i in range(len(infix) - 1, 0, -1):
        sym = infix[i]
        # 2. if symbol is operand, append it to prefix.
        if sym.isdigit():
            prefix = prefix + sym
        # 5. if closing ) is found, push it on stack
        elif sym == ')':
            s.push(sym)
        # 6. if opening ( is found,
        # pop all operators from stack one by one and append to prefix, until closing ) is found on stack.
        elif sym == '(':
            while s.peek() != ')':
                prefix = prefix + s.pop()
            s.pop()  # pop and discard closing ) as well.
        else:  # 3. if symbol is operator, push it on stack.
            # * if priority of topmost operator > priority of current operator,
            # then pop it and append to posfix.
            while not s.is_empty() and pri(s.peek()) > pri(sym):
                prefix = prefix + s.pop()
            s.push(sym)
    # 4. if all symbols from infix are over,
    # then pop all operators from stack one by one and append to prefix.
    while not s.is_empty():
        prefix = prefix + s.pop()
    return prefix[::-1]


def postfix_evaluation(postfix):
    s = Stack()
    # 1. access symbols from postfix from left to right.
    for i in range(0, len(postfix)):
        sym = postfix[i]
        # 2. if symbol is operand, push it on the stack.
        if sym.isdigit():
            s.push(int(sym))
        # 3. if symbol is operator, pop two operands from stack, calculate result & push on stack.
        else:
            b = s.pop()
            a = s.pop()
            res = calc(a, b, sym)
            s.push(res)
    # 4. repeat until all symbols from postfix are finished.
    return s.pop()  # 5. pop the final result from stack and return it.


def prefix_evaluation(prefix):
    s = Stack()
    # 1. access symbols from prefix from right to left.
    for i in range(len(prefix) - 1, -1, -1):
        sym = prefix[i]
        # 2. if symbol is operand, push it on the stack.
        if sym.isdigit():
            s.push(int(sym))
        # 3. if symbol is operator, pop two operands from stack, calculate result & push on stack.
        else:
            a = s.pop()
            b = s.pop()
            res = calc(a, b, sym)
            s.push(res)
    # 4. repeat until all symbols from prefix are finished.
    return s.pop()  # 5. pop the final result from stack and return it.


def postfix_to_infix(postfix):
    s = Stack()
    for i in range(0, len(postfix)):
        sym = postfix[i]
        if sym.isdigit():
            s.push(str(sym))
        else:
            b = s.pop()
            a = s.pop()
            s.push('(' + a + sym + b + ')')
    return s.pop()


def prefix_to_postfix(prefix):
    s = Stack()
    for i in range(len(prefix) - 1, -1, -1):
        sym = prefix[i]
        if sym.isdigit():
            s.push(str(sym))
        else:
            a = s.pop()
            b = s.pop()
            s.push(a + b + sym)
    return s.pop()


def main():
    # infix = '1+2*3'
    infix = "5+9-4*(8-6/2)+1$(7-3)"
    postfix = infix_to_postfix(infix)
    print("Postfix: " + postfix)
    prefix = infix_to_prefix(infix)
    print("Prefix: " + prefix)

    postfix = "59+4862/-*-173-$+"
    res = postfix_evaluation(postfix)
    print("Postfix  Result: " + str(res))
    prefix = "+-+59*4-8/62$1-73"
    res = prefix_evaluation(prefix)
    print("Prefix Result: " + str(res))
    infix = postfix_to_infix(postfix)
    print("Infix Expr: " + infix)
    converted_postfix = prefix_to_postfix(prefix)
    print("Postfix Expr: " + converted_postfix)


if __name__ == "__main__":
    main()
