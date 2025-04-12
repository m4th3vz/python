# Guia rápido de métodos de string em Python

# ======================
# Verificação de conteúdo
# ======================
print("abc".isalpha())         # True
print("123".isdigit())         # True
print("123".isdecimal())       # True
print("Ⅻ".isnumeric())         # True
print("abc123".isalnum())      # True
print("   \t\n".isspace())     # True
print("letra".islower())       # True
print("LETRA".isupper())       # True
print("Python Code".istitle()) # True
print("variavel".isidentifier()) # True
print("texto imprimivel".isprintable()) # True
print("ascii".isascii())       # True

# ======================
# Transformação de texto
# ======================
print("Python".lower())        # "python"
print("python".upper())        # "PYTHON"
print("python".capitalize())   # "Python"
print("python code".title())   # "Python Code"
print("PyTHon".swapcase())     # "pYthON"
print("  texto  ".strip())     # "texto"
print("  texto  ".lstrip())    # "texto  "
print("  texto  ".rstrip())    # "  texto"
print("olá mundo".replace("mundo", "Matheus")) # "olá Matheus"
print("42".zfill(5))           # "00042"
print("centralizado".center(20)) # string centralizada
print("esquerda".ljust(15))    # alinhado à esquerda
print("direita".rjust(15))     # alinhado à direita

# ======================
# Busca e análise
# ======================
print("Matheus".startswith("Mat")) # True
print("Matheus".endswith("eus"))   # True
print("banana".find("na"))         # 2
print("banana".rfind("na"))        # 4
print("banana".index("na"))        # 2
print("banana".count("na"))        # 2

# ======================
# Divisão e junção
# ======================
print("um dois três".split())      # ['um', 'dois', 'três']
print("linha1\nlinha2".splitlines()) # ['linha1', 'linha2']
print("-".join(["a", "b", "c"]))   # "a-b-c"
print("python=vida".partition("="))  # ('python', '=', 'vida')
print("chave:valor".rpartition(":")) # ('chave', ':', 'valor')

# ======================
# Exemplos extras e avançados
# ======================
print("123abc".isidentifier())     # False
print("def".isidentifier())        # True (apesar de ser palavra reservada)

print("7".zfill(3))                # "007"
print("-42".zfill(5))              # "-0042"

print("um,dois,tres,quatro".split(",", 2))  # ['um', 'dois', 'tres,quatro']

nomes = ["Ana", "Bruno", "Carlos"]
print(", ".join(nomes))           # "Ana, Bruno, Carlos"

email = "matheus@gmail.com"
if email.find("@") != -1:
    print("E-mail válido!")

print("Python".rjust(10, "."))    # "....Python"

# Combinação de métodos
texto = "o pequeno príncipe"
print(texto.title().istitle())     # True

entrada = "   123   \n"
print(entrada.strip().isdigit())   # True

numero = "-123"
print(numero.lstrip("-").isdigit())  # True

# Comparação ignorando caixa e acentos
print("straße".casefold() == "STRASSE".casefold())  # True
