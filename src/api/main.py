from gerador_casos_teste.gerar_casos import gerar_casos

if __name__ == "__main__":
    cenarios = ["Login", "Cadastro", "Recuperação de Senha"]
    for cenario in cenarios:
        casos = gerar_casos(cenario)
        print(f"\nCasos para {cenario}:")
        for caso in casos:
            print(f"- {caso}")
