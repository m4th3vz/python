# __bool__
# Define valor booleano

class Item:
    def __init__(self,quantidade):
        self.quantidade=quantidade
    def __bool__(self):
        return self.quantidade>0

i=Item(3)
j=Item(0)
print(bool(i),bool(j))
