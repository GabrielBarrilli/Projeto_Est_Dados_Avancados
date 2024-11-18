from Config import API_KEY
from Menu import menu
from SistemaTransporte import SistemaTransporte


def main():
    sistema = SistemaTransporte(API_KEY)

    sistema.carregar_dados("dados_transporte.json")

    menu(sistema)

    sistema.gerar_visualizacao_interativa()

    sistema.salvar_dados("dados_transporte.json")


if __name__ == "__main__":
    main()
