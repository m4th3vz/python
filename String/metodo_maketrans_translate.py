# str.maketrans() cria uma tabela de tradução de caracteres.
# translate() aplica essa tabela à string, substituindo os caracteres.

# Substituindo letras
tabela = str.maketrans("aeiou", "12345")
print("matheus".translate(tabela))               # "m1th23s"

# Removendo caracteres (atribuindo None)
tabela2 = str.maketrans("", "", "aeiou")
print("matheus".translate(tabela2))              # "mths"

# Substituição com dicionário
tabela3 = str.maketrans({"a": "@", "e": "3"})
print("ameixa".translate(tabela3))               # "@m3ix@"

# Útil para censura, encriptação simples, ou normalização de dados
