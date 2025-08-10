import json
from Classes.classes import Cliente, Vendedor, DiscoVinil, Artista

ARQUIVO_DADOS = "dados_iniciais/dados.txt"

clientes_cadastrados = []
vendedores_cadastrados = []
artistas_cadastrados = [
    Artista("Billie Eilish"),
    Artista("Stray Kids"),
    Artista("Michael Jackson"),
    Artista("Ariana Grande")
]
discos_disponiveis = [
    DiscoVinil("Hit Me Hard and Soft", 45.00, artistas_cadastrados[0], "Pop"),
    DiscoVinil("HOP", 50.00, artistas_cadastrados[1], "K-Pop"),
    DiscoVinil("Thriller", 35.50, artistas_cadastrados[2], "Pop"),
    DiscoVinil("Positions", 50.00, artistas_cadastrados[3], "Pop")
]

def salvar_dados():
    #Salva os dados atuais (clientes, vendedores) em um arquivo de texto.
    try:
        with open(ARQUIVO_DADOS, "w") as f:
            # Serializa os dados em formato JSON
            dados = {
                "clientes": [c.__dict__ for c in clientes_cadastrados],
                "vendedores": [v.__dict__ for v in vendedores_cadastrados],
                "discos": [d.__dict__ for d in discos_disponiveis]
            }
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados():
   #Carrega os dados de um arquivo de texto, se ele existir.
    try:
        with open(ARQUIVO_DADOS, "r") as f:
            dados = json.load(f)
            
            global clientes_cadastrados, vendedores_cadastrados, discos_disponiveis
            clientes_cadastrados = [Cliente(**c) for c in dados["clientes"]]
            vendedores_cadastrados = [Vendedor(**v) for v in dados["vendedores"]]
            
            discos_carregados = []
            for d in dados["discos"]:
                # Reconstroi o objeto Artista
                artista = Artista(d["artista"]["artista"])
                discos_carregados.append(DiscoVinil(d["album"], d["preco"], artista, d["genero"]))
            discos_disponiveis = discos_carregados
            
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Aviso: Arquivo de dados '{ARQUIVO_DADOS}' não encontrado ou inválido. Iniciando com dados padrão.")
        # Se houver um erro, as listas globais manterão os dados de exemplo definidos acima