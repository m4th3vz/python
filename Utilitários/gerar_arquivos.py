import os

funcoes = [
    'abs', 'aiter', 'all', 'any', 'anext', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
    'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir',
    'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'getattr',
    'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
    'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
    'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set',
    'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
    'zip', '__import__'
]

# Cria a pasta se não existir
os.makedirs("funcoes_builtin", exist_ok=True)

for funcao in funcoes:
    nome_funcao = funcao.replace('__', '') if funcao == '__import__' else funcao
    nome_arquivo = f"funcoes_builtin/funcao_{nome_funcao}.py"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(f"def funcao_{nome_funcao}():\n")
        f.write(f"    \"\"\"\n    Explicação e exemplo de uso da função {funcao}.\n    \"\"\"\n")
        f.write(f"    pass\n")

print("Todos os arquivos foram criados com sucesso!")
