"""
Абстрактное синтаксическое дерево для JS-Lite
"""

class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value) if '.' in str(self.value) else int(self.value)


class String:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)


class Boolean:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return bool(self.value)


class Identifier:
    def __init__(self, name):
        self.name = name

    def eval(self, context):
        return context.get(self.name)


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) + self.right.eval(context)


class Sub(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) - self.right.eval(context)


class Mul(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) * self.right.eval(context)


class Div(BinaryOp):
    def eval(self, context):
        right_val = self.right.eval(context)
        if right_val == 0:
            raise ZeroDivisionError("Division by zero")
        return self.left.eval(context) / right_val


class Mod(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) % self.right.eval(context)


class Equal(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) == self.right.eval(context)


class NotEqual(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) != self.right.eval(context)


class LessThan(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) < self.right.eval(context)


class GreaterThan(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) > self.right.eval(context)


class LessOrEqual(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) <= self.right.eval(context)


class GreaterOrEqual(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) >= self.right.eval(context)


class And(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) and self.right.eval(context)


class Or(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) or self.right.eval(context)


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self, context):
        value = self.value.eval(context)
        context[self.name] = value
        return value


class ConsoleLog:
    def __init__(self, value):
        self.value = value

    def eval(self, context):
        result = self.value.eval(context)
        print(result)
        return result


class IfStatement:
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def eval(self, context):
        if self.condition.eval(context):
            return self.then_block.eval(context)
        elif self.else_block:
            return self.else_block.eval(context)
        return None


class WhileLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self, context):
        result = None
        while self.condition.eval(context):
            result = self.body.eval(context)
        return result


class Block:
    def __init__(self, statements):
        self.statements = statements

    def eval(self, context):
        result = None
        for stmt in self.statements:
            result = stmt.eval(context)
        return result


class VarDeclaration:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def eval(self, context):
        if self.value:
            value = self.value.eval(context)
            context[self.name] = value
            return value
        context[self.name] = None
        return None


class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def eval(self, context):
        # Простая реализация - для встроенных функций
        if self.name == 'alert':
            for arg in self.args:
                print(arg.eval(context))
            return None
        elif self.name == 'parseInt':
            if self.args:
                return int(self.args[0].eval(context))
        elif self.name == 'parseFloat':
            if self.args:
                return float(self.args[0].eval(context))
        return None