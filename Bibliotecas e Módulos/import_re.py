# Trabalha com expressões regulares, permitindo realizar buscas, correspondências e substituições em strings.
import re

# Texto de exemplo
texto = "Meu e-mail é matheus1992@gmail.com e o de suporte é suporte@empresa.com.br"

# Expressão regular para encontrar e-mails
padrao_email = r"\b[\w.-]+@[\w.-]+\.\w+\b"

# Encontrando todos os e-mails no texto
emails = re.findall(padrao_email, texto)

print("E-mails encontrados:", emails)

# Exemplo de uso de re.findall
resultados = re.findall("[A-Za-z]y", "Python ou jython")
print(resultados)

# Verifica se o texto começa com "Meu"
print(re.match(r"Meu", texto))  # retorna um objeto ou None

# Substituir e-mails por "[email]"
texto_anonimo = re.sub(padrao_email, "[email]", texto)
print("Texto anonimizado:", texto_anonimo)
