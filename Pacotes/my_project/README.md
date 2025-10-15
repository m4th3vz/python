# my_package

## Descrição  

O pacote **my_package** foi criado para:  
- Demonstrar uma estrutura simples e moderna de pacotes Python  
- Servir como modelo inicial para criação de pacotes reutilizáveis  

---

## Instalação  

Você pode instalar o pacote normalmente usando o [pip](https://pip.pypa.io/en/stable/):  

```bash
pip install my_package
```

## 🧩 Modo de Desenvolvimento

Se você estiver desenvolvendo ou testando este pacote, é recomendável instalá-lo em modo editável.  
Dessa forma, qualquer alteração no código será refletida imediatamente, sem precisar reinstalar o pacote:

```bash
pip install -e .
```

Execute este comando dentro da pasta raiz do projeto (onde está localizado o arquivo `pyproject.toml`).

## Uso

Exemplo de importação e utilização do pacote:

```python
from my_package.core import calculator, helper
from my_package.utils import logger, file_manager

print(calculator.add(3, 5))
print(helper.greet("Matheus"))
logger.log("Logger funcionando corretamente")
print(file_manager.list_files('.'))
```

## Estrutura do Projeto

```
my_project/
├── my_package/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   └── helper.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── file_manager.py
├── scripts/
│   ├── script_test.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Funcionalidades

### Core
- **calculator**: Funções matemáticas básicas
- **helper**: Funções auxiliares úteis

### Utils
- **logger**: Sistema de logging
- **file_manager**: Gerenciamento de arquivos

## Requisitos

- Python 3.7 ou superior

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.