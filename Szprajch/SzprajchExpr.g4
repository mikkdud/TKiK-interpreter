grammar SzprajchExpr;
import SzprajchTokens;


program: statement+;

statement: expression NEWLINE| NEWLINE;

expression: 
    string                                      # StringExpr
    | number                                    # NumberExpr
    | func                                      # FuncExpr
    | id                                        # IdExpr
    | (LPAREN expression RPAREN)                # ParenExpr
    | expression op=(MUL|DIV|MOD) expression    # MulDivExpr
    | expression op=(ADD|SUB) expression        # AddSubExpr
    | expression op=(GTE|GT|LTE|LT|EQ|NEQ) expression   # RelExpr
    | NOT expression                            # NotExpr
    | expression AND expression                 # AndExpr
    | expression OR expression                  # OrExpr
    | <assoc=right> expression EXP expression   # ExpExpr
    | list                                      # ListExpr
    | expression LBRACKET expression RBRACKET   # IndexExpr
    ;

func
    : lenfunc
    | valfunc
    | isnanfunc
    ;

list: LBRACKET (expression (COMMA expression)*)? RBRACKET;

string: STRINGLITERAL;

number: NUMBER;

id: functioncall | ID;

functioncall: ID LPAREN arglist? RPAREN;

arglist: expression (COMMA expression)*;

lenfunc: LEN LPAREN expression RPAREN;

valfunc: VAL LPAREN expression RPAREN;

isnanfunc: ISNAN LPAREN expression RPAREN;

//exprlist
//    : expression (COMMA expression)*
//    ;