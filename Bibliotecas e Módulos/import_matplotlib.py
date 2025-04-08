# Usado para criação de gráficos estáticos, interativos e visualizações de dados em geral.
import matplotlib.pyplot as plt

# Criando um gráfico de linha simples
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Exemplo de Gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
