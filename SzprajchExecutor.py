from gen.Szprajch.SzprajchVisitor import SzprajchVisitor

class SzprajchExecutor(SzprajchVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # Słownik na zmienne

    def visitProgram(self, ctx):
        for child in ctx.children:
            self.visit(child)

    def visitAssignmentstmt(self, ctx):
        varname = ctx.varname().getText()
        value = self.visit(ctx.expression())
        self.variables[varname] = value
        return value

    def visitNumberExpr(self, ctx):
        try:
            return int(ctx.getChild(0).getText())
        except ValueError:
            raise ValueError(f"Niepoprawna liczba: {ctx.getText()}")

    def visitIdExpr(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise NameError(f"Zmienna '{name}' nie została zadeklarowana")
        return self.variables[name]

    def visitAddSubExpr(self, ctx):
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
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()

        if operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Dzielenie przez zero")
            return left // right
        else:
            raise ValueError(f"Nieobsługiwany operator: {operator}")

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()

        if operator == "<":
            return left < right
        elif operator == ">":
            return left > right
        elif operator == "<=":
            return left <= right
        elif operator == ">=":
            return left >= right
        elif operator == "=":
            return left == right
        elif operator == "<>":
            return left != right
        else:
            raise ValueError(f"Nieobsługiwany operator porównania: {operator}")

    def visitPrintstmt(self, ctx):
        value = self.visit(ctx.expression())
        print(value)

    def visitComment(self, ctx):
        pass

    def visitIfstmt(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.block())
        elif ctx.elsestmt():
            self.visit(ctx.elsestmt())

    def visitForstmt(self, ctx):
        varname = ctx.varname().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        step = self.visit(ctx.expression(2)) if ctx.expression(2) else 1

        self.variables[varname] = start
        while (step > 0 and self.variables[varname] <= end) or (step < 0 and self.variables[varname] >= end):
            self.visit(ctx.block())
            self.variables[varname] += step

