import ace from 'ace-builds/src-noconflict/ace';

// Zasady kolorowania
const SzprajchHighlightRules = function () {
  this.$rules = {
    start: [
      { token: "comment.line", regex: "GODKA.*$" },
      { token: "keyword.control", regex: "\\b(?:JAK|POTYM|INKSZY|KONIEC|FUNKCYJO|NAZOT)\\b" },
      { token: "keyword", regex: "\\b(?:GODEJ|wkludz|ZMIYNNO|GODKA|DLA|PÓKI|CIOMPLOJ|AŻ|AZ|CO|NEXT|CIŚ|CIS|STOPNIJ|VAL|LEN|ISNAN)\\b" },
      { token: "constant.numeric", regex: "\\b\\d+(?:\\.\\d+)?\\b" },
      { token: "string", regex: '".*?"' },
      { token: "keyword.operator", regex: "\\+|\\-|\\*|\\/|\\^|=|<>|>=|<=|>|<|MOD|I|ALBO|NIY" },
      { token: "paren.lparen", regex: "[\\(\\[\\{]" },
      { token: "paren.rparen", regex: "[\\)\\]\\}]" },
      { token: "text", regex: "\\s+" },
      { token: "identifier", regex: "[a-zA-Z_][a-zA-Z0-9_]*" },
    ],
  };
};

ace.define("ace/mode/szprajch_highlight_rules", ["require", "exports", "module", "ace/lib/oop", "ace/mode/text_highlight_rules"], function (require, exports, module) {
  const oop = require("ace/lib/oop");
  const TextHighlightRules = require("ace/mode/text_highlight_rules").TextHighlightRules;
  oop.inherits(SzprajchHighlightRules, TextHighlightRules);
  exports.SzprajchHighlightRules = SzprajchHighlightRules;
});

ace.define("ace/mode/szprajch", ["require", "exports", "module", "ace/lib/oop", "ace/mode/text", "ace/mode/szprajch_highlight_rules"], function (require, exports, module) {
  const oop = require("ace/lib/oop");
  const TextMode = require("ace/mode/text").Mode;
  const SzprajchHighlightRules = require("ace/mode/szprajch_highlight_rules").SzprajchHighlightRules;

  const Mode = function () {
    this.HighlightRules = SzprajchHighlightRules;
    this.$behaviour = this.$defaultBehaviour;
  };
  oop.inherits(Mode, TextMode);

  (function () {
    this.lineCommentStart = "GODKA";
    this.$id = "ace/mode/szprajch";
  }).call(Mode.prototype);

  exports.Mode = Mode;
});