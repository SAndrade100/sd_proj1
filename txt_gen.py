import random
import os

os.makedirs("data", exist_ok=True)

palavras = ["casa", "carro", "livro", "janela", "sol", "lua", "teclado", "monitor", "mouse", "fone"]
target_size = 1024 * 1024 * 1024  # 1 GB
arquivo = os.path.join("data", "arquivo.txt")


with open(arquivo, "w", encoding="utf-8") as f:
    tamanho_atual = 0
    while tamanho_atual < target_size:
        linha = " ".join(random.choices(palavras, k=10)) + "\n"
        f.write(linha)
        tamanho_atual += len(linha.encode("utf-8"))
