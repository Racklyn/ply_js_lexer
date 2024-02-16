import ply.lex as lex

reserved = {
    'let': 'LET',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'return': 'RETURN',

}

tokens = [
    'INT',
    'FLOAT',
    'ID',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LESS_THAN',
    'INCREMENT',
    'ASSIGN',
    'EQUALS',
    'STRING',
] + list(reserved.values())

literals = '.,;(){}[]'

t_INCREMENT = r'\+\+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_LESS_THAN = r'\<'
t_EQUALS = r'\=='
t_ASSIGN = r'\='

t_ignore = r' '


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_newline(t):
    r'\n+'

def t_error(t):
    print('Caracteres inesperados! ')
    t.lexer.skip(1)

lexer = lex.lex()



program = """
function calc(op, a, b){
    if(op == "soma"){
        return a+b;
    }else if(op == "sub"){
        return a-b;
    }else if(op == "multi"){
        return a*b;
    }else if(op == "div"){
        return a/b;
    }
}

let operacoes = ["soma", "sub", "multi", "div"];

for(var i = 0; i < operacoes.length; i++ ){
    console.log(calc(operacoes[i], 10, 2))
}"""


lexer.input(program)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
