from flask import Flask, request, jsonify
from flask_cors import CORS
from antlr4 import InputStream, CommonTokenStream
from gen.Szprajch.SzprajchLexer import SzprajchLexer
from gen.Szprajch.SzprajchParser import SzprajchParser
from SzprajchExecutor import SzprajchExecutor
from SzprajchErrorListener import SzprajchErrorListener

app = Flask(__name__)
CORS(app)  # Umożliwia komunikację z Reactem

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    try:
        lexer = SzprajchLexer(InputStream(code))
        lexer.removeErrorListeners()
        lexer.addErrorListener(SzprajchErrorListener())
        tokens = CommonTokenStream(lexer)
        parser = SzprajchParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(SzprajchErrorListener())
        tree = parser.program()
        executor = SzprajchExecutor()

        executor.visit(tree)
        result = '\n'.join(executor.output)
        
        return jsonify({
            'output': 'Program wykonany pomyślnie.',
            # 'variables': executor.variables,
            'result': result
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(port=5000)
