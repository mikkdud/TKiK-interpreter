# "Szprajch" – język umożliwiający komunikację Ślązaków z komputerem

## Autorzy  
Paweł Adamczyk, Mikołaj Dudkiewicz  

<details>
  <summary>Dane kontaktowe</summary>
  Email: 
        <br>adamczyk@student.agh.edu.pl
        <br>mdudkiewicz@student.agh.edu.pl
</details>

## Założenia projektu  
- **Cel:** Stworzenie interpretera własnego języka programowania (inspirowanego językiem śląskim), którego składnia opiera się na BASIC-u.  
- **Rodzaj translatora:** Interpreter (bez kompilacji do kodu pośredniego).  
- **Wynik działania programu:** Bezpośrednie wykonanie kodu źródłowego (interaktywnie lub wczytując plik).  

## Technologie  
- **Język implementacji:** Python   
- **Generator skanerów/parserów:** ANTLR  

## Opis tokenów 
```java
// Tokeny
  PLUS: '+';
  MINUS: '-';
  MUL: '*';
  DIV: '/';
  POW: '**';
  EQ: '=';
  LPAREN: '(';
  RPAREN: ')';
  LSQUARE: '[';
  RSQUARE:']';
  EE: '==';
  NE: '!=';
  LT: '<';
  GT: '>';
  LTE: '<=';
  GTE: '>=';
  COMMA: ',';
  DOT: '.';
  AMPERSAND: '&';
  COLON: ':';
  SEMICOLON: ';';
  ARROW: '->';
  NEWLINE: '\n';
 
// Słowa kluczowe
  VAR: 'ZMIYNNO';
  AND: 'I';
  OR: 'ALBO';
  NOT: 'NIY';
  IF: 'JAK';
  ELIF: 'ALIJAK';
  ELSE: 'INKSZY';
  FOR: 'DLA';
  TO: 'DO';
  STEP: 'CO';
  WHILE: 'PÓKI';
  FUN: 'FUNKCYJO';
  THEN: 'POTYM';
  END: 'KONIEC';
  RETURN: 'NAZOT';
  CONTINUE: 'CIŚ';
  BREAK: 'STOPNIJ';

// Typy
  INT: 'COŁKOWITO';
  FLOAT: 'RUCHOMY';
  STRING: 'ZNAKI';	
  IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Komentarze
  COMMENT: '\'' ~[\r\n]* -> skip;
```

Pełna gramatyka znajduje się w pliku `Szprajch/grammar.g4`