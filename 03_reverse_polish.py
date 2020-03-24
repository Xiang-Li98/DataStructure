from stack import Stack
from queue import Queue
"""顺序栈,顺序队列实现四则运算表达式"""


def calculate(s, rp_exp):
    """后缀表达式运算"""
    while rp_exp.size() != 0:
        if rp_exp.get_head().isdigit():
            s.push(int(rp_exp.dequeue()))
        else:
            assert is_operator(rp_exp.get_head()) or rp_exp.get_head() == '(' or rp_exp.get_head() == ')', "%s is illegal operator" % rp_exp.get_head()
            assert s.size() >= 2, "The expression is illegal"
            second = s.pop()
            first = s.pop()
            s.push(count(first, second, rp_exp.dequeue()))
    assert s.size() == 1, "The expression is illegal"
    return s.pop()


def is_operator(exp):
    """判断运算符是否合法"""
    if exp == '+'or exp == '-' or exp == '*' or exp == '/':
        return True
    else:
        return False


def count(a, b, op):
    """四则运算"""
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == "/":
        return a / b


def priority(op1, op2):
    """判断运算符优先级
       op1 >= op2    True
       op1 < op2    False
    """
    return op1 in ['*', '/'] and op2 in['+', '-']


def reverse_polish(s, q, exp):
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            tempt = exp[i]
            i += 1
            if i < len(exp):
                while exp[i].isdigit():
                    tempt += exp[i]
                    i += 1
                    if i == len(exp):
                        break
            q.enqueue(tempt)
            if i == len(exp):
                while s.size() != 0:
                    q.enqueue(s.pop())
            continue
        else:
            if exp[i] == ')':
                while s.peek() != '(':
                    q.enqueue(s.pop())
                s.pop()
            elif is_operator(exp[i]):
                if priority(exp[i], s.peek()):
                    s.push(exp[i])
                else:
                    while not priority(exp[i], s.peek()):
                        if s.peek() == '(' or s.size() == 0:
                            break
                        q.enqueue(s.pop())
                    s.push(exp[i])
            else:
                s.push(exp[i])
            i += 1
            if i == len(exp):
                while s.size() != 0:
                    q.enqueue(s.pop())
    return q


if __name__ == '__main__':
    stack = Stack()
    queue = Queue()
    expr1 = '2/(1+1)*2'
    expr = '9*(3-1)/3+100/10'
    queue = reverse_polish(stack, queue, expr1)
    # while queue.size() != 0:
    #     print(queue.dequeue())
    print(calculate(stack, queue))
