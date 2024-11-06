from RedeTransporte import RedeTransporte
from Parada import Parada
from Conexao import Conexao


class SistemaTransporte:
    def __init__(self):
        self.rede = RedeTransporte()

    def limpar_console(self):
        print("\n" * 50)

    def menu(self):
        while True:
            self.limpar_console()
            print("\n--- Sistema de Transporte Público Inteligente ---")
            print("1. Adicionar Parada")
            print("2. Adicionar Conexão")
            print("3. Calcular Rota Mais Curta")
            print("4. Exibir Rede de Transporte")
            print("5. Salvar Dados")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome da parada: ")
                parada = Parada(nome)
                self.rede.adicionar_parada(parada)
            elif opcao == '2':
                origem = input("Parada de origem: ")
                destino = input("Parada de destino: ")
                tempo = float(input("Tempo de viagem: "))
                conexao = Conexao(origem, destino, tempo)
                self.rede.adicionar_conexao(conexao)
            elif opcao == '3':
                origem = input("Parada de origem: ")
                destino = input("Parada de destino: ")
                self.rede.calcular_rota_mais_curta(origem, destino)
            elif opcao == '4':
                print("Exibindo Rede de Transporte...")
                self.rede.exibir_rede()
            elif opcao == '5':
                self.rede.salvar_dados()
            elif opcao == '6':
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida.")

            input("\nPressione qualquer tecla para continuar...")
            self.limpar_console()
