class Conexao:
    def __init__(self, origem, destino, tempo, distancia):
        self.origem = origem
        self.destino = destino
        self.tempo = tempo
        self.distancia = distancia

    def to_dict(self):
        return {
            "origem": self.origem.nome,
            "destino": self.destino.nome,
            "tempo": self.tempo,
            "distancia": self.distancia
        }
