lexer grammar SzprajchTokens; 

/*
    ========= Lexer Rules =========
*/

// operators
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
EXP : '^' ;
MOD : 'MOD' ;

// logical
NEQ : '<>' ;
GTE : '>=' ;
LTE : '<=' ;
GT  : '>' ;
LT  : '<' ;
EQ  : '=' ;

// relational
AND : 'I' ;
OR  : 'ALBO' ;
NOT : 'NIY' ;

// other
COMMA  : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACKET : '['; 
RBRACKET : ']'; 

// functions
LEN : 'LEN' | 'len' ;
VAL : 'VAL' | 'val' ;
ISNAN   : 'ISNAN' | 'isnan' ;

// keywords
PRINT     : 'GODEJ' | 'godej' ;
INPUT     : 'WKLUDZ' | 'wkludz' ;
LET       : 'ZMIYNNO' ;
REM       : 'GODKA' ;
IF        : 'JAK' ;
THEN      : 'POTYM' ;
ELSE      : 'INKSZY' ;
END       : 'KONIEC';
FUNCTION  : 'FUNKCYJO';
RETURN    : 'NAZOT';
FOR       : 'DLA' ;
WHILE     : 'PÓKI' ;
REPEAT    : 'CIOMPLOJ' | 'ciomploj' ;
UNTIL     : 'AŻ' | 'AZ' ;
STEP      : 'CO' ;
NEXT      : 'NEXT' | 'next' ;
TO        : 'DO' ;
CONTINUE  : 'CIŚ' | 'CIS' ;
BREAK     : 'STOPNIJ' ;

// comments
COMMENT : REM ~[\r\n]* -> skip ;

// literals
ID              : [a-zA-Z_][a-zA-Z0-9_]* ;  // match identifiers
NUMBER          : [0-9]+ ('.' [0-9]+)?;   // match integers
STRINGLITERAL   : '"' ~ ["\r\n]* '"' ;
DOLLAR          : '$' ;
NEWLINE         :'\r'? '\n' ;  // return newlines to parser (end-statement signal)
WS              : [ \t]+ -> skip ; // toss out whitespace
