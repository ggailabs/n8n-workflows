import os
import re

PASTA = './workflows'  # ajuste para o caminho da sua pasta

arquivos = sorted([f for f in os.listdir(PASTA) if f.endswith('.json')])

# Regex para identificar arquivos já numerados
padrao_numerado = re.compile(r"^(\d+)_.*\.json$")

# Mapeia todos os arquivos para (num, nome)
numerados = []
nao_numerados = []

for nome in arquivos:
    m = padrao_numerado.match(nome)
    if m:
        numerados.append((int(m.group(1)), nome))
    else:
        nao_numerados.append(nome)

# Descobre qual é o maior número atual para continuar dali
ultimo_numero = max([num for num, _ in numerados], default=0)

# Renomeia os arquivos não numerados, incrementando o número
for nome in nao_numerados:
    ultimo_numero += 1
    novo_nome = f"{str(ultimo_numero).zfill(4)}_{nome}"
    origem = os.path.join(PASTA, nome)
    destino = os.path.join(PASTA, novo_nome)
    print(f"Renomeando: {nome} -> {novo_nome}")
    os.rename(origem, destino)

print("Tudo renomeado, padrão garantido 🚀")
