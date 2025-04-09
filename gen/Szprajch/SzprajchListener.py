# Generated from Szprajch/Szprajch.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SzprajchParser import SzprajchParser
else:
    from SzprajchParser import SzprajchParser

# This class defines a complete listener for a parse tree produced by SzprajchParser.
class SzprajchListener(ParseTreeListener):

    # Enter a parse tree produced by SzprajchParser#program.
    def enterProgram(self, ctx:SzprajchParser.ProgramContext):
        pass

    # Exit a parse tree produced by SzprajchParser#program.
    def exitProgram(self, ctx:SzprajchParser.ProgramContext):
        pass


    # Enter a parse tree produced by SzprajchParser#statement.
    def enterStatement(self, ctx:SzprajchParser.StatementContext):
        pass

    # Exit a parse tree produced by SzprajchParser#statement.
    def exitStatement(self, ctx:SzprajchParser.StatementContext):
        pass


    # Enter a parse tree produced by SzprajchParser#block.
    def enterBlock(self, ctx:SzprajchParser.BlockContext):
        pass

    # Exit a parse tree produced by SzprajchParser#block.
    def exitBlock(self, ctx:SzprajchParser.BlockContext):
        pass


    # Enter a parse tree produced by SzprajchParser#assignmentstmt.
    def enterAssignmentstmt(self, ctx:SzprajchParser.AssignmentstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#assignmentstmt.
    def exitAssignmentstmt(self, ctx:SzprajchParser.AssignmentstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#varname.
    def enterVarname(self, ctx:SzprajchParser.VarnameContext):
        pass

    # Exit a parse tree produced by SzprajchParser#varname.
    def exitVarname(self, ctx:SzprajchParser.VarnameContext):
        pass


    # Enter a parse tree produced by SzprajchParser#printstmt.
    def enterPrintstmt(self, ctx:SzprajchParser.PrintstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#printstmt.
    def exitPrintstmt(self, ctx:SzprajchParser.PrintstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#inputstmt.
    def enterInputstmt(self, ctx:SzprajchParser.InputstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#inputstmt.
    def exitInputstmt(self, ctx:SzprajchParser.InputstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#ifstmt.
    def enterIfstmt(self, ctx:SzprajchParser.IfstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#ifstmt.
    def exitIfstmt(self, ctx:SzprajchParser.IfstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#elifstmt.
    def enterElifstmt(self, ctx:SzprajchParser.ElifstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#elifstmt.
    def exitElifstmt(self, ctx:SzprajchParser.ElifstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#elsestmt.
    def enterElsestmt(self, ctx:SzprajchParser.ElsestmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#elsestmt.
    def exitElsestmt(self, ctx:SzprajchParser.ElsestmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#forstmt.
    def enterForstmt(self, ctx:SzprajchParser.ForstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#forstmt.
    def exitForstmt(self, ctx:SzprajchParser.ForstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#whilestmt.
    def enterWhilestmt(self, ctx:SzprajchParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#whilestmt.
    def exitWhilestmt(self, ctx:SzprajchParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#repeatstmt.
    def enterRepeatstmt(self, ctx:SzprajchParser.RepeatstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#repeatstmt.
    def exitRepeatstmt(self, ctx:SzprajchParser.RepeatstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#continuestmt.
    def enterContinuestmt(self, ctx:SzprajchParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#continuestmt.
    def exitContinuestmt(self, ctx:SzprajchParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#breakstmt.
    def enterBreakstmt(self, ctx:SzprajchParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by SzprajchParser#breakstmt.
    def exitBreakstmt(self, ctx:SzprajchParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by SzprajchParser#functiondef.
    def enterFunctiondef(self, ctx:SzprajchParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by SzprajchParser#functiondef.
    def exitFunctiondef(self, ctx:SzprajchParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by SzprajchParser#paramlist.
    def enterParamlist(self, ctx:SzprajchParser.ParamlistContext):
        pass

    # Exit a parse tree produced by SzprajchParser#paramlist.
    def exitParamlist(self, ctx:SzprajchParser.ParamlistContext):
        pass


    # Enter a parse tree produced by SzprajchParser#returnstmnt.
    def enterReturnstmnt(self, ctx:SzprajchParser.ReturnstmntContext):
        pass

    # Exit a parse tree produced by SzprajchParser#returnstmnt.
    def exitReturnstmnt(self, ctx:SzprajchParser.ReturnstmntContext):
        pass


    # Enter a parse tree produced by SzprajchParser#AndExpr.
    def enterAndExpr(self, ctx:SzprajchParser.AndExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#AndExpr.
    def exitAndExpr(self, ctx:SzprajchParser.AndExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#StringExpr.
    def enterStringExpr(self, ctx:SzprajchParser.StringExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#StringExpr.
    def exitStringExpr(self, ctx:SzprajchParser.StringExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#IdExpr.
    def enterIdExpr(self, ctx:SzprajchParser.IdExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#IdExpr.
    def exitIdExpr(self, ctx:SzprajchParser.IdExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#RelExpr.
    def enterRelExpr(self, ctx:SzprajchParser.RelExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#RelExpr.
    def exitRelExpr(self, ctx:SzprajchParser.RelExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#ExpExpr.
    def enterExpExpr(self, ctx:SzprajchParser.ExpExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#ExpExpr.
    def exitExpExpr(self, ctx:SzprajchParser.ExpExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#FuncExpr.
    def enterFuncExpr(self, ctx:SzprajchParser.FuncExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#FuncExpr.
    def exitFuncExpr(self, ctx:SzprajchParser.FuncExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#OrExpr.
    def enterOrExpr(self, ctx:SzprajchParser.OrExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#OrExpr.
    def exitOrExpr(self, ctx:SzprajchParser.OrExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#IndexExpr.
    def enterIndexExpr(self, ctx:SzprajchParser.IndexExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#IndexExpr.
    def exitIndexExpr(self, ctx:SzprajchParser.IndexExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:SzprajchParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:SzprajchParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#NumberExpr.
    def enterNumberExpr(self, ctx:SzprajchParser.NumberExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#NumberExpr.
    def exitNumberExpr(self, ctx:SzprajchParser.NumberExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#NotExpr.
    def enterNotExpr(self, ctx:SzprajchParser.NotExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#NotExpr.
    def exitNotExpr(self, ctx:SzprajchParser.NotExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#ListExpr.
    def enterListExpr(self, ctx:SzprajchParser.ListExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#ListExpr.
    def exitListExpr(self, ctx:SzprajchParser.ListExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#ParenExpr.
    def enterParenExpr(self, ctx:SzprajchParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#ParenExpr.
    def exitParenExpr(self, ctx:SzprajchParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:SzprajchParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SzprajchParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:SzprajchParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SzprajchParser#func.
    def enterFunc(self, ctx:SzprajchParser.FuncContext):
        pass

    # Exit a parse tree produced by SzprajchParser#func.
    def exitFunc(self, ctx:SzprajchParser.FuncContext):
        pass


    # Enter a parse tree produced by SzprajchParser#list.
    def enterList(self, ctx:SzprajchParser.ListContext):
        pass

    # Exit a parse tree produced by SzprajchParser#list.
    def exitList(self, ctx:SzprajchParser.ListContext):
        pass


    # Enter a parse tree produced by SzprajchParser#string.
    def enterString(self, ctx:SzprajchParser.StringContext):
        pass

    # Exit a parse tree produced by SzprajchParser#string.
    def exitString(self, ctx:SzprajchParser.StringContext):
        pass


    # Enter a parse tree produced by SzprajchParser#number.
    def enterNumber(self, ctx:SzprajchParser.NumberContext):
        pass

    # Exit a parse tree produced by SzprajchParser#number.
    def exitNumber(self, ctx:SzprajchParser.NumberContext):
        pass


    # Enter a parse tree produced by SzprajchParser#id.
    def enterId(self, ctx:SzprajchParser.IdContext):
        pass

    # Exit a parse tree produced by SzprajchParser#id.
    def exitId(self, ctx:SzprajchParser.IdContext):
        pass


    # Enter a parse tree produced by SzprajchParser#functioncall.
    def enterFunctioncall(self, ctx:SzprajchParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by SzprajchParser#functioncall.
    def exitFunctioncall(self, ctx:SzprajchParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by SzprajchParser#arglist.
    def enterArglist(self, ctx:SzprajchParser.ArglistContext):
        pass

    # Exit a parse tree produced by SzprajchParser#arglist.
    def exitArglist(self, ctx:SzprajchParser.ArglistContext):
        pass


    # Enter a parse tree produced by SzprajchParser#lenfunc.
    def enterLenfunc(self, ctx:SzprajchParser.LenfuncContext):
        pass

    # Exit a parse tree produced by SzprajchParser#lenfunc.
    def exitLenfunc(self, ctx:SzprajchParser.LenfuncContext):
        pass


    # Enter a parse tree produced by SzprajchParser#valfunc.
    def enterValfunc(self, ctx:SzprajchParser.ValfuncContext):
        pass

    # Exit a parse tree produced by SzprajchParser#valfunc.
    def exitValfunc(self, ctx:SzprajchParser.ValfuncContext):
        pass


    # Enter a parse tree produced by SzprajchParser#isnanfunc.
    def enterIsnanfunc(self, ctx:SzprajchParser.IsnanfuncContext):
        pass

    # Exit a parse tree produced by SzprajchParser#isnanfunc.
    def exitIsnanfunc(self, ctx:SzprajchParser.IsnanfuncContext):
        pass



del SzprajchParser