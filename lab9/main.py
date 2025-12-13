from lexer import Lexer
from parser import Parser

# Пример JavaScript кода
js_code = """
var x = 10;
var y = 5;

console.log(x + y);

if (x > y) {
    console.log("x больше y");
} else {
    console.log("x не больше y");
}

var i = 0;
while (i < 3) {
    console.log(i);
    i = i + 1;
}
"""


def main():
    # Лексический анализ
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(js_code)

    print("Токены:")
    for token in tokens:
        print(f"  {token}")
    print()

    # Синтаксический анализ
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    # Перезагружаем токены для парсера
    tokens = lexer.lex(js_code)

    try:
        ast = parser.parse(tokens)
        print("AST построено успешно!")
        print()

        # Интерпретация
        print("Результат выполнения:")
        print("-" * 30)
        context = {}
        ast.eval(context)
        print("-" * 30)

        print(f"\nКонтекст после выполнения: {context}")

    except ValueError as e:
        print(f"Ошибка парсинга: {e}")


if __name__ == "__main__":
    main()