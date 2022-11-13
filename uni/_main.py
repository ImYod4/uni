from luna.match import is_matched_parentheses
from ._expression_tree import ExpressionTree
from luna.priority_queue import HeapPriorityQueue


def expression(ex):
    if not is_matched_parentheses(ex):
        raise ValueError('Parentheses does not match')
    ex = ''.join(c for c in ex.split() if c != ' ')
    return _build_expression_tree(ex)


def _build_expression_tree(token):
    s = []
    for t in token:
        if t in '+-*/=':
            s.append(t)
        elif t not in '()':
            s.append(ExpressionTree(t))
        elif t == ')':
            right = s.pop()
            op = s.pop()
            left = s.pop()
            s.append(ExpressionTree(op, left, right))
    return s.pop()


def _sort(tree):
    for position in tree.positions():
        print(position.element())
    heapq = HeapPriorityQueue()
    for position in tree.positions():
        if tree.is_leaf(position):
            continue
        if position.element() in '*/':
            heapq.add(position, 0)
        elif position.element() in '+-':
            heapq.add(position, 1)
        else:
            heapq.add(position, 2)
