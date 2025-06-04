from antlr4.error.ErrorListener import ErrorListener

class SzprajchErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Błąd składni w linii {line}, kolumna {column}: {msg}")
