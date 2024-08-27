def excluir_carro(carros):
    carro_para_excluir = input("Qual carro deseja excluir? ")

    if carro_para_excluir in carros:
        carros.remove(carro_para_excluir)
        print(f"{carro_para_excluir} foi removido do estoque.")
    else:
        print(f"{carro_para_excluir} não está no estoque.")

    print("Estoque atualizado:", carros)
