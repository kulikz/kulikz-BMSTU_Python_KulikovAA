from lexer import Lexer
from parser import Parser
from codegen import CodeGen

# JS код
js_code = """
let flag = false;
let R = 5;
let x = 2;
let y = 3;

alert(flag);
"""

# Создаем CodeGen
codegen = CodeGen()

# Создаем лексер и парсер
lexer = Lexer().get_lexer()
parser = Parser(codegen)
parser.parse()
pg = parser.get_parser()

# Разбираем и выполняем
tokens = lexer.lex(js_code)
ast = pg.parse(tokens)
ast.eval()

# Компилируем и запускаем
codegen.create_ir()
codegen.save_ir("output.ll")
codegen.run()

# Сохраняем исходный код
with open("input.js", "w", encoding="utf-8") as f:
    f.write(js_code)