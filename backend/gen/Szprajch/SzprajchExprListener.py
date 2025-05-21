# Generated from Szprajch/SzprajchExpr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SzprajchExprParser import SzprajchExprParser
else:
    from SzprajchExprParser import SzprajchExprParser

# This class defines a complete listener for a parse tree produced by SzprajchExprParser.
class SzprajchExprListener(ParseTreeListener):

    # Enter a parse tree produced by SzprajchExprParser#program.
    def enterProgram(self, ctx:SzprajchExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#program.
    def exitProgram(self, ctx:SzprajchExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#statement.
    def enterStatement(self, ctx:SzprajchExprParser.StatementContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#statement.
    def exitStatement(self, ctx:SzprajchExprParser.StatementContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#AndExpr.
    def enterAndExpr(self, ctx:SzprajchExprParser.AndExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#AndExpr.
    def exitAndExpr(self, ctx:SzprajchExprParser.AndExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#StringExpr.
    def enterStringExpr(self, ctx:SzprajchExprParser.StringExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#StringExpr.
    def exitStringExpr(self, ctx:SzprajchExprParser.StringExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#IdExpr.
    def enterIdExpr(self, ctx:SzprajchExprParser.IdExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#IdExpr.
    def exitIdExpr(self, ctx:SzprajchExprParser.IdExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#RelExpr.
    def enterRelExpr(self, ctx:SzprajchExprParser.RelExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#RelExpr.
    def exitRelExpr(self, ctx:SzprajchExprParser.RelExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#ExpExpr.
    def enterExpExpr(self, ctx:SzprajchExprParser.ExpExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#ExpExpr.
    def exitExpExpr(self, ctx:SzprajchExprParser.ExpExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#FuncExpr.
    def enterFuncExpr(self, ctx:SzprajchExprParser.FuncExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#FuncExpr.
    def exitFuncExpr(self, ctx:SzprajchExprParser.FuncExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#OrExpr.
    def enterOrExpr(self, ctx:SzprajchExprParser.OrExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#OrExpr.
    def exitOrExpr(self, ctx:SzprajchExprParser.OrExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#IndexExpr.
    def enterIndexExpr(self, ctx:SzprajchExprParser.IndexExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#IndexExpr.
    def exitIndexExpr(self, ctx:SzprajchExprParser.IndexExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#NegateExpr.
    def enterNegateExpr(self, ctx:SzprajchExprParser.NegateExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#NegateExpr.
    def exitNegateExpr(self, ctx:SzprajchExprParser.NegateExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:SzprajchExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:SzprajchExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#NumberExpr.
    def enterNumberExpr(self, ctx:SzprajchExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#NumberExpr.
    def exitNumberExpr(self, ctx:SzprajchExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#NotExpr.
    def enterNotExpr(self, ctx:SzprajchExprParser.NotExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#NotExpr.
    def exitNotExpr(self, ctx:SzprajchExprParser.NotExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#ListExpr.
    def enterListExpr(self, ctx:SzprajchExprParser.ListExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#ListExpr.
    def exitListExpr(self, ctx:SzprajchExprParser.ListExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#ParenExpr.
    def enterParenExpr(self, ctx:SzprajchExprParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#ParenExpr.
    def exitParenExpr(self, ctx:SzprajchExprParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:SzprajchExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:SzprajchExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:SzprajchExprParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:SzprajchExprParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#func.
    def enterFunc(self, ctx:SzprajchExprParser.FuncContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#func.
    def exitFunc(self, ctx:SzprajchExprParser.FuncContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#list.
    def enterList(self, ctx:SzprajchExprParser.ListContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#list.
    def exitList(self, ctx:SzprajchExprParser.ListContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#string.
    def enterString(self, ctx:SzprajchExprParser.StringContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#string.
    def exitString(self, ctx:SzprajchExprParser.StringContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#number.
    def enterNumber(self, ctx:SzprajchExprParser.NumberContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#number.
    def exitNumber(self, ctx:SzprajchExprParser.NumberContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#functioncall.
    def enterFunctioncall(self, ctx:SzprajchExprParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#functioncall.
    def exitFunctioncall(self, ctx:SzprajchExprParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#arglist.
    def enterArglist(self, ctx:SzprajchExprParser.ArglistContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#arglist.
    def exitArglist(self, ctx:SzprajchExprParser.ArglistContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#lenfunc.
    def enterLenfunc(self, ctx:SzprajchExprParser.LenfuncContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#lenfunc.
    def exitLenfunc(self, ctx:SzprajchExprParser.LenfuncContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#valfunc.
    def enterValfunc(self, ctx:SzprajchExprParser.ValfuncContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#valfunc.
    def exitValfunc(self, ctx:SzprajchExprParser.ValfuncContext):
        pass


    # Enter a parse tree produced by SzprajchExprParser#isnanfunc.
    def enterIsnanfunc(self, ctx:SzprajchExprParser.IsnanfuncContext):
        pass

    # Exit a parse tree produced by SzprajchExprParser#isnanfunc.
    def exitIsnanfunc(self, ctx:SzprajchExprParser.IsnanfuncContext):
        pass



del SzprajchExprParser