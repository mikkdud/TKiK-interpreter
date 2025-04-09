# "Szprajch" – język umożliwiający komunikację Ślązaków z komputerem

## Autorzy  
Paweł Adamczyk, Mikołaj Dudkiewicz  

<details>
  <summary>Dane kontaktowe</summary>
  Email: 
        <br>adamczyk@student.agh.edu.pl
        <br>mdudkiewicz@student.agh.edu.pl
</details>

---

## 📌 Założenia projektu

- **Cel:** Stworzenie interpretera własnego języka programowania (inspirowanego językiem śląskim), którego składnia opiera się na BASIC-u.  
- **Rodzaj translatora:** Interpreter (bez kompilacji do kodu pośredniego).  
- **Wynik działania programu:** Bezpośrednie wykonanie kodu źródłowego (interaktywnie lub wczytując plik).  

---

## 🧰 Technologie

- **Język implementacji:** Python  
- **Generator skanerów/parserów:** ANTLR v4  
- **Wizualizacja AST:** `graphviz`

---

## 🧱 Tokeny (SzprajchTokens.g4)

```antlr
// Operatory
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
EXP : '^' ;
MOD : 'MOD' ;

// Operatory logiczne
NEQ : '<>' ;
GTE : '>=' ;
LTE : '<=' ;
GT  : '>' ;
LT  : '<' ;
EQ  : '=' ;

// Operatory relacyjne
AND : 'I' ;
OR  : 'ALBO' ;
NOT : 'NIY' ;

// Inne
COMMA  : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACKET : '['; 
RBRACKET : ']' ;

// Funkcje
LEN : 'LEN' | 'len' ;
VAL : 'VAL' | 'val' ;
ISNAN : 'ISNAN' | 'isnan' ;

// Słowa kluczowe
PRINT     : 'GODEJ' | 'godej' ;
INPUT     : 'WKLUDZ' | 'wkludz' ;
LET       : 'ZMIYNNO' ;
REM       : 'GODKA' ;
IF        : 'JAK' ;
THEN      : 'POTYM' ;
ELSE      : 'INKSZY' ;
END       : 'KONIEC' ;
FUNCTION  : 'FUNKCYJO' ;
RETURN    : 'NAZOT' ;
FOR       : 'DLA' ;
WHILE     : 'PÓKI' ;
REPEAT    : 'CIOMPLOJ' | 'cimploj' ;
UNTIL     : 'AŻ' ;
STEP      : 'CO' ;
NEXT      : 'NEXT' | 'next' ;
TO        : 'DO' ;
CONTINUE  : 'CIŚ' ;
BREAK     : 'STOPNIJ' ;

// Komentarze
COMMENT : GODKA ~[\r\n]* -> skip ;

// Literały
ID              : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER          : [0-9]+ ('.' [0-9]+)? ;
STRINGLITERAL   : '"' ~["\r\n]* '"' ;
DOLLAR          : '$' ;
NEWLINE         : '\r'? '\n' ;
WS              : [ \t]+ -> skip ;


Pełna gramatyka znajduje się w plikach `Szprajch/*.g4`





# 🔧 Instalacja ANTLR (dla języka Szprajch)

Instrukcja konfiguracji ANTLR-a w systemach Linux i Windows.

---

## 📦 Wymagania wstępne

- Java JDK (`java -version`)
- Python 3 (`python3 --version`)
- pip (`pip3 --version` lub `python -m pip`)

---

## 🐧 Linux / WSL

### 1. Pobierz ANTLR

```bash
cd /usr/local/lib
sudo curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
```

### 2. Dodaj alias i CLASSPATH

```bash
echo "export CLASSPATH=\"/usr/local/lib/antlr-4.13.1-complete.jar:\$CLASSPATH\"" >> ~/.bashrc
echo "alias antlr4='java -jar /usr/local/lib/antlr-4.13.1-complete.jar'" >> ~/.bashrc
source ~/.bashrc
```

### 3. Stwórz środowisko wirtualne i zainstaluj bibliotekę ANTLR

```bash
cd /ścieżka/do/projektu
python3 -m venv venv
source venv/bin/activate
pip install antlr4-python3-runtime
```

---

## 🪟 Windows

### 1. Pobierz ANTLR

Pobierz plik `.jar` z:

[https://www.antlr.org/download/antlr-4.13.1-complete.jar](https://www.antlr.org/download/antlr-4.13.1-complete.jar)

Zapisz np. do `C:\antlr\antlr-4.13.1-complete.jar`

### 2. Ustaw zmienne środowiskowe

W `cmd` lub `PowerShell`:

```cmd
setx CLASSPATH "C:\antlr\antlr-4.13.1-complete.jar;%CLASSPATH%"
```

Stwórz plik `antlr4.bat` np. w `C:\antlr\bin`:

```bat
@echo off
java -jar C:\antlr\antlr-4.13.1-complete.jar %*
```

Dodaj ten folder do `PATH`.

### 3. Utwórz środowisko i zainstaluj bibliotekę

```powershell
cd C:\ścieżka\do\projektu
python -m venv venv
.\venv\Scripts\activate
pip install antlr4-python3-runtime
```

---

## ✅ Użycie ANTLR

Po instalacji możesz wygenerować parser:

```bash
antlr4 Szprajch.g4 -Dlanguage=Python3 -visitor -o gen
```

Pliki zostaną zapisane w folderze `gen/`.

---

Gotowe! Możesz działać z własnym językiem programowania 🚀

---

## 💡 Dodatkowa wskazówka: VS Code i interpreter Pythona

Jeśli używasz VS Code i środowisko `venv` zostało utworzone, ale nie działa np. import `antlr4`, upewnij się, że edytor korzysta z odpowiedniego interpretera.

### ✅ Jak to zrobić:
1. Wciśnij `Ctrl + Shift + P`
2. Wpisz: `Python: Select Interpreter`
3. Wybierz **(Recommended)** lub interpreter znajdujący się w `./venv/bin/python`

To pozwala edytorowi korzystać z dokładnie tego samego środowiska, w którym zainstalowano bibliotekę `antlr4-python3-runtime`.
