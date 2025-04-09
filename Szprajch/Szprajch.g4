grammar Szprajch;
import SzprajchExpr, SzprajchTokens;

/*
    ========= Parser Rules =========
*/
program: block EOF;

statement
    : assignmentstmt
    | printstmt
    | inputstmt
    | ifstmt
    | forstmt
    | whilestmt
    | functiondef
    | returnstmnt
    | repeatstmt // ?
    | continuestmt // ?
    | breakstmt
    | COMMENT;

block: (statement (NEWLINE+ | EOF))*;

assignmentstmt: LET? varname EQ expression;

varname: ID;

printstmt: PRINT expression;

inputstmt: INPUT string varname;

ifstmt: 
    IF expression NEWLINE* THEN NEWLINE+ block elifstmt* elsestmt? END;

elifstmt: 
    ELSE IF expression NEWLINE* THEN NEWLINE+ block;

elsestmt: 
    ELSE NEWLINE+ block;

forstmt: 
    FOR varname EQ expression TO expression (STEP expression)? NEWLINE+ block NEXT;

whilestmt: 
    WHILE expression NEWLINE+ block END;

repeatstmt: REPEAT NEWLINE+ block NEWLINE* UNTIL expression;

continuestmt: CONTINUE;

breakstmt: BREAK;

functiondef:
    FUNCTION ID LPAREN paramlist? RPAREN NEWLINE+ block END;

paramlist: ID (COMMA ID)*;

returnstmnt: RETURN expression;