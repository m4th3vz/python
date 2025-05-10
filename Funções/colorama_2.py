from colorama import Fore, Back, Style, init

# Inicializa o colorama
init(autoreset=True)

# Texto com todas as cores de primeiro plano (texto)
print("Texto com as cores do primeiro plano (Fore):")
for color in [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET]:
    print(color + 'Este é um texto de cor: ' + color.strip().split('.')[-1])

# Texto com todas as cores de fundo (Back)
print("\nTexto com as cores de fundo (Back):")
for color in [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.RESET]:
    print(color + 'Este é um texto com fundo de cor: ' + color.strip().split('.')[-1])

# Texto com todos os estilos (Style)
print("\nTexto com todos os estilos (Style):")
for style in [Style.BRIGHT, Style.DIM, Style.NORMAL, Style.RESET_ALL]:
    print(style + 'Este é um texto com estilo: ' + style.strip().split('.')[-1])

# Exemplo de combinação de texto e fundo
print("\nCombinando texto e fundo:")
print(Fore.YELLOW + Back.BLUE + 'Texto amarelo com fundo azul')
print(Fore.BLACK + Back.WHITE + 'Texto preto com fundo branco')

# Finalizando com uma mensagem normal
print("\nMensagem normal (sem estilo ou cor):")
print('Texto sem cores ou estilos aplicados.')
