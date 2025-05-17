from gen.Szprajch.SzprajchVisitor import SzprajchVisitor

class SzprajchExecutor(SzprajchVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # Słownik na zmienne

    def visitProgram(self, ctx):
        # Przechodzi po wszystkich dzieciach programu (np. instrukcjach)
        for child in ctx.children:
            self.visit(child)

    def visitAssignmentstmt(self, ctx):
        # Przypisanie wartości do zmiennej
        varname = ctx.varname().getText()
        value = self.visit(ctx.expression())
        self.variables[varname] = value
        return value

    def visitNumberExpr(self, ctx):
        # Pobranie liczby z drzewa składniowego
        try:
            return int(ctx.getChild(0).getText())
        except ValueError:
            raise ValueError(f"Niepoprawna liczba: {ctx.getText()}")

    def visitIdExpr(self, ctx):
        # Pobranie wartości zmiennej
        name = ctx.getText()
        if name not in self.variables:
            raise NameError(f"Zmienna '{name}' nie została zadeklarowana")
        return self.variables[name]

    def visitAddSubExpr(self, ctx):
        # Obsługa dodawania i odejmowania
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        else:
            raise ValueError(f"Nieobsługiwany operator: {operator}")

    def visitMulDivExpr(self, ctx):
        # Obsługa mnożenia i dzielenia całkowitego
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()

        if operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Dzielenie przez zero")
            return left // right  # dzielenie całkowite
        else:
            raise ValueError(f"Nieobsługiwany operator: {operator}")

    def visitPrintstmt(self, ctx):
        # Obsługa polecenia GODEJ (print)
        value = self.visit(ctx.expression())
        print(value)

    def visitComment(self, ctx):
        # Komentarze są ignorowane
        pass