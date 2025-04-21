# Função ascii() em Python

"""
A função built-in ascii() retorna uma versão “escapada” de um objeto string,
onde **caracteres não ASCII** são convertidos para sequências de escape Unicode.

Útil para visualizar strings com acentos, emojis, símbolos e caracteres internacionais.
"""

# Exemplo com string com acentos
texto = "Olá, você está bem?"
print("ascii(texto) =", ascii(texto))
# Saída: 'Ol\u00e1, voc\u00ea est\u00e1 bem?'

# Exemplo com emoji
emoji = "Python 🐍 é legal!"
print("ascii(emoji) =", ascii(emoji))
# Saída: 'Python \U0001f40d \u00e9 legal!'

# Exemplo com outros símbolos Unicode
simbolos = "Δ, λ, π"
print("ascii(simbolos) =", ascii(simbolos))
# Saída: '\u0394, \u03bb, \u03c0'

"""
A função ascii() é parecida com repr(), mas com foco em compatibilidade ASCII.
É útil, por exemplo, para gerar logs legíveis ou garantir que uma string possa ser salva em arquivos ASCII.
"""

# Comparação entre print() e ascii()
nome = "João"
print("print normal:", nome)        # Saída: João
print("usando ascii():", ascii(nome))  # Saída: 'Jo\u00e3o'

"""
Resumo:
- ascii() é ótimo para inspecionar strings com caracteres especiais.
- Ideal para ambientes onde você precisa escapar tudo para ASCII puro (como logs, debug, arquivos texto simples).
"""

# Dica: se quiser salvar uma string em ASCII puro, combine ascii() com open(..., encoding='ascii', errors='ignore') ou 'backslashreplace'
