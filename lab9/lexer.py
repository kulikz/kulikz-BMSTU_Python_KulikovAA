from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Ключевые слова
        self.lexer.add('VAR', r'\bvar\b')
        self.lexer.add('LET', r'\blet\b')
        self.lexer.add('CONST', r'\bconst\b')
        self.lexer.add('IF', r'\bif\b')
        self.lexer.add('ELSE', r'\belse\b')
        self.lexer.add('WHILE', r'\bwhile\b')
        self.lexer.add('TRUE', r'\btrue\b')
        self.lexer.add('FALSE', r'\bfalse\b')
        self.lexer.add('NULL', r'\bnull\b')
        self.lexer.add('FUNCTION', r'\bfunction\b')
        self.lexer.add('RETURN', r'\breturn\b')

        # Встроенные функции
        self.lexer.add('CONSOLE_LOG', r'\bconsole\.log\b')
        self.lexer.add('ALERT', r'\balert\b')
        self.lexer.add('PARSE_INT', r'\bparseInt\b')
        self.lexer.add('PARSE_FLOAT', r'\bparseFloat\b')

        # Идентификаторы
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_$][a-zA-Z0-9_$]*')

        # Числа (целые и с плавающей точкой)
        self.lexer.add('NUMBER', r'\d+(\.\d+)?')

        # Строки
        self.lexer.add('STRING', r'\"([^\\\"]|\\.)*\"|\'([^\\\']|\\.)*\'')

        # Операторы
        self.lexer.add('ASSIGN', r'=')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'\-')
        self.lexer.add('MULTIPLY', r'\*')
        self.lexer.add('DIVIDE', r'\/')
        self.lexer.add('MODULO', r'%')

        # Операторы сравнения
        self.lexer.add('EQUAL', r'==')
        self.lexer.add('NOT_EQUAL', r'!=')
        self.lexer.add('LESS_THAN', r'<')
        self.lexer.add('GREATER_THAN', r'>')
        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('GREATER_EQUAL', r'>=')

        # Логические операторы
        self.lexer.add('AND', r'&&')
        self.lexer.add('OR', r'\|\|')
        self.lexer.add('NOT', r'!')

        # Скобки и разделители
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_BRACE', r'\{')
        self.lexer.add('CLOSE_BRACE', r'\}')
        self.lexer.add('SEMICOLON', r'\;')
        self.lexer.add('COMMA', r'\,')

        # Игнорируем пробелы, табуляции и переводы строк
        self.lexer.ignore(r'\s+')

        # Игнорируем однострочные комментарии
        self.lexer.ignore(r'//[^\n]*')

        # Игнорируем многострочные комментарии
        self.lexer.ignore(r'/\*[\s\S]*?\*/')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()