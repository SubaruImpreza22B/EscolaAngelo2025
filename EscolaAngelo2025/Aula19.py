nomes = "Ana, Maria, Pedro, João, Carlos, José, Antônio, Francisco, Luiz, Paulo".split(", ")

print(f"A primeira ocorrencia de Carlos é no índice:{nomes.index('Carlos')}")

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)

copiaNomes = nomes.copy()
print(f"Nomes copiados: {copiaNomes}")