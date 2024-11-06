import networkx as nx
import matplotlib.pyplot as plt
import os
import time


class RedeTransporte:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def adicionar_parada(self, nome):
        self.grafo.add_node(nome)
        print(f"Parada '{nome}' adicionada ao sistema.")

    def adicionar_conexao(self, origem, destino, tempo):
        self.grafo.add_edge(origem, destino, weight=tempo)
        print(f"Conexão adicionada de '{origem}' para '{destino}' com tempo de viagem de {tempo} minutos.")

    def calcular_menor_tempo(self, origem, destino):
        try:
            caminho = nx.dijkstra_path(self.grafo, source=origem, target=destino, weight='weight')
            tempo_total = nx.dijkstra_path_length(self.grafo, source=origem, target=destino, weight='weight')
            print(f"Caminho mais curto de '{origem}' para '{destino}': {' -> '.join(caminho)}")
            print(f"Tempo total estimado: {tempo_total} minutos")
        except nx.NetworkXNoPath:
            print(f"Não existe um caminho entre '{origem}' e '{destino}'.")

    def exibir_rede(self):
        pos = nx.spring_layout(self.grafo)
        nx.draw(self.grafo, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10)
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=nx.get_edge_attributes(self.grafo, 'weight'))
        plt.show()


def limpar_console():
    # Simula a limpeza do console imprimindo várias linhas em branco
    print("\n" * 100)


def menu_interativo():
    rede_transporte = RedeTransporte()

    while True:
        print("\n--- Sistema de Transporte Público Inteligente ---")
        print("1. Adicionar Parada")
        print("2. Adicionar Conexão")
        print("3. Calcular Rota Mais Curta")
        print("4. Exibir Rede de Transporte")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_parada = input("Nome da Parada: ")
            rede_transporte.adicionar_parada(nome_parada)

        elif opcao == "2":
            origem = input("Parada de Origem: ")
            destino = input("Parada de Destino: ")
            tempo = int(input("Tempo de Viagem (em minutos): "))
            rede_transporte.adicionar_conexao(origem, destino, tempo)

        elif opcao == "3":
            origem = input("Parada de Origem: ")
            destino = input("Parada de Destino: ")
            rede_transporte.calcular_menor_tempo(origem, destino)

        elif opcao == "4":
            print("Exibindo Rede de Transporte...")
            rede_transporte.exibir_rede()

        elif opcao == "5":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

        # Espera 2 segundos e "limpa" o console imprimindo várias linhas em branco
        time.sleep(2)
        limpar_console()


# Inicia o Menu Interativo
if __name__ == "__main__":
    menu_interativo()
