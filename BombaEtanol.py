from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def _init_(self, valor_litro, quantidade_disponivel):
        super()._init_(valor_litro, quantidade_disponivel)
        