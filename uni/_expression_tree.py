from luna.tree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        if not isinstance(token, str):
            raise TypeError('Token must be a proper string')
        super().__init__()
        self.add_root(token)
        if not left is None:
            if not token in '+-*/=':
                raise ValueError('Token must be a proper operator')
            self._attach(self.root(), left, right)
    def evaluate(self):
        return self._evaluate_recur(self.root())
    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_value = self._evaluate_recur(self.left(p))
            right_value = self._evaluate_recur(self.right(p))

            if op == '+':
                return left_value + right_value
            elif op == '-':
                return left_value - right_value
            elif op == '*':
                return left_value * right_value
            elif op == '/':
                return left_value / right_value
            else:
                return left_value == right_value
    def __str__(self):
        pieces = []
        self._parenthesized_recur(self.root(), pieces)
        return ''.join(pieces)
    def _parenthesized_recur(self, p, result):
        if self.is_leaf(p):
            result.append(p.element())
        else:
            result.append('(')
            self._parenthesized_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesized_recur(self.right(p), result)
            result.append(')')
