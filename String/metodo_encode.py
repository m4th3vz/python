# Codifica a string em bytes, usando a codificação especificada (padrão: 'utf-8').
# É útil para gravar arquivos, enviar dados pela internet, etc.

print("matheus".encode())                   # b'matheus' (UTF-8 padrão)
print("áéíóú".encode("utf-8"))              # b'\xc3\xa1\xc3\xa9\xc3\xad\xc3\xb3\xc3\xba'
print("ç".encode("latin1"))                 # b'\xe7'
print("漢字".encode("utf-8"))               # b'\xe6\xbc\xa2\xe5\xad\x97'
# print("漢字".encode("ascii"))             # UnicodeEncodeError

texto = "Olá, mundo!"
dados = texto.encode("utf-8")
print(dados)                                # b'Ol\xc3\xa1, mundo!'
