from my_package.core import calculator, helper
from my_package.utils import logger, file_manager

# Testes simples
print("Add:", calculator.add(3, 5))
print("Multiply:", calculator.multiply(4, 5))
print(helper.greet("Matheus"))
logger.log("Teste do logger funcionando")
print("Arquivos na raiz:", file_manager.list_files("."))
