from gen.Szprajch.SzprajchVisitor import SzprajchVisitor

class SzprajchExecutor(SzprajchVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}

    def visitProgram(self, ctx):
        for child in ctx.children:
            self.visit(child)

    def visitAssignmentstmt(self, ctx):
        varname = ctx.varname().getText()
        value = self.visit(ctx.expression())
        self.variables[varname] = value
        return value

    def visitNumberExpr(self, ctx):
        # Bezpieczne pobranie liczby z pierwszego dziecka
        try:
            return int(ctx.getChild(0).getText())
        except ValueError:
            raise ValueError(f"Niepoprawna liczba: {ctx.getText()}")

    def visitIdExpr(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise NameError(f"Zmienna '{name}' nie została zadeklarowana")
        return self.variables[name]