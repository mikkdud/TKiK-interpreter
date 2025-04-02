# "Szprajch" – język umożliwiający komunikację Ślązaków z komputerem

## Autorzy  
Paweł Adamczyk, Mikołaj Dudkiewicz  

<details>
  <summary>Dane kontaktowe</summary>
  Email: adamczyk@student.agh.edu.pl 
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
  ARROW: '->';
  NEWLINE: '\n';
  EOF: ;
 
// Słowa kluczowe
  VAR: 'ZMIYNNO';
  AND: 'I';
  OR: 'ALBO';
  NOT: 'NIY';
  IF: 'JAK';
  ELIF: 'ALIJAK';
  ELSE: 'INKSZI';
  FOR: 'DLA';
  TO: 'DO';
  STEP: 'CO';
  WHILE: 'PÓKI';
  FUN: 'FUNKCJO';
  THEN: 'TOŻ';
  END: 'KONIEC';
  RETURN: 'ODDOJ';
  CONTINUE: 'LEĆ';
  BREAK: 'STOP';

// Typy
INT: ;
FLOAT: ;
STRING: ;	
IDENTIFIER: ;
KEYWORD: ;

```
