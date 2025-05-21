# Generated from Szprajch/SzprajchExpr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SzprajchExprParser import SzprajchExprParser
else:
    from SzprajchExprParser import SzprajchExprParser

# This class defines a complete generic visitor for a parse tree produced by SzprajchExprParser.

class SzprajchExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SzprajchExprParser#program.
    def visitProgram(self, ctx:SzprajchExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#statement.
    def visitStatement(self, ctx:SzprajchExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#AndExpr.
    def visitAndExpr(self, ctx:SzprajchExprParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#StringExpr.
    def visitStringExpr(self, ctx:SzprajchExprParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#IdExpr.
    def visitIdExpr(self, ctx:SzprajchExprParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#RelExpr.
    def visitRelExpr(self, ctx:SzprajchExprParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#ExpExpr.
    def visitExpExpr(self, ctx:SzprajchExprParser.ExpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#FuncExpr.
    def visitFuncExpr(self, ctx:SzprajchExprParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#OrExpr.
    def visitOrExpr(self, ctx:SzprajchExprParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#IndexExpr.
    def visitIndexExpr(self, ctx:SzprajchExprParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#NegateExpr.
    def visitNegateExpr(self, ctx:SzprajchExprParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:SzprajchExprParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#NumberExpr.
    def visitNumberExpr(self, ctx:SzprajchExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#NotExpr.
    def visitNotExpr(self, ctx:SzprajchExprParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#ListExpr.
    def visitListExpr(self, ctx:SzprajchExprParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#ParenExpr.
    def visitParenExpr(self, ctx:SzprajchExprParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:SzprajchExprParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:SzprajchExprParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#func.
    def visitFunc(self, ctx:SzprajchExprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#list.
    def visitList(self, ctx:SzprajchExprParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#string.
    def visitString(self, ctx:SzprajchExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#number.
    def visitNumber(self, ctx:SzprajchExprParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#functioncall.
    def visitFunctioncall(self, ctx:SzprajchExprParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#arglist.
    def visitArglist(self, ctx:SzprajchExprParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#lenfunc.
    def visitLenfunc(self, ctx:SzprajchExprParser.LenfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#valfunc.
    def visitValfunc(self, ctx:SzprajchExprParser.ValfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SzprajchExprParser#isnanfunc.
    def visitIsnanfunc(self, ctx:SzprajchExprParser.IsnanfuncContext):
        return self.visitChildren(ctx)



del SzprajchExprParser