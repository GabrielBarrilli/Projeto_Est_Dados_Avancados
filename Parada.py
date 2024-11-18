class Parada:
    def __init__(self, nome, latitude, longitude):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        """Converte a parada para um formato de dicionário, adequado para JSON."""
        return {
            "nome": self.nome,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
