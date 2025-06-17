# Permite executar o gerador diretamente pelo terminal, sem usar API
from gerador_casos_teste.gerar_casos import gerar_casos

# Lista dos cenários que você quer gerar
cenarios = ["Login", "Cadastro", "Recuperação de Senha"]

# Loop para cada cenário
for cenario in cenarios:
    casos = gerar_casos(cenario)  # Gera os casos
    print(f"\nCasos para {cenario}:")
    for caso in casos:
        print(f"- {caso}")
