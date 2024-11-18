import json

import networkx as nx


class Grafo:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def adicionar_parada(self, nome, latitude, longitude):
        self.grafo.add_node(nome, latitude=latitude, longitude=longitude)

    def adicionar_conexao(self, origem, destino, distancia):
        self.grafo.add_edge(origem, destino, distancia=distancia)

    def exibir_conexoes(self):
        if len(self.grafo.edges) == 0:
            print("Nenhuma conexão foi adicionada ainda.")
        for origem, destino, dados in self.grafo.edges(data=True):
            print(f"{origem} -> {destino} | Distância: {dados['distancia']} km")

    def salvar_dados(self, arquivo):
        dados_grafo = {
            'nodes': [(n, self.grafo.nodes[n]) for n in self.grafo.nodes],
            'edges': [(u, v, d) for u, v, d in self.grafo.edges(data=True)],
        }
        with open(arquivo, 'w') as f:
            json.dump(dados_grafo, f)

    def carregar_dados(self, arquivo):
        with open(arquivo, 'r') as f:
            dados_grafo = json.load(f)

        for node, data in dados_grafo['nodes']:
            self.grafo.add_node(node, **data)

        for origem, destino, data in dados_grafo['edges']:
            self.grafo.add_edge(origem, destino, **data)

    def gerar_grafo(self):
        if len(self.grafo.nodes) == 0:
            print("O grafo está vazio. Adicione paradas e conexões antes de gerar a visualização.")
        else:
            import matplotlib.pyplot as plt
            pos = nx.spring_layout(self.grafo, seed=42)
            plt.figure(figsize=(12, 8))
            nx.draw(self.grafo, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12,
                    font_weight='bold', edge_color='gray', width=2)
            edge_labels = nx.get_edge_attributes(self.grafo, 'distancia')
            nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=edge_labels, font_size=10)
            plt.title('Visualização do Grafo', fontsize=16)
            plt.show()
