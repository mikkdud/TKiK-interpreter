from antlr4 import *
from gen.Szprajch.SzprajchLexer import SzprajchLexer
from gen.Szprajch.SzprajchParser import SzprajchParser
from gen.Szprajch.SzprajchVisitor import SzprajchVisitor


from graphviz import Digraph

def print_tree(node, parser, graph, parent_id=None, node_id=0):
    label = parser.ruleNames[node.getRuleIndex()] if hasattr(node, "getRuleIndex") else str(node)
    cur_id = str(node_id)
    graph.node(cur_id, label)

    if parent_id is not None:
        graph.edge(parent_id, cur_id)

    if hasattr(node, 'children'):
        child_id = node_id + 1
        for child in node.children:
            child_id = print_tree(child, parser, graph, cur_id, child_id)
        return child_id
    else:
        return node_id + 1

def visualize_tree(tree, parser):
    dot = Digraph(comment='AST')
    print_tree(tree, parser, dot)
    dot.render('ast_output', view=True, format='png')  # ast_output.png


input_text = FileStream("main.sz")
lexer = SzprajchLexer(input_text)
stream = CommonTokenStream(lexer)
parser = SzprajchParser(stream)

tree = parser.program()

print(tree.toStringTree(recog=parser))
visualize_tree(tree, parser)