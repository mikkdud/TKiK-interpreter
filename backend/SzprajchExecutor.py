from gen.Szprajch.SzprajchVisitor import SzprajchVisitor
from gen.Szprajch.SzprajchParser import SzprajchParser

class SzprajchExecutor(SzprajchVisitor):
    def __init__(self):
        super().__init__()
        self.output = []            # Lista na wyniki wypisywane przez GODEJ
        self.variable_stack = [{}]  # stos słowników zmiennych
        self.functions = {}         # Słownik na funkcje użytkownika

    def get_variable(self, name):
        for scope in reversed(self.variable_stack):
            if name in scope:
                return scope[name]
        raise NameError(f"Zmienna '{name}' nie została zadeklarowana")

    def set_variable(self, name, value):
        self.variable_stack[-1][name] = value

    def visitProgram(self, ctx):
        # Główna pętla programu - odwiedza wszystkie instrukcje
        for child in ctx.children:
            self.visit(child)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitVarAssignment(self, ctx):
        # Przypisanie wartości do zmiennej
        varname = ctx.varname().getText()
        value = self.visit(ctx.expression())
        self.set_variable(varname, value)
        return value

    def visitListElementAssignment(self, ctx):
        # Przypisanie do elementu listy, np. lista[1] = 5
        list_name = ctx.varname().getText()
        index = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        list_obj = self.get_variable(list_name)

        if not isinstance(list_obj, list):
            raise TypeError(f"Zmienna '{list_name}' nie jest listą")

        if not (0 <= index < len(list_obj)):
            raise IndexError(f"Indeks {index} poza zakresem listy '{list_name}'")

        list_obj[index] = value
        return value

    def visitNumberExpr(self, ctx):
        # Zwraca liczbę całkowitą z drzewa składniowego
        return int(ctx.getChild(0).getText())

    def visitIdExpr(self, ctx):
        # Zwraca wartość zmiennej
        return self.get_variable(ctx.getText())

    def visitAddSubExpr(self, ctx):
        # Obsługa dodawania i odejmowania
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()
        
        # print(f"AddSubExpr: {left} ({type(left)}), ({str(left)}), {operator}, {right} ({type(right)}) ({str(right)})")
        if operator == '+':
        # Obsługa konkatenacji stringów
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif operator == '-':
            return left - right
        else:
            raise ValueError(f"Nieobsługiwany operator: {operator}. Linia: {ctx.start.line}")

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
            return left // right
        elif operator == 'MOD':
            return left % right
        else:
            raise ValueError(f"Nieobsługiwany operator: {operator}")

    def visitRelExpr(self, ctx):
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
        # Obsługa GODEJ (print)
        value = self.visit(ctx.expression())
        self.output.append(str(value))
        print(value)

    def visitComment(self, ctx):
        # Komentarze są ignorowane
        pass

    def visitIfstmt(self, ctx):
        # Instrukcja warunkowa IF/ELIF/ELSE
        if self.visit(ctx.expression()):
            self.visit(ctx.block())
            return  # zakończ, nie sprawdzaj elif/else
        for elif_ctx in ctx.elifstmt():
            if self.visit(elif_ctx.expression()):
                self.visit(elif_ctx.block())
                return  # zakończ po pierwszym trafionym elif
        if ctx.elsestmt():
            self.visit(ctx.elsestmt())

    def visitElifstmt(self, ctx):
        # Obsługa ELIF
        if self.visit(ctx.expression()):
            self.visit(ctx.block())
            return True # informuje, że warunek był spełniony
        return False

    def visitElsestmt(self, ctx):
        # Obsługa ELSE
        self.visit(ctx.block())

    def visitForstmt(self, ctx):
        # Pętla FOR
        varname = ctx.varname().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        step = self.visit(ctx.expression(2)) if ctx.expression(2) else 1

        self.set_variable(varname, start)
        while (step > 0 and self.get_variable(varname) <= end) or (step < 0 and self.get_variable(varname) >= end):
            self.visit(ctx.loop_block())
            self.set_variable(varname, self.get_variable(varname) + step)

    def visitNotExpr(self, ctx):
        # Negacja logiczna
        value = self.visit(ctx.expression())
        return int(not value)

    def visitLogicalAndExpr(self, ctx):
        # Operator logiczny AND
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return int(bool(left) and bool(right))

    def visitNegateExpr(self, ctx):
        # Negacja liczby (np. -x)
        return -self.visit(ctx.expression())

    def visitFunctiondef(self, ctx):
        # Definicja funkcji użytkownika
        func_name = ctx.ID().getText()
        params = [token.getText() for token in ctx.paramlist().getTokens(SzprajchParser.ID)]
        block = ctx.function_block()
        self.functions[func_name] = (params, block)

    def visitFunctioncall(self, ctx):
    # Wywołanie funkcji użytkownika
        name = ctx.ID().getText()
        args = [self.visit(arg) for arg in ctx.arglist().expression()] if ctx.arglist() else []

        if name not in self.functions:
            raise NameError(f"Nie znaleziono funkcji '{name}'")

        params, block = self.functions[name]
        if len(params) != len(args):
            raise TypeError(f"Funkcja '{name}' oczekuje {len(params)} argumentów, a otrzymano {len(args)}")

        # Nowy zakres zmiennych
        self.variable_stack.append(dict(zip(params, args)))

        try:
            for stmt in block.function_statement():
                self.visit(stmt)
            # Jeśli nie było return, to None
            result = None
        except ReturnValue as rv:
            result = rv.value
        finally:
            self.variable_stack.pop()

        return result


    def visitReturnstmnt(self, ctx):
        # Zwraca wartość z funkcji
        value = self.visit(ctx.expression())
        raise ReturnValue(value)

    def visitFunctionCallExpr(self, ctx):
        # Wywołanie funkcji jako wyrażenie
        return self.visit(ctx.functioncall())

    def visitList(self, ctx):
        # Tworzenie listy
        return [self.visit(child) for child in ctx.expression()]

    def visitIndexExpr(self, ctx):
        # Dostęp do elementu listy przez indeks
        list_obj = self.visit(ctx.expression(0))
        index = self.visit(ctx.expression(1))
        return list_obj[index]

    def visitLenfunc(self, ctx):
        # Funkcja LEN - długość listy
        list_obj = self.visit(ctx.expression())
        if not isinstance(list_obj, list):
            raise TypeError("Funkcja LEN oczekuje listy jako argumentu")
        return len(list_obj)

    def visitRepeatstmt(self, ctx):
        # Pętla repeat-until
        while True:
            # Wykonaj blok pętli
            for child in ctx.loop_block().children:
                result = self.visit(child)
                
                # Obsługa break/continue
                if isinstance(result, BreakSignal):
                    return
                if isinstance(result, ContinueSignal):
                    break
            # Sprawdź warunek zakończenia pętli
            condition = self.visit(ctx.expression())
            if condition:
                break

    def visitBreakstmt(self, ctx):
        # Obsługa break
        return BreakSignal()

    def visitContinuestmt(self, ctx):
        # Obsługa continue
        return ContinueSignal()

    def visitWhilestmt(self, ctx):
        # Pętla while (POKI ... POTYM ... KONIEC)
        while self.visit(ctx.expression()):
            for child in ctx.loop_block().children:
                result = self.visit(child)
                if isinstance(result, BreakSignal):
                    return
                if isinstance(result, ContinueSignal):
                    break
                
    def visitStringExpr(self, ctx):
        text = ctx.getText()
        # Usuwamy cudzysłowy na początku i końcu (np. "tekst" -> tekst)
        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        return text

    def visitExpExpr(self, ctx):
        base = self.visit(ctx.expression(0))
        exponent = self.visit(ctx.expression(1))
        return base ** exponent
    
    def visitValfunc(self, ctx):
        # Funkcja VAL - konwersja stringa na liczbę
        val = self.visit(ctx.expression())
        try:
            # Jeśli zawiera kropkę, traktuj jako float
            return int(val) if '.' not in str(val) else float(val)
        except (ValueError, TypeError):
            return float('nan')  # zwraca NaN, jeśli nie można sparsować

    def visitIsnanfunc(self, ctx):
        val = self.visit(ctx.expression())
        try:
            return isinstance(val, float) and val != val  # tylko NaN jest różne od siebie
        except:
            return False



# Pomocnicze klasy
class BreakSignal: pass
class ContinueSignal: pass

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
