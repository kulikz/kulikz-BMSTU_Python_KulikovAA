from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Ключевые слова
        self.lexer.add('PRINT', r'console\.log|alert')
        self.lexer.add('LET', r'let|var')
        self.lexer.add('CONST', r'const')

        #Условия
        self.lexer.add('IF', r'if')
        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('GREATER_EQUAL', r'>=')
        self.lexer.add('LESS', r'<')
        self.lexer.add('GREATER', r'>')
        self.lexer.add('EQUAL_EQUAL', r'==')
        self.lexer.add('OPEN_BRACE', r'\{')
        self.lexer.add('CLOSE_BRACE', r'\}')
        self.lexer.add('FALSE', r'false')

        # Скобки
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Точка с запятой
        self.lexer.add('SEMI_COLON', r'\;')

        # Операторы
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('ASSIGN', r'\=')

        # Числа
        self.lexer.add('NUMBER', r'\d+')

        # Идентификаторы
        self.lexer.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Игнорируем пробелы
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()