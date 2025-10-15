# 🧮 meu_pacote

## 📘 Descrição  

O pacote **meu_pacote** foi criado para:  
- Demonstrar uma estrutura moderna e organizada de pacotes Python  
- Servir como modelo inicial para projetos modulares em português  
- Implementar operações matemáticas básicas (adição, subtração, multiplicação e divisão)  

---

## ⚙️ Instalação  

Você pode instalar o pacote normalmente usando o [pip](https://pip.pypa.io/en/stable/):  

```bash
pip install meu_pacote
```

## 🧩 Modo de Desenvolvimento

Se você estiver desenvolvendo ou testando este pacote, é recomendável instalá-lo em modo editável.  
Assim, qualquer modificação no código será refletida imediatamente, sem precisar reinstalar o pacote:

```bash
pip install -e .
```

Execute este comando dentro da pasta raiz do projeto (onde está o arquivo `pyproject.toml`).

## 🧠 Uso

Exemplo de importação e utilização do pacote:

```python
from meu_pacote.nucleo import somar, subtrair, multiplicar, dividir
from meu_pacote.utilitarios import validar_numeros, registrar_log

a, b = 10, 5

if validar_numeros(a, b):
    registrar_log("Iniciando operações matemáticas...")
    print(f"Soma: {somar(a, b)}")
    print(f"Subtração: {subtrair(a, b)}")
    print(f"Multiplicação: {multiplicar(a, b)}")
    print(f"Divisão: {dividir(a, b)}")
    registrar_log("Operações concluídas com sucesso!")
```

## 📂 Estrutura do Projeto

```
meu_projeto/
├── meu_pacote/
│   ├── __init__.py
│   ├── nucleo/
│   │   ├── __init__.py
│   │   ├── adicao.py
│   │   ├── subtracao.py
│   │   ├── multiplicacao.py
│   │   └── divisao.py
│   └── utilitarios/
│       ├── __init__.py
│       ├── validador.py
│       └── logger.py
├── scripts/
│   └── teste_script.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## 🧩 Módulos e Funcionalidades

### 🔹 nucleo

Contém as operações matemáticas básicas:

- **adicao.py** → Função `somar(a, b)`
- **subtracao.py** → Função `subtrair(a, b)`
- **multiplicacao.py** → Função `multiplicar(a, b)`
- **divisao.py** → Função `dividir(a, b)`

### 🔹 utilitarios

Funções auxiliares para o pacote:

- **validador.py** → Validação de números
- **logger.py** → Sistema simples de registro de logs com data e hora

## 📋 Requisitos

- Python 3.8 ou superior

## 🤝 Contribuição

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas ideias.

## Licença

Este projeto está licenciado sob a licença MIT.  
Você é livre para usá-lo, modificá-lo e distribuí-lo com os devidos créditos.