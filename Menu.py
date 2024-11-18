def menu(sistema):
    while True:
        print("--- Sistema de Transporte Público Inteligente ---")
        print("1. Adicionar Parada")
        print("2. Adicionar Conexão")
        print("3. Exibir Rede de Transporte")
        print("4. Gerar Visualização do Grafo")
        print("5. Salvar Dados")
        print("6. Carregar Dados")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da parada: ")
            latitude = float(input("Latitude: "))
            longitude = float(input("Longitude: "))
            sistema.adicionar_parada(nome, latitude, longitude)

        elif escolha == "2":
            origem = input("Origem: ")
            destino = input("Destino: ")
            sistema.adicionar_conexao(origem, destino)

        elif escolha == "3":
            sistema.exibir_conexoes()

        elif escolha == "4":
            sistema.gerar_grafo()

        elif escolha == "5":
            arquivo = input("Nome do arquivo para salvar os dados: ")
            sistema.salvar_dados(arquivo)

        elif escolha == "6":
            arquivo = input("Nome do arquivo para carregar os dados: ")
            sistema.carregar_dados(arquivo)

        elif escolha == "7":
            print("Saindo do sistema.")
            break
