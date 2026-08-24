#1. leia os dados;
#2. armazene-os no dicionário;
#3. exiba os dados;
#4. altere o preço;
#5. adicione uma informação chamada `categoria`.

livro = {
    "Nome": "O Senhor dos aneis",
    "Autor": "J.R.R. Tolkien",
    "Ano": "1954",
    "Preço": "R$ 99,99"
}

print(livro["Nome"])
print(livro["Autor"])
print(livro["Ano"])
print(livro["Preço"])
print()

livro["Preço"] = "120.00"
livro["Categoria"] = "Fantasia"

print(livro["Nome"])
print(livro["Autor"])
print(livro["Ano"])
print(livro["Preço"])
print(livro["Categoria"])