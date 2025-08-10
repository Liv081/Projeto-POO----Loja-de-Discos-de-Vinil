# Classe base para qualquer pessoa no sistema
class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
# Cliente herda de pessoa e adiciona o telefone
class Cliente(Pessoa):
    def __init__(self, nome, email, telefone):
        super().__init__(nome, email)
        self.telefone = telefone

    def to_dict(self):
        #Converte o objeto Cliente em um dicionário para serialização.
        return {
            'tipo': 'Cliente',
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }

    @staticmethod
    def from_dict(dados):
        #Cria um objeto Cliente a partir de um dicionário.
        return Cliente(dados['nome'], dados['email'], dados['telefone'])
        
# Funcionário herda de pessoa e adiciona o salário
class Vendedor(Pessoa):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario
    
    def to_dict(self):
        #Converte o objeto Vendedor em um dicionário para serialização.
        return {
            'tipo': 'Vendedor',
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }

    @staticmethod
    def from_dict(dados):
        #Cria um objeto Vendedor a partir de um dicionário.
        return Vendedor(dados['nome'], dados['email'], dados['telefone'])

# Classe Artista
class Artista:
    def __init__(self, artista):
        self.artista = artista
        self.albuns = [] #Lista de objetos DiscoDeVinil

    def adicionar_album(self, disco):
        self.albuns.append(disco)

    def to_dict(self):
        return {'artista': self.artista, 'albuns': [disco.to_dict() for disco in self.albuns]}

    @staticmethod
    def from_dict(dados):
        artista = Artista(dados['artista'])
        # Reconstituímos os discos, mas para este exemplo, não precisamos salvar todos os detalhes.
        return artista

# Classe para qualquer Vinil venddo na loja
class DiscoVinil:
    def __init__(self, album, preco, artista, genero):
        self.album = album
        self.preco = preco
        self.artista = artista
        self.genero = genero
        
    def to_dict(self):
        return {
            'album': self.album,
            'preco': self.preco,
            'artista': self.artista.artista, # Salva apenas o nome do artista
            'genero': self.genero
        }

    @staticmethod
    def from_dict(dados):
        # Aqui, para simplificar, criamos um objeto Artista com apenas o nome
        artista = Artista(dados['artista'])
        return DiscoVinil(dados['album'], dados['preco'], artista, dados['genero'])
   
        
# Representa um produto pedido e sua quantidade
class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto 
        self.quantidade = quantidade
        
    # Calcula o subtotal da compra
    def subtotal(self):
        return self.produto.preco * self.quantidade
        
    
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []  # Lista de ItemPedido (Produtos pedidos pelo cliente)
        
    # Adiciona um item ao pedido
    def adicionar_item(self, item):
        self.itens.append(item)
        
    # Calcula o valor total do pedio somando os subtotais dos itens
    def total(self):
        return sum(item.subtotal() for item in self.itens)