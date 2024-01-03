
class Lista:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def concat(self, other_list):
        new_list = Lista()
        new_list.items = self.items + other_list.items
        return new_list

    def divide(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice fora dos limites")

        first_half = Lista()
        second_half = Lista()

        first_half.items = self.items[:index]
        second_half.items = self.items[index:]

        return first_half, second_half

    def copy(self):
        new_list = Lista()
        new_list.items = self.items.copy()
        return new_list

    def search(self, element):
        return element in self.items

# Exemplo de uso:
lista1 = Lista()
lista1.append(1)
lista1.append(2)
lista1.append(3)

lista2 = Lista()
lista2.append(4)
lista2.append(5)
lista2.append(6)

# Concatenação
concatenada = lista1.concat(lista2)
print("Concatenada:", concatenada.items)

# Divisão
dividida1, dividida2 = lista1.divide(2)
print("Dividida 1:", dividida1.items)
print("Dividida 2:", dividida2.items)

# Cópia
copia = lista1.copy()
print("Cópia:", copia.items)

# Pesquisa
elemento = 3
print(f"O elemento {elemento} está na lista: {lista1.search(elemento)}")
