# Generated from Szprajch/Szprajch.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SzprajchParser import SzprajchParser
else:
    from SzprajchParser import SzprajchParser

# This class defines a complete generic visitor for a parse tree produced by SzprajchParser.

class SzprajchVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SzprajchParser#program.
    def visitProgram(self, ctx:SzprajchParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#statement.
    def visitStatement(self, ctx:SzprajchParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#block.
    def visitBlock(self, ctx:SzprajchParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#assignmentstmt.
    def visitAssignmentstmt(self, ctx:SzprajchParser.AssignmentstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#varname.
    def visitVarname(self, ctx:SzprajchParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#printstmt.
    def visitPrintstmt(self, ctx:SzprajchParser.PrintstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#inputstmt.
    def visitInputstmt(self, ctx:SzprajchParser.InputstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#ifstmt.
    def visitIfstmt(self, ctx:SzprajchParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#elifstmt.
    def visitElifstmt(self, ctx:SzprajchParser.ElifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#elsestmt.
    def visitElsestmt(self, ctx:SzprajchParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#forstmt.
    def visitForstmt(self, ctx:SzprajchParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#whilestmt.
    def visitWhilestmt(self, ctx:SzprajchParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#repeatstmt.
    def visitRepeatstmt(self, ctx:SzprajchParser.RepeatstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#continuestmt.
    def visitContinuestmt(self, ctx:SzprajchParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#breakstmt.
    def visitBreakstmt(self, ctx:SzprajchParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#functiondef.
    def visitFunctiondef(self, ctx:SzprajchParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#paramlist.
    def visitParamlist(self, ctx:SzprajchParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#returnstmnt.
    def visitReturnstmnt(self, ctx:SzprajchParser.ReturnstmntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#AndExpr.
    def visitAndExpr(self, ctx:SzprajchParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#StringExpr.
    def visitStringExpr(self, ctx:SzprajchParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#IdExpr.
    def visitIdExpr(self, ctx:SzprajchParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#RelExpr.
    def visitRelExpr(self, ctx:SzprajchParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#ExpExpr.
    def visitExpExpr(self, ctx:SzprajchParser.ExpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#FuncExpr.
    def visitFuncExpr(self, ctx:SzprajchParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#OrExpr.
    def visitOrExpr(self, ctx:SzprajchParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#IndexExpr.
    def visitIndexExpr(self, ctx:SzprajchParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:SzprajchParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#NumberExpr.
    def visitNumberExpr(self, ctx:SzprajchParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#NotExpr.
    def visitNotExpr(self, ctx:SzprajchParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#ListExpr.
    def visitListExpr(self, ctx:SzprajchParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#ParenExpr.
    def visitParenExpr(self, ctx:SzprajchParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:SzprajchParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#func.
    def visitFunc(self, ctx:SzprajchParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#list.
    def visitList(self, ctx:SzprajchParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#string.
    def visitString(self, ctx:SzprajchParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#number.
    def visitNumber(self, ctx:SzprajchParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#id.
    def visitId(self, ctx:SzprajchParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#functioncall.
    def visitFunctioncall(self, ctx:SzprajchParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#arglist.
    def visitArglist(self, ctx:SzprajchParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#lenfunc.
    def visitLenfunc(self, ctx:SzprajchParser.LenfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#valfunc.
    def visitValfunc(self, ctx:SzprajchParser.ValfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchParser#isnanfunc.
    def visitIsnanfunc(self, ctx:SzprajchParser.IsnanfuncContext):
        return self.visitChildren(ctx)



del SzprajchParser