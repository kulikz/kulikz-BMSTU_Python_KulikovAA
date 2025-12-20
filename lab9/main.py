from lexer import Lexer
from parser import Parser

# Тестовый код на JavaScript
js_code = """
let x = 10;
const y = 18;
console.log(x+y);
console.log(x * y);
alert(x-y);
"""
# Инициализация лексера и парсера
lexer = Lexer().get_lexer()
parser = Parser()
parser.parse()
pg = parser.get_parser()
# Лексический анализ
tokens = lexer.lex(js_code)
ast = pg.parse(tokens)
result = ast.eval()

