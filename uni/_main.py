from luna.match import is_matched_parentheses
from ._expression_tree import ExpressionTree

def expression(ex):
    if not is_matched_parentheses(ex):
        raise ValueError('Parentheses does not match')
    ex = '('.join(ex.split())
    ex += ')'
    return _build_expression_tree(ex)

def _build_expression_tree(token):
    S = []
    for t in token:
        if t in '+-*/=':
            S.append(t)
        elif not t in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()
