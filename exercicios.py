#Crie uma estrutura para armazenar informações de um livro
#incluindo titulo, autor e ano de publicacao. Imprima cada informacao

livro = {
    "titulo": "livro01",
    "autor": "autor1",
    "ano": 2009
}

lista_de_elementos = livro.items()
for elemento in lista_de_elementos:
    print(elemento)

lista_de_livros = []
lista_de_livros.append(livro)
print(lista_de_livros)