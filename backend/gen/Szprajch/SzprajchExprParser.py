# Generated from Szprajch/SzprajchExpr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,133,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,51,8,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,3,1,3,1,3,3,3,84,8,3,1,4,1,4,
        1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,3,4,95,8,4,1,4,1,4,1,5,1,5,1,
        6,1,6,1,7,1,7,1,7,3,7,106,8,7,1,7,1,7,1,8,1,8,1,8,5,8,113,8,8,10,
        8,12,8,116,9,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,0,1,4,12,0,2,4,6,8,10,12,14,16,18,20,22,
        0,3,2,0,1,2,6,6,1,0,3,4,1,0,7,12,143,0,25,1,0,0,0,2,33,1,0,0,0,4,
        50,1,0,0,0,6,83,1,0,0,0,8,85,1,0,0,0,10,98,1,0,0,0,12,100,1,0,0,
        0,14,102,1,0,0,0,16,109,1,0,0,0,18,117,1,0,0,0,20,122,1,0,0,0,22,
        127,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,
        0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,30,3,4,2,0,30,31,5,48,0,0,31,34,
        1,0,0,0,32,34,5,48,0,0,33,29,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,
        35,36,6,2,-1,0,36,51,3,10,5,0,37,51,3,12,6,0,38,51,3,6,3,0,39,51,
        3,14,7,0,40,51,5,44,0,0,41,42,5,17,0,0,42,43,3,4,2,0,43,44,5,18,
        0,0,44,51,1,0,0,0,45,46,5,4,0,0,46,51,3,4,2,10,47,48,5,15,0,0,48,
        51,3,4,2,6,49,51,3,8,4,0,50,35,1,0,0,0,50,37,1,0,0,0,50,38,1,0,0,
        0,50,39,1,0,0,0,50,40,1,0,0,0,50,41,1,0,0,0,50,45,1,0,0,0,50,47,
        1,0,0,0,50,49,1,0,0,0,51,77,1,0,0,0,52,53,10,9,0,0,53,54,7,0,0,0,
        54,76,3,4,2,10,55,56,10,8,0,0,56,57,7,1,0,0,57,76,3,4,2,9,58,59,
        10,7,0,0,59,60,7,2,0,0,60,76,3,4,2,8,61,62,10,5,0,0,62,63,5,13,0,
        0,63,76,3,4,2,6,64,65,10,4,0,0,65,66,5,14,0,0,66,76,3,4,2,5,67,68,
        10,3,0,0,68,69,5,5,0,0,69,76,3,4,2,3,70,71,10,1,0,0,71,72,5,19,0,
        0,72,73,3,4,2,0,73,74,5,20,0,0,74,76,1,0,0,0,75,52,1,0,0,0,75,55,
        1,0,0,0,75,58,1,0,0,0,75,61,1,0,0,0,75,64,1,0,0,0,75,67,1,0,0,0,
        75,70,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,5,1,0,
        0,0,79,77,1,0,0,0,80,84,3,18,9,0,81,84,3,20,10,0,82,84,3,22,11,0,
        83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,7,1,0,0,0,85,94,5,19,
        0,0,86,91,3,4,2,0,87,88,5,16,0,0,88,90,3,4,2,0,89,87,1,0,0,0,90,
        93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,
        0,94,86,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,5,20,0,0,97,9,
        1,0,0,0,98,99,5,46,0,0,99,11,1,0,0,0,100,101,5,45,0,0,101,13,1,0,
        0,0,102,103,5,44,0,0,103,105,5,17,0,0,104,106,3,16,8,0,105,104,1,
        0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,18,0,0,108,15,1,
        0,0,0,109,114,3,4,2,0,110,111,5,16,0,0,111,113,3,4,2,0,112,110,1,
        0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,17,1,0,
        0,0,116,114,1,0,0,0,117,118,5,21,0,0,118,119,5,17,0,0,119,120,3,
        4,2,0,120,121,5,18,0,0,121,19,1,0,0,0,122,123,5,22,0,0,123,124,5,
        17,0,0,124,125,3,4,2,0,125,126,5,18,0,0,126,21,1,0,0,0,127,128,5,
        23,0,0,128,129,5,17,0,0,129,130,3,4,2,0,130,131,5,18,0,0,131,23,
        1,0,0,0,10,27,33,50,75,77,83,91,94,105,114
    ]

class SzprajchExprParser ( Parser ):

    grammarFileName = "SzprajchExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'^'", "'MOD'", 
                     "'<>'", "'>='", "'<='", "'>'", "'<'", "'='", "'I'", 
                     "'ALBO'", "'NIY'", "','", "'('", "')'", "'['", "']'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'ZMIYNNO'", "'GODKA'", "'JAK'", "'POTYM'", 
                     "'INKSZY'", "'KONIEC'", "'FUNKCYJO'", "'NAZOT'", "'DLA'", 
                     "'POKI'", "<INVALID>", "<INVALID>", "'CO'", "<INVALID>", 
                     "'DO'", "<INVALID>", "'STOPNIJ'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'$'" ]

    symbolicNames = [ "<INVALID>", "MUL", "DIV", "ADD", "SUB", "EXP", "MOD", 
                      "NEQ", "GTE", "LTE", "GT", "LT", "EQ", "AND", "OR", 
                      "NOT", "COMMA", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "LEN", "VAL", "ISNAN", "PRINT", "INPUT", "LET", "REM", 
                      "IF", "THEN", "ELSE", "END", "FUNCTION", "RETURN", 
                      "FOR", "WHILE", "REPEAT", "UNTIL", "STEP", "NEXT", 
                      "TO", "CONTINUE", "BREAK", "COMMENT", "ID", "NUMBER", 
                      "STRINGLITERAL", "DOLLAR", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_func = 3
    RULE_list = 4
    RULE_string = 5
    RULE_number = 6
    RULE_functioncall = 7
    RULE_arglist = 8
    RULE_lenfunc = 9
    RULE_valfunc = 10
    RULE_isnanfunc = 11

    ruleNames =  [ "program", "statement", "expression", "func", "list", 
                   "string", "number", "functioncall", "arglist", "lenfunc", 
                   "valfunc", "isnanfunc" ]

    EOF = Token.EOF
    MUL=1
    DIV=2
    ADD=3
    SUB=4
    EXP=5
    MOD=6
    NEQ=7
    GTE=8
    LTE=9
    GT=10
    LT=11
    EQ=12
    AND=13
    OR=14
    NOT=15
    COMMA=16
    LPAREN=17
    RPAREN=18
    LBRACKET=19
    RBRACKET=20
    LEN=21
    VAL=22
    ISNAN=23
    PRINT=24
    INPUT=25
    LET=26
    REM=27
    IF=28
    THEN=29
    ELSE=30
    END=31
    FUNCTION=32
    RETURN=33
    FOR=34
    WHILE=35
    REPEAT=36
    UNTIL=37
    STEP=38
    NEXT=39
    TO=40
    CONTINUE=41
    BREAK=42
    COMMENT=43
    ID=44
    NUMBER=45
    STRINGLITERAL=46
    DOLLAR=47
    NEWLINE=48
    WS=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.StatementContext,i)


        def getRuleIndex(self):
            return SzprajchExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SzprajchExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 404620294389776) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(SzprajchExprParser.NEWLINE, 0)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SzprajchExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 15, 17, 19, 21, 22, 23, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.expression(0)
                self.state = 30
                self.match(SzprajchExprParser.NEWLINE)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(SzprajchExprParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SzprajchExprParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(SzprajchExprParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(SzprajchExprParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SzprajchExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def GTE(self):
            return self.getToken(SzprajchExprParser.GTE, 0)
        def GT(self):
            return self.getToken(SzprajchExprParser.GT, 0)
        def LTE(self):
            return self.getToken(SzprajchExprParser.LTE, 0)
        def LT(self):
            return self.getToken(SzprajchExprParser.LT, 0)
        def EQ(self):
            return self.getToken(SzprajchExprParser.EQ, 0)
        def NEQ(self):
            return self.getToken(SzprajchExprParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExpExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def EXP(self):
            return self.getToken(SzprajchExprParser.EXP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpExpr" ):
                listener.enterExpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpExpr" ):
                listener.exitExpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpExpr" ):
                return visitor.visitExpExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(SzprajchExprParser.FuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncExpr" ):
                listener.enterFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncExpr" ):
                listener.exitFuncExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncExpr" ):
                return visitor.visitFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(SzprajchExprParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class IndexExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def LBRACKET(self):
            return self.getToken(SzprajchExprParser.LBRACKET, 0)
        def RBRACKET(self):
            return self.getToken(SzprajchExprParser.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexExpr" ):
                listener.enterIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexExpr" ):
                listener.exitIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegateExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(SzprajchExprParser.SUB, 0)
        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateExpr" ):
                listener.enterNegateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateExpr" ):
                listener.exitNegateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegateExpr" ):
                return visitor.visitNegateExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(SzprajchExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(SzprajchExprParser.DIV, 0)
        def MOD(self):
            return self.getToken(SzprajchExprParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(SzprajchExprParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SzprajchExprParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(SzprajchExprParser.ListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SzprajchExprParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(SzprajchExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(SzprajchExprParser.ADD, 0)
        def SUB(self):
            return self.getToken(SzprajchExprParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SzprajchExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functioncall(self):
            return self.getTypedRuleContext(SzprajchExprParser.FunctioncallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SzprajchExprParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SzprajchExprParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.string()
                pass

            elif la_ == 2:
                localctx = SzprajchExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.number()
                pass

            elif la_ == 3:
                localctx = SzprajchExprParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.func()
                pass

            elif la_ == 4:
                localctx = SzprajchExprParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.functioncall()
                pass

            elif la_ == 5:
                localctx = SzprajchExprParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(SzprajchExprParser.ID)
                pass

            elif la_ == 6:
                localctx = SzprajchExprParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(SzprajchExprParser.LPAREN)
                self.state = 42
                self.expression(0)
                self.state = 43
                self.match(SzprajchExprParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = SzprajchExprParser.NegateExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(SzprajchExprParser.SUB)
                self.state = 46
                self.expression(10)
                pass

            elif la_ == 8:
                localctx = SzprajchExprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(SzprajchExprParser.NOT)
                self.state = 48
                self.expression(6)
                pass

            elif la_ == 9:
                localctx = SzprajchExprParser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.list_()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SzprajchExprParser.MulDivExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = SzprajchExprParser.AddSubExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = SzprajchExprParser.RelExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = SzprajchExprParser.AndExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 62
                        self.match(SzprajchExprParser.AND)
                        self.state = 63
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = SzprajchExprParser.OrExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 65
                        self.match(SzprajchExprParser.OR)
                        self.state = 66
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = SzprajchExprParser.ExpExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 67
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 68
                        self.match(SzprajchExprParser.EXP)
                        self.state = 69
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = SzprajchExprParser.IndexExprContext(self, SzprajchExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 70
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 71
                        self.match(SzprajchExprParser.LBRACKET)
                        self.state = 72
                        self.expression(0)
                        self.state = 73
                        self.match(SzprajchExprParser.RBRACKET)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lenfunc(self):
            return self.getTypedRuleContext(SzprajchExprParser.LenfuncContext,0)


        def valfunc(self):
            return self.getTypedRuleContext(SzprajchExprParser.ValfuncContext,0)


        def isnanfunc(self):
            return self.getTypedRuleContext(SzprajchExprParser.IsnanfuncContext,0)


        def getRuleIndex(self):
            return SzprajchExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = SzprajchExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.lenfunc()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.valfunc()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.isnanfunc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(SzprajchExprParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(SzprajchExprParser.RBRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SzprajchExprParser.COMMA)
            else:
                return self.getToken(SzprajchExprParser.COMMA, i)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = SzprajchExprParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SzprajchExprParser.LBRACKET)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 123145317679120) != 0):
                self.state = 86
                self.expression(0)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 87
                    self.match(SzprajchExprParser.COMMA)
                    self.state = 88
                    self.expression(0)
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 96
            self.match(SzprajchExprParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(SzprajchExprParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = SzprajchExprParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(SzprajchExprParser.STRINGLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SzprajchExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = SzprajchExprParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SzprajchExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SzprajchExprParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SzprajchExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SzprajchExprParser.RPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(SzprajchExprParser.ArglistContext,0)


        def getRuleIndex(self):
            return SzprajchExprParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = SzprajchExprParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(SzprajchExprParser.ID)
            self.state = 103
            self.match(SzprajchExprParser.LPAREN)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 123145317679120) != 0):
                self.state = 104
                self.arglist()


            self.state = 107
            self.match(SzprajchExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SzprajchExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SzprajchExprParser.COMMA)
            else:
                return self.getToken(SzprajchExprParser.COMMA, i)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = SzprajchExprParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.expression(0)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 110
                self.match(SzprajchExprParser.COMMA)
                self.state = 111
                self.expression(0)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LenfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEN(self):
            return self.getToken(SzprajchExprParser.LEN, 0)

        def LPAREN(self):
            return self.getToken(SzprajchExprParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SzprajchExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_lenfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLenfunc" ):
                listener.enterLenfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLenfunc" ):
                listener.exitLenfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLenfunc" ):
                return visitor.visitLenfunc(self)
            else:
                return visitor.visitChildren(self)




    def lenfunc(self):

        localctx = SzprajchExprParser.LenfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lenfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(SzprajchExprParser.LEN)
            self.state = 118
            self.match(SzprajchExprParser.LPAREN)
            self.state = 119
            self.expression(0)
            self.state = 120
            self.match(SzprajchExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(SzprajchExprParser.VAL, 0)

        def LPAREN(self):
            return self.getToken(SzprajchExprParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SzprajchExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_valfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValfunc" ):
                listener.enterValfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValfunc" ):
                listener.exitValfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValfunc" ):
                return visitor.visitValfunc(self)
            else:
                return visitor.visitChildren(self)




    def valfunc(self):

        localctx = SzprajchExprParser.ValfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_valfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(SzprajchExprParser.VAL)
            self.state = 123
            self.match(SzprajchExprParser.LPAREN)
            self.state = 124
            self.expression(0)
            self.state = 125
            self.match(SzprajchExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsnanfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ISNAN(self):
            return self.getToken(SzprajchExprParser.ISNAN, 0)

        def LPAREN(self):
            return self.getToken(SzprajchExprParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SzprajchExprParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SzprajchExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return SzprajchExprParser.RULE_isnanfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsnanfunc" ):
                listener.enterIsnanfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsnanfunc" ):
                listener.exitIsnanfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsnanfunc" ):
                return visitor.visitIsnanfunc(self)
            else:
                return visitor.visitChildren(self)




    def isnanfunc(self):

        localctx = SzprajchExprParser.IsnanfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_isnanfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(SzprajchExprParser.ISNAN)
            self.state = 128
            self.match(SzprajchExprParser.LPAREN)
            self.state = 129
            self.expression(0)
            self.state = 130
            self.match(SzprajchExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




