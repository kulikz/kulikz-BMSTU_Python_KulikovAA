class Number:
    def __init__(self, value):
        self.value = value

    def eval(self, context=None):
        return int(self.value)


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self, context=None):
        return self.left.eval(context) + self.right.eval(context)


class Sub(BinaryOp):
    def eval(self, context=None):
        return self.left.eval(context) - self.right.eval(context)


class Mul(BinaryOp):
    def eval(self, context=None):
        return self.left.eval(context) * self.right.eval(context)


class Div(BinaryOp):
    def eval(self, context=None):
        right_val = self.right.eval(context)
        if right_val == 0:
            raise ZeroDivisionError("Деление на ноль")
        return self.left.eval(context) / right_val


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self, context=None):
        result = self.value.eval(context)
        print(result)
        return result


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self, context=None):
        if context is None:
            context = {}
        result = self.value.eval(context)
        context[self.name] = result
        return result


class Variable:
    def __init__(self, name):
        self.name = name

    def eval(self, context=None):
        if context is None:
            context = {}
        if self.name in context:
            return context[self.name]
        raise NameError(f"Переменная '{self.name}' не определена")


class Program:
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        context = {}
        result = None
        for stmt in self.statements:
            result = stmt.eval(context)
        return result