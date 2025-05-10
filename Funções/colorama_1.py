from colorama import Fore, Back, Style, init

# Inicializa o colorama
init(autoreset=True)

# Exemplo de texto colorido
print(Fore.RED + 'Texto em vermelho')
print(Fore.GREEN + 'Texto em verde')
print(Fore.YELLOW + 'Texto em amarelo')

# Exemplo de fundo colorido
print(Back.CYAN + 'Texto com fundo ciano')

# Exemplo de estilo (negrito, etc)
print(Style.BRIGHT + 'Texto em negrito')

# Combinação de cores de texto e fundo
print(Fore.WHITE + Back.BLUE + 'Texto branco com fundo azul')
