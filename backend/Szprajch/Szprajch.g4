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
    | repeatstmt
    | continuestmt   
    | breakstmt 
    | returnstmnt
    | functiondef
    | functioncall
    | COMMENT;

block: (statement NEWLINE* | COMMENT | NEWLINE)* ;

assignmentstmt
    : LET? varname EQ expression                              # VarAssignment
    | varname LBRACKET expression RBRACKET EQ expression          # ListElementAssignment
    ;


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
    FOR varname EQ expression TO expression (STEP expression)? NEWLINE+ loop_block NEXT;

whilestmt: 
    WHILE expression NEWLINE+ loop_block END;

repeatstmt: REPEAT NEWLINE+ loop_block NEWLINE* UNTIL expression;

continuestmt: CONTINUE;

breakstmt: BREAK;

functiondef:
    FUNCTION ID LPAREN paramlist? RPAREN NEWLINE+ function_block END;

paramlist: ID (COMMA ID)*;

returnstmnt: RETURN expression;


loop_statement
    : assignmentstmt
    | printstmt
    | inputstmt
    | ifstmt
    | forstmt
    | whilestmt
    | repeatstmt
    | continuestmt
    | breakstmt
    | COMMENT;

loop_block: (loop_statement NEWLINE+)*;

function_statement
    : assignmentstmt
    | printstmt
    | inputstmt
    | ifstmt
    | forstmt
    | whilestmt
    | repeatstmt
    | returnstmnt
    | continuestmt
    | breakstmt
    | COMMENT;

function_block: (function_statement NEWLINE+)*;
