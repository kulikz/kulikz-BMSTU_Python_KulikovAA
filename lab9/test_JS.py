from lexer import Lexer
from parser import Parser


def test_simple():
    """Простой тест арифметики"""
    code = """
    console.log(10 + 5 * 2);
    """

    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    tokens = lexer.lex(code)
    ast = parser.parse(tokens)

    context = {}
    print("Test 1 - Арифметика:")
    ast.eval(context)


def test_variables():
    """Тест переменных"""
    code = """
    var a = 10;
    var b = 20;
    console.log(a + b);
    """

    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    tokens = lexer.lex(code)
    ast = parser.parse(tokens)

    context = {}
    print("\nTest 2 - Переменные:")
    ast.eval(context)


def test_condition():
    """Тест условия"""
    code = """
    var x = 15;
    if (x > 10) {
        console.log("x больше 10");
    }
    """

    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    tokens = lexer.lex(code)
    ast = parser.parse(tokens)

    context = {}
    print("\nTest 3 - Условие:")
    ast.eval(context)


def test_loop():
    """Тест цикла"""
    code = """
    var i = 0;
    while (i < 3) {
        console.log(i);
        i = i + 1;
    }
    """

    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    tokens = lexer.lex(code)
    ast = parser.parse(tokens)

    context = {}
    print("\nTest 4 - Цикл:")
    ast.eval(context)


def test_complex():
    """Комплексный тест"""
    code = """
    var sum = 0;
    var i = 1;

    while (i <= 5) {
        sum = sum + i;
        i = i + 1;
    }

    console.log("Сумма чисел от 1 до 5: " + sum);
    """

    lexer = Lexer().get_lexer()
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()

    tokens = lexer.lex(code)
    ast = parser.parse(tokens)

    context = {}
    print("\nTest 5 - Комплексный:")
    ast.eval(context)


if __name__ == "__main__":
    test_simple()
    test_variables()
    test_condition()
    test_loop()
    test_complex()