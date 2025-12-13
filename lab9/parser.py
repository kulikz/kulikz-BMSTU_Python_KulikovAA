from rply import ParserGenerator
from ast import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # Список всех токенов
            ['NUMBER', 'STRING', 'IDENTIFIER',
             'VAR', 'LET', 'CONST', 'IF', 'ELSE', 'WHILE',
             'TRUE', 'FALSE', 'NULL', 'FUNCTION', 'RETURN',
             'CONSOLE_LOG', 'ALERT', 'PARSE_INT', 'PARSE_FLOAT',
             'ASSIGN', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO',
             'EQUAL', 'NOT_EQUAL', 'LESS_THAN', 'GREATER_THAN',
             'LESS_EQUAL', 'GREATER_EQUAL', 'AND', 'OR', 'NOT',
             'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACE', 'CLOSE_BRACE',
             'SEMICOLON', 'COMMA']
        )

    def parse(self):
        @self.pg.production('program : statements')
        def program(p):
            return Block(p[0])

        @self.pg.production('statements : statement')
        @self.pg.production('statements : statement statements')
        def statements(p):
            if len(p) == 1:
                return [p[0]]
            return [p[0]] + p[1]

        @self.pg.production('statement : expression_statement')
        @self.pg.production('statement : variable_declaration')
        @self.pg.production('statement : if_statement')
        @self.pg.production('statement : while_statement')
        @self.pg.production('statement : console_log')
        @self.pg.production('statement : block_statement')
        def statement(p):
            return p[0]

        @self.pg.production('expression_statement : expression SEMICOLON')
        def expression_statement(p):
            return p[0]

        @self.pg.production('variable_declaration : VAR IDENTIFIER ASSIGN expression SEMICOLON')
        def variable_declaration(p):
            return VarDeclaration(p[1].value, p[3])

        @self.pg.production('console_log : CONSOLE_LOG OPEN_PAREN expression CLOSE_PAREN SEMICOLON')
        def console_log(p):
            return ConsoleLog(p[2])

        @self.pg.production('if_statement : IF OPEN_PAREN expression CLOSE_PAREN statement')
        @self.pg.production('if_statement : IF OPEN_PAREN expression CLOSE_PAREN statement ELSE statement')
        def if_statement(p):
            if len(p) == 5:
                return IfStatement(p[2], p[4])
            else:
                return IfStatement(p[2], p[4], p[6])

        @self.pg.production('while_statement : WHILE OPEN_PAREN expression CLOSE_PAREN statement')
        def while_statement(p):
            return WhileLoop(p[2], p[4])

        @self.pg.production('block_statement : OPEN_BRACE statements CLOSE_BRACE')
        def block_statement(p):
            return Block(p[1])

        @self.pg.production('expression : assignment')
        @self.pg.production('expression : logical_or')
        def expression(p):
            return p[0]

        @self.pg.production('assignment : IDENTIFIER ASSIGN expression')
        def assignment(p):
            return Assignment(p[0].value, p[2])

        @self.pg.production('logical_or : logical_and')
        @self.pg.production('logical_or : logical_or OR logical_and')
        def logical_or(p):
            if len(p) == 1:
                return p[0]
            return Or(p[0], p[2])

        @self.pg.production('logical_and : equality')
        @self.pg.production('logical_and : logical_and AND equality')
        def logical_and(p):
            if len(p) == 1:
                return p[0]
            return And(p[0], p[2])

        @self.pg.production('equality : relational')
        @self.pg.production('equality : equality EQUAL relational')
        @self.pg.production('equality : equality NOT_EQUAL relational')
        def equality(p):
            if len(p) == 1:
                return p[0]
            if p[1].gettokentype() == 'EQUAL':
                return Equal(p[0], p[2])
            else:
                return NotEqual(p[0], p[2])

        @self.pg.production('relational : additive')
        @self.pg.production('relational : relational LESS_THAN additive')
        @self.pg.production('relational : relational GREATER_THAN additive')
        @self.pg.production('relational : relational LESS_EQUAL additive')
        @self.pg.production('relational : relational GREATER_EQUAL additive')
        def relational(p):
            if len(p) == 1:
                return p[0]
            if p[1].gettokentype() == 'LESS_THAN':
                return LessThan(p[0], p[2])
            elif p[1].gettokentype() == 'GREATER_THAN':
                return GreaterThan(p[0], p[2])
            elif p[1].gettokentype() == 'LESS_EQUAL':
                return LessOrEqual(p[0], p[2])
            else:
                return GreaterOrEqual(p[0], p[2])

        @self.pg.production('additive : multiplicative')
        @self.pg.production('additive : additive PLUS multiplicative')
        @self.pg.production('additive : additive MINUS multiplicative')
        def additive(p):
            if len(p) == 1:
                return p[0]
            if p[1].gettokentype() == 'PLUS':
                return Sum(p[0], p[2])
            else:
                return Sub(p[0], p[2])

        @self.pg.production('multiplicative : unary')
        @self.pg.production('multiplicative : multiplicative MULTIPLY unary')
        @self.pg.production('multiplicative : multiplicative DIVIDE unary')
        @self.pg.production('multiplicative : multiplicative MODULO unary')
        def multiplicative(p):
            if len(p) == 1:
                return p[0]
            if p[1].gettokentype() == 'MULTIPLY':
                return Mul(p[0], p[2])
            elif p[1].gettokentype() == 'DIVIDE':
                return Div(p[0], p[2])
            else:
                return Mod(p[0], p[2])

        @self.pg.production('unary : primary')
        @self.pg.production('unary : NOT unary')
        @self.pg.production('unary : MINUS unary')
        def unary(p):
            if len(p) == 1:
                return p[0]
            # Для упрощения - просто возвращаем значение
            # В реальном компиляторе здесь была бы обработка унарных операторов
            return p[1]

        @self.pg.production('primary : literal')
        @self.pg.production('primary : IDENTIFIER')
        @self.pg.production('primary : OPEN_PAREN expression CLOSE_PAREN')
        def primary(p):
            if len(p) == 1:
                return p[0]
            return p[1]

        @self.pg.production('literal : NUMBER')
        def number_literal(p):
            return Number(p[0].value)

        @self.pg.production('literal : STRING')
        def string_literal(p):
            # Убираем кавычки
            value = p[0].value[1:-1]
            return String(value)

        @self.pg.production('literal : TRUE')
        @self.pg.production('literal : FALSE')
        def boolean_literal(p):
            return Boolean(p[0].value == 'true')

        @self.pg.production('literal : NULL')
        def null_literal(p):
            return String("null")

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Unexpected token: {token}")

    def get_parser(self):
        return self.pg.build()