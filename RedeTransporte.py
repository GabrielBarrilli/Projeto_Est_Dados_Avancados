import json
import os

import matplotlib.pyplot as plt
import networkx as nx


class RedeTransporte:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.carregar_dados()

    def adicionar_parada(self, parada):
        self.grafo.add_node(parada.nome)
        print(f"Parada '{parada.nome}' adicionada com sucesso.")

    def adicionar_conexao(self, conexao):
        if not self.grafo.has_edge(conexao.origem, conexao.destino):
            self.grafo.add_edge(conexao.origem, conexao.destino, weight=conexao.tempo)
            print(
                f"Conexão de '{conexao.origem}' para '{conexao.destino}' com tempo {conexao.tempo} adicionada com sucesso.")
        else:
            print(f"Já existe uma conexão de '{conexao.origem}' para '{conexao.destino}'.")

    def calcular_rota_mais_curta(self, origem, destino):
        try:
            caminho = nx.shortest_path(self.grafo, origem, destino, weight='weight')
            distancia = nx.shortest_path_length(self.grafo, origem, destino, weight='weight')
            print(f"Rota mais curta de '{origem}' para '{destino}': {caminho} com tempo total {distancia}")
        except nx.NetworkXNoPath:
            print(f"Não há caminho entre '{origem}' e '{destino}'.")

    def exibir_rede(self):
        pos = nx.spring_layout(self.grafo)
        labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw(self.grafo, pos, with_labels=True, node_size=700, node_color="lightblue", arrows=True)
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()

    def salvar_dados(self):
        dados = {
            "paradas": list(self.grafo.nodes),
            "conexoes": [(u, v, self.grafo[u][v]['weight']) for u, v in self.grafo.edges]
        }
        with open('dados_rede.json', 'w') as arquivo:
            json.dump(dados, arquivo)
        print("Dados salvos no arquivo 'dados_rede.json'.")

    def carregar_dados(self):
        if os.path.exists('dados_rede.json'):
            with open('dados_rede.json', 'r') as arquivo:
                dados = json.load(arquivo)
                self.grafo.add_nodes_from(dados["paradas"])
                self.grafo.add_weighted_edges_from(dados["conexoes"])
            print("Dados carregados do arquivo 'dados_rede.json'.")
