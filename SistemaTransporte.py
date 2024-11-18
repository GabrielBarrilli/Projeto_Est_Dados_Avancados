from datetime import datetime

import googlemaps

from Grafo import Grafo


class SistemaTransporte:
    def __init__(self, api_key=None):
        self.grafo = Grafo()
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=self.api_key)

    def adicionar_parada(self, nome, latitude, longitude):
        self.grafo.adicionar_parada(nome, latitude, longitude)

    def adicionar_conexao(self, origem, destino):
        origem_coords = self.grafo.grafo.nodes[origem]
        destino_coords = self.grafo.grafo.nodes[destino]

        distancia = self.calcular_distancia_googlemaps(origem_coords['latitude'], origem_coords['longitude'],
                                                       destino_coords['latitude'], destino_coords['longitude'])

        self.grafo.adicionar_conexao(origem, destino, distancia)

    def calcular_distancia_googlemaps(self, lat1, lon1, lat2, lon2):
        origem = (lat1, lon1)
        destino = (lat2, lon2)
        resultado = self.gmaps.distance_matrix(origem, destino, mode="driving", departure_time=datetime.now())

        if resultado['status'] == 'OK':
            distancia_metros = resultado['rows'][0]['elements'][0]['distance']['value']
            distancia_km = distancia_metros / 1000  # Converte de metros para quilômetros
            return distancia_km
        else:
            print(f"Erro ao calcular a distância entre {origem} e {destino}.")
            return 0  # Retorna 0 caso não seja possível calcular a distância

    def exibir_conexoes(self):
        self.grafo.exibir_conexoes()

    def salvar_dados(self, arquivo):
        self.grafo.salvar_dados(arquivo)

    def carregar_dados(self, arquivo):
        self.grafo.carregar_dados(arquivo)

    def gerar_grafo(self):
        self.grafo.gerar_grafo()
