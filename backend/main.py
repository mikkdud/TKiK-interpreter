from antlr4 import *
from gen.Szprajch.SzprajchLexer import SzprajchLexer
from gen.Szprajch.SzprajchParser import SzprajchParser
from gen.Szprajch.SzprajchVisitor import SzprajchVisitor
from SzprajchExecutor import SzprajchExecutor  

from graphviz import Digraph

def print_tree(node, parser, graph, parent_id=None, node_id=0):
    if node is None or not hasattr(node, "children"):
        return node_id

    label = str(node.getText()).replace('"', r'\"')
    cur_id = node_id
    graph.node(str(cur_id), label)
    if parent_id is not None:
        graph.edge(str(parent_id), str(cur_id))

    node_id += 1
    for child in node.children:
        node_id = print_tree(child, parser, graph, cur_id, node_id)
    return node_id


def visualize_tree(tree, parser):
    dot = Digraph(comment='AST')
    print_tree(tree, parser, dot)
    dot.render('ast_output', view=False, format='png')  # ast_output.png

# === Główna logika ===

input_text = FileStream("main.sz", encoding="utf-8")
lexer = SzprajchLexer(input_text)
stream = CommonTokenStream(lexer)
parser = SzprajchParser(stream)

tree = parser.program()

# 1. Pokaż drzewo składniowe
print("Drzewo składniowe:")
print(tree.toStringTree(recog=parser))
# visualize_tree(tree, parser)

# 2. Uruchom interpreter
print("\n--- Wykonywanie programu ---")
executor = SzprajchExecutor()
executor.visit(tree)

# # 3. Wyświetl końcowy stan zmiennych
# print("\n--- Zmienne po wykonaniu ---")
# for var, val in executor.variables.items():
#     print(f"{var} = {val}")
 